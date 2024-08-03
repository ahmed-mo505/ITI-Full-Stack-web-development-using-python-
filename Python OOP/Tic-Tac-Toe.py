import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

class Player:
    def __init__(self):
        self.name = ""
        self.symbol = ""

    def choose_name(self):
        while True:    
            name = input("Enter a name (letters only): ")
            if name.isalpha():
                self.name = name
                break
            print("Invalid name. Please use letters only.")

    def choose_symbol(self):
        while True:
            symbol = input(f"{self.name}, enter a symbol (single character): ")
            if symbol.isalpha() and len(symbol) == 1:
                self.symbol = symbol.upper()
                break
            print("Invalid symbol. Please enter a single character.")        

class Menu:
    def display_main_menu(self):
        while True:
            print("\nWelcome to the X-O game!")
            print("1. Start Game")
            print("2. Quit Game")
            choice = input("Choose your option: ")
            if choice in ["1", "2"]:
                return choice
            else:
                print("Invalid choice. Please enter 1 or 2.")
    
    def display_endgame_menu(self, result):
        while True:
            menu_text = f"""
                Game Over!
                {result}
                1. Restart
                2. Quit Game
                Enter your choice: """
            choice = input(menu_text)
            if choice in ["1", "2"]:
                return choice
            else:
                print("Invalid choice. Please enter 1 or 2.")

class Board:
    def __init__(self):
        self.board = [str(i) for i in range(1, 10)]
        
    def display_board(self):
        clear_screen()
        for i in range(0, 9, 3):
            print("|".join(self.board[i:i+3]))
            if i < 6:
                print("-" * 5)

    def update_board(self, choice, symbol):
        if self.is_valid_move(choice):
            self.board[choice - 1] = symbol
            return True
        return False

    def is_valid_move(self, choice):
        return self.board[choice - 1].isdigit()
    
    def reset_board(self):
        self.board = [str(i) for i in range(1, 10)]

class Game:
    def __init__(self):
        self.players = [Player(), Player()]
        self.menu = Menu()
        self.board = Board()
        self.current_player_index = 0

    def start_game(self):
        choice = self.menu.display_main_menu()
        if choice == "1":
            self.setup_players()
            self.play_game()
        else:
            self.quit_game()

    def setup_players(self):
        for number, player in enumerate(self.players, start=1):
            print(f"Player {number}, choose your name and symbol:")
            player.choose_name()
            player.choose_symbol()
            clear_screen()

    def play_game(self):
        while True:
            self.play_turn()
            if self.check_win():
                self.board.display_board()
                Loser = self.players[self.current_player_index].name
                choice = self.menu.display_endgame_menu(f"{Loser} Lose!")
                if choice == "1":
                    self.restart_game()
                else:
                    self.quit_game()
                    break
            elif self.check_draw():
                self.board.display_board()
                choice = self.menu.display_endgame_menu("It's a draw!")
                if choice == "1":
                    self.restart_game()
                else:
                    self.quit_game()
                    break

    def restart_game(self):
        self.board.reset_board()
        self.current_player_index = 0
        self.play_game()

    def check_win(self):
        win_combinations = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],
            [0, 3, 6], [1, 4, 7], [2, 5, 8],
            [0, 4, 8], [2, 4, 6]
        ]
        for combo in win_combinations:
            if self.board.board[combo[0]] == self.board.board[combo[1]] == self.board.board[combo[2]]:
                return True
        return False

    def check_draw(self):
        return all(not cell.isdigit() for cell in self.board.board)

    def play_turn(self):
        player = self.players[self.current_player_index]
        self.board.display_board()
        print(f"{player.name}'s turn ({player.symbol})")
        while True:
            try:
                cell_choice = int(input("Choose a cell (1-9): "))
                if 1 <= cell_choice <= 9 and self.board.update_board(cell_choice, player.symbol):
                    break
                else:
                    print("Invalid move. Try again.")
            except ValueError:
                print("Invalid input. Please enter a number.")
        self.switch_player()

    def switch_player(self):
        self.current_player_index = 1 - self.current_player_index 

    def quit_game(self):
        print("Thank you for playing! Goodbye!")

game = Game()
game.start_game()
