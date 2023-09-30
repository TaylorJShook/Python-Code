#Name: Taylor Shook
#Course Code: COP2500.0V04
#Date: 1/30/2023
#Assignment Title: Travel Adventure




#Note: I added a while loop to make it easier to test for different endings.

#Story Introduction

cont=1
while(cont == 1):
  print("Once upon a time, in a far away land...")
  print("there was a small mouse named Squeaks")
  print("He was lost in the forest, and he needed to find his way home.")


#First Decision
  print("Pick where should he go")
  print("1 - Deeper into the forest")
  print("2 - The nearby field")

  choice1=int(input("Pick the number of your choice?\n"))

#First If Statement
  if (choice1 == 1):
        print("Squeaks goes deeper into the forest, large trees shading him from the sky.")
        print("He hears a twig snap behind him, and looks around anxiously.")
        print("What should Squeaks do next?")
        print("1 - Continue on foot")
        print("2 - Climb up a tree")

        choice2=int(input("Pick the number of your choice?\n"))
         #second if    
        if (choice2 == 1):
            print("Squeaks continues through the forest on foot, until he hears another noise behind him.")
            print("He worries it might be a cat, or a snake, or a fox, or a hawk! He's heard so many scary stories about them!")
            print("Squeaks needs to make a split-second decision!")
            print("1 - Turn around and face whatever is chasing him!")
            print("2 - Run fast and far until he can't hear the noise anymore!")

            choice3=int(input("Pick the number of your choice quickly!\n"))
            #3rd if
            if (choice3 == 1):
                print("Little Squeaks turns around and holds his ground!")
                print("He shakes with anticipation of his opponent, and is definitely not afraid.")
                print("He flinches at the rustling noises when all of a sudden...")
                print("His brother Buttons appears from the brush!")
                print("Squeaks is mad, what should he do?")
                print("1 - Go with Buttons")
                print("2 - Proclaim he doesn't need help")

                choice4=int(input("Pick the number of your choice?\n"))
                #4th if
                if(choice4 == 1):
                    print("Buttons laughs at young Squeaks, and although Squeaks is mad at his big brother, he is also relieved.")
                    print("Buttons leads Squeaks back to their family's burrow safely.")
                    print("Squeaks found his way home! Yay!")
                    print("The End.")
                    #End 1
                elif(choice4 == 2):
                    print("Squeaks refuses to go with Buttons, and Buttons reluctantly leaves him be.")
                    print("Squeaks is sure he doesn't need any help, so he continues on in the opposite direction.")
                    print("Squeaks is too far from home now.")
                    print("Squeaks didn't make it home.")
                    print("The End.")
                    #End 2
                else:
                    print("Not an option!")

                
                
            elif (choice3 == 2):
                print("Little Squeaks runs for his life, scampering through the woods.")
                print("He trips and falls over a big, thick vine.")
                print("He's never seen a vine with big, yellow eyes before. How weird!")
                print("What should squeaks do?")
                print("1- Stare at the Weird Vine for like, a really long time.")
                print("2 - Run Away! It's too weird to be good!")

                choice5=int(input("Pick the number of your choice?\n"))

                if(choice5 == 1):
                    print("Squeaks stares at the green vine and is very still for such a long time that the vine slithers away.")
                    print("Squeaks hears his mother call to him. Supper is ready.")
                    print("Squeaks found his way home! Yay!")
                    print("The End.")
                    #End 3

                elif(choice5 == 2):
                    print("Squeaks turns around and runs suddenly, but the vine was faster.")
                    print("Apparently it had teeth too!")
                    print("Squeaks didn't make it home.")
                    print("The End.")
                    #End 4
                else:
                    print("Not an option!")
            else:
                print("Not an option!")
                    
    
                
        elif (choice2 == 2):
            print("Squeaks climbs up a tree, and carefully hops from branch to branch.")
            print("On his journey, he finds an acorn! He snatches it up and keeps it for later.")
            print("Mice love acorns, google it.")
            print("Squeaks thinks it should be safe to climb back down now, but there might be more acorns if he continues on the tree branches.")
            print("What should he do?")
            print("1 - Climb back down with his acorn.")
            print("2 - Continue in the trees and search for more!")

            choice6=int(input("Pick the number of your choice?\n"))

            if(choice6 == 1):
                print("Squeaks climbs back down the tree, with his acorn.")
                print("He will never know how many acorns he could have found.")
                print("The little mouse continues through the woods, it is getting dark.")
                print("This place looks familiar...")
                print("He is right next to his family's burrow!")
                print("Squeaks returns home with an acorn for his family.")
                print("His parents are proud.")
                print("Squeaks found his way home! Yay!")
                print("The End.")
                #End 5
                
            elif(choice6 == 2):
                print("Squeaks continues along the tree branches, eager to find more acorns.")
                print("Just a bit ahead, there is a big pile of acorns.")
                print("He hops to the pile of acorns, excited and hungry!")
                print("The only problem is, he isn't the only one.")
                print("Squeaks hears a jingle and a meow.")
                print("Squeaks didn't make it home.")
                print("The End.")
                #End 6
            else:
                print("Not an option!")
        else:
            print("Not an option!")
            
                
                  
  elif (choice1 == 2):
        print("Squeaks turns around and scampers toward the open field nearby.")
        print("There is a pretty flower that Squeaks wants to sniff.")
        print("Should Squeaks stop to smell the flowers?")
        print("1 - Stop and sniff the pretty flower.")
        print("2 - Keep walking without smelling the flower.")

        choice7=int(input("Pick the number of your choice?\n"))

        if(choice7 == 1):
            print("Squeaks hops over to the pretty flower, admiring its beauty.")
            print("It is a bright white flower with thin petals and a yellow center.")
            print("He comes closer to sniff it, and smiles at the delight.")
            print("Squeaks must now move on, but to where?")
            print("1 - Continue along the tree-line of the field.")
            print("2 - Continue through the open field.")

            choice8=int(input("Pick the number of your choice?\n"))

            if(choice8 == 1):
                print("Squeaks decided to walk along the tree-line of the field.")
                print("He's sure he came this way before.")
                print("Squeaks finds a trail of mouse droppings, they must lead the way!")
                print("What should Squeaks do?")
                print("1- Follow the mouse-droppings!")
                print("2- Don't follow the droppings, they stink.")

                choice10=int(input("Pick the number of your choice?\n"))

                if(choice10 == 1):
                    print("Squeaks decides to follow the mouse dropping trail.")
                    print("It leads him back into the woods, further and further.")
                    print("He finds a burrow, but it's not his home.")
                    print("Squeaks decides its good enough and goes inside.")
                    print("He looks around, thinking to himself how much bigger this burrow was.")
                    print("His family could move here and have much more room.")
                    print("Alas, this home was not for the taking.")
                    print("A fluffy red fox returned home to a treat.")
                    print("At least Squeaks stopped to smell the flower.")
                    print("Squeaks didn't make it home.")
                    print("The End.")
                    #End 7

                elif(choice10 == 2):
                    print("Squeaks decides that the mouse droppings are too stinky to follow, to he continues without taking heed of them.")
                    print("After a while, he sees his family in the distance.")
                    print("He hurries to the burrow and makes it home safely.")
                    print("Squeaks tells his mom all about the pretty flower he smelt.")
                    print("Squeaks found his way home! Yay!")
                    print("The End")
                    #End 8
                    

                else:
                    print("Not an option!")

            elif(choice8 == 2):
                print("Squeaks decided to walk through the open field.")
                print("After a little while of walking, he can clearly see his family in the distance.")
                print("He hurries to the burrow and is happy to be home safe.")
                print("Squeaks tells his mom all about the pretty flower he smelt.")
                print("Squeaks found his way home! Yay!")
                print("The End")
                #End 9

            else:
                print("Not an option!")
                
        elif(choice7 == 2):
            print("Squeaks decides he doesn't have time to smell pretty flowers today.")
            print("(Little does he know, he will come to regret this decision forever)")
            print("He continues on through the field, but he needs to make a decision,")
            print("Should he...")
            print("1 - Hop on one foot all the way home.")
            print("2 - Walk normally all the way home.")

            choice9=int(input("Pick the number of your choice?\n"))

            if(choice9 == 1):
                print("Squeaks decided to hop on one foot all the way home.")
                print("He happily hops through the open field.")
                print("Squeaks hears a weird noise, almost like a shriek.")
                print("He hops once more as he looks up to see a large Hawk swooping down.")
                print("If only he stopped to smell the flower...")
                print("Squeaks didn't make it home.")
                print("The End")
                #End 10

            elif(choice9 == 2):
                print("Squeaks decided to walk normally all the way home.")
                print("Soon he sees his family in the distance.")
                print("He hurries to the burrow and happy to be home safe.")
                print("Squeaks found his way home! Yay!")
                print("The End.")
                #End 11

            else:
                print("Not an option!")

        else:
            print("Not an option!")
  else:
      print("Not an option!")


  print("\n\n")
  print("Do you want to play again?")
  print("1 - Yes!")
  print("2 - No Way")

  cont=int(input("Pick the number of your Choice.\n\n"))
           

        
print("\n\n")
print("Thanks for Playing!")
        
    



