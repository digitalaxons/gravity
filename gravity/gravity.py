__author__ = 'Derek <digital axons (at) gmail>'
import sys
import os
import syslog
import gravity.config.msg



gravity.config.msg.showbanner()
gravity.config.msg.showusage()
syslog.openlog("gravity", logoption=syslog.LOG_PID)
syslog.syslog("Gravity starting")