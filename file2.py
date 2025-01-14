# /////////// INSTRUCTIONS /////////////////

# 🦉 This spirit animal quiz is unfinished, finish the code! 

# 1️) 💻 Run the file and play through the quiz 

# 2️)  💻 Under line 36, finish the path for if the user choose ocean  
#           💻  Be sure to keep re-running your code to test your changes!  

# ////////////////////////////////////////////

print("-"*30)
print("    Spirit Animal Quiz     ")
print("-"*30)
print()

q1 = input(f"❓ Would you rather go to the moon or the ocean? (moon/ocean): ")

print()

if q1 == 'moon': 
  q1a = input(f"❓ Would you rather eat 100 dumplings or 100 chicken nuggets? (chicken/nuggets): ")

  print()
  
  if q1a == 'chicken': 
    print(f"🦉 You are an owl - hoot hoot 🦉")

  elif q1a == 'nuggets': 
    print(f"🐺 You are a wolf - aaawooooo 🐺")

  else:
    print(f"...error...")

elif q1 == 'ocean':              
  q1b = input(f"")


else:
  print(f"...error...")