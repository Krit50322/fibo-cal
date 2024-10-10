def fibo(n, cach={}):
    if n <= 1 : return(n)
    if len(cach) > n:
        return(cach[n])
    if n in cach:
        return (cach[n])
    cach[n] = fibo(n-1, cach) + fibo(n-2, cach)
    return(cach[n])

#main
while True:
    x = int(input("enter number here : "))
    print(fibo(x,{}))