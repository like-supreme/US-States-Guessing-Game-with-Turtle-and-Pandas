# US-States-Guessing-Game-with-Turtle-and-Pandas
A fun Python game that challenges users to guess U.S. states. Built using the turtle module and pandas, this interactive map displays state names on a blank U.S. map when the user types a correct guess. A great project for practicing Python, data handling with CSV, and graphical interfaces.

# 🗺️ US States Guessing Game

This project is a Python-based interactive game that tests your knowledge of U.S. geography. You’ll guess the names of U.S. states, and when you get one right, it appears on a blank map using the `turtle` graphics module!

## 📷 Preview

![Map](./blank_states_img.gif)

## 🚀 Features

- Guess U.S. state names via a popup input.
- Correct guesses are labeled on the map.
- The score updates as you go.
- Typing `Exit` generates a `states_to_learn.csv` with the states you missed.

## 📁 Project Structure

📦 us_states_game
├── main.py # Main game logic
├── 50_states.csv # State names and their (x,y) coordinates
├── blank_states_img.gif # Background map image
├── notes.md # Development notes and ideas
└── states_to_learn.csv # Auto-generated: missed states (after typing Exit)


## 📦 Requirements

- Python 3 or higher
- `pandas`

Install with:

pip install pandas
▶️ How to Run
Just run:

python main.py
Make sure blank_states_img.gif and 50_states.csv are in the same directory as main.py.

📓 Notes
This game was developed to practice:

File I/O using pandas

Drawing graphics with turtle

Handling user input and GUI elements

Basic game logic and CSV manipulation

✅ Future Ideas
Add a timer or countdown

Save high scores

Implement hints or zoom-in maps for difficulty levels
