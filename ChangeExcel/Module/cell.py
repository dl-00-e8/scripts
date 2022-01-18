#!python3
# -*- coding:utf-8 -*-

import csv
import datetime

except_lists = [

]

class cell_xlsx:
    def __init__(self, descript, ip_lists):
        self.description = descript
        self.input_lists = ip_lists
        self.now = datetime.datetime.now()
        self.now_time = str(self.now.year) + "-" + str(self.now.month) + "-" + str(self.now.day) + "-" + str(self.now.hour) + "��" + str(self.now.minute) + "��"
        self.file_name = self.now_time + "-blacklist.xlsx"
    

    def check(self):
        self.ip_list = []
        for ip in self.input_lists:
            if ip in except_lists:
                continue
            self.ip_list.append(ip)
    

    def write(self):
        self.file = open(self.file_name, 'w', newline = '')
        self.wr = csv.writer(self.file)
        self.wr.writerow(['����� �ּ�', '����� ��Ʈ', '������ �ּ�', '������ ��Ʈ', '��������', '����'])
        for ip in self.ip_list:
            self.wr.writerow(['ANY', 'ANY', ip, 'ANY', 'ANY', self.description])
    

    def save(self):
        self.file_close()
