import optparse
import socket
from socket import *
'''
端口扫描器

安装 netstat
sudo apt-get install net-tools

查看端口
netstat -tunlp
'''

def connScan(tgtHost,tgtPort):
    try:
        connSkt = socket(AF_INET,SOCK_STREAM)
        connSkt.connect((tgtHost,tgtPort))
        connSkt.send("ViolentPython")
        print('before send')
        results = connSkt.recv(100)
        print(results)
        print('[+]%d/tcp open'% tgtPort)
        print('[+] '+str(results))
        connSkt.close()
    except Exception as e:
        print(e)
        print('[-]%d/tcp close'% tgtPort)

def main():
    parser = optparse.OptionParser('usage %prog -H'+\
        '<target host> -p <target port>')
    parser.add_option('-H',dest='tgtHost',type='string',\
        help='specify target host')
    parser.add_option('-p',dest='tgtPort',type='int',\
        help='specify target port')
    (options,args) = parser.parse_args()
    tgtHost = options.tgtHost
    tgtPort = options.tgtPort
    if (tgtHost == None) | (tgtPort == None):
        print(parser.usage)
        exit(0)
    connScan(tgtHost,tgtPort)
if __name__ == '__main__':
    main()