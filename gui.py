import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import time
from character import Character


class MainMenu:
    def __init__(self, root):
        self.root = root
        self.root.title("Main Menu")
        self.root.configure(bg="black")

        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        window_width = screen_width // 2
        window_height = screen_height // 2

        self.root.geometry(f"{window_width}x{window_height}+{screen_width // 4}+{screen_height // 4}")

        label = tk.Label(self.root, text="Welcome to the Pokemon Game!", font=("Helvetica", 16), fg="white", bg="black")
        label.pack(pady=20)
        start_button = tk.Button(self.root, text="Choose Character", command=self.choose_character)
        start_button.pack(pady=10, padx=20, fill=tk.X)

        start_button = tk.Button(self.root, text="Start Game", command=self.choose_and_start_game)
        start_button.pack(pady=10, padx=20, fill=tk.X)

        settings_button = tk.Button(self.root, text="Game Settings", command=self.game_settings)
        settings_button.pack(pady=10, padx=20, fill=tk.X)

        exit_button = tk.Button(self.root, text="End Game", command=self.root.quit)
        exit_button.pack(pady=10, padx=20, fill=tk.X)

        self.selected_character = None

    def choose_and_start_game(self):
        player_character = self.choose_character()
        if player_character:
            combat_game = CombatGameWindow(self.root, player_character)

    def choose_character(self):
        character_options = [
            Character("Warrior", 10, 5, 1, 6, 60, "icons/player_image1.png", "Warrior"),
            Character("Mage", 8, 6, 2, 8, 40, "icons/player_image2.png", "Mage")
        ]

        character_selection_window = CharacterSelectionWindow(self.root, character_options)
        self.root.wait_window(character_selection_window.root)

        return character_selection_window.selected_character

    def game_settings(self):
        settings_window = GameSettingsWindow(self.root)
        self.root.wait_window(settings_window.root)


class CharacterSelectionWindow:
    def __init__(self, root, characters):
        self.root = tk.Toplevel(root)
        self.root.title("Choose Character")
        self.root.configure(bg="black")

        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        window_width = screen_width // 2
        window_height = screen_height // 2

        self.root.geometry(f"{window_width}x{window_height}+{screen_width // 4}+{screen_height // 4}")

        self.characters = characters
        self.selected_character = None

        self.create_character_selection()

    def create_character_selection(self):
        character_frame = tk.Frame(self.root, bg="black")
        character_frame.pack(expand=True, anchor=tk.W)

        for character in self.characters:
            character_info_frame = tk.Frame(character_frame, bg="black")
            character_info_frame.pack(fill=tk.X, pady=10, padx=20, expand=True)

            image = Image.open(character.image_path)
            character_image = ImageTk.PhotoImage(image)
            label = tk.Label(character_info_frame, image=character_image, bg="black")
            label.image = character_image
            label.pack(side=tk.LEFT, padx=(0, 20))

            info_text = f"{character.name}\nHP: {character.hp}/{character.max_hp}  AP: {character.ap}  DP: {character.dp}  SP: {character.sp}"
            info_label = tk.Label(character_info_frame, text=info_text, fg="white", bg="black")
            info_label.pack(side=tk.LEFT)

            select_button = tk.Button(character_info_frame, text="Select", command=lambda char=character: self.select_character(char))
            select_button.pack(side=tk.RIGHT)

    def select_character(self, character):
        self.selected_character = character
        self.root.destroy()

# ... (Previous code)

class WinWindow:
    def __init__(self, root):
        self.root = tk.Toplevel(root)
        self.root.title("Congratulations!")
        self.root.configure(bg="black")

        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        window_width = screen_width // 3
        window_height = screen_height // 3

        self.root.geometry(f"{window_width}x{window_height}+{screen_width // 3}+{screen_height // 3}")

        label = tk.Label(self.root, text="Congratulations! You Win!", font=("Helvetica", 16), fg="white", bg="black")
        label.pack(pady=20)

        main_menu_button = tk.Button(self.root, text="Main Menu", command=self.go_to_main_menu)
        main_menu_button.pack(pady=10, padx=20, fill=tk.X)

    def go_to_main_menu(self):
        self.root.destroy()


class LoseWindow:
    def __init__(self, root):
        self.root = tk.Toplevel(root)
        self.root.title("Game Over")
        self.root.configure(bg="black")

        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        window_width = screen_width // 3
        window_height = screen_height // 3

        self.root.geometry(f"{window_width}x{window_height}+{screen_width // 3}+{screen_height // 3}")

        label = tk.Label(self.root, text="Game Over! You Lose!", font=("Helvetica", 16), fg="white", bg="black")
        label.pack(pady=20)

        main_menu_button = tk.Button(self.root, text="Main Menu", command=self.go_to_main_menu)
        main_menu_button.pack(pady=10, padx=20, fill=tk.X)

    def go_to_main_menu(self):
        self.root.destroy()

class GameSettingsWindow:
    def __init__(self, root):
        self.root = tk.Toplevel(root)
        self.root.title("Game Settings")
        self.root.configure(bg="black")

        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        window_width = screen_width // 2
        window_height = screen_height // 2

        self.root.geometry(f"{window_width}x{window_height}+{screen_width // 4}+{screen_height // 4}")

        self.create_settings()

    def create_settings(self):
        audio_label = tk.Label(self.root, text="Audio:", fg="white", bg="black")
        audio_label.pack()

        audio_var = tk.IntVar()
        audio_on = tk.Radiobutton(self.root, text="On", variable=audio_var, value=1, fg="white", bg="black")
        audio_off = tk.Radiobutton(self.root, text="Off", variable=audio_var, value=0, fg="white", bg="black")
        audio_on.pack()
        audio_off.pack()

        language_label = tk.Label(self.root, text="Language:", fg="white", bg="black")
        language_label.pack()

        languages = ["English", "Spanish", "French"]
        language_var = tk.StringVar()
        language_dropdown = ttk.Combobox(self.root, textvariable=language_var, values=languages, state="readonly")
        language_dropdown.pack()

        difficulty_label = tk.Label(self.root, text="Difficulty:", fg="white", bg="black")
        difficulty_label.pack()

        difficulty_slider = tk.Scale(self.root, from_=1, to=10, orient=tk.HORIZONTAL, fg="white", bg="black")
        difficulty_slider.pack()

        apply_button = tk.Button(self.root, text="Apply", command=self.root.destroy)
        apply_button.pack()
        for widget in [audio_label, audio_on, audio_off, language_label, language_dropdown, difficulty_label, difficulty_slider, apply_button]:
            widget.pack(anchor="center", pady=5)








class CombatGameWindow:
    def __init__(self, root, player_character):
        self.root = tk.Toplevel(root)
        self.root.title("Combat Game")
        self.root.configure(bg="black")

        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        window_width = screen_width // 2
        window_height = screen_height // 2

        self.root.geometry(f"{window_width}x{window_height}+{screen_width // 4}+{screen_height // 4}")

        self.player_character = player_character
        self.enemy1 = Character("Enemy 1", 10, 6, 1, 2, 40, "icons/enemy1.png", "Enemy")

        self.create_game_screen()

        # Determine the first turn based on speed points
        characters = [self.player_character, self.enemy1]
        characters.sort(key=lambda char: char.sp, reverse=True)
        self.current_turn = characters[0]
        self.log_message(f"First turn: {self.current_turn.name}")

    def create_game_screen(self):
        character_info_frame = tk.Frame(self.root, bg="black")
        character_info_frame.pack(fill=tk.X, pady=10, padx=20)

        player_character_image = Image.open(self.player_character.image_path)
        player_character_image = player_character_image.resize((100, 100), Image.ANTIALIAS)
        player_character_image = ImageTk.PhotoImage(player_character_image)
        player_character_label = tk.Label(character_info_frame, image=player_character_image, bg="black")
        player_character_label.image = player_character_image
        player_character_label.pack(side=tk.LEFT, padx=(0, 20))

        enemy1_image = Image.open(self.enemy1.image_path)
        enemy1_image = enemy1_image.resize((100, 100), Image.ANTIALIAS)
        enemy1_image = ImageTk.PhotoImage(enemy1_image)
        enemy1_label = tk.Label(character_info_frame, image=enemy1_image, bg="black")
        enemy1_label.image = enemy1_image
        enemy1_label.pack(side=tk.RIGHT, padx=(0, 20))

        info_text = (
            f"{self.player_character.name}\n"
            f"HP: {self.player_character.hp}/{self.player_character.max_hp}  "
            f"AP: {self.player_character.ap}  DP: {self.player_character.dp}  SP: {self.player_character.sp}"
        )
        player_info_label = tk.Label(character_info_frame, text=info_text, fg="white", bg="black", justify=tk.LEFT)
        player_info_label.pack(side=tk.LEFT)

        info_text = (
            f"{self.enemy1.name}\n"
            f"HP: {self.enemy1.hp}/{self.enemy1.max_hp}  "
            f"AP: {self.enemy1.ap}  DP: {self.enemy1.dp}  SP: {self.enemy1.sp}"
        )
        enemy_info_label = tk.Label(character_info_frame, text=info_text, fg="white", bg="black", justify=tk.RIGHT)
        enemy_info_label.pack(side=tk.RIGHT)

        action_frame = tk.Frame(self.root, bg="black")
        action_frame.pack(pady=10, padx=20)

        attack_button = tk.Button(action_frame, text="Attack", command=self.attack)
        attack_button.pack(side=tk.LEFT, padx=10)

        defend_button = tk.Button(action_frame, text="Defend", command=self.defend)
        defend_button.pack(side=tk.LEFT, padx=10)

        heal_button = tk.Button(action_frame, text="Heal", command=self.heal)
        heal_button.pack(side=tk.LEFT, padx=10)

        log_frame = tk.Frame(self.root, bg="black")
        log_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)
        self.log_text = tk.Text(log_frame, height=6, fg="white", bg="black")
        self.log_text.pack(fill=tk.BOTH, expand=True)

        navigation_frame = tk.Frame(self.root, bg="black")
        navigation_frame.pack(fill=tk.X, padx=20, pady=10)

        main_menu_button = tk.Button(navigation_frame, text="Main Menu", command=self.go_to_main_menu)
        main_menu_button.pack(side=tk.LEFT, padx=10)

        restart_button = tk.Button(navigation_frame, text="Restart Game", command=self.restart_game)
        restart_button.pack(side=tk.LEFT, padx=10)

        self.log_message(f"Turn: {self.player_character.name}'s turn")

    def log_message(self, message):
        self.log_text.insert(tk.END, f"{message}\n")
        self.log_text.see(tk.END)

    def attack(self):
        target = self.enemy1
        damage = self.player_character.ap - target.dp
        if damage > 0:
            target.take_damage(damage)
        self.log_message(f"{self.player_character.name} attacked {target.name} for {damage} damage!")
        self.update_character_info()
        self.check_win_or_lose()
        self.enemy_turn()

    def enemy_attack(self, enemy):
        target = self.player_character
        damage = enemy.ap - target.dp
        if damage<=0:
            damage=0
        if damage > 0:
            target.take_damage(damage)
        self.log_message(f"{enemy.name} attacked {target.name} for {damage} damage!")
        self.update_character_info()
        self.check_win_or_lose()

    def check_win_or_lose(self):
        if self.player_character.hp <= 0:
            self.log_message("You lose! Game Over.")
            self.disable_actions()
            LoseWindow(self.root)
        elif self.enemy1.hp <= 0:
            self.log_message("Congratulations! You win!")
            self.disable_actions()
            WinWindow(self.root)

    def defend(self):
        self.player_character.defend()
        self.log_message(f"{self.player_character.name} is defending!")
        self.enemy_turn()

    def heal(self):
        self.player_character.heal()
        self.log_message(f"{self.player_character.name} used Heal!")
        self.update_character_info()
        self.enemy_turn()

    def enemy_turn(self):
        if self.enemy1.hp > 0:
            self.enemy_attack(self.enemy1)

    def update_character_info(self):
        info_text = (
            f"{self.player_character.name}\n"
            f"HP: {self.player_character.hp}/{self.player_character.max_hp}  "
            f"AP: {self.player_character.ap}  DP: {self.player_character.dp}  SP: {self.player_character.sp}"
        )
        player_info_label = tk.Label(self.root, text=info_text, fg="white", bg="black", justify=tk.LEFT)
        player_info_label.place(x=20, y=140)

        info_text = (
            f"{self.enemy1.name}\n"
            f"HP: {self.enemy1.hp}/{self.enemy1.max_hp}  "
            f"AP: {self.enemy1.ap}  DP: {self.enemy1.dp}  SP: {self.enemy1.sp}"
        )
        enemy_info_label = tk.Label(self.root, text=info_text, fg="white", bg="black", justify=tk.RIGHT)
        enemy_info_label.place(x=500, y=140)
        


    def disable_actions(self):
        for widget in self.root.winfo_children():
            if isinstance(widget, tk.Button):
                widget.config(state=tk.DISABLED)

    def go_to_main_menu(self):
        self.root.destroy()

    def restart_game(self):
        self.root.destroy()
        player_character = main_menu.choose_character()
        if player_character:
            combat_game = CombatGameWindow(root, player_character)

    def update(self):
        self.root.update()


# Create the main Tkinter window
root = tk.Tk()
main_menu = MainMenu(root)
root.mainloop()
