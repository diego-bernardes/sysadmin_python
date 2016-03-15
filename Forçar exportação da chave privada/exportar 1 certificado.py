#! C:\python34\python.exe

import subprocess, os

def gera_menu():
	n = 1
	menu = {}
	for x in certificados:
		menu[n] = x
		n += 1
	return(menu)

def escolha(menu):
    print('\nCertificados disponíveis')
    for x in menu: print(x, ' - ', menu[x])
    try:
        escolha = int(input('Certificado a ser exportado: '))
        
        return (escolha)
    except:
        print('Escolha inválida')
        menu()
        

print('Backup de Certificados Digitais')

certificados = subprocess.getoutput('jbstore.exe -l | find "Subject Name:"').replace('Subject Name: ', '')

if not certificados:
    print('Nenhum certificado instalado para este usuário!')
    exit(1)

certificados = certificados.split('\n')

menu = gera_menu()
escolha = escolha(menu)
if escolha in menu.keys():
    #os.system('cls')    
    print('Exportando Certificado: ', menu[escolha])
    senha = input('Defina uma senha para este certificado: ')
    os.system('jbstore.exe -1 -n "{nome}" -p "{senha}" -o "{saida}.pfx"'
                         .format(nome = menu[escolha], senha = senha, saida = menu[escolha].replace(':', ' ')))
    os.system('echo {senha} > {certificado}.txt'
              .format(senha = senha, certificado = menu[escolha].replace(':', ' ')))
else:
    print('Escolha inválida !')
    menu()
