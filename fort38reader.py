import pandas
from collections import OrderedDict

class Fort38record:
    """ """
    def __init__(self,fieldList,headerList):
        self.titrPoints=OrderedDict()
        self.confName=fieldList[0]
        #fieldList.readline()
        #headerList.readline()
        for i in range(1,len(fieldList)):
            #print(headerList[i])
            #print(fieldList[i])
            self.titrPoints[float(headerList[i])]=float(fieldList[i])

    def __repr__(self):
         return self.confName+" " +' '.join(str(x) for x in self.titrPoints.values())

class Fort38reader:
    """ """
    def __init__(self):
         self.recordList={}

    def readFort38(self,path):
         f = open(path, 'r')
         headerList=f.readline().split()
         for line in f:
             fieldList=line.split()
             f38r = Fort38record(fieldList,headerList)
             self.recordList[fieldList[0]]=f38r

