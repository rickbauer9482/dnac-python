from dnacentersdk import DNACenterAPI
from pprint import pprint
from dnacreds import DNAC_USER, DNAC_PASS, DNAC_URL, DNAC_VER
import time


#  create_site(site=None, type=None, headers=None, payload=None, active_validation=True, **request_parameters)
api = DNACenterAPI(username= DNAC_USER, password= DNAC_PASS, base_url=DNAC_URL, version=DNAC_VER, verify=False)

# Parent containers cannot be deleted when children are present so must delete in reverse order from create
# Use dnac_get_sites.py to find the ID of the site object you wish to delete
delete_floor = api.sites.delete_site(site_id='FLOOR ID FROM GET SITES')
time.sleep(3)
delete_building = api.sites.delete_site(site_id='BUILDING ID FROM GET SITES')
time.sleep(3)
delete_area = api.sites.delete_site(site_id='AREA ID FROM GET SITES')
