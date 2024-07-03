if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    nums = list(set(arr))
    nums.sort()
    print(nums[-2])