ansible-playbook ../playbook/get_list_ins.yml # Get the installed package list.
ansible-playbook ../playbook/get_list_rep.yml # Get the package list stored in the repository.
ansible-playbook ../playbook/get_list_upg.yml # Get the package list that can be updated.
ansible-playbook ../playbook/install_pkg.yml --extra-vars "pkg_name=rolldice" # Install the specific package.
