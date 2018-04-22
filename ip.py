import socket
def retBanner(ip,prot):
    try:
        socket.setdefaulttimeout(2)#设置超时时间
        s = socket.socket()
        s.connect((ip,prot))
        banner = s.recv(1024)
        return banner
    except:
        return


def checkValues(banner):
    if 'FreeFloat Ftp Server (Version 1.00) ' in banner:
        print('[+] FreeFloat Ftp Server is vulnerable')
    elif '3Com 3CDaemon FTP Server is vulnerable' in banner:
        print('[+] 3CDaemon FTP Server is vulnerable')  
    elif 'Ability Server 2.34' in banner:
        print('[+] Ability Ftp Server is vulnerable')
    elif 'Sami Ftp Server 2.0.2' in banner:
        print('[+] Sami Ftp Server is vulnerable')
    else:
        print('[-] Ftp Server is not vulnerable')      
    return 

def main():
    protList = [21,22,25,80,110,443]
    for x in range(1,255):
        ip = '192.168.95.'+str(x)
        for prot in protList:
            banner = retBanner(ip,prot)
            if banner:
                print('[+] ' + ip + ': ' + banner)
                checkValues(banner)

if __name__ == '__main__':
    main()