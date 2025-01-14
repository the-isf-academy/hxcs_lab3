# /////////// INSTRUCTIONS /////////////////
# 🎨 Now it's up to you to create your own Choose your Own Adventure! 
#     Finish this story or change it entirely! 

# 💻 Your code should include:
#    - if, elif, or else statements 
#    - multiple endings 

# 🤔 Extension Ideas
#      - can you include randomness into your quiz? 
#      - can you ensure upper case letters are still a correct response?
#      - how could you use a list?

# ////////////////////////////////////////////

print("-"*30)
print("     Choose Your Own Adventure     ")
print("-"*30)
print()

name = input("Enter your name: ") 
print("-"*10)
print()

print(f"Once upon a time {name} walked into CKS at the ISF Academy.")
print(f"As {name} enters the school, they see a giant boar!")

print()
q1 = input("--- ❓ Do you run away or attack? (run away, attack): ")
print()

if q1 == "run away":
    print(f"You ran awaaaaaaaay! All the way to Mcdonald's :)")
    
    print()
    q1a = input("--- ❓ What do you order? (fries, mcgriddle): ")


# 💻 Your code goes below here 
