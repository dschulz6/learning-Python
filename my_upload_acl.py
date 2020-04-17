#! /usr/bin/env python
"""
copy acl's from file to router
note: "ip scp server enable" on router

"""
import json
from napalm import get_network_driver

driver = get_network_driver('ios')
iosv = driver('192.168.0.200', 'Engineer', 'ilfnb980')
iosv.open()

# add acls from a file
print ("Accessing 192.168.0.200")
iosv.load_merge_candidate(filename='acl_cfg.txt')
iosv.commit_config()
iosv.close()


