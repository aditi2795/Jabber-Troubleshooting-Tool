import socket
import ssl
import subprocess
import re
import base64
from xml.etree import ElementTree as ET
import requests
import urllib2
import types
from UserDetails import system
from GetDns import dnsclass
from ManualLogin import *
from ServiceProfile import *



class impclass():
    def impfn(self):
        dnsobject = dnsclass()
        file2 = open(manualobj.browseValue+"/otp.txt", 'w+')
        file1 = open(manualobj.browseValue+"/imp_soap_response.txt", 'w+')
        file3 = open(manualobj.browseValue+"/get_all_config.txt", 'w+')
        file4=open(manualobj.browseValue+"/imp_login.txt",'w+')
        file5=open(manualobj.browseValue+"/imp_xmpp_messages.txt",'w+')
        file_summary=open(manualobj.browseValue+'/imp_summary.txt','w+')
        file_status = open(manualobj.browseValue+'/imp_status.txt','w+')
        try:
            if manualobj.impflag==0:
                file = open(manualobj.browseValue+"/service.txt", 'r').read()
                info = file.split('\n')
                for row in info:

                    if "IMP" in row:
                        IMP1 = row.split(':')[2]
                        print (IMP1)
                        try:
                            IMP1_IP = socket.gethostbyname(IMP1)
                            impip=IMP1_IP
                        except:
                            file_status.write("imp_unreachable")
                            file_summary.write("Unable to reach the server or unable to resolve fqdn")
                        print impip, "impip"
                        break

            else:
                fileimp=open(manualobj.browseValue+"/impmanualip.txt",'r')
                fileimp1=fileimp.read()
                print (fileimp1)
                impip=str(fileimp1)
            file=open(manualobj.browseValue+"/credentials.txt",'r').read()
            info=file.split('\n')
            for row in info:
                if 'Username' in row:

                    userName=row.split(":")[1]
                    print userName
                if "Password" in row:
                    password=row.split(":")[1]
                    print password
                    password=base64.b64decode(bytes(password))
            #userName='ambabu'
            #password='C1sc0123!'

            userNameUtf8 = userName.encode('utf-8')
            passwordUtf8 = password.encode('utf-8')
            #print userNameUtf8, passwordUtf8, " usenameutf8, passwordutf8"
            jabberAuthSoapHeaders = {u'Content-Type': 'application/soap+xml; charset=utf-8',

                                     'SOAPAction': u'urn:cisco:epas:soap/EpasSoapServiceInterface/login'}
            jabberAuthSoapBody = """<?xml version="1.0" encoding="UTF-8"?>
            <SOAP-ENV:Envelope xmlns:SOAP-ENV="http://www.w3.org/2003/05/soap-envelope"
            xmlns:SOAP-ENC="http://www.w3.org/2003/05/soap-encoding"
            xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
            xmlns:xsd="http://www.w3.org/2001/XMLSchema"
            xmlns:ns1="urn:cisco:epas:soap">
            <SOAP-ENV:Body><ns1:login client-version="9.7.0.18474"
            client-type="CUPC" force="true"><ns1:username>%s</ns1:username>
            <ns1:password>%s</ns1:password>
            </ns1:login></SOAP-ENV:Body>
            </SOAP-ENV:Envelope>""".encode('utf-8') % (userNameUtf8, passwordUtf8)
            # SoapAuthentication
            jabberAuthRequest = requests.post('https://'+impip+':8443/EPASSoap/service/v80',
                                              verify=False,
                                              data=jabberAuthSoapBody, headers=jabberAuthSoapHeaders)
            print "jabberAuthRequest.status_code -" + str(jabberAuthRequest.status_code)

            if jabberAuthRequest.status_code==200:
                file1.write(jabberAuthRequest.text)
                jabberAuthResponse = ET.fromstring(jabberAuthRequest.text.encode('utf-8'))
                print ("jabberAuthResponse -" + str(jabberAuthResponse))
                sessionKey = jabberAuthResponse.find('{http://www.w3.org/2003/05/soap-envelope}Body/{urn:cisco:epas:soap}login-resp/{urn:cisco:epas:soap}success/')
                if type(sessionKey)!=NoneType:
                    file4.write("SOAP LOGIN"+" "*(20-(len("SOAP LOGIN")))+":SUCCESSFUL\n")
                    file4.write("SESSION KEY"+" "*(20-(len("SESSION KEY")))+":"+str(sessionKey.text)+"\n")
                else:
                    file4.write("SOAP LOGIN" + " " *(20 - (len("SOAP LOGIN"))) + ":Failed\n")
                    file4.write("SESSION KEY" + " " *(20 - (len("SESSION KEY"))) + ":" +"N/A" + "\n")
                    file4.write("GET ALL CONFIG" + " " * (20 - len("GET ALL CONFIG")) + ":FAILURE\n")
                    file4.write("PRESENCE DOMAIN" + " " * (20 - len("PRESENCE DOMAIN")) + str(":PRESENCE DOMAIN NOT FOUND\n"))
                    file4.write("OTP" + " " * (20 - len("OTP")) + ":FAIL\n")
                    file4.write("XMPP AUTHENTICATION" + " " * (20 - len("XMPP AUTHENTICATION")) + ":FAIL\n")
                    file_summary.write("SOAP LOGIN" + " " * (20 - (len("SOAP LOGIN"))) + ":Failed\n")
                    file_summary.write("SESSION KEY" + " " * (20 - (len("SESSION KEY"))) + ":" + "N/A" + "\n")
                    file_summary.write("GET ALL CONFIG" + " " * (20 - len("GET ALL CONFIG")) + ":FAILURE\n")
                    file_summary.write(
                        "PRESENCE DOMAIN" + " " * (20 - len("PRESENCE DOMAIN")) + str(":PRESENCE DOMAIN NOT FOUND\n"))
                    file_summary.write("OTP" + " " * (20 - len("OTP")) + ":FAIL\n")
                    file_summary.write("XMPP AUTHENTICATION" + " " * (20 - len("XMPP AUTHENTICATION")) + ":FAIL\n")


            else:
                file1.write("Unable to load page \n Check if the user is assigned for im and presence")

            # get User Config
            if type(sessionKey) != NoneType:
                jabberUserConfigHeaders = {u'Content-Type': 'application/soap+xml; charset=utf-8',
                                           'SOAPAction': u'urn:cisco:epas:soap/EpasSoapServiceInterface/get_all_config'}

                jabberUserConfigSoapBody = """<?xml version="1.0" encoding="UTF-8"?>
                <soapenv:Envelope xmlns:soapenv="http://www.w3.org/2003/05/soap-envelope"
                                  xmlns:xsd="http://www.w3.org/2001/XMLSchema"
                                  xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
                                  xmlns:epas="urn:cisco:epas:soap"
                                  xmlns="urn:cisco:epas:soap">
                   <soapenv:Header>
                      <session-key>%s</session-key>
                   </soapenv:Header>
                   <soapenv:Body>
                      <get-all-config>
                          <system-config/>
                          <user-config/>
                          <federated-domains auth-policy="all"/>
                          <non-presence-aware-contacts/>
                          <contact-info/>
                      </get-all-config>
                   </soapenv:Body>
                </soapenv:Envelope>""" % sessionKey.text

                jabberUserConfigRequest = requests.post('https://'+impip+':8443/EPASSoap/service/v80',
                                                        verify=False,
                                                        data=str(jabberUserConfigSoapBody), headers=jabberUserConfigHeaders)

                print "jabberUserConfigRequest.status_code-" + str(jabberUserConfigRequest.status_code)
                if jabberUserConfigRequest.status_code==200:
                    file3.write(jabberUserConfigRequest.text)
                    flag=0
                    if "Invalid request" in jabberUserConfigRequest.text:
                        flag=1
                    if flag!=1:
                        jabberUserConfig = ET.fromstring(jabberUserConfigRequest.text.encode('utf-8'))
                        jabberPresenceDomain = jabberUserConfig.find("{http://www.w3.org/2003/05/soap-envelope}Body/{urn:cisco:epas:soap}get-all-config-resp/{urn:cisco:epas:soap}get-system-config-resp/{urn:cisco:epas:soap}property[@name='Presence.Domain']")
                        file4.write("GET ALL CONFIG"+" "*(20-len("GET ALL CONFIG"))+":SUCCESSFUL\n")
                        print (jabberPresenceDomain)
                        if type(jabberPresenceDomain)!=NoneType:
                            file4.write("PRESENCE DOMAIN"+" "*(20-len("PRESENCE DOMAIN"))+":"+str(jabberPresenceDomain.text)+"\n")
                        else:
                            file4.write("PRESENCE DOMAIN" + " " * (20 - len("PRESENCE DOMAIN")) + str("PRESENCE DOMAIN NOT FOUND\n"))
                            file_summary.write("PRESENCE DOMAIN" + " " * (20 - len("PRESENCE DOMAIN")) + str(
                                "PRESENCE DOMAIN NOT FOUND\n"))
                    else:
                        file4.write("GET ALL CONFIG" + " " * (20 - len("GET ALL CONFIG")) + ":FAILURE\n")
                        file4.write("PRESENCE DOMAIN" + " " * (20 - len("PRESENCE DOMAIN")) + str(":PRESENCE DOMAIN NOT FOUND\n"))
                        file_summary.write("GET ALL CONFIG" + " " * (20 - len("GET ALL CONFIG")) + ":FAILURE\n")
                        file_summary.write(
                        "PRESENCE DOMAIN" + " " * (20 - len("PRESENCE DOMAIN")) + str(":PRESENCE DOMAIN NOT FOUND\n"))



                # One Time Password


                # jabberOTPSoapHeaders = {'SOAPAction': 'urn:cisco:epas:soap/EpasSoapServiceInterface/get_onetime_password', 'Content-Type': 'application/soap+xml; charset=utf-8; \
                # action="urn:cisco:epas:soap/EpasSoapServiceInterface/get_onetime_password'}
                if flag != 1:
                    jabberOTPSoapBody = """<?xml version="1.0" encoding="UTF-8"?>
                     <soapenv:Envelope xmlns:soapenv="http://www.w3.org/2003/05/soap-envelope"
                     xmlns:xsd="http://www.w3.org/2001/XMLSchema"
                    xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
                    xmlns:epas="urn:cisco:epas:soap" xmlns="urn:cisco:epas:soap">
                       <soapenv:Header>
                         <session-key>%s</session-key>
                       </soapenv:Header>
                       <soapenv:Body>
                     <get-onetime-password/>
                     </soapenv:Body>
                     </soapenv:Envelope>""" % sessionKey.text

                    jabberOTPRequest = requests.post('https://'+impip+':8443/EPASSoap/service/v80',
                                                     verify=False,
                                                     data=str(jabberOTPSoapBody))
                    print (jabberOTPRequest.status_code)
                    jabberOTPResponse = jabberOTPRequest.text

                    file2.write(jabberOTPResponse)
                    flag2=0
                    if "Invalid request" in jabberOTPResponse:
                        flag2=1
                    if flag2!=1:
                        jabberOTPResponse = ET.fromstring(jabberOTPResponse.encode('utf-8'))
                        oneTimePassword = jabberOTPResponse.find(
                            '{http://www.w3.org/2003/05/soap-envelope}Body/{urn:cisco:epas:soap}get-onetime-password-resp/{urn:cisco:epas:soap}success/{urn:cisco:epas:soap}password')
                        print (oneTimePassword.text)
                        file4.write("OTP"+" "*(20-len("OTP"))+":SUCCESSFUL\n")
                        file4.write("OTP Value" + " " * (20 - len("OTP Value")) + ":"+str(oneTimePassword.text)+"\n")

                        # Authenticate with XMPP

                        # Create the VTG Auth Token

                        xmppToken = base64.encodestring('userid=%s@%s\0token=%s' % (userName, jabberPresenceDomain.text, oneTimePassword.text)).replace('\n', '')
                        print ('xmpptoken', xmppToken)

                        # Canned XMPP Messages
                        xmppStreamOn = "<?xml version='1.0' ?><stream:stream to='%s' xmlns='jabber:client' xmlns:stream='http://etherx.jabber.org/streams'  xml:lang='en' version='1.0'>" % jabberPresenceDomain.text
                        xmppStartTlsClient = "<starttls xmlns='urn:ietf:params:xml:ns:xmpp-tls' cookie='0'/>"
                        xmppAuthBody = '<auth xmlns="urn:ietf:params:xml:ns:xmpp-sasl" mechanism="CISCO-VTG-TOKEN">%s</auth>' % xmppToken
                        xmppStreamOff = "</stream:stream>"

                        xmppSocket = socket.socket()
                        xmppSocket.connect((impip, 5222))
                        xmppSocket.settimeout(15)

                        # Start the actual XMPP Auth Handshake
                        file5.write("Actual XMPP Auth Handshake\n")
                        file5.write("Send:"+str(xmppSocket.sendall(xmppStreamOn))+"\n")

                        # Log the next two messages. Stream on response and Features
                        file5.write("Stream on Response and Features\n")
                        file5.write("Recv:"+str(xmppSocket.recv(1024).encode('utf-8')+"\n"))
                        file5.write("Recv:"+str(xmppSocket.recv(1024).encode('utf-8')+"\n"))

                        # Send Start TLS Message and log response
                        file5.write("TLS Message and log\n")
                        file5.write("Send:"+str(xmppSocket.sendall(xmppStartTlsClient))+"\n")
                        file5.write("Recv:"+str(xmppSocket.recv(1024).encode('utf-8')+"\n"))

                        # # Start SSL
                        file5.write("Start SSL\n")
                        xmppSocket = ssl.wrap_socket(xmppSocket)
                        file5.write("Send:"+str(xmppSocket.sendall(xmppStreamOn))+"\n")
                        # Next message should be the TLS stream on response
                        file5.write("TLS stream on response\n")
                        file5.write(xmppSocket.recv(1024).encode('utf-8')+"\n")

                        xmppAuthFeatures = (xmppSocket.recv(1024))

                        authMechanisms = re.findall('<mechanism>(.*?)</mechanism>', xmppAuthFeatures)
                        if len(authMechanisms) == 0:

                            xmppSocket.close()

                        elif 'CISCO-VTG-TOKEN' not in authMechanisms:
                            print ('CISCO_VTG_TOKEN not in AUTHMECHANISM')
                        else:

                            for i in authMechanisms:
                                print (i)
                        # Finally send the authentication token

                        xmppSocket.sendall(xmppAuthBody)
                        xmppAuthResponse = xmppSocket.recv(1024)
                        file5.write(xmppAuthResponse+"\n")

                        if 'success' in xmppAuthResponse:

                            # Be polite and send a stream off
                            xmppSocket.sendall(xmppStreamOff)
                            print ("XMPP successfull")
                            file4.write("XMPP AUTHENTICATION"+" "*(20-len("XMPP AUTHENTICATION"))+":SUCCESSFUL\n")
                            file_status.write("imp_success")
                            print " IM&P Running before certificate"
                        else:
                            print ('XMPP error')
                            file4.write("XMPP AUTHENTICATION" + " " * (20 - len("XMPP AUTHENTICATION")) + ":FAIL\n")
                            file_status.write("imp_fail")
                        # Close the socket
                        xmppSocket.close()

                    else:
                        file4.write("OTP" + " " * (20 - len("OTP")) + ":FAILURE\n")
                        file4.write("OTP Value" + " " * (20 - len("OTP Value")) + ":" + "N/A" + "\n")
                        file4.write("XMPP AUTHENTICATION" + " " * (20 - len("XMPP AUTHENTICATION")) + ":FAIL\n")
                        file_status.write("imp_fail")
        except:
            file4.write("SOAP LOGIN" + " " * (20 - (len("SOAP LOGIN"))) + ":Failed\n")
            file4.write("SESSION KEY" + " " * (20 - (len("SESSION KEY"))) + ":" + "N/A" + "\n")
            file4.write("GET ALL CONFIG" + " " * (20 - len("GET ALL CONFIG")) + ":FAILURE\n")
            file4.write("PRESENCE DOMAIN" + " " * (20 - len("PRESENCE DOMAIN")) + str(":PRESENCE DOMAIN NOT FOUND\n"))
            file4.write("OTP" + " " * (20 - len("OTP")) + ":FAIL\n")
            file4.write("XMPP AUTHENTICATION" + " " * (20 - len("XMPP AUTHENTICATION")) + ":FAIL\n")
            file_summary.write("SOAP LOGIN" + " " * (20 - (len("SOAP LOGIN"))) + ":Failed\n")
            file_summary.write("SESSION KEY" + " " * (20 - (len("SESSION KEY"))) + ":" + "N/A" + "\n")
            file_summary.write("GET ALL CONFIG" + " " * (20 - len("GET ALL CONFIG")) + ":FAILURE\n")
            file_summary.write(
                "PRESENCE DOMAIN" + " " * (20 - len("PRESENCE DOMAIN")) + str(":PRESENCE DOMAIN NOT FOUND\n"))
            file_summary.write("OTP" + " " * (20 - len("OTP")) + ":FAIL\n")
            file_summary.write("XMPP AUTHENTICATION" + " " * (20 - len("XMPP AUTHENTICATION")) + ":FAIL\n")
            file_status.write("imp_fail")
