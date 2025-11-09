# ds-labs
linear search and binary
def LS(LIST, search):
    for i in range(len(LIST)):
        if LIST[i] == search:
            return i
    return -1


def BS(LIST, search, low, high):
    while low <= high:
        mid = (low + high) // 2
        if LIST[mid] == search:
            return mid
        elif LIST[mid] < search:
            low = mid + 1
        else:
            high = mid - 1
    return -1


# --- Main program ---
size = int(input("Enter the number of customers: "))
LIST = []

for i in range(size):
    id = int(input("Enter the ID: "))
    LIST.append(id)

print("Customer IDs are:", LIST)
search = int(input("Enter the number to be searched: "))

print("\nEnter 1 for Linear Search or 2 for Binary Search")
choice = int(input("Enter your choice: "))

if choice == 1:
    result = LS(LIST, search)
    if result != -1:
        print(f"Number found using Linear Search at position {result}")
    else:
        print("Number not found")

elif choice == 2:
    # Binary Search works only on sorted lists
    LIST.sort()
    print("Sorted Customer IDs for Binary Search:", LIST)
    result = BS(LIST, search, 0, len(LIST) - 1)
    if result != -1:
        print(f"Number found using Binary Search at position {result}")
    else:
        print("Number not found")

else:
    print("Invalid choice!")


output--------
Enter the number of customers: 3
Enter the ID: 1
Enter the ID: 2
Enter the ID: 3
Customer IDs are: [1, 2, 3]
Enter the number to be searched: 2

Enter 1 for Linear Search or 2 for Binary Search
Enter your choice: 1
Number found using Linear Search at position 1




    
