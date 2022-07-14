# Henry Barth
# Start Date: 7.13.2022
# Project: Utah LTAP Test

import csv
import datetime
from modules.yard2Mile import yard2Mile
from modules.makeGraph import makeGraph

def main():
    filePath = "StreetProvo.csv"
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

    except FileNotFoundError:
        print("File Not Found")
        exit()

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
    write2CSV(finalList, headers, "csvFiles\\test-7.13.2022.csv")

    #Creates HTML using final list
    makeGraph(finalList, graphFilePath)
    #########################END OF MAIN#################################################

def splitDate(date):
    """the first parameter is a string with a date and then a time separated by a space
    eg: MM/DD/YYYY 12:00:00
    it will return a string like: MM/DD/YYYY
    """
    return date.split(" ")[0]  #the split method returns a list object, and we only want to access the first element

def write2CSV(multiDimensionalList, headers, pathName):
    """Writes our organized data into a csv file for all to enjoy!"""
    #Opens file in write mode
    with open(pathName, "w", newline="") as f:
        writer = csv.writer(f)  #make csv writer object
        writer.writerow(headers)
        for row in multiDimensionalList:
            writer.writerow(row)


if __name__ == "__main__":
    main()
