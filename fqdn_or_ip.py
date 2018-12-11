import re
from ManualLogin import *
from ServiceProfile import *
class fqdnclass():
    def fqdnfn(self):
        flag=0
        file=open(manualobj.browseValue+"/service.txt","r").read()
        file_write=open(manualobj.browseValue+"/fqdn.txt","w")

        try:
            for row in file.split('\n'):
                info = str(row)
                info= info.split(":")
                info = filter(None,info)
                if len(info)>=3:
                    if re.search('[a-zA-Z]', info[2]) == None:
                        if flag==0:
                            file_write.write("If users attempt to connect to a server with an IP address or hostname, and the server certificate identifies the server with an FQDN, the client cannot identify the server as trusted and prompts the user.\n If your server certificates identify the servers with FQDNs, you should plan to specify each server name as FQDN in many places on your servers\n Following servers have ip address configured\n")
                            flag=1
                            file_write.write(info[0] + " " + info[1]+" has ip address configured.\n")
                        else:
                            file_write.write(info[0] + " " + info[1] + " has ip address configured.\n")
        except:
            pass
fqdnobj=fqdnclass()
