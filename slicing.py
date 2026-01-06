# Getting the slice from your data or subdata from your data
Planet = "Closest to Sun"
print(Planet)

print(Planet[0])
print(Planet[1])

# negative indexing
print(Planet[-1])
print(Planet[-2])
print(Planet[-3])

#slicing a string, getting a substring from a string
print(Planet[1:4])
print(Planet[:7])
print(Planet[11:])

#slicing a tuple
devops = ("Ansible", "Bash scripting", "terraform", "Python")
print(devops[0])
print(devops[1:4])
print(devops[1:4][0])
print(devops[1:4][0][5:11])

# Dictionary example
Skills = {"devops":("AWS", "Jenkins", "Ansible"), "development": ["Java", "NodeJS"]}
print(Skills)
print(Skills["devops"])