import os

## Number of days you want to make commits
for i in range(1,130):
    d = str(i) + ' day ago'
    ## Open a text file and modify it
    with open('file.txt', 'a') as file:
        file.write(d)
    ## Add bot.txt to staging area
    os.system('git add file.txt')
    ## Commit it
    os.system('git commit --date="' + d + '" -m "first commit"')

import subprocess

# Comando git push
command = ['git', 'push', '-u', 'origin', 'main']

# Ejecutar el comando
result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

# Verificar el resultado
if result.returncode == 0:
    print("Push exitoso")
else:
    print("Error en el push:", result.stderr.decode('utf-8'))
