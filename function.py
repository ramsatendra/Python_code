"""
def add(arg1, arg2):
    total = arg1 + arg2
    return total

out = add(2, 3)
print(out)
print(add(10, 30))
"""

# Default function
def greetings(MSG):
    print (f"Good {MSG}")
    print ("welcome to the function")
greetings("Morning")

def vac_feedback(vac, efficacy):
    print(f"{vac} Vaccine is having {efficacy} % efficacy.")
    if (efficacy > 50) and (efficacy  <= 75):
        print (" not effective")
    elif (efficacy > 75) and (efficacy < 90):
        print (" can be considered")
    else:
        print(" need more trial")

vac_feedback("pfizer", 70)