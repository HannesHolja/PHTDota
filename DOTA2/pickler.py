import pickle


def saveplayers(playerlist):
    with open("players.txt","wb") as currentitem:
        pickle.dump(playerlist,currentitem)
def specificdump(playerlist, filename):
    with open(filename,'wb') as currentitem:
        pickle.dump(playerlist,currentitem)
def load():
    playerlist = {}
    try:
        with open("players.txt","rb") as currentitem:
            playerlist = pickle.load(currentitem)
            if playerlist == None:
                return {}
            else:
                return playerlist
    except IOError:
        return {}
    except EOFError:
        return {}
def specificload(currentitem):
    playerlist = {}
    try:
        with open(currentitem,"rb") as currentitem:
            playerlist = pickle.load(currentitem)
            return playerlist
    except IOError:
        return {}
    except EOFError:
        return {}
