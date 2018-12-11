import re
import requests
from xml.dom import minidom
file_xml=open("C:\Users\\anshsinh\Desktop\collab\New_folder\jabber_local_cnf.xml",'w')
file_txt=open("C:\Users\\anshsinh\Desktop\collab\New_folder\jabber_local_cnf.txt",'w')
cnf_response=open("C:\Users\\anshsinh\Desktop\collab\New_folder\_cnf.txt",'r').read()
url = re.findall(r'<ciscoSupportField>(.*?)</ciscoSupportField>', cnf_response, re.I | re.M)
url=url[0]
url = url.split('=')
print url[1]
response = requests.get("http://" + '10.127.230.200' + ":6970/"+url[1], verify=False)
if response.status_code==200:
    file_xml.write(response.text)
else:
    file_txt.write(" unable to load local config file")

file_xml.close()
config_local = minidom.parse("C:\Users\\anshsinh\Desktop\collab\New_folder"+"/jabber_local_cnf.xml")
Client=config_local.getElementsByTagName("config")[0]
file_txt.write("\n\nConfig\n")
file_txt.write("------\n\n")
for node in Client.childNodes:
    if node.hasChildNodes:
        for cn in node.childNodes:
            if cn.nodeType==cn.TEXT_NODE:
                file_txt.write(str(node.tagName)+" "*(40-len(str(node.tagName))) +":"+ str(cn.wholeText)+'\n')
