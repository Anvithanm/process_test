import subprocess
import re
import os
import signal
import sys
# import psutil
def processes(sys1):
	try:	
		global y
		global datalist
		global templist
		global datatuple
		global newlist
		datalist = []
		templist = []
		datatuple = []
		newlist = []
		res = []		
		count = 0
		cmd = subprocess.Popen(["ps", "-eF"], 	stdout=subprocess.PIPE)
		a = cmd.communicate() #Returns a tuple of running process
		for i in a:
			i = i.split("\n")
			b = re.compile(str(sys1))	
			process = filter(b.search, i) #Filtering the string based on the regular expression
			process.pop(-1)
			if process:
				print "The running processes are"
				for pro in process:
					count += 1		
					pro = pro.split()
					profile = str(count)+ " "+ pro[1]+ " "+ "-" "The PID of the running process-"+ pro[-1]
					print profile					
					datalist.append(str(count))
					newlist.append(profile)
					templist = datalist[:] #copying the list to templist
				for x in templist:		
					datatuple.append(x)
					y = tuple(datatuple)
			else:	
				print "There is no Process running for the given pattern \n"
				sys.exit()
	except AttributeError:
		pass	
def elimination():
	try:	
		count1 = 0
		while count1 < 3:
			userinp = raw_input("Enter the value: ")
			if userinp in y:
				count1 = 0		
				for data in newlist:		
					cc = data.split()
					if userinp == cc[0]:
						print "The process selected by the user is"+ " "+ cc[1]+ "-" + cc[-1] 
						os.kill(int(cc[1]), signal.SIGKILL) #SIGKILL signal is sent to the process to cause it to terminate it immediately
						print "Process is killed"
				processes(sys1)
			elif userinp == "exit":
				sys.exit()
			else:
				print "Invalid value"
				count1 += 1
	except Exception as e:
		print "Error log--%s-%s\n" %(e,cc[1])
		#raise 
		#print e
		pass
try:
	sys1 = sys.argv[1]
	processes(sys1)
	elimination()
except IndexError:
		print "Add the process name as command line argument"
		print "Example: python running_everyprocess.py"+ " "+ "<Process Name>"
