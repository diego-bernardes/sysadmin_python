#! C:\python34\python.exe

import subprocess, os

print('Backup de Certificados Digitais')

certificados = subprocess.getoutput('jbstore.exe -l | find "Subject Name:"').replace('Subject Name: ', '')

if not certificados:
    print('Nenhum certificado instalado para este usuário!')
    exit(1)

certificados = certificados.split('\n')
senha = input('Senha: ') 
for certificado in certificados:
        print('Exportando Certificado: ', certificado)
        os.system('jbstore.exe -1 -n "{nome}" -p "{senha}" -o "{saida}.pfx"'
                         .format(nome = certificado, senha = senha, saida = certificado.replace(':', ' ')))
os.system('echo {senha} > senha_mestra.txt'
          .format(senha=senha))
