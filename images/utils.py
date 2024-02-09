import os

def rename_files(directory):
    for filename in os.listdir(directory):
        if filename.endswith(".JPG"):
            # Define the new filename
            new_filename = filename[:-4] + '.jpg'
            # Define the full old and new file paths
            old_file = os.path.join(directory, filename)
            new_file = os.path.join(directory, new_filename)
            # Rename the file
            os.rename(old_file, new_file)
            print(f"Renamed '{old_file}' to '{new_file}'")

def compare_files(directory1, directory2):
    files1 = {file.lower() for file in os.listdir(directory1)}
    files2 = {file.lower() for file in os.listdir(directory2)}

    common_files = files1.intersection(files2)
    unique_to_dir1 = files1.difference(files2)
    unique_to_dir2 = files2.difference(files1)

    print(f"Common files ({len(common_files)}):", common_files)
    print(f"Unique to {directory1} ({len(unique_to_dir1)}):", unique_to_dir1)
    print(f"Unique to {directory2} ({len(unique_to_dir2)}):", unique_to_dir2)


fulls_path = './fulls'
thumbs_path = './thumbs'

rename_files(fulls_path)
rename_files(thumbs_path)
compare_files(fulls_path, thumbs_path)