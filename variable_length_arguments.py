# variable length arguments (non keyword)
"""
def order_food(min_order, *args):
    print(f"you have ordered: {min_order}")
    for item in args:
        print(f"(you have ordered: {item}")

    print("your food will be delivered in 30 mins:")


order_food("salad", "pizza", "Biryani")

"""
import random
def time_activity(*args,**kwargs):
    print(args)
    print(kwargs)
    min = sum(args) + random.randint(0, 60)
    print(min)
    choice = random.choice(list(kwargs.keys()))
    print(choice)
    print("you have to spend {min} in {kwargs[choice]} ")
time_activity(10,20,10, hobby="Gym", sport="boxing", fun="driving")
