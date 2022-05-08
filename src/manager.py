

import os

from algorithm import FileRecognitionAlgorithm

class FileManager:

    path: str
    destination: str


    def __init__(self, path: str, destination: str):
        self.path = path
        self.destination = destination
        self.files = None

    def get_all_files(self):
        #get all files and dirs from directory
        try:
            self.files = os.scandir(self.path)
        except FileNotFoundError:
            print(f"\nError!\nDirectory cannot be found: {self.path}")
            exit()

    def create_dirs_if_not_exist(self, modes: dict):
        self.load_modes(modes)
        # Creating directory if doesn't exist
        for directory in modes:
            if not os.path.isdir(f"{self.destination}{directory}\\"):
                try:
                    os.mkdir(f"{self.destination}{directory}\\")
                except os.error as error:
                    print(f"Cannot create directory {directory}\nError:\n{error}")
                    exit()

    def load_modes(self, modes: dict):
        FileRecognitionAlgorithm.load_modes(modes)

    def move_files(self):
        for file in self.files:
            file_algo = FileRecognitionAlgorithm(file)
            try:
                dir_name = file_algo.get_directory()
                os.rename(f"{self.destination}{file.name}", f"{self.destination}{dir_name}\\{file.name}")
            except Exception as ex:
                print(f"Exception: {ex}")
                pass
            
            