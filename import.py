from wos import WokmwsSoapClient

soap = WokmwsSoapClient()
results = soap.search("ROBERT Lydia")

print results
