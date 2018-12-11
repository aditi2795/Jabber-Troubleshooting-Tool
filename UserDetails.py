import urllib2
import ssl
from requests.auth import HTTPBasicAuth
from xml.etree import ElementTree as ET
import re
import requests
from GetDns import *
import socket
#import mock_login
import Tkinter
import tkMessageBox
from xml.dom import minidom
#import wxpython as wx
import time
import base64
from MockLogin import *
import logging
from ManualLogin import *


from tkinter import messagebox
# Create an OpenerDirector with support for Basic HTTP Authentication...
# Create an OpenerDirector with support for Basic HTTP Authentication...
class system:
    username = ""
    email = ""
    impserver = ""
    enableimppresence = ""
    serviceprofile = ""

    def usersys(self):

       file1 = open(manualobj.browseValue + "/userdetails.txt", "w+")
       file_cred = open(manualobj.browseValue + "/credentials.txt", "r").read()
       file_summary = open(manualobj.browseValue + '/usersummary.txt', 'w')
       file_status= open(manualobj.browseValue + '/userdetails_status.txt', 'w')
       try :



        logging.basicConfig(filename= manualobj.browseValue+'/Logs.log',level = logging.DEBUG)
        LOG_FILENAME = manualobj.browseValue+'/Log.log'
        logging.basicConfig(filename=LOG_FILENAME, level=logging.DEBUG)


        username = re.findall(r'Username:(.*?)\n',file_cred,re.I|re.M)
        password = re.findall(r'Password:(.*?)\n',file_cred,re.I|re.M)



        if username != [] and password != [] :
            password = base64.b64decode(password[0])
            file = open(manualobj.browseValue+"/userConfig.xml", "w")
            logging.debug("Credentials not empty")
            flag = 0

            length = len(dnsobject.serv)
            print (length, "dnsobject.serv length")
            try:
                for list in range(length):
                    ip = dnsobject.serv[list]
                    print (ip)
                    ip = socket.gethostbyname(ip)
                    print ip


                    response = requests.get('https://' + ip + ':8443/cucm-uds/user/' + username[0], verify=False,
                                            auth=(username[0], password))

                    print (response.status_code, "response code of user details")
                    if response.status_code == 200:
                        flag=1
                        logging.debug("Succesful query to cucm-uds")
                        file_summary.write("Authentication Successful\n")
                        break

                    elif response.status_code==404:
                        logging.error("Unable to reach the cucm server")
                        file_summary.write("\nUnable to reach the CUCM server\n\n ERROR CODE 404\n")
                        file_status.write("userdetails_fail\n")


                    elif response.status_code==401:
                        logging.error("Invalid username or password")
                        file_summary.write("\nInvalid Username or Password\n ERROR CODE 401\n")
                        file_status.write("authentication_fail\n")
                        file_status.write("userdetails_fail\n")
                    else:
                        file_summary.write("\n Unable to fetch the user details\n ")
                        file_status.write("userdetails_fail\n")


            except:
                file_summary.write("\nUnable to resovle the fqdn or unable to reach the server or invalid username password\n")
                file_status.write("userdetails_fail\n")




               # return 1
            if flag==1:
                file = open(manualobj.browseValue+"/userConfig.xml","w+")

                file.write(response.text)
                #print(response.text)

                file = open(manualobj.browseValue+"/userConfig.xml","r")
                filedata = file.read()
                print (filedata)
                x = re.findall(r'<!-- custom Cisco error page -->', filedata, re.I | re.M)
                # if len(x) != 0:
                #     messagebox.showerror("INVALID AUTHENTICATION", "Please enter valid credentials")
                file.close()

                # parsing data


                try:
                    xmldoc = minidom.parse(manualobj.browseValue+"/userConfig.xml")
                    server = xmldoc.getElementsByTagName("server")
                    servlength = server.length
                    service_profile = xmldoc.getElementsByTagName("uri")
                    servicelength = service_profile.length
                    for i in [1]:
                        # user = xmldoc.getElementsByTagName("user")[0]
                        # file1.write("version=" + str(user.getAttribute("version")))
                        # file1.write("\n")


                            try:
                                username = xmldoc.getElementsByTagName("userName")[0].firstChild.data
                                file1.write("userName=" + username)
                                file1.write("\n")
                            except:
                                pass
                            try:
                                firstName = xmldoc.getElementsByTagName("firstName")[0].firstChild.data
                                file1.write("firstName=" + firstName)
                                file1.write("\n")
                            except:
                                pass
                            try:
                                lastName = xmldoc.getElementsByTagName("lastName")[0].firstChild.data
                                file1.write("lastName=" + lastName)
                                file1.write("\n")
                            except:
                                pass
                            try:
                                email = xmldoc.getElementsByTagName("email")[0].firstChild.data
                                file1.write("email=" + email)
                                file1.write("\n")
                            except:
                                pass
                            try:
                                title = xmldoc.getElementsByTagName("title")[0].firstChild.data
                                file1.write("title=" + title)
                                file1.write("\n")
                            except:
                                pass
                            try:
                                directoryuri = xmldoc.getElementsByTagName("directoryUri")[0].firstChild
                                if (directoryuri) != None:
                                    file1.write("Directoryuri=" + directoryuri)
                                    file1.write("\n")
                                else:
                                    file1.write("Directoryuri=" + "No directory uri exists")
                                    file1.write("\n")
                            except:
                                pass
                            try:
                                account_type = xmldoc.getElementsByTagName("accountType")
                                for element in account_type:
                                    ldap_value = element.getAttribute("useLdapAuth")
                                file1.write("useLdapAuth=" + ldap_value)
                                file1.write("\n")
                            except:
                                pass
                            try:
                                home_cluster = xmldoc.getElementsByTagName("homeCluster")
                                for element in home_cluster:
                                    enable_for_presence = element.getAttribute("enableImAndPresence")
                                file1.write("enableImAndPresence=" + enable_for_presence)
                                file1.write("\n")
                            except:
                                pass
                            try:
                                for j in range(servicelength):
                                    service = (xmldoc.getElementsByTagName("uri")[j].firstChild.data)
                                    file1.write("serviceProfile=" + str(service))
                                    file1.write("\n")
                                    logging.debug("Getting user detals is successful ")
                                    file_status.write("userdetails_success")
                            except:
                                pass


                except:
                    logging.error("Fetching user details failed")
                    file1.write("parsing failed")
                    file_status.write("userdetails_fail\n")

       except:
              file1.write("\nunable to perform the query successfully\n")
              file_summary.write("\nunable to perform the query successfully\n  Unable to reach the server or Invalid userName and password\n")
              file_status.write("userdetails_fail\n")



sysobject=system()
#sysobject.usersys()

# sysobject.out=open('c:\Python27\userdetails.txt','r').read()
# if __name__=="__main__":
#    sysobject.usersys()
#    print(sysobject.out)