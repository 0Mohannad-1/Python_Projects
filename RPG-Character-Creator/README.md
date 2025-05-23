# 🧙‍♂️ RPG Character Creator 🛡️

![Python](https://img.shields.io/badge/Language-Python-blue.svg)
![Status](https://img.shields.io/badge/Status-In_Progress-yellow)
![License](https://img.shields.io/badge/License-MIT-green)

A beginner-friendly, text-based RPG character creator where players can enter a custom name, choose a class (Warrior or Mage), and view their unique stats.

---

## 🎮 Features

- 📝 Enter your custom character name
- 🧝 Choose between **Warrior** or **Mage**
- 📊 View detailed stats based on your chosen class
- 🔁 Input validation to prevent wrong class selection
- 🧠 Clean formatting with `.strip()`, `.title()`, and spacing fixes

---

## 🖥️ Demo

```text
Please Enter The Username Of Your Character:   potato        human   

Hello, Potato Human And Welcome To The Game!

Your Attributes As A Warrior:
+---------------------+
| Your Hp: 150        |
| Your mana: 100      |
| Your strength: 10   |
+---------------------+

Your Attributes As A Mage:
+---------------------+
| Your Hp: 100        |
| Your mana: 150      |
| Your strength: 10   |
+---------------------+

Pick A Class To Play With, Warrior Or Mage: mage

You Have Picked A Mage As Your Class!
Here Are Your Attributes As A Mage
+---------------------+
| Your Hp: 100        |
| Your mana: 150      |
| Your strength: 10   |
+---------------------+

```text
Future Improvements

- Add more classes (e.g. Archer, Rogue, Healer)
- Implement abilities or skill points
- Create a battle system (PvE or PvP)
- Add leveling and experience
- Save character progress to a file
- Create a GUI version using Tkinter or PyGame