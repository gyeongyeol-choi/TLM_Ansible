#!/bin/bash 
flag=0
while read line 
do 
	if [[ "$line" =~ "The following packages will be upgraded:" ]];then
		flag=1
	fi
	if [[ "$line" =~ "not upgraded." ]];then
		flag=0
	fi
	if [[ $flag == 1 ]];then
		echo $line
	fi
done < "pkg_list_upg_pre.txt"
