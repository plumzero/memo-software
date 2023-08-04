
from tasks import add
from tasks import minus
from tasks import hello

def notifyAdd(a, b):
    result = add.delay(a, b)
    return result

def notifyMinus(a, b):
    result = minus.apply_async(args=[a, b])
    return result
    
def notifyHello(x):
    result = hello.apply_async(args=[x])
    return result
    
if __name__ == '__main__':
    res = notifyAdd(3, 9)
    print('3 + 9 = ', res.get())

    res = notifyMinus(9, 5)
    print('9 - 5 = ', res.get())
    
    para = "world"
    res = notifyHello(para)
    print(res.get())