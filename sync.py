#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
FTP loc sync
"""
import time
from ftplib import FTP
import os
from loguru import logger


class FTP_OP(object):
    def __init__(self, host, username, password, port):
        """
        初始化ftp
      :param host: ftp主机ip
      :param username: ftp用户名
      :param password: ftp密码
      :param port: ftp端口 （默认21）
      """
        self.host = host
        self.username = username
        self.password = password
        self.port = port

    def ftp_connect(self):
        """
        连接ftp
        :return:
        """
        ftp = FTP()
        ftp.set_debuglevel(0)  # 不开启调试模式
        ftp.encoding = 'gbk'

        ftp.connect(host=self.host, port=self.port)  # 连接ftp
        ftp.login(self.username, self.password)  # 登录ftp
        ftp.set_pasv(False)  ##ftp有主动 被动模式 需要调整
        return ftp

    def download_file(self, ftp_file_path, dst_file_path):
        buffer_size = 102400  # 默认是8192
        ftp = self.ftp_connect()
        ftp.getwelcome()
        # logger.info()
        file_list = ftp.nlst(ftp_file_path)
        for file_name in file_list:
            file_name = file_name.split("/")[-1]
            ftp_file = os.path.join(ftp_file_path, file_name)
            write_file = dst_file_path + file_name
            if '.' not in file_name:
                try:
                    os.makedirs(write_file)
                    logger.info(f"创建文件夹:{write_file}")
                except FileExistsError:
                    logger.info(f"文件夹{write_file}已存在")
                ftp_c = FTP_OP(host=host, username=username, password=password, port=port)
                ftp_c.download_file(ftp_file_path + '/' + file_name, write_file + "/")
            else:
                if not os.path.exists(write_file):
                    logger.info(f"新增文件：{file_name}")
                    try:
                        with open(write_file, "wb") as f:
                            ftp.retrbinary('RETR %s' % ftp_file, f.write, buffer_size)
                    except OSError:
                        logger.warning(f"错误文件：{file_name}")
                    except Exception as e:
                        logger.error(f"严重错误:{e}")
        ftp.quit()

    def whileTrue(self, sepTime):
        logger.info(f"开始循环同步任务")
        count = 0
        while True:
            count += 1
            logger.info(f"times:{count}")
            time.sleep(sepTime)
            ftp = FTP_OP(host=host, username=username, password=password, port=port)
            ftp.download_file(ftp_file_path=ftp_file_path, dst_file_path=dst_file_path)


if __name__ == '__main__':
    host = "192.168.1.201"
    username = ""
    password = ""
    port = 21
    ftp_file_path = "UserUpload"  # FTP目录
    dst_file_path = r"./"  # 本地目录
    this = FTP_OP(host=host, username=username, password=password, port=port)
    this.whileTrue(sepTime=5)
    # ftp.download_file(ftp_file_path=ftp_file_path, dst_file_path=dst_file_path)
