import socket
import dns.resolver

# Basic query
file1 = open("C:\Python27\d.txt","w")
for rdata in dns.resolver.query('_cisco-uds._tcp.vucis2.com', 'SRV') :
    print rdata.target
    file1.write(rdata.target)

# Set the DNS Server
# resolver = dns.resolver.Resolver()
# resolver.nameservers=[socket.gethostbyname('ns1.cisco.com')]
# for rdata in resolver.query('www.yahoo.com', 'CNAME') :
#     print rdata.target