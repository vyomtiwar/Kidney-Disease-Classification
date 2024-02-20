import os
import shutil
from src.cnnClassifier import logger


STAGE_NAME = "Model_Inserted"


class Model:
    def __init__(self):
        pass
    
    def main(self):
    # Define paths
        source_dir = "artifacts/training"
        destination_dir = "model"
        file_name = "model.h5"

    # Ensure the source directory exists
        if not os.path.exists(source_dir):
            print(f"Source directory '{source_dir}' does not exist.")
            return

    # Ensure the destination directory exists
        if not os.path.exists(destination_dir):
            os.makedirs(destination_dir)

    # Construct full paths for source and destination files
        source_file = os.path.join(source_dir, file_name)
        destination_file = os.path.join(destination_dir, file_name)

    # Copy file from source to destination
        try:
            shutil.copyfile(source_file, destination_file)
            print(f"File '{file_name}' copied successfully from '{source_dir}' to '{destination_dir}'.")
        except FileNotFoundError:
            print(f"File '{file_name}' not found in '{source_dir}'.")

if __name__ == "__main__":
    try:
        logger.info(f"*******************")
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = Model()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e
