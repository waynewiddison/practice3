"""
Rename files from a folder
get: http://icarus.cs.weber.edu/~hvalle/hafb/prank.zip
"""
import os


def main():
    rename_files()


def rename_files():
    """
    Rename files in a folder
    :return: nothing
    """
    folder_dir = r"C:\Users\CCEClass1.AD.000.001.002.003.004.005.006.007\Desktop\hafb\prank\prankOrig"
    files = os.listdir(folder_dir)
    saved_path = os.getcwd()  # save current directory, next we'll go to files's directory
    os.chdir(folder_dir)
    for file in files:
        # Remove digits from name
        new_file = file.lstrip('0123456789')  # this will strip all the 1's then the 2's, etc
        print("old name", file, "new name", new_file)
        # Rename file to new name
        os.rename(file, new_file)
     # get back home
    os.chdir (saved_path)


if __name__ == '__main__':
    main()
    exit(0)
