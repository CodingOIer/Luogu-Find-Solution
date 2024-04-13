import os

print('Start Update')

os.system('python ./get.py > get.log')
os.system('python ./update.py > update.log')

print('Update Successfully')
