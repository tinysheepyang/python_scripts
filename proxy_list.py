# -*- coding: utf-8 -*-

# 验证ip是否有效
import urllib2,re,time,urllib,random, os, requests, json
import redis,threading

user_agents = [
    'Mozilla/5.0 (Windows; U; Windows NT 5.1; it; rv:1.8.1.11) Gecko/20071127 Firefox/2.0.0.11',
    'Opera/9.25 (Windows NT 5.1; U; en)',
    'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)',
    'Mozilla/5.0 (compatible; Konqueror/3.5; Linux) KHTML/3.5.5 (like Gecko) (Kubuntu)',
    'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.0.12) Gecko/20070731 Ubuntu/dapper-security Firefox/1.5.0.12',
    'Lynx/2.8.5rel.1 libwww-FM/2.14 SSL-MM/1.4.1 GNUTLS/1.2.9',
]



def proxy(url):
    try:
        data = urllib2.urlopen(url).read()

    except Exception,e:
        print 'proxy 出问题了',e

    s = json.loads(data)
    try:
        if len(s['msg']) == 0:

            return s['data']['proxy_list']
        else:
            print '返回None'
            return None
    except Exception,e:
        print e


def Check(ip_list):
    proxy_ip_list = []
    try:
        for ip in ip_list:
            lock = threading.Lock()
            cookie = "PHPSESSID=5f7mbqghvk1kt5n9illa0nr175; kmsign=56023b6880039; KMUID=ezsEg1YCOzxg97EwAwUXAg=="
            try:
                proxy = 'http://'+ ip

                proxy_support = urllib2.ProxyHandler({'http': proxy})
                opener = urllib2.build_opener(proxy_support, urllib2.HTTPHandler)
                urllib2.install_opener(opener)
                request = urllib2.Request('http://www.baidu.com')
                request.add_header("cookie",cookie)
                request.add_header("User-Agent", random.choice(user_agents))
                content = urllib2.urlopen(request,timeout=4).read()


                if len(content) >= 1000:
                    lock.acquire()
                    proxy_ip_list.append(ip)
                    lock.release()
                else:
                    print '出现验证码或IP被封杀'
            except Exception, error:
                print ip, error
    except Exception, e:
        print 'ip_list', ip_list, e


    return proxy_ip_list

if __name__ == '__main__':
    pool = redis.ConnectionPool(host='192.168.0.42', port=6379, db=0)
    r = redis.Redis(connection_pool=pool)

    proxy_list = Check(proxy('http://dps.kuaidaili.com/api/getdps/?orderid=996639436139576&num=30&ut=1&format=json&sep=2'))

    if len(proxy_list) != 0:
        r.delete('proxy_list')
        print 'delete redis[proxy_list] done'
        for ip in proxy_list:
            r.lpush('proxy_list', ip)
        print 'lpush redis[proxy_list] done'

        print 'proxy_list', len(r.lrange('proxy_list', 0, -1)), random.choice(r.lrange('proxy_list', 0, -1))

    print 'done'
