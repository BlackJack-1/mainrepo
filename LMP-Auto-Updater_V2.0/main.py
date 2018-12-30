#This is the master file for LMP-Auto-Updater V2.0

import os

def run_shell(version_number):
	filename = 'latest_version.txt'
	with open(filename, 'w') as file_object:
		file_object.write(version_number)
		
	os.system('sh '+'autoupdater.sh')

latest_version = "0.19.0"

run_shell(latest_version)
