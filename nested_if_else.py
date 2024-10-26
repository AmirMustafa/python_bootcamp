gpa = float(input("Please enter student's grade point avg? "))
inst_app = input("Is this student going to be educated in an approved institution? ")

if gpa >= 3.7:
    if inst_app == "yes":
        print('Student qualifies for - low APR loans.')
    else:
        print('Applicant did not qualify - since not accepted approved institution.')
else:
    print('Applicant did not qualify - since not enough grade to qualify.')