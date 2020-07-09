import csv
import plotly.express as px
import numpy as np

def getDataSource(data_path):
    sizeOfTv=[]  
    averageTimeSpent=[]
    with open(data_path)as csv_files:
        csv_reader=csv.DictReader(csv_files)
        for row in csv_reader:
            sizeOfTv.append(float(row["Size of Tv"]))
            averageTimeSpent.append(float(row["\tAverage time spent watching TV in a week (hours)"]))

    return{"x":sizeOfTv,"y":averageTimeSpent}

def findCorrelation(dataSource):
    correlation=np.corrcoef(dataSource["x"],dataSource["y"])
    print("correlation between size of TV and average time spent watching TV in a week- \n--->",correlation[0,1])

def setup():
    data_path="/Size of TV,_Average time spent watching TV in a week (hours).csv"
    dataSource=getDataSource(data_path)
    findCorrelation(dataSource)

setup()
