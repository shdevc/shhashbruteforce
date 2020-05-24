#! /usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import os
import hashlib


#Main and Options

def main():
	print("""

\t\tMMMMMMMMMMMMMMWXK00O000KXWWMMMMMMMMMMMMM
\t\tMMMMMMMMMWXOdo:,;:'..,;',coxOXWMMMMMMMMM
\t\tMMMMMMMNOo;.,c,.,c,.',,..c;..cdONMMMMMMM
\t\tMMMMMNk;'::.';,''.....'',;,.',..ckNMMMMM
\t\tMMMWKl:;',:;,'............',;'':,.c0WMMM
\t\tMMWO:.';;;;,,...'clc:lc'...,;;:;.',:OWMM
\t\tMM0:,:,,cclk0Oc..l000Kd..:k0Oolc::;.;0MM
\t\tMNl..';ccd0KKX0dd0NNNNKdoOXKKKxlc,,;,lNM
\t\tM0:,'.:::x00K0O0XWWWWWWN0O0000xccc:l;;0M
\t\tMk'...codkOOxc',xWWMMWWk,'cdkOkddl...'kM
\t\tMO,'..lxxxl:,...dXWWWWNd...,;lxxxl..',OM
\t\tMK:',.:kx;...'';:o0KK0d:;''...,dk:.,':KM
\t\tMWx'',cxc.  ..''',;;;;,'''..  .cdc,''xWM
\t\tMMNo.;:,,;.   .,cccccccc,.   .;,'::'oNMM
\t\tMMMNx;''.',,....cdkOOkdc....,,'.'';xNMMM
\t\tMMMMWO:..'.''''..',,,,'..''''.'..:OWMMMM
\t\tMMMMMMNk:'.....'........'.....':kNMMMMMM
\t\tMMMMMMMMW0dc,''..........'';cd0WMMMMMMMM
\t\tMMMMMMMMMMMWX0kdolcccclodk0XWMMMMMMMMMMM
\t\tMMMMMMMMMMMMMMMMMMWWWWMMMMMMMMMMMMMMMMMM

\t____ ____ _  _ _  _ _  _ ____ _  _ _  _ ____ ____ _  _ ____ ____ 
\t[__  |__| |  | |  | |\ | |__| |\ | |__| |__| |    |_/  |___ |__/ 
\t___] |  |  \/  |__| | \| |  | | \| |  | |  | |___ | \_ |___ |  \ 
                                                                 
                                                                                                              
                

    \tBruteforce Options
    \t------------------
	[1] MD5 Bruteforce
	[2] SHA256 Bruteforce
	[3] SHA1 Bruteforce
	[4] SHA224 Bruteforce
	[5] SHA384 Bruteforce
	----------------------
	[10] Exit

""")


	select = raw_input("\n\tSelect Options : ")
	if (select=="1"):
		md5b()
	elif(select=="2"):
		sha256b()
	elif(select=="3"):
		sha1b()
	elif(select=="4"):
		sha224b()
	elif(select=="5"):
		sha384b()
	elif(select=="10"):
		print("\n\t[-] Exit")
		sys.exit()
	else:
		main()

#MD5 Hash Decode

def md5b():
	counter = 0
	lines = 0
        md5text=raw_input("\n\tMD5 Hash : ")
        wordlist = raw_input("\n\tWordlist : ")
        try:
                wordlistfile = open(wordlist)
                for line in open(wordlist):
                        lines += 1
        except IOError:

                print "\n\t[!] İnvalid Wordlist"
                mainback = raw_input("\n\tBack To Menu [y/n] : ")
                if (mainback=="y"):
                	main()
                elif (mainback=="n"):
                	print "\n\n\t[!] Exit"
                	sys.exit()
        else:
                pass
        for line in wordlistfile:
                algorithim = hashlib.md5()
                line = line.replace("\n","")
                algorithim.update(line)
                wordlistdecrypted = algorithim.hexdigest()
                counter += 1
                percentage_raw = float(counter) / float(lines) * 100
                percentage_raw ="\tTry...\t%0f" % percentage_raw; percentage = str(percentage_raw)
                print(percentage)
                if wordlistdecrypted == md5text:
                        print '\n\t[+] Decrypted : %s' % line
                        mainback = raw_input("\n\tBack To Menu [y/n] : ")
                        if (mainback=="y"):
                        	main()
                        elif (mainback=="n"):
                        	print "\n\n\t[!] Exit"
                        	sys.exit()

#SHA256 Hash Decode

def sha256b():
	counter = 0
	lines = 0
        sha256text=raw_input("\n\tSHA256 Hash : ")
        wordList = raw_input("\n\tWordlist : ")
        try:
                wordlistfile = open(wordList)
                for line in open(wordList):
                        lines += 1
        except IOError:

                print "\n\t[!] İnvalid Wordlist"
                mainback = raw_input("\n\tBack To Menu [y/n] : ")
                if (mainback=="y"):
                	main()
                elif (mainback=="n"):
                	print "\n\n\t[!] Exit"
                	sys.exit()
        else:
                pass
        for line in wordlistfile:
                algorithim = hashlib.sha256()
                line = line.replace("\n","")
                algorithim.update(line)
                wordlistdecrypted = algorithim.hexdigest()
                counter += 1
                percentage_raw = float(counter) / float(lines) * 100
                percentage_raw ="\tTry...\t%0f" % percentage_raw; percentage = str(percentage_raw)
                print(percentage)
                if wordlistdecrypted == sha256text:
                        print '\n\t[+] Decrypted : %s' % line
                        mainback = raw_input("\n\tBack To Menu [y/n] : ")
                        if (mainback=="y"):
                        	main()
                        elif (mainback=="n"):
                        	print "\n\n\t[!] Exit"
                        	sys.exit()

#SHA1 Hash Decode

def sha1b():
	counter = 0
	lines = 0
        sha1text=raw_input("\n\tSHA1 Hash : ")
        wordList = raw_input("\n\tWordlist : ")
        try:
                wordlistfile = open(wordList)
                for line in open(wordList):
                        lines += 1
        except IOError:

                print "\n\t[!] İnvalid Wordlist"
                mainback = raw_input("\n\tBack To Menu [y/n] : ")
                if (mainback=="y"):
                	main()
                elif (mainback=="n"):
                	print "\n\n\t[!] Exit"
                	sys.exit()
        else:
                pass
        for line in wordlistfile:
                algorithim = hashlib.sha1()
                line = line.replace("\n","")
                algorithim.update(line)
                wordlistdecrypted = algorithim.hexdigest()
                counter += 1
                percentage_raw = float(counter) / float(lines) * 100
                percentage_raw ="\tTry...\t%0f" % percentage_raw; percentage = str(percentage_raw)
                print(percentage)
                if wordlistdecrypted == sha1text:
                        print '\n\t[+] Decrypted : %s' % line
                        mainback = raw_input("\n\tBack To Menu [y/n] : ")
                        if (mainback=="y"):
                        	main()
                        elif (mainback=="n"):
                        	print "\n\n\t[!] Exit"
                        	sys.exit()

#SHA224 Hash Decode

def sha224b():
	counter = 0
	lines = 0
        sha224text=raw_input("\n\tSHA224 Hash : ")
        wordList = raw_input("\n\tWordlist : ")
        try:
                wordlistfile = open(wordList)
                for line in open(wordList):
                        lines += 1
        except IOError:

                print "\n\t[!] İnvalid Wordlist"
                mainback = raw_input("\n\tBack To Menu [y/n] : ")
                if (mainback=="y"):
                	main()
                elif (mainback=="n"):
                	print "\n\n\t[!] Exit"
                	sys.exit()
        else:
                pass
        for line in wordlistfile:
                algorithim = hashlib.sha224()
                line = line.replace("\n","")
                algorithim.update(line)
                wordlistdecrypted = algorithim.hexdigest()
                counter += 1
                percentage_raw = float(counter) / float(lines) * 100
                percentage_raw ="\tTry...\t%0f" % percentage_raw; percentage = str(percentage_raw)
                print(percentage)
                if wordlistdecrypted == sha224text:
                        print '\n\t[+] Decrypted : %s' % line
                        mainback = raw_input("\n\tBack To Menu [y/n] : ")
                        if (mainback=="y"):
                        	main()
                        elif (mainback=="n"):
                        	print "\n\n\t[!] Exit"
                        	sys.exit()



#SHA384 Hash Decode

def sha384b():
	counter = 0
	lines = 0
        sha384text =raw_input("\n\tSHA384 Hash : ")
        wordList = raw_input("\n\tWordlist : ")
        try:
                wordlistfile = open(wordList)
                for line in open(wordList):
                        lines += 1
        except IOError:

                print "\n\t[!] İnvalid Wordlist"
                mainback = raw_input("\n\tBack To Menu [y/n] : ")
                if (mainback=="y"):
                	main()
                elif (mainback=="n"):
                	print "\n\n\t[!] Exit"
                	sys.exit()
        else:
                pass
        for line in wordlistfile:
                algorithim = hashlib.sha384()
                line = line.replace("\n","")
                algorithim.update(line)
                wordlistdecrypted = algorithim.hexdigest()
                counter += 1
                percentage_raw = float(counter) / float(lines) * 100
                percentage_raw ="\tTry...\t%0f" % percentage_raw; percentage = str(percentage_raw)
                print(percentage)
                if wordlistdecrypted == sha384text:
                        print '\n\t[+] Decrypted : %s' % line
                        mainback = raw_input("\n\tBack To Menu [y/n] : ")
                        if (mainback=="y"):
                        	main()
                        elif (mainback=="n"):
                        	print "\n\n\t[!] Exit"
                        	sys.exit()

if __name__ == "__main__":
	try:
		main()
	except KeyboardInterrupt as err:
		print "\n\n\t[!] Exit"
		sys.exit()