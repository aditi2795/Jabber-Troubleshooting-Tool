from socket import socket
import ssl
import socket
import subprocess
import re
import time
from ManualLogin import *

class Certs:

    def certImp(self):
        fileimp = open(manualobj.browseValue + "/certcompleteimp.txt", "w+")
        file_certimp = open(manualobj.browseValue + "/certdataimp.txt", "w+")
        try:
            if manualobj.flag!=2:
                file = open(manualobj.browseValue + "/service.txt", 'r').read()
                info = file.split('\n')
                for row in info:

                    if "IMP" in row:
                        IMP1 = row.split(':')[2]
                        print
                        IMP1
                        IMP1_IP = socket.gethostbyname(IMP1)
                        break
                        # if "IMP SECONDARY ADDRESS" in row:
                        #     IMP2 = row.split(':')[1]
                        #     print IMP2
                        # if "IMP TERTIARY ADDRESS" in row:
                        #     IMP3 = row.split(':')[1]

                # print IMP1_IP
                certificate = (ssl.get_server_certificate((IMP1_IP, 443)))
            else:
                file = open(manualobj.browseValue + "/imp_jabber.txt", 'r').read()
                info = file.split('\n')
                for row in info:

                    if "IMP" in row:
                        IMP1 = row.split(':')[2]
                        print
                        IMP1
                        IMP1_IP = socket.gethostbyname(IMP1)
                        break
                        # if "IMP SECONDARY ADDRESS" in row:
                        #     IMP2 = row.split(':')[1]
                        #     print IMP2
                        # if "IMP TERTIARY ADDRESS" in row:
                        #     IMP3 = row.split(':')[1]

                print
                IMP1_IP
                certificate = (ssl.get_server_certificate((IMP1_IP, 443)))
            try:

                file_cert_original = open(manualobj.browseValue + "/certificatesimp.der", "w+")
                file_cert_original.write(certificate)
                proc2 = subprocess.Popen("openssl x509 -in " + manualobj.browseValue + "/certificatesimp.pem -noout -text", shell=True)
                time.sleep(2)
                proc2.kill()
                file_cert_original = open(manualobj.browseValue + "/certificatesimp.pem", "w+")
                file_cert_original.write(certificate)
                proc2 = subprocess.Popen(
                    "openssl x509 -in " + manualobj.browseValue + "/certificatesimp.pem -noout -text", shell=True)
                time.sleep(2)
                proc2.kill()
                file_cert_original = open(manualobj.browseValue + "/certificatesimp.der", "w+")
                file_cert_original.write(certificate)
                proc2 = subprocess.Popen(
                    "openssl x509 -in " + manualobj.browseValue + "/certificatesimp.pem -noout -text", stdout=fileimp,
                    shell=True)
                time.sleep(2)
                proc2.kill()
            except:
                file_certimp.write("Unable to load the certificate")
            cert_text = open(manualobj.browseValue + "/certcompleteimp.txt", "r").read()

            cert_txt = cert_text.split('\n')
            for row in cert_txt:

                if "Version" in row:
                    a = row.split()
                    # a = '{:2} {:2} {:2}'.format(a[0], a[1], a[2])

                    file_certimp.write("\n" + "".join(str(x) for x in a) + "\n")

                if "  Issuer:" in row:
                    a = row.split()
                    # a='{:2} {:2}'.format(a[0],a[1])
                    file_certimp.write("\n" + "".join(str(x) for x in a) + "\n")

                if "Subject:" in row:
                    a = row.split()
                    # a = '{:2} {:2} {:2} {:2} {:2} {:2} {:2} {:2}'.format(a[0],a[7], a[6],a[5], a[4], a[3] , a[2],a[1])
                    file_certimp.write("\n" + "".join(str(x) for x in a) + "\n")

                if "Not Before" in row:
                    a = row.split()
                    # a = '{:2} {:2} {:2} {:2} {:2} {:2} {:2}'.format(a[0], a[1], a[2],a[3], a[4], a[5] , a[6])

                    file_certimp.write("\n" + "".join(str(x) for x in a) + "\n")

                if "Not After" in row:
                    a = row.split()
                    # a = '{:2} {:2} {:2} {:2} {:2} {:2} {:2} {:2}'.format(a[0], a[1], a[2], a[3],a[4],a[5],a[6],a[7])
                    file_certimp.write("\n" + "".join(str(x) for x in a) + "\n")
        except:
            file_certimp.write("Unable to load certificate")

    def certVoice(self):
        filevoice = open(manualobj.browseValue + "/certcompletevoice.txt", "w+")
        file_certvoice = open(manualobj.browseValue + "/certdatavoice.txt", "w+")

        try:
            if manualobj.flag!=2:
                file = open(manualobj.browseValue + "/service.txt", 'r').read()
                info = file.split('\n')
                for row in info:
                    if "VoiceMail" in row:
                        voice1 = row.split(':')[2]
                        print
                        voice1
                        break

                    if "VoiceMail" in row:
                        voice2 = row.split(':')[2]
                    if "VoiceMail" in row:
                        voice3 = row.split(':')[2]

                voice1_ip = socket.gethostbyname(voice1)
                certificate = (ssl.get_server_certificate((voice1_ip, 443)))
                print
                voice1_ip
                file_cert_original = open(manualobj.browseValue + "/certificatesvoice.der", "w+")
                file_cert_original.write(certificate)
            else:
                file = open(manualobj.browseValue + "/imp_jabber.txt", 'r').read()
                info = file.split('\n')
                for row in info:
                    if "VoiceMail" in row:
                        voice1 = row.split(':')[2]
                        print
                        voice1
                        break

                    if "VoiceMail" in row:
                        voice2 = row.split(':')[2]
                    if "VoiceMail" in row:
                        voice3 = row.split(':')[2]

                voice1_ip = socket.gethostbyname(voice1)
                certificate = (ssl.get_server_certificate((voice1_ip, 443)))
                print
                voice1_ip
                file_cert_original = open(manualobj.browseValue + "/certificatesvoice.der", "w+")
                file_cert_original.write(certificate)
            # file_cert_originale.close()
            proc2 = subprocess.Popen(
                "openssl x509 -in " + manualobj.browseValue + "/certificatesvoice.pem -noout -text", shell=True)
            time.sleep(2)
            proc2.kill()

            file_cert_original = open(manualobj.browseValue + "/certificatesvoice.pem", "w+")
            file_cert_original.write(certificate)
            proc2 = subprocess.Popen(
                "openssl x509 -in " + manualobj.browseValue + "\\certificatesvoice.pem -noout -text", shell=True)
            time.sleep(2)
            proc2.kill()

            file_cert_original = open(manualobj.browseValue + "/certificatesvoice.der", "w+")
            file_cert_original.write(certificate)
            # file_cert_originale.close()
            proc2 = subprocess.Popen(
                "openssl x509 -in " + manualobj.browseValue + "/certificatesvoice.pem -noout -text", stdout=filevoice,
                shell=True)
            time.sleep(2)
            proc2.kill()

            cert_text = open(manualobj.browseValue + "/certcompletevoice.txt", "r").read()

            cert_txt = cert_text.split('\n')
            for row in cert_txt:

                if "Version" in row:
                    a = row.split()
                    # a = '{:2} {:2} {:2}'.format(a[0], a[1], a[2])

                    file_certvoice.write("\n" + "".join(str(x) for x in a) + "\n")

                if "  Issuer:" in row:
                    a = row.split()
                    # a='{:2} {:2}'.format(a[0],a[1])

                    file_certvoice.write("\n" + "".join(str(x) for x in a) + "\n")

                if "Not Before" in row:
                    a = row.split()
                    # a = '{:2} {:2} {:2} {:2} {:2} {:2} {:2}'.format(a[0], a[1], a[2],a[3], a[4], a[5] , a[6])

                    file_certvoice.write("\n" + "".join(str(x) for x in a) + "\n")

                if "Not After" in row:
                    a = row.split()
                    # a = '{:2} {:2} {:2} {:2} {:2} {:2} {:2} {:2}'.format(a[0], a[1], a[2], a[3],a[4],a[5],a[6],a[7])

                    file_certvoice.write("\n" + "".join(str(x) for x in a) + "\n")

                if "Subject:" in row:
                    a = row.split()
                    # a = '{:2} {:2} {:2} {:2} {:2} {:2} {:2}'.format(a[0], a[6],a[5], a[4], a[3] , a[2],a[1])

                    file_certvoice.write("\n" + "".join(str(x) for x in a) + "\n")
                if "Signature Algorith" in row:
                    a = row.split()
                    file_certvoice.write('\n' + "".join(str(x) for x in a) + "\n")
            cert_text = cert_text.split()
            print
            cert_text
            for count, elem in enumerate(cert_text):
                if elem == "Serial":
                    file_certvoice.write('Serial Number  : ' + cert_text[count + 2] + '\n')

            file_certvoice.close()


        except:
            file_certvoice.write("Unable to load certificate")


    def certCucm(self):
        file = open(manualobj.browseValue + "/certcomplete.txt", "w+")
        file_cert = open(manualobj.browseValue + "/certdata.txt", "w+")
        try:
            if manualobj.flag!=2:
                fileservice = open(manualobj.browseValue + "/service.txt", 'r').read()
                info = fileservice.split('\n')
                for row in info:
                    if "CTI" in row:
                        cti1 = row.split(':')[2]
                        cti1_ip = socket.gethostbyname(cti1)
                        print(cti1_ip)
                        break
                        # if "CTI SECONDARY ADDRESS" in row:
                        #     cti2 = row.split(':')[2]
                        #     cti2_ip = socket.gethostbyname(cti2)
                        #     print cti2_ip
                        # if "CTI TERTIARY ADDRESS" in row:
                        #     cti3 = row.split(':')[2]
                certificate = (ssl.get_server_certificate((cti1_ip, 443)))
            else:
                fileservice = open(manualobj.browseValue + "/imp_jabber.txt", 'r').read()
                info = fileservice.split('\n')
                for row in info:
                    if "CTI" in row:
                        cti1 = row.split(':')[2]
                        cti1_ip = socket.gethostbyname(cti1)
                        print(cti1_ip)
                        break
                        # if "CTI SECONDARY ADDRESS" in row:
                        #     cti2 = row.split(':')[2]
                        #     cti2_ip = socket.gethostbyname(cti2)
                        #     print cti2_ip
                        # if "CTI TERTIARY ADDRESS" in row:
                        #     cti3 = row.split(':')[2]
                certificate = (ssl.get_server_certificate((cti1_ip, 443)))


            file_cert_original = open(manualobj.browseValue + "\\certificates.der", "w+")
            file_cert_original.write(certificate)
            proc2 = subprocess.Popen("openssl x509 -in " + manualobj.browseValue + "\\certificates.pem -noout -text",
                                     shell=True)
            time.sleep(2)
            proc2.kill()

            file_cert_original = open(manualobj.browseValue + "\\certificates.pem", "w+")
            file_cert_original.write(certificate)
            proc2 = subprocess.Popen("openssl x509 -in " + manualobj.browseValue + "\\certificates.pem -noout -text",
                                     shell=True)
            time.sleep(2)
            proc2.kill()

            file_cert_original = open(manualobj.browseValue + "\\certificates.der", "w+")
            file_cert_original.write(certificate)
            proc2 = subprocess.Popen("openssl x509 -in " + manualobj.browseValue + "\\certificates.pem -noout -text",
                                     stdout=file, shell=True)
            time.sleep(2)
            proc2.kill()
            cert_text = open(manualobj.browseValue + "/certcomplete.txt", "r").read()

            cert_txt = cert_text.split('\n')
            for row in cert_txt:

                if "Version" in row:
                    a = row.split()
                    # a = '{:2} {:2} {:2}'.format(a[0], a[1], a[2])

                    file_cert.write("\n" + "".join(str(x) for x in a) + "\n")

                if "  Issuer:" in row:
                    a = row.split()
                    # a='{:2} {:2}'.format(a[0],a[1])

                    file_cert.write("\n" + "".join(str(x) for x in a) + "\n")

                if "Not Before" in row:
                    a = row.split()
                    # a = '{:2} {:2} {:2} {:2} {:2} {:2} {:2}'.format(a[0], a[1], a[2],a[3], a[4], a[5] , a[6])

                    file_cert.write("\n" + "".join(str(x) for x in a) + "\n")

                if "Not After" in row:
                    a = row.split()
                    # a = '{:2} {:2} {:2} {:2} {:2} {:2} {:2} {:2}'.format(a[0], a[1], a[2], a[3],a[4],a[5],a[6],a[7])

                    file_cert.write("\n" + "".join(str(x) for x in a) + "\n")

                if "Subject:" in row:
                    a = row.split()
                    # a = '{:2} {:2} {:2} {:2} {:2} {:2} {:2} {:2}'.format(a[0], a[7], a[6],a[5], a[4], a[3] , a[2],a[1])

                    file_cert.write("\n" + "".join(str(x) for x in a) + "\n")

        except:
            file_cert.write("unable to load certificate")

    def certdTrusted(self):
        fileopen=open(manualobj.browseValue+"/root certificates.txt","w")
        file=open(manualobj.browseValue+"/trusted certificates.txt",'w')
        proc1=subprocess.Popen(["C:\\Windows\\system32\\WindowsPowerShell\\v1.0\\powershell.exe","ls -r cert:"], stdout=fileopen, shell=True)
        time.sleep(5)
        proc1.kill()
        info=open(manualobj.browseValue+"/root certificates.txt","r").read()
        try:
            for row in info.split("\n"):
                if "Locations" in row or "StoreNames" in row or "Name" in row or "Subject" in row or "Issuer" in row or  "NotBefore " in row or "NotAfter " in row:
                    file.write("\n"+row+"\n")
                elif "Thumbprint" in row :
                    file.write('\n' + row +'\n')
                    file.write('\n'+'-'*100 + '\n\n\n\n')
            print "Certificate is coming before"
        except:
            file.write("Unable to Load the root / trusted certificates from the PC")







certobject=Certs()
