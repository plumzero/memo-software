    
from tasks import hello

def on_raw_message(body):
    print(body)

if __name__ == '__main__':
    r = hello.delay(30, 42)
    print(r.get(on_message=on_raw_message, propagate=False))
