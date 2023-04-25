n=int(input("Enter sum of sequence to be printed:"))
def f(n):
    a=0
    b=1
    d=a+b
    if n<2:
        print("invaid")
    else:
        for i in range(n-2):
            c=a+b
            a=b
            b=c
            d=d+c
    print(d)
f(n)