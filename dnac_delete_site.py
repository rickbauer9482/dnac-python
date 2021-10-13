from dnacentersdk import DNACenterAPI
from pprint import pprint
from dnacreds import DNAC_USER, DNAC_PASS, DNAC_URL, DNAC_VER
import time


#  create_site(site=None, type=None, headers=None, payload=None, active_validation=True, **request_parameters)
api = DNACenterAPI(username= DNAC_USER, password= DNAC_PASS, base_url=DNAC_URL, version=DNAC_VER, verify=False)

delete_floor = api.sites.delete_site(site_id='9a4eef54-5bca-48d8-9966-4c9d488f8f4d')
time.sleep(3)
delete_building = api.sites.delete_site(site_id='9f7844d2-2c93-4c77-b268-ae08f56ef18e')
time.sleep(3)
delete_area = api.sites.delete_site(site_id='1ee1b8cb-7b62-47c9-ba47-52e6e3cc78c1')
