"""
DownloadedFileOrganizer

@version: 0.1.0
@python 3.10
@license: Apache License
@author: Pawel Podgórski
"""

from settings.settings import *
from manager import FileManager

print("\nWelcome to DownloadedFileOrganizer!\n")

file_manager = FileManager(PATH, DESTIN_PATH)

file_manager.get_all_files()

file_manager.create_dirs_if_not_exist(MODES)

file_manager.move_files()

print("Operation ended with success!")


