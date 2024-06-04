def fizz_buzz():
    print("fizzbuzz")

def buzz(i):
    if (i % 5) == 0:
        return True

    return False

if __name__ == '__main__':
    n = int(input())
    for i in range(1, n+1):
        if fizz_buzz(i):
            print("FizzBuzz", end=' ')
        elif fizz(i):
            print("Fizz", end=' ')
        elif buzz(i):
            print("Buzz", end=' ')
        else:
            print(i, end=' ')
