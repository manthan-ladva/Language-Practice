import pandas
import pylab

data = pandas.read_csv("http://www.pythonhow.com/data/sampledata.txt")
data.plot(x='x', y='y', kind='scatter')
pylab.show()
