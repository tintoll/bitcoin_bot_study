import threading

x = 0

def foo():
    global x
    for i in range(1000000):
        x += 1
def bar():
    global x
    for i in range(1000000):
        x -= 1

t0 = threading.Thread(target=foo)
t1 = threading.Thread(target=bar)
t0.start()
t1.start()
t0.join() # 스레드가 끝날때까지 기다린다.
t1.join()
print(x)