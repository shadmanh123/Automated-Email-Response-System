#Shadman Hossain 
#Oct.5, 2019
#User will enter required information and choose a subject line and depending on the subject line, program will provide an automated response

#Ask user for email
def get_user_email():
  user_email = input("Enter your Email: ")
  return(user_email)
user_email_saved = get_user_email() #Save user email information

#Ask user for message subject
def get_message_subject():
  message_subject = input("Enter your Message Subject: ")
  return(message_subject)
message_subject_saved = get_message_subject() #Save message subject information

#Ask user for message body
def get_message_body():
  message_body = input("Enter your Message Body: ")
  return(message_body)
message_body_saved = get_message_body() #Save message body information

#Check which message subject corresponds to message subject input by user
message_subject_1 = "Problem Saving File"

message_subject_2 = "I Lost My License"

message_subject_3 = "Where is My Program Installed?" 

message_subject_4 = "How Do I Open My Program?"

message_subject_5 = "How Do I Open My File In Microsoft Word?"

message_subject_6 = "Do You Offer Refunds?"

if message_subject_saved == "Problem Saving File" or message_subject_saved == "1" or message_subject_saved.lower() == message_subject_1.lower():
  message_subject_one = "    Thank you for contacting our company. Saving a file is done by pressing CTRL-S (Windows) or CMD-S (Mac)."
  message_subject_saved = message_subject_one

elif message_subject_saved == "I Lost My License" or message_subject_saved == "2" or message_subject_saved.lower() == message_subject_2.lower():
  message_subject_two = "    Thank you for contacting our company. You will be contacted via email to verify your license request."
  message_subject_saved = message_subject_two

elif message_subject_saved == "Where is My Program Installed?" or message_subject_saved == "3" or message_subject_saved == "How Do I Open My Program?" or message_subject_saved == "4" or message_subject_saved.lower() == message_subject_3.lower() or message_subject_saved.lower() == message_subject_4.lower() :
  message_subject_three_or_four = "    Thank you for contacting our company. The application is located in the folder: \n                     My Computer > Program Files \n                   Double click on the application to launch and run it."
  message_subject_saved = message_subject_three_or_four

elif message_subject_saved == "How Do I Open My File In Microsoft Word?" or message_subject_saved == "5" or message_subject_saved.lower() == message_subject_5.lower():
  message_subject_five = "    Thank you for contacting our company. First export the file in .doc format in our application. Then open the .doc file in Microsoft Word."
  message_subject_saved = message_subject_five

elif message_subject_saved == "Do You Offer Refunds?" or message_subject_saved == "6" or message_subject_saved.lower() == message_subject_6.lower():
  message_subject_six = "    Thank you for contacting our company. Sorry, we do not offer refunds."
  message_subject_saved = message_subject_six

#Look for key phrases in message body to determine response if no message subject is given

key_phrases1 = ["can't save file","saving","save"]

key_phrases2 = ["license", "lost license"]

key_phrases3_or_4 = ["can’t find my program","cannot find my program","can’t find the program","where is the program","can’t open my program","cannot open my program","can't open the program"]

key_phrases5 = ["open in word","open in ms word"]

key_phrases6 = ["refund","have a refund","get a refund","want a refund", "REFUND"]

if message_subject_saved == "":
  for phrases in key_phrases1:
    if phrases in message_body_saved:
      message_subject_one = "    Thank you for contacting our company. Saving a file ic)."
      message_subject_saved = message_subject_one

  for phrases in key_phrases2:
    if phrases in message_body_saved:
      message_subject_two = "    Thank you for contacting our company. You will be contacted via email to verify your license request."
      message_subject_saved = message_subject_two

  for phrases in key_phrases3_or_4:
    if phrases in message_body_saved:
      message_subject_three_or_four = "    Thank you for contacting our company. The application is located in the folder: \n                     My Computer > Program Files \n                   Double click on the application to launch and run it."
      message_subject_saved = message_subject_three_or_four
    

  for phrases in key_phrases5:
    if phrases in message_body_saved:
      message_subject_five = "    Thank you for contacting our company. First export the file in .doc format in our application. Then open the .doc file in Microsoft Word."
      message_subject_saved = message_subject_five

  for phrases in key_phrases6:
    if phrases in message_body_saved:
      message_subject_six = "    Thank you for contacting our company. Sorry, we do not offer refunds."
      message_subject_saved = message_subject_six


#print blank line
print()

#Greet user
print("Dear", user_email_saved+",")

#Display automated message appropriate to Subject line
print(message_subject_saved)

#Thank user
print("Thank you,")

#Display company name
print("Company Customer Service")

#End response
