# Start
g_points = 0
h_points = 0
s_points = 0 
r_points = 0 

print("")
print("This is a personality test to find out which Harry Potter house you best fit in!")
print("_________________________________________________________")
print("")


# Middle
# question 1
answer = input("You're free to go to Hogsmead! Are you going to, A) Zonko's joke shop, B) The Scrivenshaft's Quill shop, C) Honeydukes, D) the Shrieking shack")
if answer == "A":
	g_points += 1
elif answer == "B":
	r_points += 1
elif answer == "C":
	h_points += 1
elif answer == "D":
    s_points += 1
print("")


# question 2:
answer = input("Its the weekend! What do you want to do? A) Study, B) Pull a prank on a teacher,  C) Hangout with friends, D) Adventure around campus?")
if answer == "A":
	r_points += 1
elif answer == "B":
	s_points += 1
elif answer == "C":
	h_points += 1
elif answer == "D":
    g_points += 1


# question 3:
print("")
print("A kid comes up to them and demands you give them your money. What do you do?")
answer = input("A) Give them your money willingly B) Start yelling at them, C) Walk away, D) Refuse")
if answer == "A":
	h_points += 1
elif answer == "B":
	s_points += 1
elif answer == "C":
	r_points += 1
elif answer == "D":
	g_points += 1


# question 4
print("")
print("You forgot to do your homework! You meet one of your friends on the way to class, do you:")
answer = input("A) Not ask your friend to give you answers, B) Ask them to give you answers but don't make them, C) Threaten them to give you the answers, D) Tell confess to the teacher instead?")
if answer == "A":
	r_points += 1
elif answer == "B":
	h_points += 1
elif answer == "C":
	s_points += 1
elif answer == "D":
	g_points += 1


# question 5 
print("")
print("What's your favorite class?")
answer = input("A) History of Magic, B) Herbology, C) Potions, D) Care of Magical Creatures ")
if answer == "A":
	r_points += 1
elif answer == "B":
	h_points += 1
elif answer == "C":
	s_points += 1
elif answer == "D":
	g_points += 1


# question 6 
print("")
print("Uh-oh.. you got a howler from your parents! What is it for?")
answer = input("A) Stealing from Hogsmead, B) Bullying a student C) Cheating on your OWL's, D) Going into the forbidden forest at night")
if answer == "A":
	s_points += 1
elif answer == "B":
	h_points += 1 
elif answer == "C":
	r_points += 1
elif answer == "D":
	g_points += 1


# question 7 
print("") 
print("It'd desert time after dinner, what are you grabbing for first?")
answer = input("A) Pumpkin pasties  B) Caldron cakes C) Berty Bots Every Flavored Beans, D) Treacle Tart")
if answer == "A":
	h_points += 1
elif answer == "B":
	s_points += 1
elif answer == "C":
	g_points += 1
elif answer == "D": 
	r_points += 1



# Results
print("")
if g_points > s_points and g_points > r_points and g_points > h_points:
	print("Yay! You fit into the Gryffindor house!")
elif s_points > g_points and s_points > r_points and s_points > h_points:
    print("...I guess, you go into Slytherin..Woo..")
elif r_points > g_points and r_points > h_points and r_points > s_points:
	print("You are a Ravenclaw! Welcome fellow nerd")
elif h_points > g_points and h_points > r_points and h_points > s_points:
	print("You belong in the Hufflepuff house! You'll make great friends.")
