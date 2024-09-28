# Game Instructions

## Setup

1. Ensure you have Python installed on your system.
2. Install the required libraries by running:
   
**   pip install tkinter pillow**

Character Class
The game utilizes a Character class defined in the character.py module. This class allows customization of character attributes such as:

Name
Hit Points (HP)
Attack Power (AP)
Defense Power (DP)
Speed Points (SP)
Run the Game
Open a terminal or command prompt.
Navigate to the directory containing the game files.
Run the main script:
bash
Copy code
python -u main.py
Main Menu
Upon running the game, the main menu will appear with the following options:

Choose Character: Click this button to select your character for the game. A new window will appear with character options. Click the "Select" button to choose a character.
Start Game: Begin the combat game with the selected character. Combat actions include Attack, Defend, and Heal.
Game Settings: Adjust audio settings (On/Off), select language (English, Spanish, French), and set game difficulty (1-10).
End Game: Exit the game.
Character Selection
In the character selection window:

Click on a character's "Select" button to choose your character for the game.
Game Settings
In the settings window, you can:

Toggle audio On/Off.
Select a language from the dropdown.
Adjust the game difficulty using the slider.
Click the "Apply" button to save settings and close the window.
Combat Game
In the combat game window, you'll see information about your character and the enemy. The following buttons are available for combat actions:

Attack: Click to attack the enemy.
Defend: Click to reduce incoming damage.
Heal: Click to restore your character's health.
Combat actions are turn-based, meaning your character and the enemy take turns attacking.

When the battle concludes (either your HP or the enemy's HP reaches 0), a win or lose window will appear. From this window, you can:

Return to the main menu.
Restart the game.
