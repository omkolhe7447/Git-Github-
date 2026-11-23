name = input("Enter your name:")

m1 = int(input("Enter Python marks:"))
m2 = int(input("Enter sql marks:"))
m3 = int(input("Enter Excell marks:"))

total = m1 + m2 + m3
percentage = total / 3 * 100

print(f"Student Name: {name} \n Total Marks: {total} \n Percentage: {percentage}")

print("Welcome to Grading System")

if percentage >= 90 and percentage <= 100:
    print("Grade A+")

elif percentage >= 80 and percentage <= 90:
    print("Grade A")

elif percentage >= 70 and percentage <= 80:
    print("Grade B")

elif percentage >= 60 and percentage <= 70:
    print("Grade C")

else:
    print("Grade D")
