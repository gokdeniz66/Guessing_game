# Guess my number game
# User must attempt to guess randomly selected number within a range in fewest possible attempts

from tkinter import *
import random
import winsound

class Application(Frame):
    """A GUI application which which generates random number and gets user input"""

    def __init__(self, master): #initialize newly created Application object
        """Initialize the frame"""
        Frame.__init__(self, master) # super(Application, self).__init__(master) in python 3
        self.grid()
        self.create_widgets()
        self.number = random.randint(1, 20)
        self.numberofguesses = 0



    def create_widgets(self):
        """Get user inputs"""
        # create instruction label
        Label(self, text = "Gok een getal tussen de 1 en 20").grid(row = 0, column = 0, sticky = W)
        Label(self, text = "Probeer het binnen 5 keer te gokken!").grid(row = 1, column = 0, sticky = W)

        # create guess input prompt label and entry
        self.guess_ent = Entry(self, width=30)
        self.guess_ent.grid(row = 2, column = 0, sticky = W)

        # create start game prompt label and submit button
        Button(self, text = "Gok", command = self.run_game).grid(row = 2, column = 0)
        Button(self, text = "Reset", command = self.reset_game).grid(row = 3, column = 0, sticky=W)


        # create submit button
        #Button(self, text = "Submit", command = )

        # create computer feedback text box
        self.text = Text(self, width=75, height=2, wrap=WORD)
        self.text.grid(row=4, column=0, columnspan=2)

    def run_game(self):
        """Generate number and get user input"""
        try:
            guess = int(self.guess_ent.get())
            self.numberofguesses += 1
            print(self.numberofguesses)



            if guess == self.number:
                print_text = "Goed gedaan! Je hebt het nummer gegokt. het was {0}".format(self.number)
                self.text.delete(0.0, END)
                self.text.insert(0.0, print_text)
                self.numberofguesses = 0
                self.guess_ent.delete(0, END)
                self.number = random.randint(1, 20)

                
            else:
                if guess > self.number:
                   print_text = "Je gokt {0}.".format(guess)
                   print_text += " nummer is te hoog"
                   self.text.delete(0.0, END)
                   self.text.insert(0.0, print_text)
                   self.guess_ent.delete(0, END)
                   
                else:
                    print_text = "Je gokt {0}.".format(guess)
                    print_text += " nummer is te laag"
                    self.text.delete(0.0, END)
                    self.text.insert(0.0, print_text)
                    self.guess_ent.delete(0, END)
                if self.numberofguesses == 5:
                    print_text = "Je bent af, alle 5 levens zijn op! Het getal was {0}".format(self.number)
                    self.text.delete(0.0, END)
                    self.text.insert(0.0, print_text)
                    self.guess_ent.delete(0, END)
                    self.numberofguesses = 0
                    self.number = random.randint(1, 20)

        except:
            print('Ongeldige nummer')                         


    def reset_game(self):          
            print_text = "Game is gereset!"
            self.number = random.randint(1, 20)
            self.text.delete(0.0, END)
            self.text.insert(0.0, print_text)
            self.numberofguesses = 0

# main
root = Tk()
root.resizable(0,0)
winsound.PlaySound("C:/LOCATION/guessing_game/song.wav", winsound.SND_ASYNC)
root.geometry('420x120')
root.title("Guessing Game")
app = Application(root)
app.configure(bg='lightgrey')
root.mainloop()
