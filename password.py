import crypt
import itertools as its
import hashlib

def testpass(cryptPass):
    salt = cryptPass
    print(salt)
    dictFile = open('password.txt','r')
    for word in dictFile.readlines():
        word = word.split('\n')
        cryptWord = crypt.crypt(word[0],salt)
        if (cryptWord == cryptPass):
            print('[+] Found Password : '+word+'\n')
            return
        print('[-] Password Not Found \n')
        return

def getCryptPass(password):
    m = hashlib.sha512()
    m = hashlib.sha384()
    m.update('root'.encode("utf8")) 
    print(m.hexdigest())

def createPassword(repeat=4):
    file = open('./password.txt','w')
    codes = list()
    for ch in range(33,127):
        codes.append(chr(ch))
    passwords = its.product(codes,repeat=repeat)
    for p in passwords:
        file.write("".join(p)+'\n')
    file.close()

def main():
    passFile = open('passwords.txt')
    for line in passFile.readlines():
        if ':' in line:
            user = line.split(':')[0]
            cryptPass = line.split(':')[1].split('  ')
            print('[*] Cracking Password For: ' + user)
            testpass(cryptPass[0])
if __name__ in '__main__':
    #main()
    #createPassword()
    getCryptPass('')