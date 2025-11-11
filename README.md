<h1 align="center"> Hangman Python Game (CLI Based)</h1>

<p align="center">
  <img src="https://github.com/user-attachments/assets/bfd7cd59-9e57-43d3-ab55-de8783e5f95e" alt="Hangman Banner" width="700">
</p>

This is a simple **console-based Hangman Game** developed in **Python**.  
It was created as part of my **Programming Fundamentals (PF)** course during my **1st semester at university**.

The project recreates the classic word-guessing game in a fun, interactive way.  
Players must guess letters to uncover a hidden word. Each wrong guess brings the ASCII hangman closer to its doom!

---

## 🎮 Gameplay Summary

- A random word is selected from a predefined word list.  
- The player guesses one letter at a time.  
- Each wrong guess adds a new part to the hangman drawing.  
- The game ends when:  
  ✅ The player correctly guesses the entire word (**Win**)  
  ❌ The player reaches 10 incorrect guesses (**Lose**)  
- Players can choose to **play again** after each game.

---

## 🧱 Features

- 🎲 **Random word selection** using Python’s `random` library  
- 🎨 **Dynamic ASCII art** for hangman progression  
- 🌈 **Colorful console effects** with `colorama`  
- 🧭 **Interactive main menu** (Play, How To Play, Exit)  
- 🔁 **Replay option** for multiple rounds  
- 💬 **Input validation** to ensure smooth gameplay  

---

## 🧩 Example Word List

```python
['ahmed', 'python', 'programming', 'snake', 'oreo']
```

---

## 📁 Project Structure

```
HangmanPython/
├── hangman.py
├── README.md
```

---

## ⚙️ How to Run

### 1. Install Python  
Make sure you have **Python 3.8+** installed on your system.

### 2. Install Dependencies  
Run the following command in your terminal:

```bash
pip install colorama
```

### 3. Run the Game  
```bash
python hangman.py
```

💡 **Note:** The game runs best in a Windows Command Prompt or any terminal that supports colored output.

---

## 🧠 Skills Demonstrated

- Python programming fundamentals  
- Functions and control structures (loops, conditionals)  
- Use of external libraries (`colorama`, `random`)  
- Input handling and validation  
- ASCII art-based UI design  
- Text animation and user experience logic  

---

## 🖥️ Output Preview

```
WELCOME TO HANGMAN!!!
Guess The Word: _ _ _ _ _
Enter a letter: a
```

<p align="center">
  <img src="https://github.com/user-attachments/assets/d1f7998f-3950-444d-ad8d-b21772751b04" alt="Gameplay Screenshot 1" width="750">
</p>

<p align="center">
  <img src="https://github.com/user-attachments/assets/6da7e134-9055-47a3-a979-201174f1eac1" alt="Gameplay Screenshot 2" width="750">
</p>

🎯 Correct guesses reveal letters; incorrect ones draw the hangman.

---

## 📚 How It Works

### Core Components

| Function | Description |
|-----------|-------------|
| `startmenu()` | Displays the game’s main menu |
| `header()` | Shows the ASCII header and welcome text |
| `hangman()` | Contains the core logic for guessing, turns, and game progress |
| `turn0()` – `turn9()` | Each represents a visual stage of the hangman’s state |

### Game Logic

1. A word is randomly chosen from the list.  
2. The player inputs guesses one letter at a time.  
3. The number of remaining turns decreases with each wrong guess.  
4. The game loop continues until the word is guessed or turns run out.

---

## 🧮 Tools and Libraries Used

| Tool / Library | Purpose |
|-----------------|----------|
| `random` | Random word selection |
| `colorama` | Adds color effects to the console |
| `input()` | User interaction |
| `while True` loop | Continuous game flow |

---

## 🧾 Flowchart

<p align="center">
  <img src="https://github.com/user-attachments/assets/eb894b03-35c0-4e9f-a7f6-1584b78d57fc" alt="Flowchart" width="650">
</p>

---

## 🏁 Conclusion

The **Hangman Python Game Project** demonstrates the creative blend of classic gameplay and modern programming principles.  
Through structured logic, user-friendly design, and visual ASCII art, it offers both **entertainment** and **educational value** making it a strong foundational project in **Programming Fundamentals**.

---

## 👤 Author

**Ahmed Hussain**  
**Instructor:** Miss Mehwish  

---

This project stands as a reflection of **collaborative learning** and the **continuous journey toward excellence**.
