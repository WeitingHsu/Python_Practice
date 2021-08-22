
'''
amount = input("How long should be fibonacci?")
# minus one is due to python index starting from 0
endpoint = int(amount)-1

fibonacci = [0,1]
for i in range(1,endpoint,1):
    fibonacci.append(fibonacci[i]+fibonacci[i-1])
print(fibonacci)

'''

def fibonnacci(n):
    a = 0
    b = 1

    if n == 1:
        print(a)
    else:
        print(a)
        print(b)
        for i in range(2,n):
            c = a+b
            a = b
            b = c
            print(c)

def fibonaccilessthan(n):
    a = 0
    b = 1

    if n == 0:
        print("Every element in fibonacci sequence should be larger than 0")
    elif n==1:
        print(0)
    else:
        while True:
            c = a+b
            a = b
            b = c
            if (c>=n):
                print(a)
                break


def factorial(n):
    c = 1
    for i in range(1,n+1):
        c = i*c
    print(c)
            
       


fibonnacci(5)

fibonaccilessthan(3)

factorial(6)