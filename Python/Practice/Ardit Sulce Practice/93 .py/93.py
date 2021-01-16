import glob2

all = glob2.glob("subdirs/**/*.py", recursive = True)
print(len(all))
