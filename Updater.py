from subprocess import call
import Version as V1
call(['mv', 'PiCar/Version.py', 'Tmp.py'])
import Tmp as V2
if V2.version > V1.Version:
	# Need to update
	pass
call(['rm', 'Tmp.py'])
