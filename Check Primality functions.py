### determines prime numbers ###

def user_input():
    return int(input("Give me a number and I will determine its primality: "))
user = user_input()


def total_factors(x):
    # gets factors of user input
    num_list = range(1, user+1)
    factors = [num for num in num_list if user % num == 0]
    print("These are the factors of {}:".format(user), factors)

    # counts number of factors
    for _ in factors:
        x += 1
    return x
total = total_factors(0)


def primality():
    if total == 2:
        print("{} is only divisible by 1 and itself so it is a prime number.".format(user))

    else:
        print("{} is divisible by 1, itself, and {} other numbers, so it is not prime.".format(user, total-2))
primality()
