class Turn:

    current_player = "a"
    turns = 0

    won = False

    @classmethod
    def switch(cls):
        cls.current_player = ("a" if cls.current_player != "a" else "b")
        cls.turns += 1

    @classmethod
    def set_won(cls, player):
        cls.won = True

        file = open("highscores.dat", "a")

        file.write("Player " + player.upper() + " won after " + str(cls.turns) + " turns.\n")

        file.close()
