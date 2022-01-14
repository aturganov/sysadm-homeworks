### Как сдавать задания

Вы уже изучили блок «Системы управления версиями», и начиная с этого занятия все ваши работы будут приниматься ссылками на .md-файлы, размещённые в вашем публичном репозитории.

Скопируйте в свой .md-файл содержимое этого файла; исходники можно посмотреть [здесь](https://raw.githubusercontent.com/netology-code/sysadm-homeworks/devsys10/04-script-03-yaml/README.md). Заполните недостающие части документа решением задач (заменяйте `???`, ОСТАЛЬНОЕ В ШАБЛОНЕ НЕ ТРОГАЙТЕ чтобы не сломать форматирование текста, подсветку синтаксиса и прочее, иначе можно отправиться на доработку) и отправляйте на проверку. Вместо логов можно вставить скриншоты по желани.

# Домашнее задание к занятию "4.3. Языки разметки JSON и YAML"


## Обязательная задача 1
Мы выгрузили JSON, который получили через API запрос к нашему сервису:
```
    { "info" : "Sample JSON output from our service\t",
        "elements" :[
            { "name" : "first",
            "type" : "server",
            "ip" : 7175 
            }
            { "name" : "second",
            "type" : "proxy",
            "ip : 71.78.22.43
            }
        ]
    }
```
  Нужно найти и исправить все ошибки, которые допускает наш сервис
```
Решение:
import json

json_str = '''
    { "info" : "Sample JSON output from our service\t",
        "elements" :[
            { "name" : "first",
            "type" : "server",
            "ip" : 7175 
            },
            { "name" : "second",
            "type" : "proxy",
            "ip" : "71.78.22.43"
            }
        ]
    }
# Check
json_dump = json.dumps(json_str)
print(str(json_dump))
```

## Обязательная задача 2
В прошлый рабочий день мы создавали скрипт, позволяющий опрашивать веб-сервисы и получать их IP. К уже реализованному функционалу нам нужно добавить возможность записи JSON и YAML файлов, описывающих наши сервисы. Формат записи JSON по одному сервису: `{ "имя сервиса" : "его IP"}`. Формат записи YAML по одному сервису: `- имя сервиса: его IP`. Если в момент исполнения скрипта меняется IP у сервиса - он должен так же поменяться в yml и json файле.

### Ваш скрипт:
```python
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
```

### Вывод скрипта при запуске при тестировании:
```
...
drive.google.com 173.194.220.194
mail.google.com 64.233.164.19
google.com. 64.233.164.101
2022-01-14 22:53:09 IPs checked.
drive.google.com 173.194.220.194
mail.google.com 64.233.164.19
google.com. 64.233.164.101
2022-01-14 22:53:11 IPs checked.
drive.google.com 173.194.220.194
mail.google.com 209.85.233.18
[ERROR]:  mail.google.com  IP mismatch:  64.233.164.19   209.85.233.18 .
google.com. 64.233.164.101
2022-01-14 22:53:13 IPs checked.

Process finished with exit code 0

```

### json-файл(ы), который(е) записал ваш скрипт:
```json
{"drive.google.com": "173.194.220.194", "mail.google.com": "Error: 209.85.233.18 -> 209.85.233.18", "google.com.": "64.233.164.101"}
```

### yml-файл(ы), который(е) записал ваш скрипт:
```yaml
...
- mail.google.com: 64.233.164.19
- google.com.: 64.233.164.101
- drive.google.com: 173.194.220.194
- mail.google.com: 64.233.164.19
- google.com.: 64.233.164.101
- drive.google.com: 173.194.220.194
- mail.google.com: 64.233.164.19
- google.com.: 64.233.164.101
- drive.google.com: 173.194.220.194
- mail.google.com: 64.233.164.19
- google.com.: 64.233.164.101
- drive.google.com: 173.194.220.194
- mail.google.com: 64.233.164.19
- google.com.: 64.233.164.101
- drive.google.com: 173.194.220.194
- mail.google.com: 64.233.164.19
- google.com.: 64.233.164.101
- drive.google.com: 173.194.220.194
- mail.google.com: 64.233.164.19
- google.com.: 64.233.164.101
- drive.google.com: 173.194.220.194
- mail.google.com: 64.233.164.19
- google.com.: 64.233.164.101
- drive.google.com: 173.194.220.194
- mail.google.com: 64.233.164.19
- google.com.: 64.233.164.101
- drive.google.com: 173.194.220.194
- mail.google.com: 64.233.164.19
- google.com.: 64.233.164.101
- drive.google.com: 173.194.220.194
- mail.google.com: 64.233.164.19
- google.com.: 64.233.164.101
- drive.google.com: 173.194.220.194
- mail.google.com: 209.85.233.18
{"mail.google.com": "Error: 209.85.233.18 -> 209.85.233.18"}- google.com.: 64.233.164.101

```

## Дополнительное задание (со звездочкой*) - необязательно к выполнению

Так как команды в нашей компании никак не могут прийти к единому мнению о том, какой формат разметки данных использовать: JSON или YAML, нам нужно реализовать парсер из одного формата в другой. Он должен уметь:
   * Принимать на вход имя файла
   * Проверять формат исходного файла. Если файл не json или yml - скрипт должен остановить свою работу
   * Распознавать какой формат данных в файле. Считается, что файлы *.json и *.yml могут быть перепутаны
   * Перекодировать данные из исходного формата во второй доступный (из JSON в YAML, из YAML в JSON)
   * При обнаружении ошибки в исходном файле - указать в стандартном выводе строку с ошибкой синтаксиса и её номер
   * Полученный файл должен иметь имя исходного файла, разница в наименовании обеспечивается разницей расширения файлов

### Ваш скрипт:
```python
???
```

### Пример работы скрипта:
???
