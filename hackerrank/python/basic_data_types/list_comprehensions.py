if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    # Using list comprehension to find all permutations of x,y,z values whose sum is not equal to n
    permutation_list = [[a,b,c] for a in range(x+1) for b in range(y+1) for c in range(z+1) if (a+b+c) != n]
    print(permutation_list)