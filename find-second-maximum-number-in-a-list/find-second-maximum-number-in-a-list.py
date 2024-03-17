if __name__ == '__main__':
    n = int(input())
    arr = set(map(int, input().split()))
    sorted_arr = sorted(list(arr), reverse=True)
    if len(sorted_arr) >= 2:
        print(sorted_arr[1]) 
    