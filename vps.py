import os
cmd='''apt-get install python-pip
pip install shadowsocks
'''
os.system(cmd)
os.system("hostname -I")
ss_ip=input("please input your vps ip:")
ss_port=input("please input your shadowsocks server port:")
ss_password=input("please input your shadowsocks password:")
shadowsocks_json='''
{
    "server":"your_server_ip",
    "server_port":%s,
    "local_address": "127.0.0.1",
    "local_port":1080,
    "password":"%s",
    "timeout":300,
    "method":"aes-256-cfb",
    "fast_open": false
}
''' % (ss_ip,ss_port,ss_password)
if os.path.exists("/etc/shadowsocks.json"):
    os.system("rm /etc/shadowsocks.json")
with open("/etc/shadowsocks.json","a+") as f:
    f.write(shadowsocks_json)
print("your shadowsocks config file content is:\n"+shadowsocks_json)
os.system("ssserver -c /etc/shadowsocks -d start")
lang2utf8='''
sudo apt-get install language-selector language-env language-pack-zh-hans
dpkg-reconfigure locales
echo 'LANG="zh_CN.UTF-8"' > /etc/default/locale
echo 'LANGUAGE="zh_CN:zh"' >> /etc/default/locale
'''
os.system("lang2utf8")
os.system("wget https://raw.githubusercontent.com/3xp10it/mytools/master/xPre.py && python3 xPre.py")

