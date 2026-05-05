marks = input("Enter your marks: ")
marks = int(marks)

if marks >=90:
    print("A")

elif marks >=75 and marks <90:
    print("B")
elif marks >=50 and marks <75:
    print("C")
elif marks<50:
    print("Fail")
else:
    print("Invalid marks")

if marks >=50:
    print("Pass")
else:
    print("Fail")