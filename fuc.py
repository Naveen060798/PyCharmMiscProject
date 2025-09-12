def divisible(n):
    if n%3==0 and n%5==0:
        print("Pk")
    elif n%5==0:
        print("Kariya")
    elif n%3==0:
        print("Mukesh")
    else:
        print(n)

n = int(input("Enter a number: "))
divisible(n)
