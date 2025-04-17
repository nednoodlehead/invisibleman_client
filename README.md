# Invisible Man!

An asset management database client that interfaces with a centralized postgreSQL server to relay IT assets within a LAN. Built with PyQt5

Includes:
1. An intuitive interface
2. Simple search and filtering functionality
3. Easy to use, and externally modify config
4. Dark mode :o
5. Customizable dropdowns
6. Asset depreciation tracking (Customizable)
7. Customizable graphs for viewing data
8. Exportable reports (CSV, Excel)
9. A simple backup / restore system (Semi-WIP)
10. Asset depreciation early warning calendar


Invisible man: Inventory Manager -> Inv Man -> Invisible Man (hiliarous I know)


Usage instructions:

1. Configure invisman server
2. Go into windows credential manager and set some generic credentials:
Cred1:
Internet or network address: invisman
User name: <Username for the linux server>
Password: <password for the user account on linux> (this should be the same name as the database name)

Cred2:
Internet or network address: invisman_sshkey
User name: <Path to your private key>
Password: <Password for your private key>
3. Create a public/private ssh key (ssh-keygen)
3a. put the public key's string inside of ~/.ssh/authorized_keys  <- this is a file, not a folder

Once you have git cloned invisman, you should go into the "Settings" tab and fill out the related network settings (Ip of server, username for db/linux and where you ssh keyfile is)
