from dnacentersdk import DNACenterAPI
from pprint import pprint
from dnacreds import DNAC_USER, DNAC_PASS, DNAC_URL, DNAC_VER

api = DNACenterAPI(username= DNAC_USER, password= DNAC_PASS, base_url=DNAC_URL, version=DNAC_VER, verify=False)

mydevice = api.devices.get_device_list(serialNumber='FDO2016E0H0')

pprint(mydevice)
