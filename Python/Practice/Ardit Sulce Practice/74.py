import pandas

data1 = pandas.read_csv("http://www.pythonhow.com/data/sampledata.txt")
data2 = pandas.read_csv("sample2.txt")

a = pandas.concat([data1, data2])
a.to_csv("sample3.txt", index = None)
