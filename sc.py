#!/usr/bin/python3
import os
import sys
import json
import ansible


host_ip = "192.168.27.52"
pkg_list = []
cnt=0
#f = open("/home/tmax/test_dir/"+host_ip+"/pkg_list_ins.txt")
f = open("/home/tmax/test_dir/"+host_ip+"/pkg_list_rep.txt")
#f = open("/home/tmax/test_dir/"+host_ip+"/pkg_list_upg.txt")




while 1:
	line = f.readline().replace("\n", "")
	if not line: break
	
	pkg_list.append(line)

	cnt = cnt + 1

dic = {"ip": host_ip, "pkg": pkg_list}
#print(dic)

jsonString = json.dumps(dic, indent=4)
print(jsonString)
