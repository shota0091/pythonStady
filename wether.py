import random

def wether(wether):

    if wether == "晴れ":
        print("晴れているので日傘が必要")
    elif wether == "雨":
        print("雨が降っているので傘が必要")


num = random.randrange(2)
wethers = ["晴れ","雨"]
wether(wethers[num])