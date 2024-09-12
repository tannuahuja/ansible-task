# ansible-task
 
cd /etc/ansible 
is a default file in which we have ansible invertory and ansible.cfg file 

and in a folder we have created the yml file in which we have added the instructions 

ansible all -m ping
to check ping pong and to check the connectivity

ansible-playbook file.yml
yml file is to be run on this 

it is asking password 
ansible-playbook  configure-logs.yml --ask-become-pass

this is the command which ask password to login in =to the servers which needs passwords 
