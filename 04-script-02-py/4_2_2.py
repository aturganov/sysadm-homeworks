    #!/usr/bin/env python3

    import os
    from pathlib import Path

    # bash_command = ["cd ~/netology/sysadm-homeworks", "git status"]
    # специфика windows машины

    folder_check = str(Path.home()) + "\\Documents\\netology\\sysadm-homeworks"
    bash_command = ["cd " + folder_check, "git status"]

    result_os = os.popen(' && '.join(bash_command)).read()
    is_change = False

    for result in result_os.split('\n'):
        if result.find('modified') != -1:
            prepare_result = result.replace('\tmodified:   ', '')
            # Добавляем полный путь
            print(folder_check + '\\' + prepare_result)
            # Убираем break, чтоб видеть все изменения
            # break