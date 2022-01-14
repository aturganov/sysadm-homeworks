#!/usr/bin/env python3

import datetime as dt
import socket
import time
import json
import yaml


def check_ip(hosts):
    is_ip_static = True
    hosts_matrix = {}
    print(dt.datetime.now().strftime('%Y-%m-%d %H:%M:%S'), 'Старт проверки ip.')
    j_file = open("hosts.json", "w")
    j_file.close()
    y_file = open("hosts.yaml", 'w')

    while is_ip_static:
        for host in hosts:
            ip = socket.gethostbyname(host)
            print(host, ip)
            # json
            if open("hosts.json", "r+").read():
                data = json.load(open("hosts.json"))
                data.update({host: ip})
            else:
                data = {host: ip}
            j_data = json.dumps(data)
            j_file = open("hosts.json", "w")
            j_file.write(j_data)
            j_file.close()
            # yaml
            y_data = yaml.dump([{host: ip}])
            y_file.write(y_data)
            # set current ip dict
            if not hosts_matrix.get(host):
                hosts_matrix.update({host: ip})
            else:
                if hosts_matrix.get(host) != ip:
                    print('[ERROR]: ',  host, ' IP mismatch: ', hosts_matrix.get(host), ' ', ip, '.')
                    y_file.write(json.dumps({host: 'Error: ' + str(ip) + ' -> ' + str(ip)}))
                    data = json.load(open("hosts.json"))
                    data.update({host: 'Error: ' + str(ip) + ' -> ' + str(ip)})
                    j_file = open("hosts.json", "w")
                    j_file.write(json.dumps(data))
                    j_file.close()
                    is_ip_static = False

        print(dt.datetime.now().strftime('%Y-%m-%d %H:%M:%S'), 'IPs checked.')

        time.sleep(2)


# Запуск загрузки
if __name__ == "__main__":
    hosts = ['drive.google.com', 'mail.google.com', 'google.com.']
    check_ip(hosts)