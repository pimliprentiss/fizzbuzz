# prints fizz for multiples of 3 and buzz for multiples of 5, fizzbuzz for both.

def fizzbuzz():
    for n in range(1,101):
        if n % 5 == 0 and n % 3 == 0:
            print(f"{n} fizzbuzz")
        if n % 5 == 0:
            print(f"{n} buzz")
        if n % 3 == 0:
            print(f"{n} fizz")
        else:
            print(n)
