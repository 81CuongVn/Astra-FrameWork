#!/usr/bin/python
#
# quick installer for SET
#
#
from __future__ import print_function
import subprocess
import os
subprocess.Popen("mkdir /usr/share/setoolkit/;mkdir /etc/setoolkit/;cp -rf * /usr/share/setoolkit/;cp src/core/config.baseline /etc/setoolkit/set.config", shell=True).wait()
filewrite = open("/usr/local/bin/setoolkit", "w")
filewrite.write("#!/bin/sh\ncd /usr/share/setoolkit\n./setoolkit")
filewrite.close()
subprocess.Popen("chmod +x /usr/local/bin/setoolkit", shell=True).wait()