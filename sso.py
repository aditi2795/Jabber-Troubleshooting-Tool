from xml.dom import minidom
import requests
from ManualLogin import *
from ServiceProfile import *

class ssoclass:

    def ssofn(self):
        #sso
        file1=open(manualobj.browseValue+"/sso_voicemail.txt",'w+')
        file2=open(manualobj.browseValue+"/sso_voicemail.xml",'w+')
        file_mess = open(manualobj.browseValue+"/messages.xml", 'w+')
        file_ver = open(manualobj.browseValue+"/version.xml", 'w+')
        file_servicex=open(manualobj.browseValue+"/service.txt",'r')
        file_service=open(manualobj.browseValue+"/service.txt",'r').read()
        file = open(str(manualobj.browseValue)+"/credentials.txt", 'r').read()
        file_sso_voice_status=open(manualobj.browseValue+"/voice_status.txt",'w')
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
                if "VoiceMail" in row:
                    item=row.split(":")[2]
                    server.append(item)
            server = filter(lambda name: name.strip(), server)
            print server
            length=len(server)
            for j in range(length):
                if server[j]!="Not Configured":
                    try:
                        ip=socket.gethostbyname(str(server[j]))
                        requests1=requests.get("https://"+ip+":8443/ssosp/ws/public/singleSignOn",verify=False)

                    except:
                        file_sso_voice_status.write("voicemail_fail")
                    if requests1.status_code==200:
                        file2.write(requests1.text)
                        file2.close()
                        ssoresult = minidom.parse(manualobj.browseValue+"/sso_voicemail.xml")
                        response = ssoresult.getElementsByTagName("Response")[0]
                        single = response.getElementsByTagName("SingleSignOn")[0]
                        for node in single.childNodes:
                            if  node.tagName=="Status":
                                file1.write("Status Enabled-"+str(server[j])+" "*(30-(len(str(ip))+len("Status Enabled")))+":"+node.getAttribute('enabled')+"\n")
                    break


                #file_servicex.close

            file_service1x = open(manualobj.browseValue+"/service.txt", 'r')
            file_service1 = open(manualobj.browseValue+"/service.txt", 'r').read()
            server1 = []
            for row in file_service1.split('\n'):
                if "VoiceMail" in row:
                    item = row.split(":")[2]
                    itemip=socket.gethostbyname(item)
                    req = requests.get('https://' + itemip + '/vmrest/mailbox/folders/inbox/messages',
                                       verify=False,
                                       auth=(userName,password))
                    if req.status_code==200:
                        file_mess.write(req.text)
                        file_mess.close()
                        doc = minidom.parse(manualobj.browseValue+"/messages.xml")
                        print doc
                        mess = doc.getElementsByTagName("Messages")[0]
                        file1.write("No. of Messages" +" "*(30-len("No. of Messages"))+":"+ str(mess.getAttribute("total"))+"\n")
                        break
            else:
                file1.write("Unable to connect to server\n")
            #file_service1x.close()

            file_service2x = open(manualobj.browseValue+"/service.txt", 'r')
            file_service2 = open(manualobj.browseValue+"/service.txt", 'r').read()
            for row in file_service2.split('\n'):
                if "VoiceMail" in row:
                    item = row.split(":")[2]
                    itemip = socket.gethostbyname(item)
                    req = requests.get('https://'+itemip+'/vmrest/version', verify=False, auth=(userName,password))
                    if req.status_code == 200:
                        file_ver.write(req.text)
                        file_ver.close()
                        doc = minidom.parse(manualobj.browseValue+"/version.xml")
                        ver = doc.getElementsByTagName("version")[0]
                        file1.write("version" + " "*(30-len("version"))+":"+str(ver.firstChild.data)+"\n")
                        file_sso_voice_status.write("voicemail_success")
                        break
            else:
                file1.write("Unable to get the version\n")
            #file_service2x.close()
        except:
            file1.write("unable to load sso")

# ssoobj=ssoclass()
# ssoobj.ssofn()










