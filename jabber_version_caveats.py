from ManualLogin import *
class caveatsclass():
    def caveatsfn(self):
        file_list_of_programs = open(manualobj.browseValue + "\\sysdetails.txt",'r').read()
        file_jabber_caveats = open(manualobj.browseValue + "\\jabber_caveats.txt",'w')
        try:
            info=file_list_of_programs.split('\n')
            for row in info:
                if "Cisco Jabber" in row:
                    value=row
                    break
            print value
            list=value.split()
            list=filter(None,list)
            version= list[2]
            print version
            if "11.8.0"==version[:6]:
                with open(manualobj.browseValue + "\sysdetails.txt") as f:
                    with open(manualobj.browseValue + "\\jabber_caveats.txt", "w") as f1:
                        for line in f:
                            f1.write(line)
            else:
                with open(manualobj.browseValue + "\\dns.txt") as f:
                    with open(manualobj.browseValue + "\\jabber_caveats.txt", "w") as f1:
                        for line in f:
                            f1.write(line)
        except:
            print "jabber caveats problem"