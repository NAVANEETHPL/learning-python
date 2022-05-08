name = input("what is your name?\n")


if name == "ben" or name == "patrecia" or name == "loki" :
  evil_status = input("are you evil?\n")
  evil_num = int(input("how many good things have you did today\n"))
  
  if evil_status == "yes" and evil_num == "< 4":
   print("you're not welcome here evil " + name 
         + "!!. get out ")
   exit()
  else:
    print("so you're one of the good " + name + " come in.") 
else:    
 print("hello " + name + ", thank you for coming,have a geat day.\n")
   
menu = "\n black coffee  \n espresso  \n latte  \n cappucino\n frappuccino \n"

order = input("what would you like from our menu today? Here is what we serving." + menu )



quantity = input("how many " + order +  "s would you like?\n")


price = 8

if order == "frappuccino":
 price = 13

if order == "black coffee":
 price = 3



if order == "latte":
 price = 9



if order == "cappuccino":
 price = 4

total = price * int(quantity)

print("Thank you. Your total is:$ " + str(total))
print("Sounds good " + name +",We will have your " + quantity + " " + order + " in a moment.")


