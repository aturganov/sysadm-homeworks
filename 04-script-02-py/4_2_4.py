#!/usr/bin/env python3

import datetime as dt
import socket
import time


def check_ip(hosts):
    is_ip_static = True
    hosts_matrix = {}
    print(dt.datetime.now().strftime('%Y-%m-%d %H:%M:%S'), 'Старт проверки ip.')

    while is_ip_static:
        for host in hosts:
            ip = socket.gethostbyname(host)
            print(host, ip)

            # set current ip dict
            if not hosts_matrix.get(host):
                hosts_matrix.update({host: ip})
            else:
                if hosts_matrix.get(host) != ip:
                    print('[ERROR]: ',  host, ' IP mismatch: ', hosts_matrix.get(host), ' ', ip, '.')
                    is_ip_static = False

        print(dt.datetime.now().strftime('%Y-%m-%d %H:%M:%S'), 'IPs checked.')

        time.sleep(2)


# Запуск загрузки
if __name__ == "__main__":
    hosts = ['drive.google.com', 'mail.google.com', 'google.com.']
    check_ip(hosts)
