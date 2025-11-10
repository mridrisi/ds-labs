# Selection Sort to sort an array
def selection(n, A):
    for i in range(n - 1):                     
        min_index = i                         
        for j in range(i + 1, n):              
            if A[j] < A[min_index]:          
                min_index = j
        if min_index != i:                   
            A[i], A[min_index] = A[min_index], A[i]  

    print("Sorted array:", A)                


def main():
    Array = [20, 40, 10, 90, 50, 89, 7, 34, 30, 70]
    length = len(Array)
    selection(length, Array)            


main()                                         
