import random
from os import listdir

counts = []
currentlyVoting = False
OPTION_COUNT = 4

# This is a temporary set-in - the voteOptions should be decided based on the game
voteOptions = [f for f in listdir("LaptopWebsiteIcons\\Peggle")]
selectedOptions = {}

class VoteClass:
    def __init__(self, name, voteCount):
        self.name = name
        self.voteCount = voteCount

def createVote():
    # We'll expand this to customize the amount of options,
    # but for testing, keep it at 2
    global counts, currentlyVoting, OPTION_COUNT, voteOptions, selectedOptions

    # make my OWN pass-by-value here cause python makes this by reference???
    remainingOptions = []
    for value in voteOptions:
        remainingOptions.append(value)
    selectedOptions = {}

    for voteNumber in range(0, OPTION_COUNT):
        tempSelect = random.randint(0, len(remainingOptions) - 1)
        selectedOptions[voteNumber] = VoteClass(remainingOptions[tempSelect], 0)
        remainingOptions.pop(tempSelect)

    currentlyVoting = True

    for option in selectedOptions:
        print(option)

    return selectedOptions

def takeVote(vote):
    global selectedOptions
    vote = int(vote) - 1
    selectedOptions[vote].voteCount += 1
    print("Vote recorded for " + selectedOptions[vote].name + "!")
    print(f'{selectedOptions[vote].name} now has {selectedOptions[vote].voteCount} votes!')

def finalizeVote():
    global currentlyVoting, counts, selectedOptions

    highestCount = 0
    currentWinner = -1

    for entry in selectedOptions:
        if selectedOptions[entry].voteCount > highestCount:
            highestCount = selectedOptions[entry].voteCount
            currentWinner = selectedOptions[entry].name

    finalVoteCount = highestCount

    # TODO: potentially allow for the user to switch between "no votes is no action" or "no votes is random action"
    if highestCount == 0:
        currentWinner = random.randint(0, len(selectedOptions) - 1)
        finalVoteCount = selectedOptions[currentWinner].voteCount
        currentWinner = selectedOptions[currentWinner].name

    currentlyVoting = False
    return currentWinner, finalVoteCount


