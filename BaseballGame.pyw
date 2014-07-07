# -*- coding: UTF-8 -*-

import random
from Tkinter import *


def getRandomValues():
    indexValues = []
    for i in range(1,10):
        indexValues.append(i)
    random.shuffle(indexValues)

    return [indexValues[0], indexValues[1], indexValues[2]]

def getInputValues(inputValues):
    intInputValues = []
    for each in inputValues.split(","):
        intInputValues.append(int(each))
    return intInputValues

def isSameValue(randomValue, inputValue):
    if (randomValue == inputValue):
        return True
    else:
        return False

def isSameIndex(randomIndex, inputIndex):
    if (randomIndex == inputIndex):
        return True
    else:
        return False

randomValues = getRandomValues()

def evaluate(index, inputValue):
    for m in range(3):
        randomValue = randomValues[m]
        if isSameValue(randomValue, inputValue):
            if isSameIndex(m, index):
                return 2
            else:
                return 1



# ------------------------------


app = Tk()
app.title("야구게임")
app.geometry('350x500+100+100')

label = Label(app, text="3개의 숫자를 입력하고 아래 버튼을 누르세요 (예: 2,3,4)", height=3)
entry = Entry(app, width=20)
resultText = Text(app)


remainTryCount = 10


def reset_game():
    global remainTryCount
    global randomValues

    randomValues = getRandomValues()
    print randomValues

    remainTryCount = 10

    resultText.delete(1.0, END)
    entry.delete(0, END)


def input_value():
    global remainTryCount

    if (remainTryCount == 0):
        resultText.insert(END, "모든 기회를 소진하였습니다. 새로 시작하세요.\n")
        return

    remainTryCount -= 1

    inputValues = getInputValues(entry.get())

    ball = 0
    strike = 0
    for index in range(3):
        result = evaluate(index, inputValues[index])
        if (result == 1):
            ball += 1
        elif (result == 2):
            strike += 1

    resultText.insert(END, "남은기회[%d] " % remainTryCount )
    resultText.insert(END, inputValues)
    resultText.insert(END, "-> %d strike, %d ball \n" %(strike, ball))

    if strike == 3:
        resultText.insert(END, "니가 이겼다. 새로 시작해라.\n")
        remainTryCount = 0


btnReset = Button(app, text="새로운 게임", command=reset_game)
btnDoIt = Button(app, text="Do it!", command=input_value)

btnReset.pack(fill=X)
label.pack(pady=1)
entry.pack(padx=5)
resultText.pack(padx=10, pady=10)
btnDoIt.place(x=275, y=75)

app.mainloop()


