import datetime
filename=datetime.datetime.now()

def create():
    with open(filename.strftime("%Y-%m-%d-%H"),'w') as file:
        file.write("Manthan is back")
create()
