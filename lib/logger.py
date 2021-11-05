from datetime import datetime

def writeLog(string):
    with open('log',"a") as file:
        file.write(str(datetime.now)+string+'\n')
