#Shadman Hossain 
#Oct.26, 2019
#User will enter required information and the program will calculate the total number of messages automatically responded to and the associated cost savings.

#Ask for number of messages from each category
print("ENTER NUMBER OF MESSAGES PROCESSED FOR EACH CATEGORY")
Problem_Saving_File = input("Number of Problem Saving File messages:")

I_Lost_My_License = input("Number of I Lost My License messages:")

Where_is_My_Program_Installed = input("Number of Where is My Program Installed? messages:")

How_Do_I_Open_My_Program = input("Number of How Do I Open My Program? messages:")

How_Do_I_Open_My_File_In_Microsoft_Word = input("Number of How Do I Open My File In Microsoft Word? messages:")

Do_You_Offer_Refunds = input("Number of Do You Offer Refunds? messages:")

#Calculate the savings by looking at number of messages for a particular category and the price for a message from that same category
Message_ID_1 = float(Problem_Saving_File) * 1.50
Message_ID_2 = float(I_Lost_My_License) * 3.00
Message_ID_3 = float(Where_is_My_Program_Installed) * 0.20
Message_ID_4 = float(How_Do_I_Open_My_Program) * 1.00
Message_ID_5 = float(How_Do_I_Open_My_File_In_Microsoft_Word) * 2.20
Message_ID_6 = float(Do_You_Offer_Refunds) * 1.25

#Calculate the total number of messages replied to
Total_messages = int(Problem_Saving_File) + int(I_Lost_My_License) + int(Where_is_My_Program_Installed) + int(How_Do_I_Open_My_Program) + int (How_Do_I_Open_My_File_In_Microsoft_Word) + int(Do_You_Offer_Refunds)

#print blank line
print()

#Show total number of messages replied to and the associated cost savings
print(str(Total_messages)+" total messages were automatically replied to.\nThis corresponds to a savings of" ,"$",'{0:.2f}'.format((Message_ID_1)+(Message_ID_2) +(Message_ID_3)+(Message_ID_4)+(Message_ID_5)+(Message_ID_6)))