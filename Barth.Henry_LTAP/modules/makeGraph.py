# Henry Barth
# Start Date: 7.13.2022
# Project: Make Graphs

import csv
from plotly.graph_objs import Bar, Layout
from plotly import offline
from modules.fileStuff import promptFileSave
from modules.fileStuff import promptFileOpen

def makeGraph(csvFile):
    """The graph uses plotly modules to make nice html graph of our data
    this function doesn't return anything, but it does put a html file in our plots folder
    """
    csvData = []  # This will contain the cells which contain the length data

    try:
        with open(csvFile) as file:
            reader = csv.reader(file)
            for row in reader:
                csvData.append(row)
    except TypeError:
        return "No File Selected"
    except FileNotFoundError:
        return "File Not Found"

    try:
        xVals = [x[0] for x in csvData[1:]]  #Slices through all but the Titles
        yVals = [eval(y[1]) for y in csvData[1:]]
    except IndexError:
        return "File Data Format Not Supported"
    except UnicodeDecodeError:
        return "Unsupported File Format"

    data = [Bar(x=xVals, y=yVals)]

    xAxisConfig = {"title": f"Date", "dtick": 1}
    yAxisConfig = {"title": f"Miles Travelled"}

    myLayout = Layout(title=f"Miles Traveled per Date",
                      xaxis=xAxisConfig, yaxis=yAxisConfig)

    offline.plot({"data":data, "layout":myLayout}, filename=promptFileSave())
    return "Success"

if __name__ == "__main__":
    makeGraph(promptFileOpen())
