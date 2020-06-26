def openfile(file):
    f = open(file, "r")
    lines = f.readlines()
    f.close()
    return lines

def getText(text):
    ret = '';start=False
    for bc in range(len(text)):
        if(start == True and text[bc] != "'"):
            ret += text[bc]
        elif(text[bc] == "'"):
            start = True
        else:
            start = False
    return ret

def read(text):
    var = {}
    for bc in range(len(text)):
        command = text[bc].replace('\n', '')
        if('print' in command):
            print(getText(command))
        elif('input' in command):
            nameVar = command.split(' ')
            var[nameVar[0]] = input(getText(command))
            print(var)

#main
def main():
    text = openfile('./main.itn')
    read(text)

main()