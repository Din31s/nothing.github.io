# Function for count of student absent for test
def absentSC(m, n):
    count = 0
    for i in range(n):
        if m[i] == 0:
            count += 1
    return count

# Function for Maximum-------------------------------------------->>
def maxMarks(m, n):
    max = 0
    for i in range(n):
        if max < m[i]:
            max = m[i]
    return max
# Function to calculate largest marks frequency
def largestMFreq(n, m):
    count = 0
    check = maxMarks(m, n)
    for i in range(n):
        if check == m[i]:
            count += 1
    return count
# Function for Minimum------------------------------------------->>>
def minMarks(m, n):
    min = m[0]
    for i in range(n):
        if min > m[i]:
            min = m[i]
    return min
# Function for Average--------------------------------->>>
def averageOfMarks(m, n):
    sumInitialize = 0
    for i in range(n):
        sumInitialize += m[i]
    return (sumInitialize / n)

def showList():
    print("--------------------Select Your Choice From Following list-----------------\n1) Enter 1 for Average\n2) Enter 2 for Maximum\n3) Enter 3 for Minimum\n4)Enter 4 for Largest Marks Frequency\n5)Enter 5 for Count of absent student\n6) Enter 6 to exit")
    return showList()

# main program---->>
loop = True
m = []
n = int(input("Enter No of Student: "))
count = 1
for i in range(n):
    marks = int(input(f"Enter marks for student {count}: "))
    m.append(marks)
    count += 1

print("--------------------Select Your Choice From Following list-----------------\n1) Enter 1 for Average\n2) Enter 2 for Maximum\n3) Enter 3 for Minimum\n4)Enter 4 for Largest Marks Frequency\n5)Enter 5 for Count of absent student\n6) Enter 6 to exit")

while loop:
    choice = input("Enter your choice: ")
    if choice == "1":
        print("Average marks obtained by student is:", averageOfMarks(m, n))
    elif choice == "2":
        print("Maximum marks obtained by student is: ", maxMarks(m, n))
    elif choice == "3":
        print("Minimum marks obtained by student is: ", minMarks(m, n))
    elif choice == "4":
        print(f"{maxMarks(m, n)} is largest marks and its frequency is: ",largestMFreq(n, m))
    elif choice == "5": print( "Number of absent student are: ", absentSC(m, n))
    elif choice == "6":
     loop = False
    else:
        print("You entered wrong choice try again")
