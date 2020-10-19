import urllib.request
def updatesrc():
    with open(".\\src.txt", "w") as f:
        f.write(str(urllib.request.urlopen("https://raw.githubusercontent.com/dzbanecznix/privateDoTestow/master/ascii.py").read(), encoding = 'utf-8'))
        
input("press enter to update")
updatesrc()
