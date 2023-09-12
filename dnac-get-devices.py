# on your development box add these environment variables to be called from your script
# export DNA_CENTER_USERNAME="username"
# export DNA_CENTER_PASSWORD="password"
# export DNA_CENTER_VERSION="2.3.5.3"
# export DNA_CENTER_BASE_URL="https://x.x.x.x"
# 
# Or you can import creds from a file or vault
# from dnacreds import DNAC_USER, DNAC_PASS, DNAC_URL, DNAC_VER

from dnacentersdk import DNACenterAPI
from pprint import pprint
import os

DNAC_USER = os.environ.get("DNA_CENTER_USERNAME")
DNAC_PASS = os.environ.get("DNA_CENTER_PASSWORD")
DNAC_URL = os.environ.get("DNA_CENTER_BASE_URL")
DNAC_VER = os.environ.get("DNA_CENTER_VERSION")

api = DNACenterAPI(username=DNAC_USER, password=DNAC_PASS, base_url=DNAC_URL, version=DNAC_VER, verify=False)

mydevice = api.devices.get_device_list(serialNumber='YOU_DEVICES_SN#')

pprint(mydevice)
