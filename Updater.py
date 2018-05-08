from subprocess import call
import Variables as V1
import os

def update():        
        call(['git', 'clone', '-q', 'https://www.github.com/ImMilesAhead/PiCar'])
        call(['cp', 'PiCar/Variables.py', 'Tmp.py'])
        import Tmp as V2
        # Compare newly downloaded version to current version
        if V2.version > V1.version:
                # Need to update
                print('Need to update')
                files = os.listdir('./PiCar')
                shFile = open('update.sh', 'w')
                for f in files:
                        if not f[0] == '.':
                                # Add line to new sh file
                                shFile.write('cp PiCar/' + f + ' ./\n')
                shFile.write('rm Tmp.py\n')
                shFile.write('rm -r PiCar\n')
                shFile.write('echo Done!\n')
                shFile.close()
                print('chmodding')
                call(['chmod', '+x', 'update.sh'])
                call(['sh', 'update.sh'])
                call(['rm', 'update.sh'])
        else:
                print('Version is up to date at version: ' + str(V2.version))
                call(['rm', 'Tmp.py'])
                call(['rm', '-r', 'PiCar'])

if __name__ == '__main__':
        update()
