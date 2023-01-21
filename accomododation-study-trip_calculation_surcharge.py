# General information about the group 
number_students = int(input("How many students are in the travel group? "))
number_teachers = int(input("How many teachers are in the travel group?? "))
length_stay = int(input("For how many nights is accommodation needed? "))

# Höhe der pauschalen Erstattung und Budget
reimbursement_p_student = int(input("What is the amount that students get reimbursed per night? " ))
reimbursement_p_teacher = int(input("What is the amount reimbursed per night for teachers? " ))

total_reimbursement_students = number_students * length_stay * reimbursement_p_student
total_reimbursement_teachers = number_teachers * length_stay * reimbursement_p_teacher

total_reimbursement = total_reimbursement_students + total_reimbursement_teachers

print ()
print ("Total reimbursement for students: " + str(total_reimbursement_students))
print ("Total reimbursement for teachers: " + str(total_reimbursement_teachers))
print ("Total reimbursement: " + str(total_reimbursement))


# Accommodation in the first place (Fes)
print ()
ort_1 = input("What is the first place to stay overnight? ")
length_stay_1 = int(input("How many nights the group stays in " + ort_1 + "? "))

number_single_rooms_1 = int(input("How many single rooms are needed for students? "))
number_double_rooms_1 = int(input("How many double rooms are needed for students? "))
number_triple_rooms_1 = int(input("How many triple rooms are needed for students? "))

prize_single_rooms_1 = int(input("How much does a single room cost in " + ort_1 + "? "))
prize_double_rooms_1 = int(input("How much does a double room cost in " + ort_1 + "? "))
prize_triple_rooms_1 = int(input("How much does a triple room cost in " + ort_1 + "? "))

total_prize_students_1 = length_stay_1 * (number_single_rooms_1 * prize_single_rooms_1 + number_double_rooms_1 * prize_double_rooms_1 + number_triple_rooms_1 * prize_triple_rooms_1)
total_prize_teachers_1 = length_stay_1 * number_teachers * prize_single_rooms_1
total_reimbursement_students_1 = reimbursement_p_student * length_stay_1 * number_students
total_reimbursement_teachers_1 = reimbursement_p_teacher * length_stay_1 * number_teachers

print ()
print ("The accommodation costs for students are as follows: " + str(total_prize_students_1))
print ("Reimbursable costs are: " + str(total_reimbursement_students_1))
print ()
print ("The accommodation costs for teachers are as follows: " + str(total_prize_teachers_1))
print ("Reimbursable costs are: " + str(total_reimbursement_teachers_1))
print ()

# Accommodation in the first place (Meknes)
print ()
ort_2 = input("What is the second place to stay overnight? ")
length_stay_2 = int(input("How many nights the group stays in " + ort_2 + "? "))

number_single_rooms_2 = int(input("How many single rooms are needed for students? "))
number_double_rooms_2 = int(input("How many double rooms are needed for students? "))
number_triple_rooms_2 = int(input("How many triple rooms are needed for students? "))

prize_single_rooms_2 = int(input("How much does a single room cost in " + ort_2 + "? "))
prize_double_rooms_2 = int(input("How much does a double room cost in " + ort_2 + "? "))
prize_triple_rooms_2 = int(input("How much does a triple room cost in " + ort_2 + "? "))

total_prize_students_2 = length_stay_2 * (number_single_rooms_2 * prize_single_rooms_2 + number_double_rooms_2 * prize_double_rooms_2 + number_triple_rooms_2 * prize_triple_rooms_2)
total_prize_teachers_2 = length_stay_2 * number_teachers * prize_single_rooms_2
total_reimbursement_students_2 = reimbursement_p_student * length_stay_2 * number_students
total_reimbursement_teachers_2 = reimbursement_p_teacher * length_stay_2 * number_teachers

print ()
print ("The accommodation costs for students are as follows: " + str(total_prize_students_2))
print ("Reimbursable costs are: " + str(total_reimbursement_students_2))
print ()
print ("The accommodation costs for teachers are as follows: " + str(total_prize_teachers_2))
print ("Reimbursable costs are: " + str(total_reimbursement_teachers_2))
print ()

# Accommodation in the first place (Rabat)
print ()
ort_3 = input("What is the third place to stay overnight? ")
length_stay_3 = int(input("How many nights the group stays in  " + ort_3 + "? "))

number_single_rooms_3 = int(input("How many single rooms are needed for students? "))
number_double_rooms_3 = int(input("How many double rooms are needed for students? "))
number_triple_rooms_3 = int(input("How many triple rooms are needed for students? "))

prize_single_rooms_3 = int(input("How much does a single room cost in " + ort_3 + "? "))
prize_double_rooms_3 = int(input("How much does a double room cost in " + ort_3 + "? "))
prize_triple_rooms_3 = int(input("How much does a triple room cost in " + ort_3 + "? "))

total_prize_students_3 = length_stay_3 * (number_single_rooms_3 * prize_single_rooms_3 + number_double_rooms_3 * prize_double_rooms_3 + number_triple_rooms_3 * prize_triple_rooms_3)
total_prize_teachers_3 = length_stay_3 * number_teachers * prize_single_rooms_3
total_reimbursement_students_3 = reimbursement_p_student * length_stay_3 * number_students
total_reimbursement_teachers_3 = reimbursement_p_teacher * length_stay_3 * number_teachers

print ()
print ("The accommodation costs for students are as follows: " + str(total_prize_students_3))
print ("Reimbursable costs are: " + str(total_reimbursement_students_3))
print ()
print ("The accommodation costs for teachers are as follows: " + str(total_prize_teachers_3))
print ("Reimbursable costs are: " + str(total_reimbursement_teachers_3))
print ()

# Accommodation in the first place (Marrakech)
print ()
ort_4 = input("What is the fourth place to stay overnight? ")
length_stay_4 = int(input("How many nights the group stays in  " + ort_4 + "? "))

number_single_rooms_4 = int(input("How many single rooms are needed for students? "))
number_double_rooms_4 = int(input("How many double rooms are needed for students? "))
number_triple_rooms_4 = int(input("How many triple rooms are needed for students? "))

prize_single_rooms_4 = int(input("How much does a single room cost in " + ort_4 + "? "))
prize_double_rooms_4 = int(input("How much does a double room cost in " + ort_4 + "? "))
prize_triple_rooms_4 = int(input("How much does a triple room cost in " + ort_4 + "? "))

total_prize_students_4 = length_stay_4 * (number_single_rooms_4 * prize_single_rooms_4 + number_double_rooms_4 * prize_double_rooms_4 + number_triple_rooms_4 * prize_triple_rooms_4)
total_prize_teachers_4 = length_stay_4 * number_teachers * prize_single_rooms_4
total_reimbursement_students_4 = reimbursement_p_student * length_stay_4 * number_students
total_reimbursement_teachers_4 = reimbursement_p_teacher * length_stay_4 * number_teachers

print ()
print ("The accommodation costs for students are as follows: " + str(total_prize_students_4))
print ("Reimbursable costs are: " + str(total_reimbursement_students_4))
print ()
print ("The accommodation costs for teachers are as follows: " + str(total_prize_teachers_4))
print ("Reimbursable costs are: " + str(total_reimbursement_teachers_4))
print ()

# Calculation of the surcharge for students
total_prize_students = total_prize_students_1 + total_prize_students_2 + total_prize_students_3 + total_prize_students_4
total_prize_teachers = total_prize_teachers_1 + total_prize_teachers_2 + total_prize_teachers_3 + total_prize_teachers_4
total_prize = total_prize_students + total_prize_teachers

total_surcharge_students = (total_reimbursement_students - total_prize_students)*-1
surcharge_p_student = round(total_surcharge_students / number_students, 2)

print ("The total accommodation costs for all excursion participants are as follows: " + str(total_prize))
print ()
print ("The total accommodation costs for students are: " + str(total_prize_students))
print ("For students, a total amount of " + str(total_reimbursement_students) + " gets reimbursed.")
print ("As a result, students will have to pay a surcharge in the amount of: " + str(surcharge_p_student))
print ()
print ("The total accommodation costs for teachers are: " + str(total_prize_teachers))
print ("For teachers, a maximum amount of " + str(total_reimbursement_teachers) + " gets reimbursed.")
print ()