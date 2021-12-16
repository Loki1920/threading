import threading
n = int(input("enter number :"))
def print_1_n(n):
  #main thread
  print(threading.current_thread().getName())
  for i in range(1,n+1):
    print(i)


th1 = threading.Thread(target= print_1_n,args=(n,))

th2 = threading.Thread(target=print_1_n,args=(n,))

th1.start()
th2.start()
th1.join()
th2.join()



    
  