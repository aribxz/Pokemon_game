🕹️ Terminal Pokémon Catching Game
===============================

A fun, simple terminal-based Pokémon-catching game built with Python.

🚀 Features
-----------
- Random Pokémon encounters while walking
- Each Pokémon has a random power level (1–100)
- To catch a Pokémon, guess a secret number between 1–100
- If you already have a strong Pokémon (power > 50), you get helpful hints!
- Save/load your caught Pokémon using a `save.json` file
- Pokédex summary shown at the end

🎮 How to Play
-------------
1. Clone this repository or download the files.
2. Open your terminal.
3. Run the game.
4. You'll start walking, and may encounter a Pokémon.
5. Try to catch it by guessing the correct number!
6. If you guess right, it’s added to your team and saved.
7. If you fail, the game ends and shows your Pokédex.

🧠 Hints
--------
- Always get “Too low” or “Too high” feedback.
- If you have a Pokémon with power > 50:
  - “🔥 You’re very close!” if you're within 5
  - “🥶 You’re way off…” if you're 25 or more away

💾 Save/Load System
-------------------
- Your caught Pokémon are saved in `save.json`
- When the game starts, it loads your previous progress
- So you can build your Pokédex over time!

📁 Files
-------
- `pokemon_game.py` — Main game file
- `save.json` — Your Pokédex (created automatically after first catch)
- `README.txt` — This file

🛠 Requirements
---------------
- Python 3.x
- No external packages required

🧑‍💻 Made by Arib
-----------------------
Have fun catching them all! 🧢⚡
