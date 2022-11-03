#Shadman Hossain 
#Oct.26, 2019
#User will make a decision about submitting an email to the company and getting a response, or find out about cost savings for the company

#Ask user what choice of action will they take
menu = input("A. Send an Email to Company Support\nB. Calculate Savings from Automating Replies\n\nSelect which option (A or B) you wish to execute: ")
menu_choice_saved = menu

print()

#Direct user to the desired action
if menu_choice_saved == "A" or menu_choice_saved == "a":
  import parta
  
elif menu_choice_saved == "B" or menu_choice_saved == "b":
  import partb