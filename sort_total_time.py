# -*- coding: utf-8 -*-
from sgmllib import SGMLParser 
import urllib2
import pycurl
import subprocess
import os, inspect

#统计页面加载时间并发送

class parserXml(SGMLParser):
 
       def __init__(self):
            SGMLParser.__init__(self)
            self.hrefs = []
            self.srcs= []
            #保存视频数组
            self.hrefs2=[]
      #获取超链接href值
       def start_a(self, attrs):
            href = [v for k, v in attrs if k == "href"]
            self.hrefs.extend(href)
     #获取图片超链接href值
       def start_img(self, attrs):
            src = [v for k, v in attrs if k == "src"]
            self.srcs.extend(src)
     #获取视频超链接href值
       def start_embed(self,attrs):
           href2=[v for k, v in attrs if k=="href"]
           self.hrefs2.extend(href2)

def check_link(url):

    try:
        f=urllib2.urlopen(url)
        print '被测url：'+url,f.getcode()

        parser=parserXml()
        #防止抓取网站有设防（回避spider抓取），改为浏览器请求，（抓取网站网页所有内容）
        headers = {'User-Agent':'EMAO_OPS_MONITOR/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'}


        #此处传一个url参数，是为了显示页面；如果不希望显示页面，可以直接传入具体的URL
        req=urllib2.Request(url,headers=headers)
        page_hander=urllib2.urlopen(req)
        page=page_hander.read()


        #解析
        parser.feed(page)

        #links=parser.hrefs+parser.srcs+parser.hrefs2（链接、图片和视频）
        links=parser.hrefs
        
        success_url = []
        error_url = []
        url_status = []
        

        links2=list(set(links))#去重
        links2.sort(key=links.index)#保持排序
        for link in links2:          
            if 'emao' in link:
                try:
                    s = urllib2.urlopen(link)
                    url_status.append(s.getcode())
                    success_url.append(link)
                        

                except urllib2.HTTPError,e:

                    error_url.append(link)
                    url_status.append(e.getcode())

                except urllib2.URLError,e:
                    print  link + 'invalidation'  
                    #print str(e)
                    #print e.reason
                except ValueError, e:
                    print link + ' unlawfulness'               

            
        parser.close()


    except urllib2.HTTPError,e:
        print '被测url：' + url,e.getcode()

    except urllib2.URLError,e:
        print str(e)
        print e.reason


    return success_url


class Test:
        def __init__(self):
            self.contents = ''

        def callback(self,curl):
            self.contents = self.contents + curl

def test_gzip(url): 

    

        t = Test() 
        c = pycurl.Curl()  
        c.setopt(pycurl.WRITEFUNCTION,t.callback)
        c.setopt(pycurl.ENCODING, 'gzip')
        c.setopt(pycurl.URL,url) 
        c.setopt(pycurl.USERAGENT,"User-Agent':'EMAO_OPS_MONITOR) Gecko/20091201 Firefox/3.5.6)")
        c.perform()   
          
        TOTAL_TIME = c.getinfo(c.TOTAL_TIME)
          
           
        #print "传输结束总时间：%.2f ms" %(TOTAL_TIME*1000) 
        return TOTAL_TIME * 1000


def average(url_list):
    url_time = {}
    for url in url_list:
        # 每次加载所用时间集合
        elapsed_time_list = []
        # 总共加载时间
        total_elapsed_time = 0
        # 需要访问次数
        visit_times = 50
        
        #print "###############################################################"
        #print "Loading website %s times, each elapsed time shown down:\n" % visit_times
        for i in xrange(visit_times):
            elapsed_time_list.append(test_gzip(url))

        for j in xrange(len(elapsed_time_list)):
            total_elapsed_time = total_elapsed_time + int(elapsed_time_list[j])
            #print "%s . loading %s . elapsed time %s" % (j, url, elapsed_time_list[j - 1])

        #print "\nLoading website %s times, total elapsed time: %s" % (visit_times, total_elapsed_time)
        #print "\n %s Loading website %s times, average elapsed time: %.2f\n" % (url, visit_times, float(total_elapsed_time)/visit_times)
        url_time[url] = float(total_elapsed_time)/visit_times

    return url_time

def sort_dict(url_dict):
    dic = sorted(url_dict.iteritems(), key=lambda d:d[1], reverse=True)
    long_time_url = []
    
    count = 0

    for i in dic:
        count += 1

        long_time_url.append(i)
        if count == 10:
            break

    return long_time_url   

     

if __name__ == '__main__':
    
    
    ret = sort_dict(average(check_link('http://www.emao.com')))
    sendlist = ''
    for firstlevel in ret:
        sendlist += str(firstlevel[1]).split('.')[0].strip() + 'ms' + '__' + str(firstlevel[0])
        sendlist += '___'
  
    RESULT_PATH = os.path.dirname(os.path.abspath(inspect.stack()[-1][1]))

    cmd = ["python", os.path.join(RESULT_PATH, 'mail.py'), "-e", "online", '-u', sendlist, '-t', 'ops@emao.com']

    sendsms = subprocess.Popen(cmd, stdout = subprocess.PIPE,
                stderr = subprocess.PIPE)

    sendsms.wait()
    print'sendsms ret:' 
    

    for line in sendsms.stdout.readlines():
        print line
        

    for line in sendsms.stderr.readlines():
        print line
