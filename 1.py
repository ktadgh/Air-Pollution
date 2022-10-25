def even_sum(n):
    # defining the initial last two fibonacci numbers, and the initial even sum
    fib_1 = 1
    fib_2 = 1
    result = 0

    # checking that the next number isn't greater than n
    while fib_1 + fib_2 <= n:

        # calculating the next number and updating the last two numbers
        new_fib = fib_1 + fib_2
        fib_1 = fib_2
        fib_2 = new_fib

        # adding the even numbers to the result
        if fib_2 % 2 == 0:
            result += fib_2
    return result

