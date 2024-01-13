import random
print("Welcome to my food choice decider! \n")
num_choices = int(input("How many choices do you want? "))
Food_choice_list = []
for i in range(1,num_choices+1):
  food = str(input("Enter choice " + str(i) + ": "))
  Food_choice_list.append(food)
food_choice = random.choice(Food_choice_list)
print(Food_choice_list)
print("Your food choice is " + food_choice)
reroll = input("Do you want to reroll? Types Y for Yes and N for No: ")
while reroll == "Y":
  for i in range(1,num_choices+1):
    food_choice = random.choice(Food_choice_list)
    print("Your food choice is " + food_choice)
    reroll = input("Do you want to reroll? Types Y for Yes and N for No:")

  
