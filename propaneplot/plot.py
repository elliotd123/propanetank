#!/usr/bin/env python3
import numpy
from matplotlib import pyplot
from datetime import datetime

def local_main():
    data = open("data.txt").read()
    x = []
    y = []
    currentday = None
    firstday = None
    daygap = 0
    for line in data.split('\n')[::-1]:
        if line.strip().startswith("#") or len(line.strip()) == 0:
            continue

        dateString = line.split(":")[0]
        level = int(line.split(":")[1])
        date = datetime.strptime(dateString, "%Y-%m-%d")
        if currentday != None:
            daygap = daygap + (date - currentday).days
        currentday = date
        if firstday is None:
            firstday = date
        x.append(daygap)
        y.append(level)
    
    coef = numpy.polyfit(x,y,1)
    print(coef)
    poly1d_fn = numpy.poly1d(coef)
    daystoplot = range(daygap,30)
    pyplot.plot(x,y, 'yo', daystoplot, poly1d_fn(daystoplot), '--k')
    pyplot.title("Propane Projection")
    annotation = firstday.strftime("%F") + " - " + str(y[0]) + "%"
    pyplot.annotate(annotation,(x[0],y[0]),arrowprops={})
    pyplot.xlabel("Days from the last entry")
    pyplot.ylabel("Propane Level (%)")

    pyplot.show()

if __name__ == "__main__":
    local_main()
