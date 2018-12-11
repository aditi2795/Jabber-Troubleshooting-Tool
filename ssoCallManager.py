from xml.dom import minidom
import requests
from ServiceProfile import *
class ssoclass_:
    def ssofn(self):
        #sso
        file1=open(manualobj.browseValue+"/sso_cucm.txt",'w+')
        file2=open(manualobj.browseValue+"/sso_cucm.xml",'w+')
        file_mess = open(manualobj.browseValue+"/messages.xml", 'w+')
        file_ver = open(manualobj.browseValue+"/version.xml", 'w+')


        file = open(manualobj.browseValue+"/credentials.txt", 'r').read()
        try:

            file_servicex = open(manualobj.browseValue + "/server.txt", 'r')
            file_service = open(manualobj.browseValue + "/server.txt", 'r').read()
            info = file.split('\n')
            for row in info:
                if 'Username' in row:
                    userName = row.split(":")[1]
                if "Password" in row:
                    password = row.split(":")[1]
                    password = base64.b64decode(bytes(password))
            server=[]
            for row in file_service.split('\n'):
                server.append(row)
            server = filter(lambda name: name.strip(), server)
            print server
            length=len(server)

            for j in range(length):
                ip=socket.gethostbyname(str(server[j]))
                requests1=requests.get("https://"+ip+":8443/ssosp/ws/public/singleSignOn",verify=False)
                print requests1.status_code, "req for status code"
                if requests1.status_code==200:
                    file2 = open(manualobj.browseValue+"/sso_call.xml", 'w+')
                    file2.write(requests1.text)
                    file2.close()
                    ssoresult = minidom.parse(manualobj.browseValue+"/sso_call.xml")
                    response = ssoresult.getElementsByTagName("Response")[0]
                    response
                    single = response.getElementsByTagName("SingleSignOn")[0]
                    single
                    for node in single.childNodes:
                        if node.tagName=='Status':
                            file1.write("Status Enabled-"+str(server[j])+" "*(30-(len(str(ip))+len("Status Enabled")))+":"+node.getAttribute('enabled')+"\n")
                    break
            file_servicex.close()
            file_service2 = open(manualobj.browseValue + "/server.txt", 'r').read()
            for j in range(length):
                ip = socket.gethostbyname(str(server[j]))
                req = requests.get('https://' + ip + '/cucm-uds/version', verify=False, auth=(userName, password))
                print req.status_code, "sso req status"
                if req.status_code == 200:
                    file_ver.write(req.text)
                    file_ver.close()

                    doc = minidom.parse(manualobj.browseValue + "/version.xml")
                    ver = doc.getElementsByTagName("version")[0]
                    file1.write("version" + " " * (30 - len("version")) + ":" + str(ver.firstChild.data) + "\n")

                    break
            else:
                file1.write("Unable to get the version\n")



        except:
          file1.write("Unable to get sso details")











