def bubble_sort(arr):
    for num_of_pass in range(len(arr)-1,0,-1):
        for i in range(num_of_pass):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1]= arr[i+1],arr[i]
                print(arr)

    return arr


def short_bubble_sort(arr):
    exchange = True
    no_of_pass = len(arr)-1

    while exchange and no_of_pass > 0:
        exchange = False
        for i in range(no_of_pass):
            if arr[i] > arr[i+1]:
                exchange = True
                arr[i], arr[i+1]= arr[i+1],arr[i]
                print(arr)

        no_of_pass -=1

    return  arr


if __name__ == "__main__":
    arr = list(map(int,input("").split()))

    print(bubble_sort(arr))

    print(short_bubble_sort(arr))
