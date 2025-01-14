# /////////// INSTRUCTIONS /////////////////
# 💡 Conditionals 
#  Conditional statements are if, elif, and else statements 

# 1) 💻 Run the file multiples to and type different colors

# 2️) 💻 Under Line 22, add 2 more elif statement to include more color options for this quiz
#            🟨 🟩 🟧 🟪

# 3️) 💻 Test it by running it and inputting different colors each time
# ////////////////////////////////////////////


fav_color = input(f"❓ What is your favorite color? ")
print(f"-"*10)
print()

if fav_color == "red":
  print(f"🟥 You are quick to anger.")

elif fav_color == "blue":
 print(f"🟦 You are calm and collected.")

else:
 print(f"Your color is unknown ;(")
