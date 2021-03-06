from dnacentersdk import DNACenterAPI
from pprint import pprint
from dnacreds import DNAC_USER, DNAC_PASS, DNAC_URL, DNAC_VER
import time

headers = {
    "Content-Type": "application/json",
    "Accept": "application/json"
}

area = {
    "site": {
        "area": {
            "name": "MY STATE",
            "parentName": "Global/USA"
        }
    },
    "type": "area"
}

building = {
    "site": {
        "building": {
            "name": "MY BUILDING",
            "address": "MY ADDRESS",
            "parentName": "Global/USA/MY STATE"
        }
    },
    "type": "building"
}

floor = {
    "site": {
        "floor": {
            "name": "MY FLOOR",
            "parentName": "Global/USA/MY STATE/MY BUILDING",
            "rfModel": "Cubes And Walled Offices",
            "width": 100,
            "length": 200,
            "height": 10
        }
    },
    "type": "floor"
}


#  create_site(site=None, type=None, headers=None, payload=None, active_validation=True, **request_parameters)
api = DNACenterAPI(username= DNAC_USER, password= DNAC_PASS, base_url=DNAC_URL, version=DNAC_VER, verify=False)

create_site = api.sites.create_site(payload=area)
time.sleep(3)
create_building = api.sites.create_site(payload=building)
time.sleep(3)
create_floor = api.sites.create_site(payload=floor)
