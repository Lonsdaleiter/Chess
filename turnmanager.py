current_player = "a"
won = False


def switch():
    global current_player

    current_player = "a" if current_player == "b" else "b"
