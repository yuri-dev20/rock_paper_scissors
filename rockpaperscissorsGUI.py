from tkinter import Tk, Frame, Label, Button
import random

class RockPaperScissors:
    def __init__(self):
        self.__pc_results = 0
        self.__player_results = 0
        root = Tk()
        root.title("Rock Paper Scissors")
        root.geometry("225x250")
        self.widget = Frame(root)
        self.widget.pack()
        self.result_label = Label(root, text="Result: ")
        self.result_label.pack()
        self.pc_label = Label(root, text="PC: " + str(self.__pc_results))
        self.user_label = Label(root, text="User: " + str(self.__player_results))
        self.pc_label.pack()
        self.user_label.pack()
        self.button_widget = Frame(root)
        self.paper_btn = Button(self.button_widget, padx=20, command=lambda: self.play("Paper"))
        self.paper_btn["text"] = "Paper"
        self.rock_btn = Button(self.button_widget, padx=20, command=lambda: self.play("Rock"))
        self.rock_btn["text"] = "Rock"
        self.scissors_btn = Button(self.button_widget, padx=20, command=lambda: self.play("Scissors"))
        self.scissors_btn["text"] = "Scissors"
        self.button_widget.pack(side="bottom")
        self.paper_btn.pack(side="left")
        self.rock_btn.pack(side="left")
        self.scissors_btn.pack(side="left")
        root.mainloop()

    def play(self, player_choice):
        self.pc_options = ["Paper", "Rock", "Scissors"]
        self.pc_choice = self.pc_options[random.randint(0,2)]

        if (self.pc_choice == "Paper" and player_choice == "Paper"):
            self.result_label["text"] = "Result: Draw"
            
        elif (self.pc_choice == "Paper" and player_choice == "Rock"):
            self.__pc_results += 1
            self.result_label["text"] = "Result: PC Win"
            self.pc_label["text"] = "PC: " + str(self.__pc_results)

        elif (self.pc_choice == "Paper" and player_choice == "Scissors"):
            self.__player_results += 1
            self.result_label["text"] = "Result: Player Win"
            self.user_label["text"] = "User: " + str(self.__player_results)

        elif (self.pc_choice == "Rock" and player_choice == "Paper"):
            self.__player_results += 1
            self.result_label["text"] = "Result: Player Win"
            self.user_label["text"] = "User: " + str(self.__player_results)
        
        elif (self.pc_choice == "Rock" and player_choice == "Rock"):
            self.result_label["text"] = "Result: Draw"

        elif (self.pc_choice == "Rock" and player_choice == "Scissors"):
            self.__pc_results += 1
            self.result_label["text"] = "Result: PC Win"
            self.pc_label["text"] = "PC: " + str(self.__pc_results)
        
        elif (self.pc_choice == "Scissors" and player_choice == "Paper"):
            self.__pc_results += 1
            self.result_label["text"] = "Result: PC Win"
            self.pc_label["text"] = "PC: " + str(self.__pc_results)

        elif (self.pc_choice == "Scissors" and player_choice == "Rock"):
            self.__player_results += 1
            self.result_label["text"] = "Result: Player Win"
            self.user_label["text"] = "User: " + str(self.__player_results)
        
        else:
            self.result_label["text"] = "Result: Draw"

r = RockPaperScissors()