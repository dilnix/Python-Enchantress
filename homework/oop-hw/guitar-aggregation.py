#!/bin/python

class Guitar:
    def __init__(self, pick):
        self.pick = pick

    def play(self):
        print(f"Playing on guitar with {self.pick.width} pick.")


class Pick:
    def __init__(self, width):
        self.width = width


myPick = Pick("bold")
guitar = Guitar(myPick)
guitar.play()
pick_width = myPick.width
print(
    f"My pick width is {pick_width}. Even if you destroy guitar instance, my pick will still exist.")
