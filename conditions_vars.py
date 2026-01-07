# implement on knowledge on conditions and different datatypes

print("This IT organization has various skill set.")
print("Find out your match.")

print("Enter Capitalised values: ")

Devops = ["Jenkins", "Bash", "Ansible", "Python"]  #list
development = (" NodeJS", "Java", ".net") #tuple
emp1 = {"Name":"Santa", "skill":"Blockchain", "code":1024} #dictionary}
emp2 = {"Name":"Rocky", "skill":"Python", "code":1224} #dictionary}
usr_skill = input("Enter your desired skill: ")
# print(usr_skill)

#Check in the database if its present
if usr_skill in Devops:
    print("f we have {usr_skill} in Devops")
elif usr_skill in development:
    print("f we have {usr_skill} in development")
elif (usr_skill in emp1.values()) or (usr_skill in emp2.values()):
    print("we have contract employees with this skill")
else:
    print("sKill not found")

