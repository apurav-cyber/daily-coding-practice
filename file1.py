print("collage scholarship programm")
student = input("name of student")
maths = int(input("marks in maths"))
science = int(input("marks in science"))
english = int (input("marks in english"))
print(student,maths,science,english)
total_marks = maths+science+english
print("total marks",total_marks)
percentage = total_marks/3
print("percentage of student",percentage)


if percentage>=90:
    garde = "A+ grade"
    sc ="gold scolarship"
elif percentage>=80:
    garde="A grade"
    sc = "silver scholar ship "
elif percentage>=70:
    grade="B grade"
    sc = "bronze scholarship"
elif percentage>=60:
    grade="C grade"
else:
    print("fail")


if grade=="A+ grade":
    if sc =="gold scolarship":
        print(grade,sc)
elif grade=="A grade":
    if sc=="silver scholar ship ":
        print(grade,sc)
elif grade=="B grade":
    if sc=="bronze scholarship":
         print(grade,sc)
    else:
        print("fail")

    

