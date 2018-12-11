import re
# from ImAndPresence import *
from ManualLogin import *


class impservice():
    def impservicefn(self):

        file1 = open(manualobj.browseValue + "/imp_jabber.txt", 'w+')
        file2 = open(manualobj.browseValue + "/imp_soap_response.txt", 'r').read()
        file_ = open(manualobj.browseValue + "/imp_enterprise.txt", "w+")
        file_1 = open(manualobj.browseValue + "/directory_imp.txt", 'w+')
        file3 = open(manualobj.browseValue + "/impservicesummary.txt", 'w+')
        try:
            if manualobj.flag == 2:
                x = re.findall('<epas:property name="VoiceMail.Primary.Address">(.*?)</epas:property>', file2,
                               re.I | re.M)
                x = filter(lambda name: name.strip(), x)
                if x:
                    for line in x:
                        file1.write("VoiceMail:Primary:" + line + ":")
                else:
                    file1.write("VoiceMail:Primary:Not Configured:")
                    file3.write("VoiceMail:Primary:Not Configured:\n")
                x = re.findall('<epas:property name="VoiceMail.Primary.SecureMessaging.Port">(.*?)</epas:property>',
                               file2, re.I | re.M)
                x = filter(lambda name: name.strip(), x)
                if x != []:
                    for line in x:
                        file1.write(line + ":")
                else:
                    file1.write("N/A:")
                x = re.findall('<epas:property name="VoiceMail.Primary.SecureMessaging.Protocol">(.*?)</epas:property>',
                               file2, re.I | re.M)
                x = filter(lambda name: name.strip(), x)
                if x != []:
                    for line in x:
                        file1.write(line + "\n")
                else:
                    file1.write("N/A\n")
                x = re.findall('<epas:property name="VoiceMail.Backup1.Address">(.*?)</epas:property>', file2,
                               re.I | re.M)
                x = filter(lambda name: name.strip(), x)
                if x != []:
                    for line in x:
                        file1.write("VoiceMail:Secondary:" + line + ":")
                else:
                    file1.write("VoiceMail:Secondary:Not Configured:")


                x = re.findall('<epas:property name="VoiceMail.Backup1.SecureMessaging.Port">(.*?)</epas:property>',
                               file2, re.I | re.M)
                x = filter(lambda name: name.strip(), x)
                if x != []:
                    for line in x:
                        file1.write(line + ":")
                else:
                    file1.write("N/A:")

                x = re.findall('<epas:property name="VoiceMail.Backup1.SecureMessaging.Protocol">(.*?)</epas:property>',
                               file2, re.I | re.M)
                x = filter(lambda name: name.strip(), x)

                if x != []:
                    for line in x:
                        file1.write(line + "\n")
                else:
                    file1.write("N/A\n")

                x = re.findall('<epas:property name="VoiceMail.Backup2.Address">(.*?)</epas:property>', file2,
                               re.I | re.M)
                x = filter(lambda name: name.strip(), x)
                if x != []:
                    for line in x:
                        file1.write("VoiceMail:Tertiary:" + line + ":")
                else:
                    file1.write("VoiceMail:Tertiary:Not Configured:")


                x = re.findall('<epas:property name="VoiceMail.Backup2.SecureMessaging.Port">(.*?)</epas:property>',
                               file2, re.I | re.M)
                x = filter(lambda name: name.strip(), x)
                if x != []:
                    for line in x:
                        file1.write(line + ":")
                else:
                    file1.write("N/A:")
                x = re.findall('<epas:property name="VoiceMail.Backup2.SecureMessaging.Protocol">(.*?)</epas:property>',
                               file2, re.I | re.M)

                x = filter(lambda name: name.strip(), x)

                if x != []:
                    for line in x:
                        file1.write(line + "\n")
                else:
                    file1.write("N/A \n")

                x = re.findall('<epas:property name="MailStore.Primary.Address">(.*?)</epas:property>', file2,
                               re.I | re.M)
                x = filter(lambda name: name.strip(), x)
                if x != []:
                    for line in x:
                        file1.write("MailStore:Primary:" + line + ":")
                else:
                    file1.write("MailStore:Primary:Not Configured:")
                    file3.write("MailStore:Primary:Not Configured:\n")
                x = re.findall('<epas:property name="MailStore.Primary.port">(.*?)</epas:property>', file2, re.I | re.M)
                x = filter(lambda name: name.strip(), x)
                if x != []:
                    for line in x:
                        file1.write(line + ":")
                else:
                    file1.write("N/A:")
                x = re.findall('<epas:property name="MailStore.Primary.Protocol">(.*?)</epas:property>', file2,
                               re.I | re.M)
                x = filter(lambda name: name.strip(), x)
                if x != []:
                    for line in x:
                        file1.write(line + "\n")
                else:
                    file1.write("N/A\n")
                x = re.findall('<epas:property name="MailStore.Backup1.Address">(.*?)</epas:property>', file2,
                               re.I | re.M)
                x = filter(lambda name: name.strip(), x)
                if x != []:
                    for line in x:
                        file1.write("MailStore:Secondary:" + line + ":")
                else:
                    file1.write("MailStore:Secondary:Not Configured:")


                x = re.findall('<epas:property name="MailStore.Backup1.port">(.*?)</epas:property>', file2, re.I | re.M)
                x = filter(lambda name: name.strip(), x)
                if x != []:
                    for line in x:
                        file1.write(line + ":")
                else:
                    file1.write("N/A:")
                x = re.findall('<epas:property name="MailStore.Backup1.Protocol">(.*?)</epas:property>', file2,
                               re.I | re.M)
                x = filter(lambda name: name.strip(), x)
                if x != []:
                    for line in x:
                        file1.write(line + "\n")
                else:
                    file1.write("N/A\n")

                x = re.findall('<epas:property name="MailStore.Backup2.Address">(.*?)</epas:property>', file2,
                               re.I | re.M)
                x = filter(lambda name: name.strip(), x)
                if x != []:
                    for line in x:
                        file1.write("MailStore:Tertiary:" + line + ":")
                else:
                    file1.write("MailStore:Tertiary:Not Configured:")


                x = re.findall('<epas:property name="MailStore.Backup2.port">(.*?)</epas:property>', file2, re.I | re.M)
                x = filter(lambda name: name.strip(), x)
                if x != []:
                    for line in x:
                        file1.write(line + ":")
                else:
                    file1.write("N/A:")
                x = re.findall('<epas:property name="MailStore.Backup2.Protocol">(.*?)</epas:property>', file2,
                               re.I | re.M)
                x = filter(lambda name: name.strip(), x)
                if x != []:
                    for line in x:
                        file1.write(line + "\n")
                else:
                    file1.write("N/A\n")

                x = re.findall('<epas:property name="CallControl.Primary.Address">(.*?)</epas:property>', file2,
                               re.I | re.M)
                x = filter(lambda name: name.strip(), x)
                if x != []:
                    for line in x:
                        file1.write("CTI:Primary:" + line + ":")
                else:
                    file1.write("CTI:Primary:Not Configured:")
                    file3.write("CTI:Primary:Not Configured:\n")
                x = re.findall('<epas:property name="CallControl.Primary.port">(.*?)</epas:property>', file2,
                               re.I | re.M)
                x = filter(lambda name: name.strip(), x)
                if x != []:
                    for line in x:
                        file1.write(line + ":")
                else:
                    file1.write("N/A:")
                x = re.findall('<epas:property name="CallControl.Primary.Protocol">(.*?)</epas:property>', file2,
                               re.I | re.M)
                x = filter(lambda name: name.strip(), x)
                if x != []:
                    for line in x:
                        file1.write(line + "\n")
                else:
                    file1.write("N/A\n")
                x = re.findall('<epas:property name="CallControl.Backup1.Address">(.*?)</epas:property>', file2,
                               re.I | re.M)
                x = filter(lambda name: name.strip(), x)
                if x != []:
                    for line in x:
                        file1.write("CTI:Secondary:" + line + ":")
                else:
                    file1.write("CTI:Secondary:Not Configured:")


                x = re.findall('<epas:property name="CallControl.Backup1.port">(.*?)</epas:property>', file2,
                               re.I | re.M)
                x = filter(lambda name: name.strip(), x)
                if x != []:
                    for line in x:
                        file1.write(line + ":")
                else:
                    file1.write("N/A:")
                x = re.findall('<epas:property name="CallControl.Backup1.Protocol">(.*?)</epas:property>', file2,
                               re.I | re.M)
                x = filter(lambda name: name.strip(), x)
                if x != []:
                    for line in x:
                        file1.write(line + "\n")
                else:
                    file1.write("N/A\n")

                x = re.findall('<epas:property name="CallControl.Backup2.Address">(.*?)</epas:property>', file2,
                               re.I | re.M)
                x = filter(lambda name: name.strip(), x)
                if x != []:
                    for line in x:
                        file1.write("CTI:Tertiary:" + line + ":")
                else:
                    file1.write("CTI:Tertiary:Not Configured:")


                x = re.findall('<epas:property name="CallControl.Backup2.port">(.*?)</epas:property>', file2,
                               re.I | re.M)
                x = filter(lambda name: name.strip(), x)
                if x != []:
                    for line in x:
                        file1.write(line + ":")
                else:
                    file1.write("N/A:")
                x = re.findall('<epas:property name="CallControl.Backup2.Protocol">(.*?)</epas:property>', file2,
                               re.I | re.M)
                x = filter(lambda name: name.strip(), x)
                if x != []:
                    for line in x:
                        file1.write(line + "\n")
                else:
                    file1.write("N/A\n")

                x = re.findall('<epas:property name="Directory.Primary.Address">(.*?)</epas:property>', file2,
                               re.I | re.M)
                x = filter(lambda name: name.strip(), x)
                if x != []:
                    for line in x:
                        file1.write("Directory:Primary:" + line + ":")
                else:
                    file1.write("Directory:Primary:Not Configured:")
                    file3.write("Directory:Primary:Not Configured:\n")
                x = re.findall('<epas:property name="Directory.Primary.port">(.*?)</epas:property>', file2, re.I | re.M)
                x = filter(lambda name: name.strip(), x)
                if x != []:
                    for line in x:
                        file1.write(line + ":")
                else:
                    file1.write("N/A:")
                x = re.findall('<epas:property name="Directory.Primary.Protocol">(.*?)</epas:property>', file2,
                               re.I | re.M)
                x = filter(lambda name: name.strip(), x)
                if x != []:
                    for line in x:
                        file1.write(line + "\n")
                else:
                    file1.write("N/A\n")
                x = re.findall('<epas:property name="Directory.Backup1.Address">(.*?)</epas:property>', file2,
                               re.I | re.M)
                x = filter(lambda name: name.strip(), x)
                if x != []:
                    for line in x:
                        file1.write("Directory:Secondary:" + line + ":")
                else:
                    file1.write("Directory:Secondary:Not Configured:")

                x = re.findall('<epas:property name="Directory.Backup1.port">(.*?)</epas:property>', file2, re.I | re.M)
                x = filter(lambda name: name.strip(), x)
                if x != []:
                    for line in x:
                        file1.write(line + ":")
                else:
                    file1.write("N/A:")
                x = re.findall('<epas:property name="Directory.Backup1.Protocol">(.*?)</epas:property>', file2,
                               re.I | re.M)
                x = filter(lambda name: name.strip(), x)
                if x != []:
                    for line in x:
                        file1.write(line + "\n")
                else:
                    file1.write("N/A\n")

                x = re.findall('<epas:property name="Directory.Backup2.Address">(.*?)</epas:property>', file2,
                               re.I | re.M)
                x = filter(lambda name: name.strip(), x)
                if x != []:
                    for line in x:
                        file1.write("Directory:Tertiary:" + line + ":")
                else:
                    file1.write("Directory:Tertiary:Not Configured:")


                x = re.findall('<epas:property name="Directory.Backup2.port">(.*?)</epas:property>', file2, re.I | re.M)
                if x != []:
                    for line in x:
                        file1.write(line + ":")
                else:
                    file1.write("N/A:")
                x = re.findall('<epas:property name="Directory.Backup2.Protocol">(.*?)</epas:property>', file2,
                               re.I | re.M)
                x = filter(lambda name: name.strip(), x)
                if x != []:
                    for line in x:
                        file1.write(line + "\n")
                else:
                    file1.write("N/A\n")

                x = re.findall('<epas:property name="Directory.AnonymousBind">(.*?)</epas:property>', file2,
                               re.I | re.M)
                x = filter(lambda name: name.strip(), x)
                if x != []:
                    for line in x:
                        file_1.write("Directory:AnonymousBind:" + line + "\n")
                else:
                    file_1.write("Directory:AnonymousBind:Not Configured\n")

                x = re.findall('<epas:property name="Directory.Password">(.*?)</epas:property>', file2, re.I | re.M)
                x = filter(lambda name: name.strip(), x)
                if x != []:
                    for line in x:
                        file_1.write("Directory:Password:" + line + "\n")
                else:
                    file_1.write("Directory:Password:Not Configured\n")

                x = re.findall('<epas:property name="Directory.SearchRecursive3">(.*?)</epas:property>', file2,
                               re.I | re.M)
                x = filter(lambda name: name.strip(), x)
                if x != []:
                    for line in x:
                        file_1.write("Directory:SearchRecursive3:" + line + "\n")
                else:
                    file_1.write("Directory:SearchRecursive3:Not Configured\n")

                x = re.findall('<epas:property name="Directory.SearchContext2">(.*?)</epas:property>', file2,
                               re.I | re.M)

                x = filter(lambda name: name.strip(), x)
                if x != []:
                    for line in x:
                        file_1.write("Directory:SearchContext2:" + line + "\n")
                else:
                    file_1.write("Directory:SearchContext2:Not Configured\n")

                x = re.findall('<epas:property name="Directory.SearchRecursive2">(.*?)</epas:property>', file2,
                               re.I | re.M)
                x = filter(lambda name: name.strip(), x)
                if x != []:
                    for line in x:
                        file_1.write("Directory:SearchRecursive2:" + line + "\n")
                else:
                    file_1.write("Directory:SearchRecursive2:Not Configured\n")

                x = re.findall('<epas:property name="Directory.SearchContext1">(.*?)</epas:property>', file2,
                               re.I | re.M)
                x = filter(lambda name: name.strip(), x)
                if x != []:
                    for line in x:
                        file_1.write("Directory:SearchContext1:" + line + "\n")
                else:
                    file_1.write("Directory:SearchContext1:Not Configured\n")

                x = re.findall('<epas:property name="Directory.SearchContext3">(.*?)</epas:property>', file2,
                               re.I | re.M)
                if x != []:
                    for line in x:
                        file_1.write("Directory:SearchContext3:" + line + "\n")
                else:
                    file_1.write("Directory:SearchContext3:Not Configured\n")

                x = re.findall('<epas:property name="Directory.DN">(.*?)</epas:property>', file2, re.I | re.M)
                x = filter(lambda name: name.strip(), x)
                if x != []:
                    for line in x:
                        file_1.write("Directory:DN:" + line + "\n")
                else:
                    file_1.write("Directory:DN:Not Configured\n")

                x = re.findall('<epas:property name="Directory.ConfigurationName">(.*?)</epas:property>', file2,
                               re.I | re.M)
                x = filter(lambda name: name.strip(), x)
                if x != []:
                    for line in x:
                        file_1.write("Directory:ConfigurationName:" + line + "\n")
                else:
                    file_1.write("Directory:ConfigurationName:Not Configured\n")

                x = re.findall('<epas:property name="Directory.SearchRecursive1">(.*?)</epas:property>', file2,
                               re.I | re.M)
                x = filter(lambda name: name.strip(), x)
                if x != []:
                    for line in x:
                        file_1.write("Directory:Searchrecursive1:" + line + "\n")
                else:
                    file_1.write("Directory:Searchrecursive1:Not Configured\n")

                x = re.findall('<epas:property name="Directory.SearchContext1">(.*?)</epas:property>', file2,
                               re.I | re.M)
                x = filter(lambda name: name.strip(), x)
                if x != []:
                    for line in x:
                        file_1.write("Directory:SearchContext1" + line + "\n")
                else:
                    file_1.write("Directory:SearchContext1:Not Configured\n")

                x = re.findall('<epas:property name="Presence.Primary.Address">(.*?)</epas:property>', file2,
                               re.I | re.M)
                x = filter(lambda name: name.strip(), x)
                if x != []:
                    for line in x:
                        file1.write("IMP:Primary:" + line + ":")
                else:
                    file1.write("IMP:Primary:Not Configured:")
                    file1.write("IMP:Primary:Not Configured:\n")
                x = re.findall('<epas:property name="Presence.Primary.port">(.*?)</epas:property>', file2, re.I | re.M)
                x = filter(lambda name: name.strip(), x)
                if x != []:
                    for line in x:
                        file1.write(line + ":")
                else:
                    file1.write("N/A:")
                x = re.findall('<epas:property name="Presence.Primary.Protocol">(.*?)</epas:property>', file2,
                               re.I | re.M)
                x = filter(lambda name: name.strip(), x)
                if x != []:
                    for line in x:
                        file1.write(line + "\n")
                else:
                    file1.write("N/A\n")
                x = re.findall('<epas:property name="Presence.Backup.Address">(.*?)</epas:property>', file2,
                               re.I | re.M)
                x = filter(lambda name: name.strip(), x)
                if x != []:
                    for line in x:
                        file1.write("IMP:Secondary:" + line + ":")
                else:
                    file1.write("IMP:Secondary:Not Configured:")


                x = re.findall('<epas:property name="Presence.Backup.port">(.*?)</epas:property>', file2, re.I | re.M)
                x = filter(lambda name: name.strip(), x)
                if x != []:
                    for line in x:
                        file1.write(line + ":")
                else:
                    file1.write("N/A:")
                x = re.findall('<epas:property name="Presence.Backup.Protocol">(.*?)</epas:property>', file2,
                               re.I | re.M)
                x = filter(lambda name: name.strip(), x)
                if x != []:
                    for line in x:
                        file1.write(line + "\n")
                else:
                    file1.write("N/A\n")

                x = re.findall('<epas:property name="Presence.Backup2.Address">(.*?)</epas:property>', file2,
                               re.I | re.M)
                x = filter(lambda name: name.strip(), x)
                if x != []:
                    for line in x:
                        file1.write("IMP:Tertiary:" + line + ":")
                else:
                    file1.write("IMP:Tertiary:Not Configured:")


                x = re.findall('<epas:property name="Presence.Backup2.port">(.*?)</epas:property>', file2, re.I | re.M)
                x = filter(lambda name: name.strip(), x)
                if x != []:
                    for line in x:
                        file1.write(line + ":")
                else:
                    file1.write("N/A:")

                x = re.findall('<epas:property name="Presence.Backup2.Protocol">(.*?)</epas:property>', file2,
                               re.I | re.M)
                x = filter(lambda name: name.strip(), x)
                if x != []:
                    for line in x:
                        file1.write(line + "\n")
                else:
                    file1.write("N/A\n")

                x = re.findall('<epas:property name="Presence.Domain">(.*?)</epas:property>', file2, re.I | re.M)
                x = filter(lambda name: name.strip(), x)
                if x != []:
                    for line in x:
                        file_.write("Presence Domain:" + str(line) + ":\n")
                else:
                    file_.write("Presence Domain : N/A:\n")

                x = re.findall('<epas:property name="MeetingPlace.Primary.Address">(.*?)</epas:property>', file2,
                               re.I | re.M)
                x = filter(lambda name: name.strip(), x)
                if x != []:
                    for line in x:
                        file1.write("Conferencing:Primary:" + line + ":")
                else:
                    file1.write("Conferencing:Primary:Not Configured:")
                    file3.write("Conferencing:Primary:Not Configured:\n")
                x = re.findall('<epas:property name="MeetingPlace.Primary.Port">(.*?)</epas:property>', file2,
                               re.I | re.M)

                x = filter(lambda name: name.strip(), x)
                if x != []:
                    for line in x:
                        file1.write(line + ":")
                else:
                    file1.write("N/A:")
                x = re.findall('<epas:property name="MeetingPlace.Primary.Protocol">(.*?)</epas:property>', file2,
                               re.I | re.M)
                x = filter(lambda name: name.strip(), x)
                if x != []:
                    for line in x:
                        file1.write(line + "\n")
                else:
                    file1.write("N/A\n")
                x = re.findall('<epas:property name="MeetingPlace.Backup1.Address">(.*?)</epas:property>', file2,
                               re.I | re.M)
                x = filter(lambda name: name.strip(), x)
                if x != []:
                    for line in x:
                        file1.write("Conferencing:Secondary:" + line + ":")
                else:
                    file1.write("Conferencing:Secondary:Not Configured:")


                x = re.findall('<epas:property name="MeetingPlace.Backup1.port">(.*?)</epas:property>', file2,
                               re.I | re.M)
                x = filter(lambda name: name.strip(), x)
                if x != []:
                    for line in x:
                        file1.write(line + ":")
                else:
                    file1.write("N/A:")
                x = re.findall('<epas:property name="MeetingPlace.Backup1.Protocol">(.*?)</epas:property>', file2,
                               re.I | re.M)
                x = filter(lambda name: name.strip(), x)
                if x != []:
                    for line in x:
                        file1.write(line + "\n")
                else:
                    file1.write("N/A\n")

                x = re.findall('<epas:property name="MeetingPlace.Backup2.Address">(.*?)</epas:property>', file2,
                               re.I | re.M)
                x = filter(lambda name: name.strip(), x)
                if x != []:
                    for line in x:
                        file1.write("Conferencing:Tertiary:" + line + ":")
                else:
                    file1.write("Conferencing:Tertiary:Not Configured:")


                x = re.findall('<epas:property name="MeetingPlace.Backup2.port">(.*?)</epas:property>', file2,
                               re.I | re.M)
                x = filter(lambda name: name.strip(), x)
                if x != []:
                    for line in x:
                        file1.write(line + ":")
                else:
                    file1.write("N/A:")
                x = re.findall('<epas:property name="MeetingPlace.Backup2.Protocol">(.*?)</epas:property>', file2,
                               re.I | re.M)
                x = filter(lambda name: name.strip(), x)
                if x != []:
                    for line in x:
                        file1.write(line + "\n")
                else:
                    file1.write("N/A\n")

                x = re.findall('<epas:property name="TFTP.Primary">(.*?)</epas:property>', file2, re.I | re.M)
                x = filter(lambda name: name.strip(), x)
                if x != []:
                    for line in x:
                        file1.write("TFTP:Primary:" + str(line) + ": : :\n")
                else:
                    file1.write("TFTP:Primary: N/A: : :\n")
                    file3.write("TFTP:Primary: N/A: : :\n")

                x = re.findall('<epas:property name="TFTP.Backup1">(.*?)</epas:property>', file2, re.I | re.M)
                x = filter(lambda name: name.strip(), x)
                if x != []:
                    for line in x:
                        file1.write("TFTP:Backup1:" + str(line) + ": : :\n")
                else:
                    file1.write("TFTP:Backup1 : N/A: : :\n")


                x = re.findall('<epas:property name="TFTP.Backup2">(.*?)</epas:property>', file2, re.I | re.M)
                x = filter(lambda name: name.strip(), x)
                if x != []:
                    for line in x:
                        file1.write("TFTP:Backup2:" + str(line) + ": : :\n")
                else:
                    file1.write("TFTP:Backup2: N/A: : :\n")


                x = re.findall('<epas:property name="IM.enable">(.*?)</epas:property>', file2, re.I | re.M)
                x = filter(lambda name: name.strip(), x)
                if x != []:
                    for line in x:
                        file_.write("IM enable:" + str(line) + ":\n")
                else:
                    file_.write("IM enable : N/A:\n")

                x = re.findall('<epas:property name="Presence.enableGlobal">(.*?)</epas:property>', file2, re.I | re.M)
                x = filter(lambda name: name.strip(), x)
                if x != []:
                    for line in x:
                        file_.write("Presence enableGlobal:" + str(line) + ":\n")
                else:
                    file_.write("Presence enableGlobal : N/A:\n")

                x = re.findall('<epas:property name="OfflineIM.suppress">(.*?)</epas:property>', file2, re.I | re.M)
                x = filter(lambda name: name.strip(), x)
                if x != []:
                    for line in x:
                        file_.write("OfflineIMSUPPRESS:" + str(line) + ":\n")
                else:
                    file_.write("OfflineIMSUPPRESSOfflineIMSUPPRESS: N/A:\n")

                x = re.findall('<epas:property name="PhoneDND.enable">(.*?)</epas:property>', file2, re.I | re.M)
                x = filter(lambda name: name.strip(), x)
                if x != []:
                    for line in x:
                        file_.write("PhoneDND.enable:" + str(line) + ":\n")
                else:
                    file_.write("PhoneDND.enable : N/A:\n")

                x = re.findall('<epas:property name="MeetingDND.enable">(.*?)</epas:property>', file2, re.I | re.M)
                x = filter(lambda name: name.strip(), x)
                if x != []:
                    for line in x:
                        file_.write("MeetingDND.enable:" + str(line) + ":\n")
                else:
                    file_.write("MeetingDND.enable : N/A:\n")

                x = re.findall('<epas:property name="Calendar.Primary">(.*?)</epas:property>', file2, re.I | re.M)
                x = filter(lambda name: name.strip(), x)
                if x != []:
                    for line in x:
                        file_.write("Calendar.Primary:" + str(line) + ":\n")
                else:
                    file_.write("Calendar.Primary : N/A:\n")

                x = re.findall('<epas:property name="Calendar.Backup">(.*?)</epas:property>', file2, re.I | re.M)
                x = filter(lambda name: name.strip(), x)
                if x != []:
                    for line in x:
                        file_.write("Calendar.Backup:" + str(line) + ":\n")
                else:
                    file_.write("Calendar.Backup: N/A:\n")

                x = re.findall('<epas:property name="CUP.ProxyUDPListener.Port">(.*?)</epas:property>', file2,
                               re.I | re.M)
                x = filter(lambda name: name.strip(), x)
                if x != []:
                    for line in x:
                        file_.write("CUP.ProxyUDPListener.Port:" + str(line) + ":\n")
                else:
                    file_.write("CUP.ProxyUDPListener.Port : N/A:\n")

                x = re.findall('<epas:property name="CUP.ProxyTCPListener.Port">(.*?)</epas:property>', file2,
                               re.I | re.M)
                x = filter(lambda name: name.strip(), x)
                if x != []:
                    for line in x:
                        file_.write("CUP.ProxyTCPListener.Port:" + str(line) + ":\n")
                else:
                    file_.write("CUP.ProxyTCPListener.Port : N/A:\n")

                x = re.findall('<epas:property name="CUP.ProxyTLSListenerPeerAuth.Port">(.*?)</epas:property>', file2,
                               re.I | re.M)
                x = filter(lambda name: name.strip(), x)
                if x != []:
                    for line in x:
                        file_.write("CUP.ProxyTLSListenerPeerAuth.Port:" + str(line) + ":\n")
                else:
                    file_.write("CUP.ProxyTLSListenerPeerAuth.Port: N/A:\n")

                x = re.findall('<epas:property name="CUP.ProxyTLSListenerServerAuth.Port">(.*?)</epas:property>', file2,
                               re.I | re.M)
                x = filter(lambda name: name.strip(), x)
                if x != []:
                    for line in x:
                        file_.write("CUP.ProxyTLSListenerServerAuth.Port:" + str(line) + ":\n")
                else:
                    file_.write("CUP.ProxyTLSListenerServerAuth.Port: N/A:\n")

                x = re.findall('<epas:property name="CCMCIP.Host">(.*?)</epas:property>', file2, re.I | re.M)
                x = filter(lambda name: name.strip(), x)
                if x != []:
                    for line in x:
                        file_.write("CCMCIP.Host:" + str(line) + ":\n")
                else:
                    file_.write("CCMCIP.Host: N/A:\n")

                x = re.findall('<epas:property name="CCMCIP.Host.Backup">(.*?)</epas:property>', file2, re.I | re.M)
                x = filter(lambda name: name.strip(), x)
                if x != []:
                    for line in x:
                        file_.write("CCMCIP.Host.Backup:" + str(line) + ":\n")
                else:
                    file_.write("CCMCIP.Host.Backup : N/A:\n")

                x = re.findall('<epas:property name="IM.AllowCutAndPaste">(.*?)</epas:property>', file2, re.I | re.M)
                x = filter(lambda name: name.strip(), x)
                if x != []:
                    for line in x:
                        file_.write("IM.AllowCutAndPaste:" + str(line) + ":\n")
                else:
                    file_.write("IM.AllowCutAndPaste: N/A:\n")

                x = re.findall('<epas:property name="IM.AllowLocalTranscript">(.*?)</epas:property>', file2,
                               re.I | re.M)
                x = filter(lambda name: name.strip(), x)
                if x != []:
                    for line in x:
                        file_.write("IM.AllowLocalTranscript:" + str(line) + ":\n")
                else:
                    file_.write("IM.AllowLocalTranscript: N/A:\n")

                x = re.findall('<epas:property name="AdhocSubscriptions.Enabled">(.*?)</epas:property>', file2,
                               re.I | re.M)
                x = filter(lambda name: name.strip(), x)
                if x != []:
                    for line in x:
                        file_.write("AdhocSubscriptions.Enabled:" + str(line) + ":\n")
                else:
                    file_.write("AdhocSubscriptions.Enabled : N/A:\n")

                x = re.findall('<epas:property name="AdhocSubscriptions.MaxNum">(.*?)</epas:property>', file2,
                               re.I | re.M)
                x = filter(lambda name: name.strip(), x)
                if x != []:
                    for line in x:
                        file_.write("AdhocSubscriptions.MaxNum:" + str(line) + ":\n")
                else:
                    file_.write("AdhocSubscriptions.MaxNum: N/A:\n")

                x = re.findall('<epas:property name="AdhocSubscriptions.TTL">(.*?)</epas:property>', file2, re.I | re.M)
                x = filter(lambda name: name.strip(), x)
                if x != []:
                    for line in x:
                        file_.write("AdhocSubscriptions.TTL:" + str(line) + ":\n")
                else:
                    file_.write("AdhocSubscriptions.TTL : N/A:\n")

                x = re.findall('<epas:property name="Security.CertificateDirectory">(.*?)</epas:property>', file2,
                               re.I | re.M)
                x = filter(lambda name: name.strip(), x)
                if x != []:
                    for line in x:
                        file_.write("Security.CertificateDirectory:" + str(line) + "\n")
                else:
                    file_.write("Security.CertificateDirectory: N/A:\n")

                x = re.findall('<epas:property name="Security.WebConfServiceCredentialsSource">(.*?)</epas:property>',
                               file2, re.I | re.M)
                x = filter(lambda name: name.strip(), x)
                if x != []:
                    for line in x:
                        file_.write("Security.WebConfServiceCredentialsSource:" + str(line) + ":\n")
                else:
                    file_.write("Security.WebConfServiceCredentialsSource : N/A:\n")

                x = re.findall('<epas:property name="Security.VoicemailServiceCredentialsSource">(.*?)</epas:property>',
                               file2, re.I | re.M)
                x = filter(lambda name: name.strip(), x)
                if x != []:
                    for line in x:
                        file_.write("Security.VoicemailServiceCredentialsSource:" + str(line) + ":\n")
                else:
                    file_.write("Security.VoicemailServiceCredentialsSource : N/A:\n")

                x = re.findall('<epas:property name="CUP.SRM.LowerFailoverLoginRetryLimit">(.*?)</epas:property>',
                               file2, re.I | re.M)
                x = filter(lambda name: name.strip(), x)
                if x != []:
                    for line in x:
                        file_.write("CUP.SRM.LowerFailoverLoginRetryLimit:" + str(line) + ":\n")
                else:
                    file_.write("CUP.SRM.LowerFailoverLoginRetryLimit: N/A:\n")

                x = re.findall('<epas:property name="CUP.SRM.UpperFailoverLoginRetryLimit">(.*?)</epas:property>',
                               file2, re.I | re.M)
                x = filter(lambda name: name.strip(), x)
                if x != []:
                    for line in x:
                        file_.write("CUP.SRM.UpperFailoverLoginRetryLimit:" + str(line) + ":\n")
                else:
                    file_.write("CUP.SRM.UpperFailoverLoginRetryLimit: N/A:\n")
            else:
                file3.write("\nCUCM LOGIN SELECTED, HENCE, NO IMP SERVICE PROFILE DETAILS\n")
                # impserviceobj.impservicefn()
        except:
            file1.write("ERROR in Loading IMP JABBER CONFIG FILE")


