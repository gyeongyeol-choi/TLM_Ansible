#!/bin/bash 
flag=0
while read line 
do 
	if [[ "$line" =~ "The following packages will be upgraded:" ]];then
		flag=1
		continue
	fi
	if [[ "$line" =~ "not upgraded." ]];then
		flag=0
	fi
	if [[ $flag == 1 ]];then
		echo $line | sed -e 's/ /\n/g'
	fi
done < "pkg_list_upg_pre.txt"
