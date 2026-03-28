# student grading system
while True:
    grade = float(input("Enter your grade: "))
    if grade >= 3.6 and grade <= 4.0:
        print("A")
    elif grade >= 3.4 and grade < 3.6:
        print("A-")
    elif grade >= 3.2 and grade < 3.4:
        print("B")
    else:
        print("C")

# sum of array by passing array parameter to function
def sumfun(arr):
    sum = 0
    for i in arr:
        sum += i
    return sum
arr = {2,3,4,1}
print("the sum of array is", sumfun(arr))
