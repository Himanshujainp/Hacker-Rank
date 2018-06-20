if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    arr = list(arr)
    arr1 = []
    for i in arr:
        if(i != max(arr)):
            arr1.append(i)
    print (max(arr1))
