def longest_chain():

    length = 0
    answer = 0

    for i in range(1, 1000000):
        count = 1
        print(i)
        collatz_num = i
        while collatz_num != 1:
            if collatz_num % 2 == 0:
                collatz_num = collatz_num//2
            else:
                collatz_num = 3*collatz_num + 1
            count += 1

        if count > length:
            length = count
            answer = i

    return (answer, length)

x = longest_chain()

print(x)

