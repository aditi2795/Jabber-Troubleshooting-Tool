from jabberDefault import default
from jabber import jabber_
from ManualLogin import *

class jabbercomp():
    def jabbercompfn(self):
        defaultobj = default()
        defaultobj.defaultfn()
        jabberobj = jabber_()
        jabberobj.jabber()
        file1=open(manualobj.browseValue+"/jabber_config.txt",'r').read()
        file2=open(manualobj.browseValue+"/jabber_default.txt",'r').read()
        file3=open(manualobj.browseValue+"/jabber_summary.txt",'w+')

        try:

            for row in file1.split('\n'):
                if ":" in row:
                    row=row.split(":")
                    item=row[0]
                    item = filter(lambda name: name.strip(), item)
                    value=row[1]
                    value=filter(lambda name: name.strip(), value)
                    #print item,value
                    for column in file2.split('\n'):
                        if ":" in column:
                            column=column.split(":")
                            key=column[0]
                            key = filter(lambda name: name.strip(), key)
                            check=column[1]
                            check=filter(lambda name: name.strip(), check)
                            #print key,check
                            if str(item)==str(key):

                                 if value!=check:
                                     file3.write(str(item)+"\n")
                                     break
                                 else:

                                     break
        except:
            pass
