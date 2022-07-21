# Henry Barth
# Start Date: 7.13.2022
# Project: Utah LTAP Test

import csv
import datetime
from modules.yard2Mile import yard2Mile
from modules.makeGraph import makeGraph
from modules.fileStuff import write2CSV
from modules.splitDate import splitDate
from modules.fileStuff import promptFileSave

def dataConverter(filePath):
    """
    Pass a file path to a csv file as its parameter,
    if it is successfully passed the correct file in correct format, it will return a "success" string and also return
    the file path of the new file
    """
    csvData = []  # This will contain the cells which contain the length data
    relevantIndexes = [84, 115]  #date, lengthYds
    formatCode = "%m/%d/%Y"  # date format code
    headers = ["Date", "Miles Traveled"]  #This is the final headers that will be used in the final CSV
    graphFilePath = "plots\\test-milesTraveled_7.13.2022.html"  #This is the name of the filepath for your graph

    try:
        with open(filePath) as file:
            reader = csv.reader(file)
            for row in reader:
                newLine = []
                for index in relevantIndexes:
                    newLine.append(row[index])
                csvData.append(newLine)
    except TypeError:
        return "No File Selected" , None
    except FileNotFoundError:
        return "File Not Found" , None
    except IndexError:
        return "File Data Format Not Supported" , None
    except UnicodeDecodeError:
        return "Unsupported File Format" , None

    csvData = csvData[1:]  #chops off the first element of the list which isn't needed

    for line in csvData:  #Starts at index of 1 to ignore headers from the file
        line[0] = splitDate(line[0])  #Changes the element of the list so that you cut off the time portion of the date
        line[0] = datetime.datetime.strptime(line[0], formatCode)  #change the first element into a datetime object
        line[1] = yard2Mile(float(line[1]))  #changes the second element into a float that is miles

    csvData.sort(key=lambda x: x[0])  # sorts this new list by date (first element in each line)

    # Make a list to hold unique dates in using for loop
    dates = []
    for line in csvData:
        date = line[0]
        if date not in dates:  #only adds dates that aren't in the list
            dates.append(date)

    finalList = [[date] for date in dates]  #makes a list of lists which contain the dates that were in the sheet

    # This loop is to add the total miles from csvData into the final list elements
    for lst in finalList:
        milesTotal = 0
        for line in csvData:
            if line[0] == lst[0]:
                milesTotal += line[1]
        lst.append(milesTotal)  #adds the total miles travelled to the list after the date
        lst[0] = lst[0].strftime(formatCode)  #Change the datetime object back into string representation

    #Writes the finalList which is a list of lists where each list is a date and total miles that day
    newCSVPath = promptFileSave()
    if newCSVPath == "":
        return "Cancelled", None
    write2CSV(finalList, headers, newCSVPath)    #Saves the data to csv format
    #########################END OF MAIN#################################################
    return "Success" , newCSVPath

if __name__ == "__main__":
    from modules.fileStuff import promptFileOpen
    dataConverter(promptFileOpen())
