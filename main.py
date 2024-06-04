def fizz_buzz(i):
    if i%15==0:
        return true
    else:
        return false

def fizz(i):
    if i%3==0:
        return true
    else:
        return false

def buzz(i):
    if i%5==0:
        return true
    else:
        return false

if __name__ == '__main__':
    n = int(input())
    for i in 1, n+1:
        if fizz_buzz(i):
            print("FizzBuzz", end=' ')
        elif fizz(i):
            print("Fizz")
        elif buzz(i):
            print("Buzz", end=' ')
        else:
            print(i, end=' ')
    fizz_buzz()