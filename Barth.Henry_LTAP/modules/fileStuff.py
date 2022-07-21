# Henry Barth
# Start Date: 7.16.2022
# Project: Prompt File

import tkinter
import tkinter.filedialog
import csv

def promptFileOpen():
    """Create a Tk file dialog and cleanup and return file path when finished"""
    top = tkinter.Tk()
    top.withdraw()  # hide window
    file_name = tkinter.filedialog.askopenfilename(parent=top, title="Select a CSV file")
    top.destroy()
    return file_name

def promptFileSave():
    """Create a Tk file dialog and cleanup and return file path when finished"""
    top = tkinter.Tk()
    top.withdraw()  # hide window
    file_name = tkinter.filedialog.asksaveasfilename(parent=top, title="Save file as")
    top.destroy()
    return file_name

def write2CSV(multiDimensionalList, headers, pathName):
    """Writes our organized data into a csv file for all to enjoy!"""
    #Opens file in write mode
    try:
        with open(pathName, "w", newline="") as f:
            writer = csv.writer(f)  #make csv writer object
            writer.writerow(headers)
            for row in multiDimensionalList:
                writer.writerow(row)
    except FileNotFoundError:
        return "File Not Found"

if __name__ == "__main__":
    print(promptFileSave())