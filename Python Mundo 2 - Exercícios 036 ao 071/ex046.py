from time import sleep
delay = 1
n = int(input('Digite um numero: '))
for c in range(n, -1, -1):
    print(c)
    sleep(delay)
print('BUM! BUM! AEE!')