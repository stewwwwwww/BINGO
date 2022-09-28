"""
This program simulates a BINGO game
"""

import functions

def main():
    wordList = ['motorcycle', 'police car', 'fire truck', 'ambulance', 'military vehicle', 'bus', 'airport shuttle', 'limousine', 'Hummer', 'Mini-Cooper', 'PT Cruiser', 
    'Austin Healey', 'convertible', 'electric car', 'bicycle', 'cows', 'stop sign', 'camper', 'taxi', 'pizza delivery', 'tow truck', 'dump truck', 'cemetary', 'logging truck', 
    'mattress on roof', 'sailboat', 'hotel', 'willow tree', 'blue van', 'flying pig', 'sports team bumper sticker', 'Canadian flag', 'service center', 'dog in car', 
    'someone stopped by police', 'for sale sign', 'revolving sign', 'birds on a wire', 'field of flowers', 'clothesline', 'traffic cone', 'a shoe on the road', 'Tim Hortons', 
    'baseball game', 'airplane', 'license plate starting with A', 'Quebec license plate', 'US license plate', 'yeild sign', 'construction sign', 'baby on board sign', 
    'church', 'barn', 'hawk', '']
    print(wordList)
    repeat = True
    while repeat:
        playerNum = int(input("How many player are playing? (choose from 1-3): ")) #ask for number of players
        goal = int(input("What goal do you want to choose?(input '1' for Full Card, '2' for Single Line and '3' for Four Corners): ")) #ask for goal
        
        notBingo = True
        while notBingo:
            if goal == 1:                
                if playerNum == 1:
                    player1 = input("What is the name of player 1: ") #ask for name
                    player1Card = functions.createCard(player1, wordList) #create cards
                    
                    functions.printCard(player1, player1Card) #print and format cards
                
                
                
                    roundWordList = wordList
                    wordNotChosen = True
                    while wordNotChosen:
                        randomWord = input("What word do you want to choose?: ") #ask for called word
                        if randomWord in roundWordList:
                            print("The chosen word is:", randomWord)
                            roundWordList.remove(randomWord) #remove the guessed word
                            wordNotChosen = False
                        else:
                            print("The word have been chosen or not in the word list. Please choose again") #inform to retry
                        
                        
                    for i in range(len(player1Card)):
                        if player1Card[i] == randomWord:
                            player1Card[i] = "FOUND" #check guessed word as "FOUND"
                            
                    functions.printCard(player1, player1Card)
                    
                    if functions.fullCardWinning(player1Card):
                        print(player1, "wins")
                        print("GAME START OVER")
                        notBingo = False #start over
                    
                    
                    
                    
                elif playerNum == 2:
                    player1 = input("What is the name of player 1: ")
                    player1Card = functions.createCard(player1, wordList)
                    player2 = input("What is the name of player 2: ")
                    player2Card = functions.createCard(player2, wordList)
                    
                    functions.printCard(player1, player1Card)
                    functions.printCard(player2, player2Card)
                    
                    notBingo = True
                    while notBingo:
                        roundWordList = wordList
                        wordNotChosen = True
                        while wordNotChosen:
                            randomWord = input("What word do you want to choose?: ")
                            if randomWord in roundWordList:
                                print("The chosen word is:", randomWord)
                                roundWordList.remove(randomWord)
                                wordNotChosen = False
                            else:
                                print("The word have been chosen or not in the word list. Please choose again")
                            
                            
                        for i in range(len(player1Card)):
                            if player1Card[i] == randomWord:
                                player1Card[i] = "FOUND"
                        functions.printCard(player1, player1Card)
                        
                        
                        
                        for i in range(len(player2Card)):
                            if player2Card[i] == randomWord:
                                player2Card[i] = "FOUND"
                                
                        functions.printCard(player2, player2Card)
                        
                        if functions.fullCardWinning(player1Card):
                            print(player1, "wins")
                            print("GAME START OVER")
                            notBingo = False
                        if functions.fullCardWinning(player2Card):
                            print(player2, "wins")
                            print("GAME START OVER")
                            notBingo = False
                        
                    
                elif playerNum == 3:
                    player1 = input("What is the name of player 1: ")
                    player1Card = functions.createCard(player1, wordList)
                    player2 = input("What is the name of player 2: ")
                    player2Card = functions.createCard(player2, wordList)
                    player3 = input("What is the name of player 3: ")
                    player3Card = functions.createCard(player3, wordList)
                    
                    functions.printCard(player1, player1Card)
                    functions.printCard(player2, player2Card)
                    functions.printCard(player3, player3Card)
                    
                    notBingo = True
                    while notBingo:
                        roundWordList = wordList
                        wordNotChosen = True
                        while wordNotChosen:
                            randomWord = input("What word do you want to choose?: ")
                            if randomWord in roundWordList:
                                print("The chosen word is:", randomWord)
                                roundWordList.remove(randomWord)
                                wordNotChosen = False
                            else:
                                print("The word have been chosen or not in the word list. Please choose again")
                            
                            
                        for i in range(len(player1Card)):
                            if player1Card[i] == randomWord:
                                player1Card[i] = "FOUND"
                        functions.printCard(player1, player1Card)
                        
                        for i in range(len(player2Card)):
                            if player2Card[i] == randomWord:
                                player2Card[i] = "FOUND"
                        functions.printCard(player2, player2Card)
                        
                        for i in range(len(player3Card)):
                            if player3Card[i] == randomWord:
                                player3Card[i] = "FOUND"
                        functions.printCard(player3, player3Card)
                        
                        if functions.fullCardWinning(player1Card):
                            print(player1, "wins")
                            
                            print(player2, "wins")
                            print("GAME START OVER")
                            notBingo = False
                            
                        if functions.fullCardWinning(player2Card):
                            print(player2, "wins")
                            print("GAME START OVER")
                            notBingo = False
                        if functions.fullCardWinning(player3Card):
                            print(player3, "wins")
                            print("GAME START OVER")
                            notBingo = False
            elif goal == 2:
                if playerNum == 1:
                    player1 = input("What is the name of player 1: ")
                    player1Card = functions.createCard(player1, wordList)
                    
                    functions.printCard(player1, player1Card)
                    
                    notBingo = True
                    while notBingo:
                        roundWordList = wordList
                        wordNotChosen = True
                        while wordNotChosen:
                            randomWord = input("What word do you want to choose?: ")
                            if randomWord in roundWordList:
                                print("The chosen word is:", randomWord)
                                roundWordList.remove(randomWord)
                                wordNotChosen = False
                            else:
                                print("The word have been chosen or not in the word list. Please choose again")
                            
                            
                        for i in range(len(player1Card)):
                            if player1Card[i] == randomWord:
                                player1Card[i] = "FOUND"
                                
                        functions.printCard(player1, player1Card)
                        
                        if functions.singleLineWinning(player1Card):
                            print(player1, "wins")
                            print("GAME START OVER")
                            notBingo = False
                    
                            
                        
                        
                        
                        
                elif playerNum == 2:
                    player1 = input("What is the name of player 1: ")
                    player1Card = functions.createCard(player1, wordList)
                    player2 = input("What is the name of player 2: ")
                    player2Card = functions.createCard(player2, wordList)
                    
                    functions.printCard(player1, player1Card)
                    functions.printCard(player2, player2Card)
                    
                    notBingo = True
                    while notBingo:
                        roundWordList = wordList
                        wordNotChosen = True
                        while wordNotChosen:
                            randomWord = input("What word do you want to choose?: ")
                            if randomWord in roundWordList:
                                print("The chosen word is:", randomWord)
                                roundWordList.remove(randomWord)
                                wordNotChosen = False
                            else:
                                print("The word have been chosen or not in the word list. Please choose again")
                            
                            
                        for i in range(len(player1Card)):
                            if player1Card[i] == randomWord:
                                player1Card[i] = "FOUND"
                        functions.printCard(player1, player1Card)
                        
                        for i in range(len(player2Card)):
                            if player2Card[i] == randomWord:
                                player2Card[i] = "FOUND"
                                
                        functions.printCard(player2, player2Card)
                        
                        if functions.singleLineWinning(player1Card):
                            print(player1, "wins")
                            print("GAME START OVER")
                            notBingo = False
                            
                            
                        if functions.singleLineWinning(player2Card):
                            print(player2, "wins")
                            print("GAME START OVER")
                            notBingo = False
                            
                            
                        
                    
                elif playerNum == 3:
                    player1 = input("What is the name of player 1: ")
                    player1Card = functions.createCard(player1, wordList)
                    player2 = input("What is the name of player 2: ")
                    player2Card = functions.createCard(player2, wordList)
                    player3 = input("What is the name of player 3: ")
                    player3Card = functions.createCard(player3, wordList)
                    
                    functions.printCard(player1, player1Card)
                    functions.printCard(player2, player2Card)
                    functions.printCard(player3, player3Card)
                    
                    notBingo = True
                    while notBingo:
                        roundWordList = wordList
                        wordNotChosen = True
                        while wordNotChosen:
                            randomWord = input("What word do you want to choose?: ")
                            if randomWord in roundWordList:
                                print("The chosen word is:", randomWord)
                                roundWordList.remove(randomWord)
                                wordNotChosen = False
                            else:
                                print("The word have been chosen or not in the word list. Please choose again")
                            
                            
                        for i in range(len(player1Card)):
                            if player1Card[i] == randomWord:
                                player1Card[i] = "FOUND"
                        functions.printCard(player1, player1Card)
                        
                        for i in range(len(player2Card)):
                            if player2Card[i] == randomWord:
                                player2Card[i] = "FOUND"
                        functions.printCard(player2, player2Card)
                        
                        for i in range(len(player3Card)):
                            if player3Card[i] == randomWord:
                                player3Card[i] = "FOUND"
                        functions.printCard(player3, player3Card)
                        
                        if functions.singleLineWinning(player1Card):
                            print(player1, "wins")
                            
                            print("GAME START OVER")
                            notBingo = False
                            
                            
                        if functions.singleLineWinning(player2Card):
                            print(player2, "wins")
                            
                            print("GAME START OVER")
                            notBingo = False
                            
                        if functions.singleLineWinning(player3Card):
                            print(player3, "wins")
                            
                            print("GAME START OVER")
                            notBingo = False
            elif goal == 3:
                if playerNum == 1:
                    player1 = input("What is the name of player 1: ")
                    player1Card = functions.createCard(player1, wordList)
                    
                    functions.printCard(player1, player1Card)
                    
                    notBingo = True
                    while notBingo:
                        roundWordList = wordList
                        wordNotChosen = True
                        while wordNotChosen:
                            randomWord = input("What word do you want to choose?: ")
                            if randomWord in roundWordList:
                                print("The chosen word is:", randomWord)
                                roundWordList.remove(randomWord)
                                wordNotChosen = False
                            else:
                                print("The word have been chosen or not in the word list. Please choose again")
                            
                            
                        for i in range(len(player1Card)):
                            if player1Card[i] == randomWord:
                                player1Card[i] = "FOUND"
                                
                        functions.printCard(player1, player1Card)
                        
                        if functions.fourCornersWinning(player1Card):
                            print(player1, "wins")
                            
                            print("GAME START OVER")
                            notBingo = False
                            
                            
                        
                        
                        
                        
                elif playerNum == 2:
                    player1 = input("What is the name of player 1: ")
                    player1Card = functions.createCard(player1, wordList)
                    player2 = input("What is the name of player 2: ")
                    player2Card = functions.createCard(player2, wordList)
                    
                    functions.printCard(player1, player1Card)
                    functions.printCard(player2, player2Card)
                    
                    notBingo = True
                    while notBingo:
                        roundWordList = wordList
                        wordNotChosen = True
                        while wordNotChosen:
                            randomWord = input("What word do you want to choose?: ")
                            if randomWord in roundWordList:
                                print("The chosen word is:", randomWord)
                                roundWordList.remove(randomWord)
                                wordNotChosen = False
                            else:
                                print("The word have been chosen or not in the word list. Please choose again")
                            
                            
                        for i in range(len(player1Card)):
                            if player1Card[i] == randomWord:
                                player1Card[i] = "FOUND"
                        functions.printCard(player1, player1Card)
                        
                        for i in range(len(player2Card)):
                            if player2Card[i] == randomWord:
                                player2Card[i] = "FOUND"
                                
                        functions.printCard(player2, player2Card)
                        
                        if functions.fourCornersWinning(player1Card):
                            print(player1, "wins")
                            print("GAME START OVER")
                            notBingo = False
                            
                            
                        if functions.fourCornersWinning(player2Card):
                            print(player2, "wins")
                            print("GAME START OVER")
                            notBingo = False
                            
                            
                        
                    
                elif playerNum == 3:
                    player1 = input("What is the name of player 1: ")
                    player1Card = functions.createCard(player1, wordList)
                    player2 = input("What is the name of player 2: ")
                    player2Card = functions.createCard(player2, wordList)
                    player3 = input("What is the name of player 3: ")
                    player3Card = functions.createCard(player3, wordList)
                    
                    functions.printCard(player1, player1Card)
                    functions.printCard(player2, player2Card)
                    functions.printCard(player3, player3Card)
                    
                    notBingo = True
                    while notBingo:
                        roundWordList = wordList
                        wordNotChosen = True
                        while wordNotChosen:
                            randomWord = input("What word do you want to choose?: ")
                            if randomWord in roundWordList:
                                print("The chosen word is:", randomWord)
                                roundWordList.remove(randomWord)
                                wordNotChosen = False
                            else:
                                print("The word have been chosen or not in the word list. Please choose again")
                            
                            
                        for i in range(len(player1Card)):
                            if player1Card[i] == randomWord:
                                player1Card[i] = "FOUND"
                        functions.printCard(player1, player1Card)
                        
                        for i in range(len(player2Card)):
                            if player2Card[i] == randomWord:
                                player2Card[i] = "FOUND"
                        functions.printCard(player2, player2Card)
                        
                        for i in range(len(player3Card)):
                            if player3Card[i] == randomWord:
                                player3Card[i] = "FOUND"
                        functions.printCard(player3, player3Card)
                        
                        if functions.fourCornersWinning(player1Card):
                            print(player1, "wins")
                            print("GAME START OVER")
                            notBingo = False
                            
                            functions.printCard(player1, player1Card)
                            functions.printCard(player2, player2Card)
                            functions.printCard(player3, player3Card)
                            
                        if functions.fourCornersWinning(player2Card):
                            print(player2, "wins")
                            print("GAME START OVER")
                            notBingo = False
                        if functions.fourCornersWinning(player3Card):
                            print(player3, "wins")
                            print("GAME START OVER")
                            notBingo = False
            
            

main()
