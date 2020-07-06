# -*- coding: utf-8 -*-
#------------------------------------------------------------------------------
#Filename: check_cache.py
#Author  : 陈仕洋
#Date    : 2016-01-04
#Description:渠道打开浏览器输入url，导出所有网络信息，解析导出har文件哪些没有缓存
#Usage   : Python chec_cache.py -u url -o E:\\har\\output\\output.txt -s 
#          E:\\har\\output\\sort.txt
#Notes   :此脚本在Windows下运行，运行前请先装好firefox,firebug,netexport插件 
#         firestarter不想装注释就好

import json
from haralyzer import HarParser
import codecs
import time, os, sys
from selenium import webdriver
from optparse import OptionParser

nowtime = time.strftime("%Y-%m-%d-%H_%M_%S",time.localtime(time.time()))
#url = 'www.emao.com'
webdriverlog = 'E:\\har\\webFile.txt'
har_path = 'E:\\har'
#output_file = 'E:\\har\\output\\output.txt'
#sort_file = 'E:\\har\\output\\sort.txt'

#打开浏览器导出har文件
def openURL(url):

    fireBugPath = 'C:\\Users\\csy\\AppData\\Roaming\\Mozilla\\Firefox\\Profiles\\gsmljxqq.default\\extensions\\firebug@software.joehewitt.com.xpi';
    netExportPath = 'C:\\Users\\csy\\AppData\\Roaming\\Mozilla\\Firefox\\Profiles\\gsmljxqq.default\\extensions\\netexport@getfirebug.com.xpi';
    fireStarterPath = 'C:\\Users\\csy\\AppData\\Roaming\\Mozilla\\Firefox\\Profiles\\gsmljxqq.default\\extensions\\firestarter@getfirebug.com.xpi';

    profile = webdriver.firefox.firefox_profile.FirefoxProfile(r'C:\\Users\\csy\\AppData\\Roaming\\Mozilla\\Firefox\\Profiles\\gsmljxqq.default');
    profile.add_extension( fireBugPath);
    profile.add_extension(netExportPath);
    profile.add_extension(fireStarterPath);

    #firefox preferences
    profile.set_preference("app.update.enabled", False)  
    profile.native_events_enabled = True
    profile.set_preference("webdriver.log.file", webdriverlog)
    profile.set_preference("extensions.firebug.DBG_STARTER", True);

    profile.set_preference("extensions.firebug.currentVersion", "2.0.16");#填写实际安装的firebug版本号
    profile.set_preference("extensions.firebug.addonBarOpened", True);
    profile.set_preference("extensions.firebug.addonBarOpened", True);
    profile.set_preference('extensions.firebug.consoles.enableSite', True)                          


    profile.set_preference("extensions.firebug.console.enableSites", True);
    profile.set_preference("extensions.firebug.script.enableSites", True);
    profile.set_preference("extensions.firebug.net.enableSites", True);
    profile.set_preference("extensions.firebug.previousPlacement", 1);
    profile.set_preference("extensions.firebug.allPagesActivation", "on");
    profile.set_preference("extensions.firebug.onByDefault", True);
    profile.set_preference("extensions.firebug.defaultPanelName", "net");

    #set net export preferences
    profile.set_preference("extensions.firebug.netexport.alwaysEnableAutoExport", True);
    profile.set_preference("extensions.firebug.netexport.autoExportToFile", True);
    profile.set_preference("extensions.firebug.netexport.saveFiles", True);

    profile.set_preference("extensions.firebug.netexport.autoExportToServer", False);
    profile.set_preference("extensions.firebug.netexport.Automation", True);
    profile.set_preference("extensions.firebug.netexport.showPreview", False);
    profile.set_preference("extensions.firebug.netexport.pageLoadedTimeout", 15000);
    profile.set_preference("extensions.firebug.netexport.timeout", 10000);

    profile.set_preference("extensions.firebug.netexport.defaultLogDir", har_path);
    profile.update_preferences();
    browser = webdriver.Firefox(firefox_profile=profile);
    browser.maximize_window()

    print '***',url

    time.sleep(6);
    #browser = webdriver.Chrome();
    browser.get('http://www.emao.com'); #load the url in firefox
    time.sleep(3); #wait for the page to load
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight/5);")
    time.sleep(1); #wait for the page to load
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight/4);")
    time.sleep(1); #wait for the page to load
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight/3);")
    time.sleep(1); #wait for the page to load
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight/2);")
    time.sleep(1); #wait for the page to load
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    #searchText='';
    time.sleep(20); #wait for the page to load

    browser.quit();


#冒泡取出最近时间文件
def swap(target_list):   #sorting folder list according to create time
    for i in range(len(target_list)):
        if i < (len(target_list)-1) and target_list[i][0] > target_list[i+1][0]:
            temp = target_list[i+1]
            target_list[i+1] = target_list[i]
            target_list[i] = temp
        else:
            continue
        
    return target_list

#取目录下文件和文件创建时间
def lsdir(dir_path):
    files_with_time = []
    for folder in os.listdir(dir_path):
        files_with_time.append([os.path.getctime(dir_path + '\\' + folder), dir_path + "\\" + folder])

    return files_with_time
 
#取出最新生成文件给analysis_har
def fetch_har(dir_path):

    files_with_time = lsdir(dir_path)

    #create a list with 2 elements, one is folder name and the other is create time
    cyc_times = len(files_with_time)
    i = 0
    while(i < cyc_times): # a cycle to re-arrange folder
        i = i + 1
        files_with_time = swap(files_with_time)
    print files_with_time[-1][1]

    return files_with_time[-1][1]

    
    
#解析har文件
def analysis_har(har, success_file):

    with codecs.open(har, 'r', 'utf-8') as f:
        har_parser = HarParser(json.loads(f.read()))

    log_write = codecs.open(success_file,'a','utf-8')
            
    log_write.truncate()#清空

    #遍历解析出header
    for page in har_parser.pages:
        for entry in page.entries:
            
            url = entry['request']['url']

            log_write.write('%s  %s\r\n' % (url, entry['time']))



    log_write.close()      

def check_cache(header,output_file):
            
    
    #log = codecs.open(output_file, 'a', 'utf-8')
    #log.truncate()


    for url, args in header.items():
        print "%s -> " % (url)
        
        """
    #判断是否缓存
        if not args.has_key('Last-Modified') and (not args.has_key('Cache-Control') or not args.has_key('ETag')):

            log.write('%s,\t cache:%s,\t url:%s\r\n' %(args['Rctime'], 'no cache', url))

        elif args.has_key('Cache-Control') and args.has_key('Pragma') and args.has_key('Expires'):

            if (('no-store' or 'no-cache') not in args['Cache-Control']) and ('no-cache' not in args['Pragma']) and args['status'] == 200:

              log.write('%s,\t cache:%s,\t url:%s\r\n' %(args['Rctime'], 'cache', url))
              
            else:
              log.write('%s,\t cache:%s,\t url:%s\r\n' %(args['Rctime'], 'no cache', url))
              
        elif (not args.has_key('Cache-Control') or not args.has_key('Pragma')) and args.has_key('Expires'):

            if ((args['Expires'] >= nowtime or args['Expires'] < nowtime) or (str(args['X-Cache'].split(' ', 1)[0].strip()) == 'HIT') and args['status'] == 200):

              log.write('%s,\t cache:%s,\t url:%s\r\n' %(args['Rctime'], 'cache', url))

            else:
              log.write('%s,\t cache:%s,\t url:%s\r\n' %(args['Rctime'], 'no cache', url))

        elif not args.has_key('Cache-Control') and not args.has_key('Pragma') and not args.has_key('Expires'):

            if str(args['X-Cache'].split(' ', 1)[0].strip()) == 'HIT' and args['status'] == 200:
                log.write('%s,\t cache:%s,\t url:%s\r\n' %(args['Rctime'], 'cache', url))
            else:
              log.write('%s,\t cache:%s,\t url:%s\r\n' %(args['Rctime'], 'no cache', url))
        
        """
    #log.close()    

    print 'analysis Done' 
          
 

#按请求消耗时间遍历排序
def result_sort(output_file,sort_file):

    with codecs.open(output_file,'r','utf-8') as f:
        lines = f.readlines(100000)

    aa = {}
    bb = []
    cc = []
    for line in lines[1:]:
        bb.append(line.split('\n'))
        cc.append(line.split(',')[0].strip())

    for i in range(0,len(bb)):
        aa[bb[i][0]] = int(cc[i])

    f.close()
    dd = sorted(aa.items(),key=lambda aa:aa[1],reverse=True) 

    with codecs.open(sort_file,'w','utf-8') as ff:
        for i in range(0,len(dd)):
            ff.write(dd[i][0] + '\n')

    ff.close()
    print 'Sort Done'

#获取参数
def getargs():

        usage = "usage: %prog [options] arg1 [options] arg2 [options] arg3"
        parse = OptionParser(usage=usage, version="%prog 1.0")
        # 定义参数以及说明信息
        
        parse.add_option('-u', '--url',
                         action = 'store', type = "string",
                         dest = 'url', help = 'Please enter the url')
    
        parse.add_option('-o', '--output',
                         action = 'store', type = "string",
                         dest = 'file_path', default = 'output.txt', help = 'Please enter the output file path')
        
        parse.add_option('-s', '--sort',
                         action = 'store', type = "string",
                         dest = 'sort_path', default = 'sort.txt', help = 'Please enter the sort file path')
        opts, args = parse.parse_args()

        if not opts.url or not opts.file_path:
                sys.exit(parse.print_help())
        
        print opts.url, opts.file_path
        openURL(opts.url)
        analysis_har(fetch_har(har_path), opts.file_path)
        #check_cache(headers, opts.file_path)
        #result_sort(opts.file_path, opts.sort_path)

def main():   
    getargs()
    
if __name__ =='__main__':

    main()

