import time
import datetime
import requests
from bs4 import BeautifulSoup
import random

def initialise():
	logger("##########################    Testing Nike Account Login   ##########################\n\n")

def logger(*args): #Logs information to the command line.    
	t = datetime.datetime.fromtimestamp(time.time())
	fmt = "%H:%M:%S.%f"
	now = t.strftime(fmt)[:-3]

	log = "[" + now + "] " + str(*args)
	print(log)

def create_acc():
	payload={"account":{"email":email,"passwordSettings":{"password":password,"passwordConfirm":password}},"locale":"en_US","welcomeEmailTemplate":"TSD_PROF_MS_WELC_T0_GENERIC_V1.0","registrationSiteId":"nikedotcom","username":email,"firstName":nam[0],"lastName":nam[1],"dateOfBirth":dob,"country":"GB","gender":"F","receiveEmail":True,'client_id':'PbCREuPr3iaFANEDjtiEzXooFl7mXGQ7','ux_id':'com.nike.commerce.snkrs.droid'}


def login():
	sess=requests.session()
	sess.headers.update({"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36","Accept":"*/*","Accept-Encoding":"gzip, deflate, br","Accept-Language":"en-US,en;q=0.9,ms;q=0.8"})
	sess.cookies["CONSUMERCHOICE"]="cn/zh_cn"
	sess.cookies["NIKE_COMMERCE_COUNTRY"]="CN"
	sess.cookies["NIKE_COMMERCE_LANG_LOCALE"]="zh_CN"
	sess.cookies["nike_locale"]="cn/zh_cn"

	email = "michael_goode99@hotmail.co.uk"
	password = "Cheese12"

	dob=str(random.randint(10,28))+"-"+str(random.randint(10,12))+"-"+str(random.randint(1990,1995))

	print(dob)

	logindata = {'keepMeLoggedIn':True, 'client_id':'PbCREuPr3iaFANEDjtiEzXooFl7mXGQ7','ux_id':'com.nike.commerce.snkrs.droid','grant_type':'password','username':email,'password':password}

	e=sess.post('https://api.nike.com/idn/shim/oauth/2.0/token',json=logindata,timeout=30).json()

	print(e["access_token"])

	logger("logged in")




login()
