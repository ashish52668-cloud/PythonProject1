while True:
  import random


  item_list = ["Rock", "Paper", "Scissor"]

  user_choice = input("enter your move = Rock,paper,Scissor = ")
  comp_choice = random.choice(item_list)

  print(f"user_choice = {user_choice}, computer choice = {comp_choice}")

  if user_choice == comp_choice:
      
      print("Both chooses same: Match Tie")

  elif user_choice == "Rock":
     
     if comp_choice == "Paper":
         print("Paper covers rock , computer win")
     else:
         print("Rock smashes scissor , You win")

  elif user_choice == "Paper":  
     
         if comp_choice == "Scissor":
              print("Scissor cuts paper, Computer win")
         else:
             print("Paper covers rock , You win")

  elif user_choice == "Scissor":
         if comp_choice == "Rock":
             print("Rock smashes paper, Computer win")
         else:
             print("Scissor cuts paper, You win")