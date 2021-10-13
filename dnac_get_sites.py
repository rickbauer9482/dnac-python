from dnacentersdk import DNACenterAPI
from pprint import pprint
from dnacreds import DNAC_USER, DNAC_PASS

api = DNACenterAPI(username= DNAC_USER, password= DNAC_PASS, base_url='https://10.87.125.20', version='2.2.2.3', verify=False)

mysites = api.sites.get_site()

pprint(mysites)