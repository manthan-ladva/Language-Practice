import pandas

df = pandas.read_csv("http://www.pythonhow.com/data/sampledata.txt")
data2 = df * 2
data2.to_csv("sample2.txt", index = None)
