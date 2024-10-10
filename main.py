def fibo(num):
    cach = [0,1]
    if num <= 1: return num
    else :
        x = 1
        while x > num:
            
            x += 1

#main
while True:
    x = int(input("enter number u wanna find fibo ans : "))
    print(fibo(x))
