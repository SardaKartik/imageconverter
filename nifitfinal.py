import os
import nibabel as nib
import numpy as np
import matplotlib.pyplot as plt

# Input parent folder containing all subfolders with .nii files
input_parent_folder = r"C:\Users\karti\Downloads\Sample_Nifti_Data\Sample_Nifti_Data"
# Output folder to save all PNG files
output_folder = r"C:\Users\karti\Downloads\python\output_folder2"
os.makedirs(output_folder, exist_ok=True)

main_folder_name = os.path.basename(input_parent_folder)
main_output_folder = os.path.join(output_folder, main_folder_name)
os.makedirs(main_output_folder, exist_ok=True)


for main_folder_name in os.listdir(input_parent_folder):
    main_folder_path = os.path.join(input_parent_folder, main_folder_name)

    # Ensure it's a directory
    if os.path.isdir(main_folder_path):
        # Create a corresponding folder in the output folder
        main_output_folder = os.path.join(output_folder, main_folder_name)
        os.makedirs(main_output_folder, exist_ok=True)

        # Iterate through each second-level subfolder in the main folder
        for subfolder_name in os.listdir(main_folder_path):
            subfolder_path = os.path.join(main_folder_path, subfolder_name)

            # Check if subfolder_path is a directory
            if os.path.isdir(subfolder_path):
                print(f"Processing folder: {subfolder_path}")
                
                # Iterate through files in the second-level subfolder
                for nii_file in os.listdir(subfolder_path):
                    # Process only .nii files
                    if nii_file.endswith('.nii'):
                        print("Processing file:", nii_file)
                        
                        # Load the NIFTI file
                        nii_path = os.path.join(subfolder_path, nii_file)
                        nii_image = nib.load(nii_path)
                        image_data = nii_image.get_fdata()

                        # Iterate over slices in the 3D image
                        for slice_index in range(image_data.shape[2]):
                            slice_data = image_data[:, :, slice_index]
                            print(plt.imshow(slice_data))

                            # Define output filename and save as PNG
                            output_filename = f"{main_folder_name}_{subfolder_name}_{nii_file[:-4]}_s{slice_index}.png"
                            output_path = os.path.join(main_output_folder, output_filename)

                            # Save slice as a PNG image
                            plt.imsave(output_path, slice_data, cmap='gray')

print("Conversion completed! All PNG files are saved in their respective folders within:", output_folder)