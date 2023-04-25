n=int(input("Enter nth fibonacci number to print:"))
def nthfibonumber(n):
    if n<=0:
        return -1
    if n==1:
        return 0
    if n==2:
        return 1
    return nthfibonumber(n-1)+nthfibonumber(n-2)
print(nthfibonumber(n))
