n=int(input("Enter no of sequence to be printed:"))
def f(n):
    a=0
    b=1
    if n<2:
        print("invaid")
    else:
        for i in range(n-2):
            c=a+b
            a=b
            b=c
    print(c)
f(n)