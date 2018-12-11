import dns

dns.ParseResolvConf()
domain = "vucis2.com"
srv_req = dns.Request(qtype = 'srv')
srv_result = srv_req.req('_ldap._tcp.'+ domain)

for result in srv_result.answers:
    if result['typename'] == 'SRV':
        print result['data']