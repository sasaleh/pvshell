#!/bin/python

import os;

allhosts=['yosemite','bugs','HOMER','ansi','bugzilla','cob','daffy','elmer','ipa1','ipa2','jenkins','kickstart','os','postgres','squid','win7','speedy','mysql','mongo','kali'];

os.system("clear");

#def listhosts( listall ):

print "*******************************************"
print "**                                       **"
print "** Type L to list all hosts.             **"
print "** Type O to power on a host.            **"
print "** Type D to power down a host.          **"
print "** Type E to destroy a host.             **"
print "** Type P to pause all domains.          **"
print "** Type R to resume all domains.         **"
print "** Type N to power on all domains.       **"
print "** Type Q to quit.                       **"
print "**                                       **"
print "*******************************************\n\n"

x = raw_input();

if x == 'l':
  os.system("virsh list --all");
elif x == 'o':
  os.system("clear");
  os.system("virsh list --all");
  hostx = raw_input('Enter host to power on - ')
  print  "%s is not being turned on.\n" % hostx
  cmd = "virsh start {0}".format(hostx)
  os.system(cmd)
elif x == 'd':
  os.system("clear");
  os.system("virsh list --all");
  hostx = raw_input('Enter host to power down - ')
  print  "%s is not being turned off.\n" % hostx
  cmd = "virsh shutdown {0}".format(hostx)
  os.system(cmd)
elif x == 'e':
  os.system("clear");
  os.system("virsh list --all");
  hostx = raw_input('Enter host to power down - ')
  print  "%s is now being turned off.\n" % hostx
  cmd = "virsh destroy {0}".format(hostx)
  os.system(cmd)
elif x == 'p':
  os.system("clear");
  for z in allhosts:
        subprocess.call(['virsh','pause', z])
elif x == 'r':
  os.system("clear");
  for z in allhosts:
        subprocess.call(['virsh','resume', z])
elif x == 'n':
  os.system("clear");
  for z in allhosts:
        subprocess.call(['virsh','start', z])
elif x == 'q':
  print "Exiting.... "
