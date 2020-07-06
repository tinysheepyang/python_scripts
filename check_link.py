#coding=utf-8

'''
@author: chenshiyang
@fun：爬取url
'''
import urllib2
from sgmllib import SGMLParser
 
import time,urllib2
import codecs 
#import sys 
#reload(sys) 
#sys.setdefaultencoding('utf8')

#功能爬取url

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

def check_link(url,success_file,error_file):

    try:
        f=urllib2.urlopen(url)
        print '被测url：'+url,f.getcode()

        parser=parserXml()
        #防止抓取网站有设防（回避spider抓取），改为浏览器请求，（抓取网站网页所有内容）
        headers = {'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'}


        #此处传一个url参数，是为了显示页面；如果不希望显示页面，可以直接传入具体的URL
        req=urllib2.Request(url,headers=headers)
        page_hander=urllib2.urlopen(req)
        page=page_hander.read()


        #解析
        parser.feed(page)

        #links=parser.hrefs+parser.srcs+parser.hrefs2（链接、图片和视频）
        links=parser.hrefs
        
        count_url=0
        str2='http'
        str3='javascript'
        str4='#'
        str5='backUrl'#过滤掉相对路径的URL，否则会报错

       #log_ok = codecs.open('E:/Python_emao_demo/test_report/emao_log_ok.txt','a','utf-8')
        #log_error=codecs.open('E:/Python_emao_demo/test_report/emao_log_error.txt','a','utf-8')
        log_ok = codecs.open(success_file,'a','utf-8')
        log_error=codecs.open(error_file,'a','utf-8')

        
        log_ok.truncate()#清空
        log_error.truncate()#清空

        links2=list(set(links))#去重
        links2.sort(key=links.index)#保持排序
        for link in links2:  
            #print link      

            
            #if (str3 not in link) and (str4 not in link) and link !='' and (str5 not in link) and len(link)>=10:
                

                try:
                    
                    s=urllib2.urlopen(link)
                    #log_ok.write('url:%s\r\nstatus:%s\t'%(link,s.getcode())) 
                    
                    log_ok.write('%s %s %s\r\n'%(link,s.getcode(),str(count_url)))
                    #log_ok.write('%s\r\n'%(link)) 
                    count_url+=1          


                except urllib2.HTTPError,e:
                    count_url+=1
                    print link,e.getcode(),str(count_url)
                    
                    log_error.write('**********************************************************\r\n')
                    log_error.write('url:%s\r\nstatus:%s\r\ncount_url:%s\r\n'%(link,e.getcode(),str(count_url)))
                    #log_error.write('url:%s\r\nstatus:%s\tcount_url:%s\r\n'%(link,e.getcode(),str(count_url))) 

                except urllib2.URLError,e:
                    print  link+u'无效'  
                    #print str(e)
                    #print e.reason
                except ValueError, e:
                    print link+u'不合法'                

            
        log_ok.close()
        log_error.close()
        parser.close()


    except urllib2.HTTPError,e:
        print '被测url：'+url,e.getcode()

    except urllib2.URLError,e:
        print str(e)
        print e.reason
