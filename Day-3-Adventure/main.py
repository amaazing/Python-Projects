'''
Author: Maaz Ali
Day 3 - Adventure Game
Description: An adventure game.
'''
print("You wake up after a disaster, seemingly washed up on an island.")
print("To your left, far in the distance there seems to be smoke. To your right, you see some footprints leading into a forest.")
direction = input("Which way do you want to go? (L or R): ")
if direction == "L":
    print("You decided to follow the smoke. After walking for around 30 minutes, you hear a growl. Your stomach... you need food.")
    print("You look around and find some trees growing bananas. It looks like quite a climb; but you're sure you could reach it if you tried.")
    choice = input("Do you choose to climb the tree and obtain nourishment? Or do you want to continue on your journey hoping for sustenance at the end? (Y or N to climb tree): ")
    if choice == "Y":
        print("You choose to climb the tree.")
        print("While climbing up it, you realize that it's taller than it appeared...")
        choice = input("It might be dangerous to climb even further. You can choose to jump back down(N), stay and wait(W), or just continue climbing(Y)")
        if choice == "Y":
            print("Stubbornly you choose to continue.")
            print("Right as soon as you reach the top, and try to grab the banana; your other hand's grip loosens.")
            print('As you fall... you think to yourself "this really was a bad idea".')
            print("Game Over.")
        elif choice == "N":
            print("You decide the climb is not worth it and jump back down.")
            print("The leap was longer than you expected, but you land fine.")
            print("You walk for several minutes before you feel your legs lose strength. They're bleeding...")
            print("Everything starts to fade")
            print("Game Over.")
        else:
            print("You wait and wait.")
            print("Thanks to enormous luck a banana seems to fall down. You carefully climb down and eat the banana.")
            print("You continue your journey to the smoke where you find others. They've already managed to get help.")
            print("You left the island, safe and well.")
            print("You win.")
    else:
        print("You decide to continue your journey. Better to get to the destination quicker.")
        print("However, your speed starts slowing; you feel exhausted. You really needed to grab some food.")
        print("You collapse from starvation and close your eyes.")
        print("Game Over.")
else:
    print("You follow the footprints... hoping to find some aid.")
    print("In the distance you see a figure, you shout for any help.")
    print("The figure seems to hear you and they rapidly approach.")
    print("Bad idea! The figure turned out to be a huge monkey; and the screaming seems to have agitated it.")
    print("You decide it's useless to run and accept your fate (monkeys are fast!).")
    print("Game Over.")