import datetime
import glob2
dt = datetime.datetime.now()
gl = glob2.glob("*.txt")

def create():
    with open(dt.strftime("%Y-%m-%d-%H")+".txt", 'w') as file:
        for i in gl:
            with open(i, 'r')as f:
                file.write(f.read()+"\n")
create()
