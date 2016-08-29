import pandas
from collections import OrderedDict

class Head3record:
    """ """
    def __init__(self,Conf,CONFORMER,FL,occ,crg,Em0,pKa0,ne,nH,vdw0,vdw1,tors,epol,dsolv,extra,history):
        self.Conf = Conf
        self.CONFORMER = CONFORMER
        self.FL = FL
        self.occ = float(occ)
        self.crg = float(crg)
        self.Em0 = float(Em0)
        self.pKa0 = float(pKa0)
        self.ne = int(ne)
        self.nH = int(nH)
        self.vdw0 = float(vdw0)
        self.vdw1 = float(vdw1)
        self.tors = float(tors)
        self.epol = float(epol)
        self.dsolv = float(dsolv)
        self.extra = float(extra)
        self.history = history

    def __repr__(self):
         return self.Conf+" "+self.CONFORMER+" "+self.FL+" "+'{0:.2f}'.format(self.occ)+"{} ".format(" ")+'{}'.format(self.crg,width=5)+"     "+'{0:.0f}'.format(self.Em0)

class Head3reader:
    """ """
    def __init__(self):
        self.recordList={}

    def readHead3(self,path):
        f = open(path, 'r')
        f.readline()
        recordList={}
        for line in f:
            iConf,CONFORMER,FL,occ,crg,Em0,pKa0,ne,nH,vdw0,vdw1,tors,epol,dsolv,extra,history=line.split()
            h3r = Head3record(iConf,CONFORMER,FL,occ,crg,Em0,pKa0,ne,nH,vdw0,vdw1,tors,epol,dsolv,extra,history)
            self.recordList[CONFORMER]=h3r

