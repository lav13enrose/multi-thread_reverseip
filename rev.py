import requests
import re
import time
import threading
import sys
import queue
import sys
import datetime
import random
import os
os.system('cls' if os.name == 'nt' else 'clear')
class reverse():

	apiexceded 	= 'API count exceeded'.encode()
	checkpm		= 'error check your search parameter'.encode()
	nodns 		= 'No DNS A records found'.encode()
	manyreq 	= 'Many Requests'.encode()
	proxyjelek  = 'Not authenticated or invalid authentication credentials. Make sure to update your proxy address, proxy username and port.'.encode()
	input_queue = queue.Queue()
    

	def __init__(self):

		print(r"""

    ██╗███████╗░█████╗░███╗░░██╗███████╗██╗░░██╗██████╗░██╗░░░░░░█████╗░██╗████████╗
    ██║╚════██║██╔══██╗████╗░██║██╔════╝╚██╗██╔╝██╔══██╗██║░░░░░██╔══██╗██║╚══██╔══╝
    ██║░░███╔═╝██║░░██║██╔██╗██║█████╗░░░╚███╔╝░██████╔╝██║░░░░░██║░░██║██║░░░██║░░░
    ██║██╔══╝░░██║░░██║██║╚████║██╔══╝░░░██╔██╗░██╔═══╝░██║░░░░░██║░░██║██║░░░██║░░░
    ██║███████╗╚█████╔╝██║░╚███║███████╗██╔╝╚██╗██║░░░░░███████╗╚█████╔╝██║░░░██║░░░
    ╚═╝╚══════╝░╚════╝░╚═╝░░╚══╝╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚══════╝░╚════╝░╚═╝░░░╚═╝░░░

    [ HackerTarget IPs Reverse ] - facebook.com/lav13enrose 

		""")

		self.mailist = input(" -> Enter IPs : ")
		self.proxyny = input(" -> Proxy List : ")
		self.thread = input(" -> Thread : ")
		self.count_list = len(list(open(self.mailist)))
		self.clean = input(" -> Clean Result ? (y/n) ")
		if self.clean == 'y' : self.clean_rezult()
		print('')

	def save_to_file(self,nameFile,x):
		kl = open(nameFile, 'a+')
		kl.write(x)
		kl.close()

	def clean_rezult(self):
		open('live.txt', 'w').close()
		open('die.txt', 'w').close()
		open('unknown.txt', 'w').close()
	def post_email(self,ips):
		lines = open(self.proxyny).read().splitlines()
		mylines = random.choice(lines)
		proxies = { 
		"http"  : "http://"+mylines, 
		}
		r = requests.get("http://api.hackertarget.com/reverseiplookup/?q="+ips,timeout=5,proxies=proxies)
		if self.apiexceded in r.content: return 'apiexceded'
		elif self.checkpm in r.content: return 'checkpm'
		elif self.nodns in r.content: return 'nodns'
		elif self.manyreq in r.content: return 'manyreq'
		elif self.proxyjelek in r.content: return 'proxyjelek'
		else : return r.text
	def chk(self):
		while 1:
			ips = self.input_queue.get()
			rez = self.post_email(ips)
			if rez == 'apiexceded':
				print('- CHANGEPROX - '+ips)
			elif rez == 'checkpm':
				print('- CHECKPARAM - '+ips)
			elif rez == 'nodns':
				print('- NODNS - '+ips)
			elif rez == 'manyreq':
				print('- MANYREQ - '+ips)
			elif rez == 'proxyjelek':
				print('- PROXJELEK - '+ips)
			else:
				print('SUCCESS - '+ips)
				self.save_to_file('live.txt',rez+'\n')
			self.input_queue.task_done()
	def run_thread(self):

		self.start_time = time.time()

		for x in range(int(self.thread)):
			t = threading.Thread(target=self.chk)
			t.setDaemon(True)
			t.start()

		for y in open(self.mailist, 'r').readlines():
			self.input_queue.put(y.strip())
		self.input_queue.join()

	def finish(self):
		print('')
		print('+==========================================================+')
		print('')
		print('Checking ',self.count_list,' IPs')
		print('Processing time : ',time.time() - self.start_time,'seconds')
		print('')
		print('Reversed and got : ',len(list(open('live.txt'))),'website')
		print('')

heh = reverse()
heh.run_thread()
heh.finish()
