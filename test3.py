import threading
from queue import Queue


def process_queue():
    while True:
            for i in range(0,51200000):
                bytearray(51200000) # array de bits
                G = 1024*1024*1024*1024/0.35265462456364534564
                a = 787878788888888888888888888888 *G/(i+0.3235324532543)
                a = (a/0.1365645356)/0.52635463457457347656353622356
                a = (a/0.1365645356)/0.52635463457457347656353622356
                a = (a/0.1365645356)/0.52635463457457347656353622356
                a = (a/0.1365645356)/0.52635463457457347656353622356
                print (str(a)*2)


#definimos la funcion setinterval
def set_interval(func, sec):
    def func_wrapper():
        set_interval(func, sec)
        func()
    t = threading.Timer(sec, func_wrapper)
    t.start()
    return t

if __name__ == "__main__" :
	 set_interval(process_queue, 10)