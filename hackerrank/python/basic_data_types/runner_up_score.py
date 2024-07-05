if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    # Converting to set datatype to retain only unique values. Then, it's converted to list datatype to access through indices
    nums = list(set(arr))
    nums.sort()
    # Get second last value of the list (Runner-up score)
    print(nums[-2])