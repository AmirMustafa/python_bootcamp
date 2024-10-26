student_score = float(input("Enter student's score. "))

if student_score >= 90:
    print("A")
else:
    if student_score >= 80:
        print("B")
    else:
        if student_score >= 70:
            print("C")
        else:
            if student_score >= 60:
                print("D")
            else:
                print("F")
        
        