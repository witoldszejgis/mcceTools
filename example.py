from head3reader import Head3reader
from fort38reader import Fort38reader
h=Head3reader()
h.readHead3("/Users/witoldszejgis/gits/head3reader/head3.lst")
print(h.recordList)
f=Fort38reader()
f.readFort38("/Users/witoldszejgis/gits/head3reader/fort.38")
print(f.recordList)

