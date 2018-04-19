# Verify the package by setting the key
sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 9011567A260F6FE7
    
# Construct the package list (in repository)
sudo apt list | cut -d '/' -f1  | sed '1d' > '/home/po7/SC_PKG_LIST/pkg_list_rep.txt'
