print("📝 'Boy' Quiz 💬")

# Check if user enters yes/y or no/n
want_instructions = input("Do you want to read the instructions? ").lower()
  
if want_instructions == "yes" or want_instructions == "y":
    print("You chose yes")
elif want_instructions == "no" or want_instructions == "n":
    print("You chose no")
else:
    print("You did not choose a valid response")

# main routine
want_instructions = yes_no("Do you want to read the instructions? ")
print (f"You chose {want_instructions}.")

# show instructions if yes
if want_instructions == "yes" or want_instructions == "y":
  print('''
  This is a quiz about the movie 'Boy'.
  You will be asked a series of questions about the movie.
  • Answer the questions given by typing in the correct answer.
  • If the answer is correct you will gain a point and the quiz will continue.
  • If the answer is incorrect you will move on without gaining any points.
      ''')
