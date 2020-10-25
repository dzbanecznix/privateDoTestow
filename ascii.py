from msvcrt import kbhit, getch
from time import sleep
from oauth2client.service_account import ServiceAccountCredentials
import urllib.request, os, traceback, gspread, json

__path__ = os.getcwd()

def OpenGoogleSheet(filename):
    scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]
    creds = ServiceAccountCredentials.from_json_keyfile_name(__path__+"\\test projektu-9f91d648512d.json", scope)
    client = gspread.authorize(creds)
    sheet = client.open(filename).sheet1  # Open the spreadhseet  # Get a list of all records
    return(sheet)

games = []
print("reading games data...")
games_data = OpenGoogleSheet("ascii games")
i = 0
cell = "nothing"
while cell != "":
   i += 1
   cell = games_data.cell(i+1, 1).value
   games.append([games_data.cell(i, 1).value, games_data.cell(i, 2).value, games_data.cell(i, 3).value, games_data.cell(i, 4).value])
texts = ["ads"]
downloaded = []
p = 0
clear = lambda: os.system('cls')

def waitForKeys(keys):
    while True:
        while not kbhit():
            sleep(0)
        key = getch()
        i = 0
        for k in keys:
            if key == k:
                return(i)
            i += 1
def play(gameData):
    global downloaded
    yes = True
    clear()
    while True:
        outputString = ""
        outputString += ("Play "+gameData[0]+"?\n")
        if yes:
            outputString += (">yes<\n no ")
        else:
            outputString += (" yes \n>no<")
        clear()
        print(outputString)
        key = waitForKeys([b'K', b'M', b'H', b'P', b' ']) # b'K': left, b'M': right, b'H': up, b'P': down
        if key in [0, 1, 2, 3]:
            yes = not yes
        else:
            break
    if yes:
        print("Downloading...")
        try:
            urllib.request.urlopen("https://www.google.com/", timeout = 1)
            with open(__path__ +"\\"+gameData[0]+".txt", "w") as f:
                srccode = str(urllib.request.urlopen(gameData[2]).read(), encoding = 'utf-8')
                f.write(srccode)
        except Exception as e:
            print(e)
        srccode = open(__path__+"\\"+gameData[0]+".txt", "r").read()
        clear()
        return srccode
def getDescription(index):
    global description
    if index < 0:
        description = ""
        return
    descriptionText = games[index][3]
    description = ["by "+games[index][1]]
    line = ""
    for char in descriptionText:
        if char == "\n":
            description.append(line)
            line = ""
        else:
            line += char
    description.append(line)
def getLine(index):
    if index >= len(description):
        return ""
    return description[index]
def printMenu():
    getDescription(p-len(texts))
    outputString = ""
    i = -1
    for text in texts:
        i += 1
        if i == p:
            outputString += (">" + text + "<\n")
        else:
            outputString += (" " + text + (" " *(21 - len(text))) + getLine(i) + "\n") # " by " + game[1] + 
    for game in games:
        i += 1
        if i == p:
            outputString += (">" + game[0] + "<" + (" " *(20 - len(game[0]))) + getLine(i) + "\n") #
        else:
            outputString += (" " + game[0] + (" " *(21 - len(game[0]))) + getLine(i) + "\n") # " by " + game[1] +
    while i < len(description):
        i+=1
        outputString += " "*22+getLine(i)+"\n"
    clear()
    print(outputString)
while True:
    try:
        printMenu()
    except Exception as e:
        print(e)
        input()
    key = waitForKeys([b'K', b'M', b'H', b'P', b' ']) # b'K': left, b'M': right, b'H': up, b'P': down
    if key == 0 or key == 2:
        p -= 1
        if p < 0: p = (len(games)+len(texts)-1)
    elif key == 1 or key == 3:
        p += 1
        if p > (len(games)+len(texts)-1): p = 0
    else:
        if p == 0:
            print("that's not even a game lol")
        else:
            try:
                exec(play(games[p-len(texts)]))
            except Exception as e:
                print("something went wrong :/\n")
                traceback.print_exc()
                input("\npress enter to continue.")
