# Henry Barth
# Start Date: 7.13.2022
# Project: Make Graphs

import plotly
from plotly.graph_objs import Bar, Layout
from plotly import offline

def makeGraph(multidimensionalList, pathName):
    """The graph uses plotly modules to make nice html graph of our data
    this function doesn't return anything, but it does put an html file in our plots folder
    """
    xVals = [x[0] for x in multidimensionalList]
    yVals = [y[1] for y in multidimensionalList]

    data = [Bar(x=xVals, y=yVals)]

    xAxisConfig = {"title": "Date", "dtick": 1}
    yAxisConfig = {"title": "Miles Traveled"}

    myLayout = Layout(title=f"Miles Traveled per Date",
                      xaxis=xAxisConfig, yaxis=yAxisConfig)
    offline.plot({"data":data, "layout":myLayout}, filename=pathName)
