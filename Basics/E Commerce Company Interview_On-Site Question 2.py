# This is O(n^2), disregard
def imperfect_fact(arr, list_num, output=[]):

    if len(arr) == list_num:
        for i in range(len(arr)):
            output.append(imperfect_fact(arr[:i] + arr[i+1:], list_num, output))
    else:
        product = arr.pop()
        while arr:
            product = product * arr.pop()
        return product

    return output

mylist = [1,2,3,4]
print(imperfect_fact(mylist, len(mylist)))

# Udemy's Solution
def index_prod(lst):
    # Create an empty output list
    output = [None] * len(lst)

    # Set initial product and index for greedy run forward
    product = 1
    i = 0

    while i < len(lst):
        # Set index as cumulative product
        output[i] = product

        # Cumulative product
        product *= lst[i]

        # Move forward
        i += 1

    # Now for our Greedy run Backwards
    product = 1

    # Start index at last (taking into account index 0)
    i = len(lst) - 1

    # Until the beginning of the list
    while i >= 0:
        # Same operations as before, just backwards
        output[i] *= product
        product *= lst[i]
        i -= 1

    return output

print(index_prod(mylist))