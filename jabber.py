import requests
from xml.dom import minidom
from UserDetails import *
from ManualLogin import *

class jabber_():

    def jabber(self):
        file1 = open(manualobj.browseValue+"/jabber_conf.txt", 'w+')
        file = open(manualobj.browseValue+"/jabber_config.xml", 'w+')
        file2=open(manualobj.browseValue+"/jabber_config.txt",'w+')
        file2.write("GLOBAL CONFIGURATION FILE\n")
        file2.write("-------------------------")
        file3=open(manualobj.browseValue+"/jabberlog.txt",'w+')
        file_status = open(manualobj.browseValue + "/jabber_config_status.txt", 'w')


        filex=open(manualobj.browseValue+"/userdetails.txt",'r').read()
        try:
            fqdn=[]

            for row in filex.split('\n'):
                if "serviceProfile" in row:
                    fqdn=row.split("=")[1]
                    fqdn=fqdn.split()
                    fqdn.append(fqdn)
            print fqdn
            length=len(fqdn)
            ipname=[]
            print length
            for j in range(length):
                if "6970" in fqdn[j]:
                    item=str(fqdn[j]).split(":6970")[0]
                    ipname.append(item)
                    ipname= str(ipname[0])
                    ipname=ipname.split("http://")[1]
                    print ipname

                    ip=socket.gethostbyname(str(ipname))
                    response = requests.get("http://" + ip + ":6970/jabber-config.xml", verify=False)
                    if response.status_code == 200:
                        file.write(response.text)
                        break
                    else:
                        file3.write(ipname+"Failed")


            #for item in range(length):
            file.close()
            config = minidom.parse(manualobj.browseValue+"/jabber_config.xml")
            Client=config.getElementsByTagName("Client")[0]
            file2.write("\n\nCLIENT\n")
            file2.write("------\n\n")
            for node in Client.childNodes:
                if node.hasChildNodes:
                    for cn in node.childNodes:
                        if cn.nodeType==cn.TEXT_NODE:
                            file2.write(str(node.tagName)+" "*(40-len(str(node.tagName))) +":"+ str(cn.wholeText)+'\n')

            Options = config.getElementsByTagName("Options")[0]
            file2.write('\n\nOPTIONS\n')
            file2.write("-------\n\n")
            for node in Options.childNodes:
                if node.hasChildNodes:
                    for cn in node.childNodes:
                        if cn.nodeType == cn.TEXT_NODE:
                            file2.write(str(node.tagName) + " "*(40-len(str(node.tagName))) +":"+ str(cn.wholeText)+'\n')

            Policies = config.getElementsByTagName("Policies")[0]
            file2.write('\n\nPOLICIES\n')
            file2.write("--------\n\n")
            for node in Policies.childNodes:
                if node.hasChildNodes:
                    for cn in node.childNodes:
                        if cn.nodeType == cn.TEXT_NODE:
                            file2.write((node.tagName) + " "*(40-len(str(node.tagName))) +":"+ str(cn.wholeText)+'\n')

            Directory = config.getElementsByTagName("Directory")[0]
            file2.write('\n\nDIRECTORY\n')
            file2.write("---------\n\n")
            for node in Directory.childNodes:
                if node.hasChildNodes:
                    for cn in node.childNodes:
                        if cn.nodeType == cn.TEXT_NODE:
                            file2.write(str(node.tagName) + " "*(40-len(str(node.tagName))) +":"+ str(cn.wholeText)+'\n')
            file_status.write("jabber_config_success\n")
        except:
            file2.write("unable to load jabber config")
            file2.write("Unable to download Jabber configuration file ")



        try:
            file_field=open(manualobj.browseValue + "\cnf_url.txt",'w')
            file_txt = open(manualobj.browseValue + "\jabber_local_config.txt", 'w')
            file_txt.write("\nLocal Configuration File\n")


            cnf_response = open(manualobj.browseValue+"\_cnf.txt", 'r').read()
            url = re.findall(r'<ciscoSupportField>(.*?)</ciscoSupportField>', cnf_response, re.I | re.M)
            for line in url:

                url_1 = url[0]
                url_1 = url_1.split('=')
                file_field.write(url_1[1])
                file_field.write('\n')
            file_field.close()


            file_read = open(manualobj.browseValue + "\cnf_url.txt",'r').read()
            print file_read, "file content"
            for row1 in file_read.split('\n'):

                print ip,"ip"
                print type(row1),row1,'row'
                if row1!= "":


                    response = requests.get("http://" + ip + ":6970/" + row1, verify=False)
                    file_xml = open(manualobj.browseValue + "\jabber_local_config.xml", 'w')
                    if response.status_code == 200:
                        file_xml.write(response.text)
                    else:
                        file_txt.write(" unable to load local config file")

                    file_xml.close()
                    config_local = minidom.parse(manualobj.browseValue+"\jabber_local_config.xml")
                    Client = config_local.getElementsByTagName("config")[0]
                    file_txt.write("\n\nConfig\n")
                    file_txt.write("------\n\n")
                    for node in Client.childNodes:
                        if node.hasChildNodes:
                            for cn in node.childNodes:
                                if cn.nodeType == cn.TEXT_NODE:
                                    if node.tagName == "ConnectionPassword":
                                        file_txt.write(str(node.tagName) + " " * (40 - len(str(node.tagName))) + ":" + str("*****") + '\n')
                                    else:
                                        file_txt.write(str(node.tagName) + " " * (40 - len(str(node.tagName))) + ":" + str(
                                            cn.wholeText) + '\n')
        except:
            file_txt.write(" unable to load local config file")


# obj=anshu()
# obj.anshufn()
#obj.out=open("c:/Python27/jabber_config.txt",'r').read()