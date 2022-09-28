import random


def createCard(player, wordList):
    """
    this functiuon creates a card of the player
    parameter: player, wordList
    return playerCard
    
    """
    playerCard = []
    
    playerCard = random.sample(wordList, 25)
    return playerCard


def printCard(player, playerCard):
    """
    THis function print card
    parameter: player, playerCard
    return: None
    """
    print(player +"'s card: ") 
    print(playerCard[0], playerCard[1], playerCard[2], playerCard[3], playerCard[4], sep = "\t")
    print(playerCard[5], playerCard[6], playerCard[7], playerCard[8], playerCard[9], sep = "\t")
    print(playerCard[10], playerCard[11], playerCard[12], playerCard[13], playerCard[14], sep = "\t")
    print(playerCard[15], playerCard[16], playerCard[17], playerCard[18], playerCard[19], sep = "\t")
    print(playerCard[20], playerCard[21], playerCard[22], playerCard[23], playerCard[24], sep = "\t")

def fullCardWinning(playerCard):
    """
    This check winning status
    parameter:playerCard
    return: None
    """
    result = all(element == playerCard[0] for element in playerCard)
    return result
def singleLineWinning(playerCard):
    """
    This check winning status
    parameter:playerCard
    return: None
    """
    if (playerCard[0] == playerCard[1] == playerCard[2] == playerCard[3] == playerCard[4] or
        playerCard[5] == playerCard[6] == playerCard[7] == playerCard[8] == playerCard[9] or
        playerCard[10] == playerCard[11] == playerCard[12] == playerCard[13] == playerCard[14] or
        playerCard[15] == playerCard[16] == playerCard[17] == playerCard[18] == playerCard[19] or
        playerCard[20] == playerCard[21] == playerCard[22] == playerCard[23] == playerCard[24] or
        playerCard[0] == playerCard[5] == playerCard[10] == playerCard[15] == playerCard[20] or
        playerCard[1] == playerCard[6] == playerCard[11] == playerCard[16] == playerCard[21] or
        playerCard[2] == playerCard[7] == playerCard[12] == playerCard[17] == playerCard[22] or
        playerCard[3] == playerCard[8] == playerCard[13] == playerCard[18] == playerCard[23] or
        playerCard[4] == playerCard[9] == playerCard[14] == playerCard[19] == playerCard[24] or
        playerCard[0] == playerCard[6] == playerCard[12] == playerCard[18] == playerCard[24] or
        playerCard[4] == playerCard[8] == playerCard[12] == playerCard[16] == playerCard[20]):
        
        return True    
def fourCornersWinning(playerCard):
    """
    This check winning status
    parameter:playerCard
    return: None
    """
    if playerCard[0] == playerCard[4] == playerCard[20] == playerCard[24]:
        
        return True
        