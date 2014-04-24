__author__ = 'Derek <digital axons (at) gmail>'
import sys

def showbanner():
	print
	print ("Gravity rel 0.1 | April 2014 Concept")
	print

def showusage():
	print("Usage: gravity [MODE][OPTIONS]...\n");
	print("MODE");
	print(" --on        Start deamon");
	print(" --off       Switch off deamon");
	print(" --restart   Restart deamon");
	print(" --status    Brief status information\n");
	print("OPTIONS");
	print("")
	print(" -c FILE     Configuraion file");
	print(" -h          Display this help and exit");
	print(" -v          Output version information and exit\n");

showbanner();
showusage();