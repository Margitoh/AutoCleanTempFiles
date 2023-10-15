import os
import shutil

def clean_temp_files(temp_folder):
    try:
        if os.path.exists(temp_folder):
            for filename in os.listdir(temp_folder):
                file_path = os.path.join(temp_folder, filename)
                try:
                    if os.path.isfile(file_path):
                        os.unlink(file_path)
                        print(f"Deleted {file_path}")
                    elif os.path.isdir(file_path):
                        shutil.rmtree(file_path)
                        print(f"Deleted directory {file_path}")
                except Exception as e:
                    print(f"Failed to delete {file_path}: {e}")
        else:
            print(f"Temporary folder {temp_folder} does not exist.")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    temp_folder = os.path.join(os.environ['USERPROFILE'], 'AppData', 'Local', 'Temp')
    clean_temp_files(temp_folder)