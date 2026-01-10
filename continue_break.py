"""
for i in "devops":
   print(i)
   if i == "o":
       print("found my data")
       break
print(" out of the loop")
"""
# continue
for i in "devops":
   print(i)
   if i == "o":
       print("found my data")
       continue
   print(f"value of i is {i}")
print(" out of the loop")

import random
vaccines = ["Moderna", "Pfizer", "Sputnik", "covaxin"]

random.shuffle(vaccines)
print(vaccines)