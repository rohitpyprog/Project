try:
    num = int(input("Enter a number: "))
    a=[6,3,4,5,5,3,7]
    print(a[num])
except ValueError:
    print("Invalid input")
except IndexError:
    print("Out of range")