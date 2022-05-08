

from os import DirEntry
import re
from pprint import pprint


class FileRecognitionAlgorithm:
    
    modes: dict
    file: DirEntry

    def __init__(self, file: DirEntry) -> None:
        self.file = file

    @staticmethod
    def load_modes(modes: dict) -> None:
        FileRecognitionAlgorithm.modes = modes


    def is_file(self) -> bool:
        return self.file.is_file() and not self.file.is_symlink()

    def get_directory(self) -> str:
        if not self.is_file():
            raise Exception("Not a file!")

        match = self.match_precise(self.file.name)
        if match is not False:
            print(f"Match!: {match}\n")
            return match

        raise Exception("There is not match for the file!")
        


    def match_precise(self, name):
        for directory in self.modes:
            if re.search(self.modes[directory], name):
                return directory
        return False