from ManualLogin import *
from seqdiag import parser, builder, drawer
# from ServiceProfile import *
# from GetDns import dnsclass
# from ImAndPresence import impclass
# from UserDetails import *
# #import Image

class seqclass():
    def seqfn(self):
        dns_file=open(manualobj.browseValue+'/dns_status.txt',"r").read()
        userdetails_file = open(manualobj.browseValue + '/userdetails_status.txt', "r").read()
        serviceprofile_file = open(manualobj.browseValue + '/serviceprofile_status.txt', "r").read()
        imp_file = open(manualobj.browseValue + '/imp_status.txt', "r").read()
        dnsinfo=dns_file.split('\n')
        for row in dnsinfo:
            if "dns_success" in row:
                dns=0
                break
            elif "dns_fail" in row:
                dns=1
                break

        userdetailsinfo = userdetails_file.split('\n')
        for row in userdetailsinfo:
            if "userdetails_success" in row:
                userdetails=0
                break
            elif "userdetails_fail" in row:
                userdetails=1
                break

        serviceprofileinfo = serviceprofile_file.split('\n')
        for row in serviceprofileinfo:
            if "serviceprofile_success" in row:
                serviceprofile = 0
                break
            elif "serviceprofile_fail" in row:
                serviceprofile = 1
                break

        impinfo = imp_file.split('\n')
        for row in impinfo:
            if "imp_success" in row:
                imp = 0
                break
            else :
                imp = 1
                break

        print dns,imp,serviceprofile,userdetails

        if dns==0 and serviceprofile==0 and userdetails == 0 and imp ==0:
            diagram_definition = u"""
               seqdiag {
                  user -> dns [label = "dns query"];
                  dns -> user [label = "Domain Name and other Services info and list of servers"];
                  user  -> userdetails [label = "fetching user details"];
                  userdetails -> user [label = "user details received successfully"];
                  user  -> service_profile [label = "query for service profile"];
                  service_profile -> user [label = "Service Profile received successfully"];
                  user  -> devices [label = "Quering for list of devices and device details"];
                  devices -> user [label = "devices query Successful"];
                  user -> IMP [label = "Soap and XMPP authentication"];
                  IMP -> user [label = "Soap and XMPP authentication Successful"];
                  user  -> directory_sso [label = "query for directory and sso"];
                  directory_sso -> user [label = "Success"];

               }
            """

        elif dns == 1:
            diagram_definition = u"""
                      seqdiag {
                         user -> dns [label = "dns query"];
                         dns -> user [label = "Domain Name and other Services info and list of servers"];
                         user  -> userdetails [label = "fetching user details"];
                         userdetails -> user [label = "unable to receive the user details"];

                        }
                   """

        elif userdetails==1 and dns ==0:
            diagram_definition = u"""
               seqdiag {
                  user -> dns [label = "dns query"];
                  dns -> user [label = "Domain Name and other Services info and list of servers"];
                  user  -> userdetails [label = "fetching user details"];
                  userdetails -> user [label = "unable to receive the user details"];

               }
            """
        elif dns==0 and userdetails==0 and serviceprofile==1:
            diagram_definition = u"""
               seqdiag {
                  user -> dns [label = "dns query"];
                  dns -> user [label = "Domain Name and other Services info and list of servers"];
                  user  -> userdetails [label = "fetching user details"];
                  userdetails -> user [label = "user details sent successfully"];
                  user  -> service_profile [label = "query for service profile"];
                  service_profile -> user [label = "Service Profile not received successfully"];
               }
            """

        elif dns==0 and userdetails ==0 and serviceprofile == 0 and imp ==1:
            diagram_definition = u"""
               seqdiag {
                  user -> dns [label = "dns query"];
                  dns -> user [label = "Domain Name and other Services info and list of servers"];
                  user  -> userdetails [label = "fetching user details"];
                  userdetails -> user [label = "user details sent successfully"];
                  user  -> service_profile [label = "query for service profile"];
                  service_profile -> user [label = "Service Profile received successfully"];
                  user  -> devices [label = "Quering for list of devices and device details"];
                  devices -> user [label = "devices query Successful"];
                  user -> IMP [label = "Soap and XMPP authentication"];
                  IMP -> user [label = "Soap or XMPP authentication Failed"];
               }
            """

        tree = parser.parse_string(diagram_definition)
        flow = builder.ScreenNodeBuilder.build(tree)
        draw = drawer.DiagramDraw('PNG', flow, filename=manualobj.browseValue + '/code_flow.gif')
        draw.draw()
        draw.save()

seqobj=seqclass()