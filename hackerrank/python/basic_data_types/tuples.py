if __name__ == '__main__':
    n_length = input()
    # Get the input list
    n = str(input())
    # Convert it to list of integers
    nums = [int(x) for x in n.split()]
    # Convert to tuple datatype and print the has value
    t = tuple(nums)
    print(hash(t))