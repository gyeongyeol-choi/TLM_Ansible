import os
import sys
import subprocess
import json
import ansible

def usage():
	print("""**********************************************************************************************************************
Usage : python %s [-p play] [-i host_ip]
* play: get_ins (Make the Installed package list) / get_rep (Make the package list in the repository) / ins (Install the selected package(s)) / del (Remove the selected package(s))
* host_ip : ipv4 address of the remote node
**********************************************************************************************************************""" % (sys.argv[0]))

#play=""
#pl_path=""

def configuration():
	global play
	global host_ip

	if sys.argv.count('-h') == 1:
		usage()
		sys.exit()
	if sys.argv.count('-p') == 1:
		index = sys.argv.index('-p') + 1
		play = sys.argv[index]
	else:
		print "Selecting the default playbook option (get_ins)"
		play = 'get_ins'

	if sys.argv.count('-i') == 1:
		index = sys.argv.index('-i') + 1
		host_ip = sys.argv[index]
	else:
		print "Using the default host ip (192.168.27.52)"
		host_ip = "192.168.27.52"

def playbook():
	global pl_path # Playbook Path

	if play == 'get_ins':
		pl_path = 'playbook/get_list_ins.yml'
	elif play == 'get_rep':
		pl_path = 'playbook/get_list_rep.yml'
	elif play == 'ins':
		pl_path = "playbook/install_pkg.yml --extra-vars='@./files/add.json'"
	elif play == 'del':
		pl_path = "playbook/delete_pkg.yml --extra-vars='@./files/delete.json'"
	else:
		print ("Error!!: Invalid argument (-p) ...")
		sys.exit()


if __name__ == "__main__":
	
	pkg_list = []
	
	configuration()
	print("Play: " + play)
	playbook()

	p = subprocess.call('ansible-playbook '+pl_path, shell=True)

	if play == 'get_ins':
		f = open("../test_dir/"+host_ip+"/pkg_list_ins.txt")
	elif play == 'get_rep':
		f = open("../test_dir/"+host_ip+"/pkg_list_rep.txt")
	else:
		sys.exit()

	while 1:
	        line = f.readline().replace("\n", "")
	        if not line: break

	        pkg_list.append(line)

	dic = {"nodeID": host_ip, "packName": pkg_list}

	jsonString = json.dumps(dic, indent=4)
	print(jsonString)
