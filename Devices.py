#get the list of devices
#you will get 4 devices
#go to the url of each device
#in that device .. go to provision.. uri..
import time
import re
import requests
import base64
import tkMessageBox
from ManualLogin import *
from UserDetails import *

#import user_details
class devices:
     #writing into device details all the xmls of all  the devices
     def devicesfn(self):
        file_final_device_details = open(manualobj.browseValue + "/Final_devices.txt", "a+")
        try:
            fileobj1 = open(manualobj.browseValue+"/credentials.txt", "r").read()
            ff = open(manualobj.browseValue+"/Final_devices.txt", "w+")
            file_final_device_details = open(manualobj.browseValue+"/Final_devices.txt", "a+")
            fo  = open(manualobj.browseValue+"/device_details.txt","w+")

            file = open(manualobj.browseValue+"/userConfig.xml","r")
            filedata = file.read()
            ff = open(manualobj.browseValue + "/_new.xml", "w+")
            file_cnf = open(manualobj.browseValue + "/_cnf.txt", "w+")
                # try :
            device_uri = re.findall(r'<devices uri="(.*?)"/>',filedata,re.I|re.M)  #getting url from the user config
            print(device_uri)
            #print("HELLO")





            #print(fileobj1)
        #print("att",att[0],"att2",att[1])

            username = re.findall(r'Username:(.*)\n',fileobj1,re.I|re.M)
            password = re.findall(r'Password:(.*)\n',fileobj1,re.I|re.M)
            password = base64.b64decode(password[0])

            # print("user",username,"pass",password)
            # #password=base64.b64decode(bytes(password))
            # #print password
            # print("hi",username)
            # print("bye",password)
            response = requests.get(device_uri[0],verify=False,auth = (username[0],password))

            file1 = open(manualobj.browseValue+"/device.txt","w+")
            file1.write(response.text)

            devices = re.findall(r'<device uri="(.*?)">', response.text, re.I | re.M) #getting the list of devices
            print(devices)
            device_name = re.findall(r'<name>(.*?)</name>',response.text,re.I |re.M)  #getting list of device names
            file_device = open(manualobj.browseValue+'/Devicelist.txt', 'w+')
            for line in devices:
                 file_device.write(line + "\n")
                 #devicelist has been obtained from device
            # file_device.close()
            description_editable = re.findall(r'<description editable="(.*?)"',response.text,re.I|re.M)  #fetching the devices and their editable from user/devices url

            i = 0
            count = 0
            for line in devices :    #for each device there will be 2 urls
                file_Device_details = open(manualobj.browseValue+"/device_details.txt", "w+")
                file_read = open(manualobj.browseValue+"/device_details.txt", "r")
                file_devicelist = open(manualobj.browseValue+"/Devicelist.txt","r")

                #print(line) #get the url only if editable is true
                #print ((description_editable[i]), i )
                #file_Device_details = open("C:\Python27\device_details.txt", "w+")

                print(description_editable,"\n")
                if ((description_editable[i]) == "true") : # if description editable is true, we need 2 urls which we get by querying the device url from the devicelist

                    response = requests.get(line, verify=False, auth=(username[0],password))  #getting each device url with editable as true

                    file_Device_details.write(response.text)
                    cnf_xml = re.findall(r'<uri>(.*?)</uri>',response.text,re.I|re.M) #getting 2 urls for each device
                    dn_xml=re.findall(r'<extensions uri="(.*?)"/>',response.text,re.I|re.M)
                    print dn_xml[0],"dn_xml"


                    file_final_device_details.write("\n--------------------------------------------------------------------------------------\n")
                    file_final_device_details.write("DEVICE NAME "+ device_name[i]) #beginning of final devices
                    #file_final_device_details.write(
                       # "\n\n************************************************************************\n")

                   # for line1 in cnf_xml :
                        #print("count",count)
                        #count+=1
                    print("CNF",cnf_xml[0])

                    file_cnf1= open(manualobj.browseValue+"/_cnf.txt","r").read()
                    file_dn=open(manualobj.browseValue+"/dn.txt",'w')
                    dn_response=requests.get(dn_xml[0] , verify = False , auth = (username[0],password))
                    file_dn.write(dn_response.text)

                    cnf_response = requests.get(cnf_xml[0], verify = False, auth = (username[0],password[0]))
                    file_final_device_details.write("\n---------------------------------------------------------------------------------------\n")
                    #print("\ncnf_response",cnf_response.text)
                    #cap = re.findall(r'<capfAuthMode>(.*?)</capfAuthMode>', cnf_response.text)

                    #file_cnf.write(cnf_response.text)
                    #file_cnf_read = open("C:\Python27\_cnf.txt","r").read()
                    file_cnf.write(cnf_response.text)
                    #file_cnf1.write(cnf_response.text)

                    ff.write(file_cnf1)
                    cap = re.findall(r'<capfAuthMode>(.*?)</capfAuthMode>',cnf_response.text)

                    dirno = re.findall(r'<directoryNumber>(.*?)</directoryNumber>',dn_response.text)
                    for dno in dirno:
                        print dirno, "dirno"
                        file_final_device_details.write("DirectoryNumber"+"\t\t\t\t\t"+dno+"\n")


                    for li in cap :
                        print("li",li)
                        if int(li) == 0:
                            file_final_device_details.write("\nAuthentication Mode " + "\t\t\t\t\t" + "None")
                        elif int(li) == 1:
                            file_final_device_details.write("\nAuthentication Mode " + "\t\t\t\t\t" + "By Authentication String")

                        elif int(li) == 2:
                            file_final_device_details.write("\nAuthentication Mode " + "\t\t\t\t\t" + "By Null String")

                        elif int(li) == 3:
                            file_final_device_details.write("\nAuthentication Mode " + "\t\t\t\t\t" + "By Existing Certificate (precedence to LSC)")

                        elif int(li) == 4:
                            file_final_device_details.write("\nAuthentication Mode " + "\t\t\t\t\t" + "By Existing Certificate (precedence to MIC)")



                    timer_register_expire = re.findall(r'<timerRegisterExpires>(.*?)</timerRegisterExpires>', cnf_response.text, re.I | re.M)

                    for line in timer_register_expire:
                        file_final_device_details.write("\nTimer register expires : " + "\t\t\t\t\t" + line)

                    timer_register_delta = re.findall(r'<timerRegisterDelta>(.*?)</timerRegisterDelta>', cnf_response.text, re.I | re.M)

                    for line in timer_register_delta:
                        file_final_device_details.write("\nTimer register delta : " + "\t\t\t\t\t" + line)

                    timer_keepalive_expire = re.findall(r'<timerKeepAliveExpires>(.*?)</timerKeepAliveExpires>', cnf_response.text,
                                                re.I | re.M)

                    for line in timer_keepalive_expire:
                        file_final_device_details.write("\nTimer keep alive expires : " + "\t\t\t\t\t" + line)

                    timer_subscribe = re.findall(r'<timerSubscribeExpires>(.*?)</timerSubscriberExpires>', cnf_response.text, re.M | re.I)

                    for line in timer_subscribe:
                        file_final_device_details.write("\nTimer subscribe expires : " + "\t\t\t\t\t" + line)

                    timer_subscribe_delta = re.findall(r'<timerSubscribeDelta>(.*?)</timerSubscribeDelta>', cnf_response.text, re.I | re.M)

                    for line in timer_subscribe_delta:
                        file_final_device_details.write("\nTimer subscribe delta expires in : " + "\t\t\t\t\t" + line)
                        #
                        # #list = ["DevicePool\t\t", "DateTimeSetting\t\t", "Call Manager Group\t", " ", " ", " ", "Audio name\t\t",
                        # #          " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "]
                        # # name = re.findall(r'<name>(.*?)</name>', filedata_device, re.I | re.M)
                        # # i = 0
                        # # for line in name:
                        # #     if list[i] != " ":
                        # #         file_final_device_details.write(" \n" + list[i] + " : " + "\t\t\t\t" + line)
                        # #             # file1.write(line)
                        # #     i += 1
                        #
                        # #devicepool
                        #
                        # # str = str(filedata_device)
                        # # print(str)
                        # # devicepool_p = re.findall(r'<callManagerGroup>\r\n<name>(.*?)</name>',str,re.__all__)
                        # # for line in devicepool_p :
                        # #     print("DEVICEPOOL "+ line)
                        # #     file_final_device_details.write("\nDevicepool"+"\t\t\t\t"+ line)
                        # #
                        # #
                        # # name = re.findall(r'<name>(.*?)</name>',str,re.I|re.M)
                        # # print("\n",name,"\$")
                        # # for line in name:
                        # #     file_final_device_details.write("\nName :\t\t\t"+ line)
                        #
                    dscpForAudio = re.findall(r'>(.*?)</dscpForAudio>', cnf_response.text, re.I | re.M)

                    for line in dscpForAudio:
                        file_final_device_details.write("\nDscp For Audio " + "\t\t\t\t        " + line)

                    dscpVideo = re.findall(r'>(.*)</dscpVideo>', cnf_response.text, re.I | re.M)

                    for line in dscpVideo:
                        file_final_device_details.write("\nDscp For Video " + "\t\t\t\t        " + line)
                        #
                        # ############################################
                    deviceSecurityMode = re.findall(r'<deviceSecurityMode>(.*?)</deviceSecurityMode>', cnf_response.text, re.I | re.M)
                    for line in deviceSecurityMode:
                        file_final_device_details.write("\nDevice Security Mode" + "\t\t\t\t\t" + line)
                        #
                        #
                        #
                    processNodeName = re.findall(r'<processNodeName>(.*?)</processNodeName>', cnf_response.text,re.I|re.M)
                    for line in processNodeName:
                        file_final_device_details.write("\nProcess Node Name " + "\t\t\t\t\t" + line)

                    ownerid = re.findall(r'>(.*?)</ownerId>', cnf_response.text, re.I | re.M)
                    for line in ownerid:
                        file_final_device_details.write("\nOwner ID " + "\t\t\t\t\t" + line)

                    desktopclient = re.findall(r'<desktopClient>(.*?)</desktopClient>', cnf_response.text)
                    #print(desktopclient)
                    #sep = re.findall(r'<SEP>',device_name[i],re.I|re.M)
                    sep = re.match(r'SEP',device_name[i])


                    print("SEP",device_name[i],sep)
                    if (desktopclient == [] and sep == None ) :
                     if timer_register_delta != 120:
                        logging.warning("Timer register delta mismatch!")
                        file_final_device_details.write("\n\nWARNING! Timer register delta mismatch! ")
                     if timer_register_expire != 720:
                        logging.warning("Timer register expires mismatch!")
                        file_final_device_details.write("\nWARNING! Timer register expires mismatch! ")
                     if timer_keepalive_expire != 720:
                        logging.warning("Timer keep alive mismatch!")
                        file_final_device_details.write("\nWARNING! Timer keep alive mismatch! ")
                     if timer_subscribe != 21600:
                        logging.warning("Timer subscribe expire mismatch!")
                        file_final_device_details.write("Timer subscribe expire mismatch! ")
                     if timer_subscribe_delta != 15:
                        logging.warning("WARNING! Timer subscribe delta mismatch! ")
                        file_final_device_details.write("Timer subscribe delta mismatch! ")

                    file_final_device_details.write("\n")
                         #print("\nValue of i",i


                i+=1


        except Exception as e:
            logging.error(str(e))
            #print("Error run user details")
            file_final_device_details.write("Unable to load devices")
            #tkMessageBox.showerror("Login error", "Run user details")





# start = time.time()
#devicesobj=devices()
# devicesobj.devicesfn()
# devicesobj.out=open("C:/Python27/Final_devices.txt",'r').read()
# time = time.time()-start
# print("TIME TAKEN ",time,"**")