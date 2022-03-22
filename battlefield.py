from player import Player

class Battlefield:
    def __init__(self):
        self.player_one = Player()
        self.player_two = Player()

    def run_game(self):
        self.display_welcome()

    def display_welcome(self):
        print("---------------------------------------")
        print("\tWelcome to Battlefield!")
        print("---------------------------------------")

    def battle(self):
        pass

    def player1_turn(self):
        pass

    def player2_turn(self):
        pass

    def display_winner(self):
        pass
