import os
import sys
import subprocess
import json
import ansible


host_ip = "192.168.27.52"
#pkg_list = []

p = subprocess.call('ansible-playbook playbook/get_list_ins.yml', shell=True)

f = open("../test_dir/"+host_ip+"/pkg_list_ins.txt")
#f = open("../test_dir/"+host_ip+"/pkg_list_rep.txt")
#f = open("../test_dir/"+host_ip+"/pkg_list_upg.txt")

while 1:
        line = f.readline().replace("\n", "")
        if not line: break

        pkg_list.append(line)


dic = {"nodeID": host_ip, "packName": pkg_list}

jsonString = json.dumps(dic, indent=4)
print(jsonString)
