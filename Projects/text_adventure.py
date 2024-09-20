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
        

   
    elif "park" in c2: 
        print("")
        print("You could use the fresh air so you pick the park.")
        print("Your friend sends a thumbs up confirming your plans.")

        # choice 2.2
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
    print("There's a bit of a breeze as you make your way on the shore.")
    c4 = input("Would you rather [wade] in the water or [sit] on the shore?")
    if "wade" in c4 or "water" in c4:
        print("")
        print("You stepped into the cool water letting it submerge you half way up your shins.")
        print("You walk around in the water for a bit finding shells and small sea life.")
        print("")
        print("You wade for about an hour before stepping out of the water and drying off.")
    else: 
        print("")
        print("Not wanting to get wet, you sit down on the warm sand.")
        print("You look out on the water")