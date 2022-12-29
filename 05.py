# Function for Insertion Sort of elements
def insertionSort(marks):
    if (n := len(marks)) <= 1:
        return

    for i in range(1, n):

        key = marks[i]

        # Move elements of arr[0..i-1], that are

        # greater than key, to one position ahead

        # of their current position

        j = i - 1

        while j >= 0 and key < marks[j]:
            marks[j + 1] = marks[j]

            j -= 1

        marks[j + 1] = key
    for i in range(len(marks)):
        print(marks[i])


# Shell sort in python


def shellSort(marks, n):
    # Rearrange elements at each n/2, n/4, n/8, ... intervals
    interval = n // 2
    while interval > 0:
        for i in range(interval, n):
            temp = marks[i]
            j = i
            while j >= interval and marks[j - interval] > temp:
                marks[j] = marks[j - interval]
                j -= interval

            marks[j] = temp
        interval //= 2
    for i in range(len(marks)):
        print(marks[i])


# <--------------------------------------------------------------------------------------->

# Function for displaying top five marks

def top_five_marks(marks):
    print("Top", len(marks), "Marks are : ")
    print(*marks[::-1], sep="\n")


# <---------------------------------------------------------------------------------------->

# Main

marks = []
n = int(input("Enter  of students whose marks are to be displayed : "))
print("Enter marks for", n, "students (Press ENTER after every students marks): ")
for i in range(0, n):
    ele = int(input())
    marks.append(ele)  # adding the element

print("The marks of", n, "students are : ")
print(marks)

flag = 1;
while flag == 1:
    print("\n---------------MENU---------------")
    print("1.insertion Sort of the marks")
    print("2. Shell Sort of the marks")
    print("3. Exit")
    ch = int(input("\n\nEnter your choice (from 1 to 3) : "))

    if ch == 1:
        insertionSort(marks)
        a = input("\nDo you want to display top marks from the list (yes/no) : ")
        if a == 'yes':
            top_five_marks(marks)
        else:
            print("\nThanks for using this program!")
            flag = 0

    elif ch == 2:
        shellSort(marks, n)
        a = input("\nDo you want to display top five marks from the list (yes/no) : ")
        if a == 'yes':
            top_five_marks(marks)
        else:
            print("\nThanks for using this program!")
            flag = 0

    elif ch == 3:
        print("\nThanks for using this program!!")
        flag = 0

    else:
        print("\nEnter a valid choice!!")
        print("\nThanks for using this program!!")
        flag = 0
