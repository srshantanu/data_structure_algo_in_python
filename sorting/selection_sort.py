def selection_sort(arr):
    for num_of_pass in range(len(arr)-1,0,-1):
        positionOfmax = 0
        for location in range(1,num_of_pass+1):
            if arr[location] > arr[positionOfmax]:
                positionOfmax = location

        temp = arr[num_of_pass]
        arr[num_of_pass] = arr[positionOfmax]
        arr[positionOfmax] = temp

    return arr


if __name__ == "__main__":
    arr = list(map(int,input("").split()))

    print(selection_sort(arr))