
number_of_students = int(input(("How many students are registering?: ")))

with open('reg_form.txt', 'w+') as f:
    f.write(str(number_of_students) + "\n")

    for i in range(0, number_of_students):
        if i < number_of_students:
            student_id = input('Enter your student ID: ')
            f.write(student_id + "......." + '\n')
           
        




