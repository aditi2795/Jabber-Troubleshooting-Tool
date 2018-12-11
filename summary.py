import subprocess
from powershell import *
from ManualLogin import *
import re
from xml.dom.minidom import parse
from xml.dom import minidom
import requests
from GetDns import dnsobject

class summary():
    def summaryfn(self):
        file=open(manualobj.browseValue+"/sysdetails.txt",'r').read()
        file1=open(manualobj.browseValue+"/summary.txt",'w+')
        try:

            theDomain =dnsobject.domain
            r = requests.get('http://loginp.webexconnect.com/cas/FederatedSSO?org=' + theDomain)
            result = r.text
            file_webex = open("Webex Response.xml", 'w')
            file_webex.write(result)
            file_webex.close()
            webex = minidom.parse("Webex Response.xml")
            value = webex.getElementsByTagName("errorcode")[0].firstChild
            error_code = value.data[0]
            print error_code
            if error_code == "1":
                file1.write("\nNot Enabled for WebEx\n")
            else:
                file1.write("\nEnabled for Webex\n")
        except:
            pass
        try:
            for row in file.split('\n'):
                if "Microsoft Lync" in row:
                    file1.write(str(row)+"\n")
                if "WebEx Productivity Tools" in row:
                    file1.write(str(row) + "\n")
                if "McAfee VirusScan Enterprise" in row or "Kaspersky" in row or "Norton" in row or "QuickHeal" in row:
                    file1.write(str(row) + "\n")
                if "Cisco AnyConnect" in row :
                    file1.write(str(row) + "\n")
                if "Check Point VPN" in row :
                    file1.write(str(row) + "\n")

                if "Plantronics Hub" in row:
                    file1.write(str(row)+"\n")
                if "Skype" in row:
                    file1.write(str(row)+"\n")

                if "Available Physical Memory" in row:
                    row=row.split(":")[1]
                    row = filter(lambda name: name.strip(), row)
                    item= row.split("MB")[0]
                    item=(int(item.replace(",","")))
                    if item < 128:
                        file1.write("\nAvailable Physical Memory is less than 128MB\n")

                if "Virtual Memory: Available:" in row:
                    row = row.split(":")[2]
                    row = filter(lambda name: name.strip(), row)
                    item = row.split("MB")[0]
                    item = (int(item.replace(",", "")))
                    if item < 256:
                        file1.write("\nAvailable Free Disk Space is less than 256 MB\n")

                if "OS Name: " in row:
                    row = row.split()
                    row1 = int(str(row[4]))
                    if row1 < 7:
                        file1.write("\n The OS version is not supported\n")

                if "Internet Explorer " in row:
                    row = row.split()
                    row1 = str(row[2])
                    row2 = row1.split('.')
                    if int(str(row2[0])) < 9:
                        file1.write("\nThe Internet Explorer version is not supported\n")

            output = subprocess.check_output("ipconfig /all", shell=True)
            for row in output.split('\n'):
                row = filter(None, row)

                if "IPv6" in row:

                    file1.write("\nYour computer has IPv6 Address and hence refer 'IPv6 Requirements' to know more about Jabber behaviour")
                    break




        except:
            file1.write("ERROR")
        try:
            file_devices=open(manualobj.browseValue+"/Final_devices.txt",'r').read()
            if "unable to load devices" in file_devices:
                file1.write("\nDevices\n")
                file1.write("Error in Getting Devices Details\n\n")
        except:
            pass
