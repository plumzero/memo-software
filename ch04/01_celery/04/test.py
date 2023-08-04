    
from tasks import add

if __name__ == '__main__':
    result = add.delay(30, 42)
    print('30 + 42 = ', result.get())
