# -*- coding: utf-8 -*-
# @Time    : 2020-07-05 11:14
# @Author  : chenshiyang
# @Email   : chenshiyang@blued.com
# @File    : Jenkins_qrcode.py
# @Software: PyCharm

import qrcode
import time
import os

#获取最新构建的数据包
class Qr_config():
    def __init__(self):
        self.jenkins_pro_address = '' # jenkins 地址
        self.project_name = '' # 项目名称
        self.apk_home = '' # apk地址
        self.jenkins_space = '' # Jenkins工作空间
        self.today_time = time.strftime("%Y-%m-%d")

    def get_apk_url(self):

        today_dir = "%s\\jobs\\%s\\workspace\\%s\\%s" % (self.jenkins_space,
                                                   self.project_name,
                                                   self.apk_home,
                                                   self.today_time)
        if os.path.exists(today_dir):
            file_list = os.listdir(today_dir)
            file_name = file_list[-1]
            if file_name:
                down_url = "%s/job/%s/ws/%s/%s/%s" % (self.jenkins_pro_address,
                                            self.project_name,
                                            self.apk_home,
                                            self.today_time,
                                            file_name)
                return down_url
            else:
                print ("文件不存在，今日构建失败！")
        else:
            print ("今日不存在构建！")

if __name__ == "__main__":
    link = Qr_config().get_apk_url()
    qr = qrcode.QRCode(version=1,
                       error_correction=qrcode.constants.ERROR_CORRECT_L,
                       box_size=8,
                       border=8,)

    qr.add_data(link)
    qr.make(fit=True)
    img = qr.make_image()
    img.save("android_qr_code.png", '')