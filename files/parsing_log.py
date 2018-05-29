import os
import sys
import subprocess
import json
import ansible
import re

if __name__ == "__main__":
	
	flag = False

	host_ip = []
	st_1 = []
	st_2 = []
	st_3 = []
	st_4 = []
	ind = 0

	f_1 = open("./result_pre.log", 'r')
	f_2 = open("./result.log", 'w')


	#data = f_del.read()
	#dic = json.loads(data)

	#print(data)
	#print(dic['packName'])

	while 1:
		line = f_1.readline().rstrip('\n')
		#tmp=line.split(':')
		#print(tmp)
		#data=line.split(' ')
		#print(data)
		#print(line)
		
		if flag and not line:
			break

		if line.count('RECAP') > 0:
			flag = True
			continue
			
		if flag:
			#print(line)	
			f_2.write(line)
			data=re.split("[\:\s]*", line)
			
			#print(data[0])
			host_ip.append(data[0])
			
			st_1.append(data[1].replace('ok=',''))
			st_2.append(data[2].replace('changed=',''))
			st_3.append(data[3].replace('unreachable=',''))
			st_4.append(data[4].replace('failed=',''))
			ind = ind+1

	print(host_ip)
	print(st_1)
	print(st_2)
	print(st_3)
	print(st_4)
		
		#if dic['packName'].count(line) > 0:
		#	dic['packName'].remove(line)
			#print(dic['packName'].index(line))

	
	#print(data)
	#print(dic['packName'])
	#jsonString = json.dumps(dic, indent=4)
	#print(jsonString)

	#f_del2.write(jsonString)

		
'''
	while 1:
	        line = f.readline().replace("\n", "")
	        if not line: break

		if play == 'get_upg':
			pkg_list.extend(line.split())
		else:
	        	pkg_list.append(line)

	dic = {"nodeID": host_ip, "packName": pkg_list}

	jsonString = json.dumps(dic, indent=4)
	print(jsonString)
'''
