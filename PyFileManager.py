from pathlib import Path
import os

def listOfFiles():
    path = Path('')
    items = list(path.rglob('*'))
    for i, item in enumerate(items):
        print(f"{i + 1}: {item}")

def createFile():
    try:
        listOfFiles()
        name = input("Enter the name of the file you want to create: ")
        p = Path(name)
        if not p.exists():
            with open(p, "a") as fs:
                data = input("Enter text to write in your file: ")
                fs.write(data)
            print("FILE CREATED SUCCESSFULLY")
        else:
            print("This file already exists")
    except Exception as err:
        print(f"An exception occurred: {err}")

def readFile():
    listOfFiles()
    try:
        name = input("Enter the name of the file you want to read: ")
        p = Path(name)
        if p.exists():
            with open(p, "r") as fs:
                data = fs.read()
                print(data)
            print("READ SUCCESSFULLY")
        else:
            print("This file does not exist")
    except Exception as err:
        print(f"An exception occurred: {err}")

def updateFile():
    try:
        listOfFiles()
        name = input("Enter the name of the file you want to update: ")
        p = Path(name)
        print("Press 1 to rename your file")
        print("Press 2 to overwrite data in your file")
        print("Press 3 to append content to your file")

        res = int(input("Enter your choice: "))
        if res == 1:
            name2 = input("Enter the new name for the file: ")
            p2 = Path(name2)
            p.rename(p2)
            print("RENAMED SUCCESSFULLY")
        elif res == 2:
            with open(p, "w") as fs:
                data = input("Enter data to overwrite in file: ")
                fs.write(data)
            print("OVERWRITTEN SUCCESSFULLY")
        elif res == 3:
            with open(p, "a") as fs:
                data = input("Enter data to append to file: ")
                fs.write(data)
            print("APPENDED TEXT SUCCESSFULLY")
        else:
            print("Invalid choice")
    except Exception as err:
        print(f"An exception occurred: {err}")

def deleteFile():
    try:
        listOfFiles()
        name = input("Enter the name of the file you want to delete: ")
        p = Path(name)
        if p.exists():
            os.remove(p)
            print("FILE REMOVED SUCCESSFULLY")
        else:
            print("This file does not exist")
    except Exception as err:
        print(f"An exception occurred: {err}")

# Optionally, you can create a menu for the user to select operations:
if __name__ == "__main__":
    print("File Management System")
    print("1: List files")
    print("2: Create file")
    print("3: Read file")
    print("4: Update file")
    print("5: Delete file")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        listOfFiles()
    elif choice == 2:
        createFile()
    elif choice == 3:
        readFile()
    elif choice == 4:
        updateFile()
    elif choice == 5:
        deleteFile()
    else:
        print("Invalid choice")
