# Author Jack Shields jcs6283@psu.edu

gradepoint1 = input("Enter your course 1 letter grade: ")
credit1 = input("Enter your course 1 credit: ")

if (gradepoint1 == 'A' or gradepoint1 == 'a'):
    print("Grade point for course 1 is: 4.0")
    gradepoint1 = 4.0
elif (gradepoint1 == 'A-' or gradepoint1 == 'a-'):
    print("Grade point for course 1 is: 3.67")
    gradepoint1 = 3.67
elif (gradepoint1 == 'B+' or gradepoint1 == 'b+'):
    print("Grade point for course 1 is: 3.33")
    gradepoint1 = 3.33
elif (gradepoint1 == 'B' or gradepoint1 == 'b'):
    print("Grade point for course 1 is: 3.0")
    gradepoint1 = 3.0
elif (gradepoint1 == 'B-' or gradepoint1 == 'b-'):
    print("Grade point for course 1 is: 2.67")
    gradepoint1 = 2.67
elif (gradepoint1 == 'C+' or gradepoint1 == 'c+'):
    print("Grade point for course 1 is: 2.33")
    gradepoint1 = 2.33
elif (gradepoint1 == 'C' or gradepoint1 == 'c'):
    print("Grade point for course 1 is: 2.0")
    gradepoint1 = 2.0
elif (gradepoint1 == 'D' or gradepoint1 == 'd'):
    print("Grade point for course 1 is: 1.0")
    gradepoint1 = 1.0
else:
    print("Grade point for course 1 is: 0.0")
    gradepoint1 = 0.0

gradepoint2 = input("Enter your course 2 letter grade: ")
credit2 = input("Enter your course 2 credit: ")

if (gradepoint2 == 'A' or gradepoint2 == 'a'):
    print("Grade point for course 2 is: 4.0")
    gradepoint1 = 4.0
elif (gradepoint2 == 'A-' or gradepoint2 == 'a-'):
    print("Grade point for course 2 is: 3.67")
    gradepoint2 = 3.67
elif (gradepoint2 == 'B+' or gradepoint2 == 'b+'):
    print("Grade point for course 2 is: 3.33")
    gradepoint2 = 3.33
elif (gradepoint2 == 'B' or gradepoint2 == 'b'):
    print("Grade point for course 2 is: 3.0")
    gradepoint2 = 3.0
elif (gradepoint2 == 'B-' or gradepoint2 == 'b-'):
    print("Grade point for course 2 is: 2.67")
    gradepoint2 = 2.67
elif (gradepoint2 == 'C+' or gradepoint2 == 'c+'):
    print("Grade point for course 2 is: 2.33")
    gradepoint2 = 2.33
elif (gradepoint2 == 'C' or gradepoint2 == 'c'):
    print("Grade point for course 2 is: 2.0")
    gradepoint2 = 2.0
elif (gradepoint2 == 'D' or gradepoint2 == 'd'):
    print("Grade point for course 2 is: 1.0")
    gradepoint2 = 1.0
else:
    print("Grade point for course 3 is: 0.0")
    gradepoint2 = 0.0

gradepoint3 = input("Enter your course 3 letter grade: ")
credit3 = input("Enter your course 3 credit: ")

if (gradepoint3 == 'A' or gradepoint3 == 'a'):
    print("Grade point for course 3 is: 4.0")
    gradepoint3 = 4.0
elif (gradepoint3 == 'A-' or gradepoint3 == 'a-'):
    print("Grade point for course 3 is: 3.67")
    gradepoint3 = 3.67
elif (gradepoint3 == 'B+' or gradepoint3 == 'b+'):
    print("Grade point for course 3 is: 3.33")
    gradepoint3 = 3.33
elif (gradepoint3 == 'B' or gradepoint3 == 'b'):
    print("Grade point for course 3 is: 3.0")
    gradepoint3 = 3.0
elif (gradepoint3 == 'B-' or gradepoint3 == 'b-'):
    print("Grade point for course 3 is: 2.67")
    gradepoint3 = 2.67
elif (gradepoint3 == 'C+' or gradepoint3 == 'c+'):
    print("Grade point for course 3 is: 2.33")
    gradepoint3 = 2.33
elif (gradepoint3 == 'C' or gradepoint3 == 'c'):
    print("Grade point for course 3 is: 2.0")
    gradepoint3 = 2.0
elif (gradepoint3 == 'D' or gradepoint3 == 'd'):
    print("Grade point for course 3 is: 1.0")
    gradepoint3 = 1.0
else:
    print("Grade point for course 3 is: 0.0")
    gradepoint3 = 0.0

credit1 = float(credit1)
credit2 = float(credit2)
credit3 = float(credit3)

GPA = (gradepoint1 * credit1 + gradepoint2 * credit2 +
       gradepoint3 * credit3) / (credit1 + credit2 + credit3)
print(f"Your GPA is: {GPA}")
