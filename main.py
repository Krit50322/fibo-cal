def fibo(num):
    cach = [0,1]
    if num == 0 or num == 1: return num
    else :
        ans = fibo(num-1) + fibo(num-2)
        return ans

#main
while True:
    x = int(input("enter number u wanna find fibo ans : "))
    print(fibo(x))
