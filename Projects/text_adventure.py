# Intro
print("")
print("It's the first day of summer!")
print("Its bright and sunny outside, the sun seeping through your bedroom curtains.")
print("")
print("You have so many things you want to do today, what do you want to start with?")
print("____________________________________________________________________")
print("")

# choice 1
c1 = input("Do you want to [text friends] or [go to the beach]?")
if "text" in c1 or "friends" in c1: 
    print("You sit up in bed and pull out your phone to ask anyone if they want to hangout.")
    print("")
    print("Your friend responds saying they want to!")
    
    # choice 2
    print("Your friend follows up with asking where you want to hang out.")
    print("")
    c2 = input("Do you want to go to a [cafe] the [park] or the [mall]?")
    if "Cafe" in c2 or "cafe" in c2:
        print("")
        print("You could use a pick me up so you picked the cafe.")
        print("Your friend sends a thumbs up confirming your plans.")
        print("")
        print("You get up and get ready to go to the cafe, heading out the door.")
        print("As you enter the cafe, you see your friend waiting for you.")
        print("As you sit down next to them and a waiter comes up to take your orders.")
        
        # choice 5
        c5 = input("Do you want a [latte], a [lemonade] or just [black coffee]?")
        if"latte" in c5:
            print("")
            print("The waiter comes back with a latte and you sip it being careful not to burn your tongue.")
        
        elif"lemonade" in c5:
            print("")
            print("The waiter comes back with the lemomade and you sip it slowly suprised about how sour it is.")
        
        else:
            print("You order just black coffee (WHY. ITS SO BITTER) and the waiter comes back with your cup.")
            print("You sip it trying to keep your face stoic from the intense bitterness from the coffee.")

        # Cafe ending 
        print("")
        print("You and your friend talk for a bit laughing and making plans for later in the summer.")
        print("After about two hours your friend had to go so you paid and left as well.")
        print("As you leave, your phone buzzes and you pull it out to check it.")
        print("")
        print("It's your friend telling you their waiting for you at the cafe.")
        print("________________________________________________________________________________")
        print("CAFE ENDING")

   
    elif "park" in c2: 
        print("")
        print("You could use the fresh air so you pick the park.")
        print("Your friend sends a thumbs up confirming your plans.")

        # choice 6
        print("")
        print("You get up and get ready to go to the park, heading out the door.")
        print("You soon see your friend sitting on a bench and you call their name.")
        print("")
        print("They notice you and smile, standing up and walking over to you.")

   
    else:
        print("")
        print("The mall sounds fun to you so you suggest it to your friend.")
        print("Your friend sends a thumbs up confirming your plans.")



else:
    print("")
    print("You decided today was not the day to see friends. Going to the beach sounds much better.")

    # choice 3 
    print("You get out of bed and get ready to go to the beach.")
    print("Before you go, you pack a small bag with the necessities and head out the door.")
    c3 = input("There are two paths to get to the beach, will you go [left] or [right]?")
    if "left" in c3:
        print("")
        print("You decided to go to the left, it winds through a thicket.")
        print("But soon, you can hear the ocean, and the thicket clears out to the shore.")
    else: 
        print("")
        print("You decided to go to the right, the path leading to the platform above the beach.")
        print("You then make your way down to the shore.")

    # choice 4 
    print("")
    print("There's a bit of a breeze as you step on to the beach.")
    c4 = input("Would you rather [wade] in the water or [sit] on the shore?")
    if "wade" in c4 or "water" in c4:
        print("")
        print("You stepped into the cool water letting it submerge you half way up your shins.")
        print("You walk around in the water, finding shells and small sea life.")
        print("")
        print("You wade for about an hour and a half before stepping out of the water and drying off.") 
      
        # beach ending 1 
        print("")
        print("After you finished drying of, you decided to head home for the day.")
        print("As you head back, you were happy this was how you spent your day.")
        print("____________________________________________________________________")
        print("")
        print("BEACH ENDING 1")

        


    else: 
        print("")
        print("Not wanting to get wet, you sit down on the warm sand.")
        print("You look out on the water")
        print("The ocean shimmers in the sun, and the warm sand makes you tired....")
        print("")
        print("You drift asleep on the beach.")

        # Beach ending 1.5
        print("")
        print("You wake up still on the beach but the sun is almost set.")
        print("You look around orienting yourself, and you suddenly see a humanoid figure in front of you.")
        print("You ask whose there, are surprisingly met with your own voice.")
        print("") 
        print("You shake your head thinking it's still a dream.")
        c7 = input("Do you want to [investigate] or [go home]?")
        if"investigate" in c7:
            print("")
            print("You get up and walk towards the humanoid looking thing.")
            print("Turns out, it was just a pile of rocks.")
            print("....")
            print("But then where did the voice come from?")
            print("____________________________________________")
            print("")
            print("BEACH ENDING 1.5")

        else:
            print("")
            print("You decide your probably just tired from waking up, and leave it at that.")
            print("On your way home you ignore your own voice calling your name.")
            print("___________________________________________________________")
            print("BEACH ENDING 2")
            
         

