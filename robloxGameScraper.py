import requests
from bs4 import BeautifulSoup
import random
import matplotlib.pyplot as plt


# 1, goes through links in consecutive order;
# 2, goes through random roblox/games IDs
# both returns url and title and checks if they are a game, not a game, and a "place" game and makes a graph
print("\n1, goes through links in consecutive order\n2, goes through random roblox/games IDs\nboth returns url and title and checks if they are a game, not a game, and a 'place' game and makes a graph")
    


def modeone():
    selectStartingNumber = input("1 - specific starting number\n2 - random starting number\n")
    loops = int(input("Please type in number of loops: "))


    data = {
            'noGame': 0, 
            'game': 0, 
            'place game': 0}

    if selectStartingNumber == "1":
        startingNumber = int(input("Input place id\n"))
        for n in range(loops):
            currentNumber = startingNumber
            # response = requests.get("https://www.roblox.com/games/{}/".format(linkNumber))
            response = requests.get("https://www.roblox.com/games/{}/".format(str(currentNumber+ n )))    
            if response.status_code == 200:
                bs4 = BeautifulSoup(response.text, 'html.parser')
                soup = bs4.find("h1", {"class": "game-name"})
                print("\n" + soup.text + "\n" + "https://www.roblox.com/games/{}/".format(currentNumber+n) + "\n" + str(currentNumber+n))
                if soup.text.split()[-1] == "Place":
                    data['place game'] = data['place game'] + 1
                else:
                    data['game'] = data['game'] + 1
            else:
                data['noGame'] = data['noGame'] + 1
            print(str(n) + " loop done")
    else:
        startingNumber = random.randint(100000000,900000000)
        for n in range(loops):
            currentNumber = startingNumber
            # response = requests.get("https://www.roblox.com/games/{}/".format(linkNumber))
            response = requests.get("https://www.roblox.com/games/{}/".format(str(currentNumber+ n )))    
            if response.status_code == 200:
                bs4 = BeautifulSoup(response.text, 'html.parser')
                soup = bs4.find("h1", {"class": "game-name"})
                print("\n" + soup.text + "\n" + "https://www.roblox.com/games/{}/".format(currentNumber+n) + "\n" + str(currentNumber+n))
                if soup.text.split()[-1] == "Place":
                    data['place game'] = data['place game'] + 1
                else:

                    data['game'] = data['game'] + 1
            else:
                data['noGame'] = data['noGame'] + 1
            print(str(n) + " loop done")
    print(data)

    labels = 'X\'s Place Game', 'Game', 'No Game'
    sizes = [data['place game'], data['game'], data['noGame']]
    plt.pie(sizes, labels=labels, autopct="%1.1f%%")
    plt.show()
   

def modetwo():
    print('this is mode 2 running')
    loops = int(input("Please type in number of loops: "))
    data = {
            'noGame': 0, 
            'game': 0, 
            'place game': 0}

    for n in range(loops):
        startingNumber = 5803957966
        currentNumber = startingNumber
        
        linkNumber = random.randint(100000000,startingNumber)
        response = requests.get("https://www.roblox.com/games/{}/".format(linkNumber))
        # response = requests.get("https://www.roblox.com/games/{}/".format(str(currentNumber+ n )))    

        if response.status_code == 200:
            bs4 = BeautifulSoup(response.text, 'html.parser')
            soup = bs4.find("h1", {"class": "game-name"})
            print("\n" + soup.text + "\n" + "https://www.roblox.com/games/{}/".format(linkNumber) + "\n" + str(linkNumber))
            if soup.text.split()[-1] == "Place":
                data['place game'] = data['place game'] + 1
            else:

                data['game'] = data['game'] + 1
        
        else:
            data['noGame'] = data['noGame'] + 1
        print(str(n) + " loop done")

    print(data)

    labels = 'X\'s Place Game', 'Game', 'No Game'
    sizes = [data['place game'], data['game'], data['noGame']]
    plt.pie(sizes, labels=labels, autopct="%1.1f%%")
    plt.show()

userinput = int(input("choose mode: 1, 2\n"))

match userinput:
    case 1:
        modeone()
    case 2:
        modetwo()