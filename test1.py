# -*- coding: utf-8 -*-
# @Time    : 2020-09-19 10:25
# @Author  : chenshiyang
# @Email   : chenshiyang@blued.com
# @File    : test1.py
# @Software: PyCharm

import requests
import json


url = "http://106.75.100.161/ticktocks/7316/comments"

payload = {
	"source": "posting",
	"reply_id": "",
	"gmt": "111000010000000",
	"text": "首先是出错了重试大约只需1ms。ping一下大约0.93ms（一次往返）；三次握手也是一次往返（第三次握手不用返回）。根据80/20原理，1ms可以忽略不计；又考虑到长连接的扩展性不如短连接好、修改nginx和tomcat的配置代价很大（所有后台服务都需要修改）；所以这里并没有使用长连接。ping服务器的时间如下图：",
	"is_reply": "0"
}
headers = {
  'Authorization': 'Basic MTUzOTgyNDM6M3dzMTM5czlVd1Y3MmsvcDNhTVc0MHAvc0xCbUoycDFvSTlQSmVPemxDbHN4SmZTQUxEcDVGUmZOVGZHbnVEbTFPdFFHL2RpKzNwVTY5QThqNWlUZ3pBNFV0b05BUndraGZZQ3NNV1Z4Z3hZY3dteEJhNktFVVJXTUoxY0ozZWJma25udis1NUhoQkhaT2Q3V3haSXM2V3N6SzF0eUNyVnNOOWZCT3dPeER5dnIzMjU1U2NZWHd1Q1l4R01adlN6UHprWGN0WVIwTThnWTdjVkxycTFSNlpYWVBUditZaGRNZUNPRkpsRnoybUhtcDVYYlpjVkUzVTJtdndwRHcyell5Y092UGV2bkhTRGRxR1ZlMHdoZFYxRWROVE9iMXprY2FwY3JyVTBYcm95aHVFREtpdmVCVWZjZnhjWEZZUVhoUlFYenZuL3REVHJlM3BTUXZRQStQTERoYW4yQ1ZmTkNycWhiMzBrODIrOW9TYjRTM2VCZ2NSMDlxb0lraGpRVjh5bEtSUmdjb2ZZbFhzNWx4UjJqbS9q',
  'User-Agent': 'Mozilla/5.0 (Linux; U; Android 10; M2006J10C MIUI/V12.0.11.0.QJNCNXM) Android/260307_6.3.7_6532_0801 (Asia/Shanghai) Dalvik/2.1.0 app/1',
  'Content-Type': 'application/json',

}

response = requests.request("POST", url, headers=headers, data = payload)

print(response.text)