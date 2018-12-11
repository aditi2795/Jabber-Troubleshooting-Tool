from xml.dom import minidom
import requests
from ManualLogin import *
from ServiceProfile import *

class sso_impclass:

    def ssoimpfn(self):
        #sso
        file1=open(manualobj.browseValue+"/sso_imp.txt",'w+')
        file2=open(manualobj.browseValue+"/sso_imp.xml",'w+')
        file_servicex=open(manualobj.browseValue+"/service.txt",'r')
        file_service=open(manualobj.browseValue+"/service.txt",'r').read()
        file = open(str(manualobj.browseValue)+"/credentials.txt", 'r').read()
        try:

            info = file.split('\n')
            for row in info:
                if 'Username' in row:
                    userName = row.split(":")[1]
                if "Password" in row:
                    password = row.split(":")[1]
                    password = base64.b64decode(bytes(password))
            server=[]
            for row in file_service.split('\n'):
                if "IMP" in row:
                    item=row.split(":")[2]
                    server.append(item)
            server = filter(lambda name: name.strip(), server)
            print server
            length=len(server)
            for j in range(length):
                if server[j]!="Not Configured":
                    ip=socket.gethostbyname(str(server[j]))
                    requests1=requests.get("https://"+ip+":8443/ssosp/ws/public/singleSignOn",verify=False)
                    if requests1.status_code==200:
                        file2.write(requests1.text)
                        file2.close()
                        ssoresult = minidom.parse(manualobj.browseValue+"/sso_imp.xml")
                        response = ssoresult.getElementsByTagName("Response")[0]
                        single = response.getElementsByTagName("SingleSignOn")[0]
                        for node in single.childNodes:
                            if  node.tagName=="Status":
                                file1.write("Status Enabled-"+str(server[j])+" "*(30-(len(str(ip))+len("Status Enabled")))+":"+node.getAttribute('enabled')+"\n")
                        file1.write("Version-" + str(server[j]) + " " * (30 - (len(str(ip)) + len("Version"))) + ":" + single.getAttribute('version') + "\n")
        except:
            pass












