
import os
import re
from pprint import pprint

cwd = os.getcwd()
SETTINGS_DIR = "\\src\\settings\\settings.py"

REGEX = "regex"
EXT = "extension"
NAME = "name"

def correct_path(path: str):
    if not path.endswith("\\"):
        path = path + "\\"
    return re.sub(r"\\", r"\\\\", path)


print("\n\n\nWelcome to OrginzerApp")
print("Here you will setup your app\n\n")
print("All your settings will be written to src/settings/settings.py")

if os.path.isfile(cwd + SETTINGS_DIR):
    print("Do you want to override existing settings?")
    setts = input("yes/no [no]\n")
    if setts != "yes":
        print("Settings will not be override!\nExit setup!")
        exit()

path = input("Enter FULL PATH of directory from which files will be taken\n")
if not os.path.isdir(path):
    print("Incorrect path!\nExit setup!")
    exit()
path = correct_path(path)

destination = input("Enter FULL PATH of directory to which files will be taken\n")
if not os.path.isdir(destination):
    print("Directory not exist! Would you like to create it?\n")
    create = input("yes/no [no]\n")
    if create == "yes":
        try:
            os.mkdir(destination)
        except Exception as e:
            print("Cannot create directory\n")
            print(e)
            print("Exit setup!")
            exit()
    else:
        print("Incorrect path!\nExit setup!")
        exit()
destination = correct_path(destination)


mode_write = True
modes = {}
print("\n\nStart creating modes:\n")

while mode_write == True:

    folder = input("1. Enter folder path:\n")
    if folder == "":
        break

    mode = input(f"2. Select mode:\n{REGEX}|{EXT}|{NAME}: Default: {REGEX}\n")
    if mode == "":
        mode = REGEX

    regex = input(f"3. Enter {mode}:\n")
    if regex == "":
        break

    if mode == EXT:
        regex = regex + "$"
    else:
        pass
    modes[folder] = regex
    print("\nMode created:")
    print(f"{folder}: {regex}\n\n")


print("Created MODES:\n")
pprint(modes)

with open(cwd + SETTINGS_DIR, 'w') as file:
    file.write(f"PATH = '{path}'\n\n")
    file.write(f"DESTIN_PATH = '{destination}'\n\n")
    file.write("MODES = {\n")
    for mode in modes:
        file.write(f'\t"{mode}": "{modes[mode]}",\n')
    file.write("}\n")
