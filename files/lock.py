import os
import sys
import subprocess
import json
import ansible

if __name__ == "__main__":
	
	#pkg_list = []
	host_ip = "192.168.9.82"
	
	f_del = open("./delete.json", 'r')
	f_del2 = open("./delete_post.json", 'w')
	f_lock = open("/home/po7/SC_PKG_LIST/"+host_ip+"/pkg_list_lock.txt")	


	data = f_del.read()
	dic = json.loads(data)

	#print(data)
	#print(dic['packName'])

	while 1:
		line = f_lock.readline().rstrip('\n')
		if not line: break


		#while 1:
		if dic['packName'].count(line) > 0:
			dic['packName'].remove(line)
			#print(dic['packName'].index(line))

	
	#print(data)
	#print(dic['packName'])
	jsonString = json.dumps(dic, indent=4)
	#print(jsonString)

	f_del2.write(jsonString)

		
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
