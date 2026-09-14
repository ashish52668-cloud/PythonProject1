'''
1 for snake
-1 for water
0 for gun
'''

while True:
  import random


  item_dict = {1:"snake", -1:"water", 0:"gun"}

  user_choice = int(input("enter your move (1,-1,0): "))
  comp_choice = random.choice(list(item_dict.keys()))

  print(f"user_choice = {item_dict[user_choice]}, computer choice = {item_dict[comp_choice]}")

  if user_choice == comp_choice:
      
      print("Both chooses same: Match Tie")

  elif user_choice == 1:
     
     if comp_choice == -1:
         print("snake drinks water, you win")
     else:
         print("Gun kills snake , computer win")

  elif user_choice == -1:  
     
         if comp_choice == 0:
              print("water destroy gun, You win")
         else:
             print("snake drinks water, computer win")

  elif user_choice == 0:
         if comp_choice == 1:
             print("Gun kills snake, Computer win")
         else:
             print("water destry gun, You win")