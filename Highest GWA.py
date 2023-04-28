#Alexza Jean R. Catanoy
#BSCPE 1-4
#Highest GWA

#Title
print("\033[0;36m*" * 90)
print("\033[1;97mA program that read a file conatining the name of 20 students together with their GWA".center(97))
print("\033[0;36m*" * 90)

print("\033[1;32m\nHello! Your programmers name is Alexza Jean.")
print("\033[1;32m\nShe's from BSCPE 1-4")
print("-" * 90)

def student():
        
    #Open Student GWA.txt (read)
    with open("Student GWA.txt", "r") as input_gwa:
        student_data = {}

        #From the first line to the end, read Student GWA.txt
        for line in input_gwa:
            name_surname, gwa = line.strip().split(",")
            gwa = float(gwa)
            student_data[name_surname] = gwa

        #Get the students maximum GWA
        student_highest_gwa = max(student_data, key = student_data.get)
        highest_gwa = student_data[student_highest_gwa]

        #Output, print the students name and surname together with their GWA
        print("\033[0;35mAmong all the 20 students, he/she got the highest GWA: \033[1;37m" + student_highest_gwa)
        print("\033[0;35mHis/Her GWA is: \033[1;37m" + str(highest_gwa))

    student()

            


