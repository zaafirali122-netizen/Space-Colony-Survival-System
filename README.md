# 🚀 Space Colony Survival — Python

![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python&logoColor=white)
![OOP](https://img.shields.io/badge/OOP-Class%20Based-green?style=for-the-badge&logo=python&logoColor=white)
![Game](https://img.shields.io/badge/Game-Simulation-orange?style=for-the-badge)
![Theme](https://img.shields.io/badge/Theme-Space-purple?style=for-the-badge)
![Interface](https://img.shields.io/badge/Interface-CLI-black?style=for-the-badge)

A futuristic command-line survival simulation built with **Python** using **Object-Oriented Programming (OOP)** concepts.

Players must manage **Oxygen, Food, Energy, and Robots** while defending their colony from **Alien Attacks, Solar Storms, and Oxygen Leakages**.

---

# 📸 Preview

<p align="center">
  <img src="images/preview.png" alt="Space Colony Survival Preview" width="800">
</p>

---

# ✨ Features

- 🚀 Manage colony resources
- 🫁 Oxygen management
- 🍖 Food management
- ⚡ Energy management
- 🤖 Robot maintenance
- 👨‍🚀 Multiple character types
- 👽 Random alien attacks
- ☀️ Solar storm disasters
- 💨 Oxygen leakage events
- 📅 7-Day survival challenge
- 🏆 Score tracking
- 🎲 Randomized gameplay
- 💀 Multiple game-over conditions

---

# 🎯 Game Objective

Survive on the alien planet for **7 days** while keeping your colony operational.

Manage:

- 🫁 Oxygen
- 🍖 Food
- ⚡ Energy
- 🤖 Robots

If any critical resource reaches **0**, the colony collapses.

---

# 🎮 Gameplay Actions

## ⛏ Collect Resources

- Uses Energy
- Collects Oxygen
- Collects Food
- Increases Score

## 🔧 Repair Colony

- Repairs damaged systems
- Prevents oxygen leaks
- Uses Energy
- Increases Score

## 🤖 Recharge Robots

- Consumes Energy
- Restores robot efficiency
- Improves resource collection

## 🍽 Eat Food

- Consumes Food
- Restores Energy
- Improves astronaut health

## 📅 Next Day

- Advances to the next day
- Triggers random events
- Updates colony status

---

# ⚠️ Random Events

## 👽 Alien Attack

Possible enemies:

- 👾 Scout Alien
- 👾 Warrior Alien
- 👾 Alien Beast

Effects:

- Energy decreases
- Robots take damage
- Colony health decreases

## 💨 Oxygen Leakage

- Oxygen rapidly decreases
- Repairs are required
- Colony efficiency drops

## ☀️ Solar Storm

- Robot malfunction
- Energy loss
- Communication failure

## 🌌 Peaceful Day

No disaster occurs.

Resources remain safe.

---

# 👨‍🚀 Colony Characters

## 👨‍🚀 Astronaut

- Collects resources
- Explores nearby areas
- Consumes energy

## 👨‍🔧 Engineer

- Repairs colony systems
- Fixes oxygen leaks
- Maintains equipment

## 🤖 Robot

- Automates work
- Collects resources
- Requires recharging

## 👽 Alien

- Attacks the colony
- Damages resources
- Creates survival challenges

---

# 🏆 Win Condition

```text
🏆 CONGRATULATIONS!

SPACE COLONY SURVIVED!

You successfully protected the colony
for 7 days.

Humanity has a new future.
```

---

# 💀 Game Over Conditions

```text
💀 COLONY DESTROYED!
```

The game ends if:

- 🫁 Oxygen reaches **0**
- 🍖 Food reaches **0**
- ⚡ Energy reaches **0**
- 🤖 All robots are destroyed

---

# 🚀 Installation

## Clone Repository

```bash
git clone https://github.com/YourUsername/Space-Colony-Survival.git
```

## Open Project Folder

```bash
cd Space-Colony-Survival
```

## Run Program

```bash
python main.py
```

---

# 🗂️ Project Structure

```text
Space-Colony-Survival/
│
├── main.py
├── README.md
├── images/
│   └── preview.png
│
├── Character (Abstract Class)
├── Human
│   ├── Astronaut
│   └── Engineer
│
├── Robot
├── Alien
│
└── SpaceColony
```

---

# 📚 OOP Concepts Used

| Concept | Usage |
|---------|-------|
| Abstraction | Character abstract class |
| Inheritance | Astronaut and Engineer inherit Human |
| Polymorphism | Different `perform_duty()` methods |
| Encapsulation | Oxygen, Food, Energy, Robot Status |
| Composition | SpaceColony contains Humans, Robots and Aliens |
| Method Overriding | Child classes override methods |

---

# 🧠 Learning Outcomes

This project demonstrates:

- ✅ Object-Oriented Programming
- ✅ Class Design
- ✅ Inheritance
- ✅ Polymorphism
- ✅ Encapsulation
- ✅ Abstraction
- ✅ Random Event Simulation
- ✅ Resource Management
- ✅ Simulation-Based Game Development

---

# 🔮 Future Improvements

- ✅ Inventory System
- ✅ More Alien Species
- ✅ Robot Upgrades
- ✅ Colony Expansion
- ✅ Weather System
- ✅ Difficulty Levels
- ✅ Save / Load Feature
- ✅ GUI Version using Tkinter
- ✅ Multiplayer Mode
- ✅ Achievement System

---
