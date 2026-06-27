# Space-Colony-Survival-System
An open-source survival game where players build, manage, and expand a space colony.
🚀 Space Colony Survival — Python
Python OOP Simulation Game (CLI)

A futuristic command-line survival simulation built with Python using Object-Oriented Programming (OOP) concepts.

In this game, Earth is no longer safe, and humanity has established a colony on a distant planet. As the colony commander, your mission is to keep everyone alive by managing Oxygen, Food, Energy, and Robots while defending the colony against dangerous Alien Attacks, Solar Storms, and Oxygen Leakages.

📸 Preview
===================================
        SPACE COLONY SURVIVAL
===================================

DAY : 1/7

Oxygen : 100
Food    : 100
Energy  : 100
Robots  : 3
Score   : 0

===================================

1. Collect Resources
2. Repair Colony
3. Recharge Robots
4. Eat Food
5. Next Day
6. Exit

Enter Choice:
✨ Features

🚀 Manage colony resources

🫁 Oxygen management system

🍖 Food management

⚡ Energy management

🤖 Robot maintenance

👨‍🚀 Multiple character types

👽 Random alien attacks

☀️ Solar storm disasters

💨 Oxygen leakage events

📅 7-Day survival challenge

🏆 Score tracking system

🎲 Randomized gameplay

💀 Multiple game-over conditions

🎯 Game Objective

Survive on the alien planet for 7 days while keeping your colony operational.

Manage:

🫁 Oxygen

🍖 Food

⚡ Energy

🤖 Robots

If any critical resource reaches 0, the colony collapses.

🎮 Gameplay Actions
⛏ Collect Resources

Uses Energy

Collects Food

Collects Oxygen

Increases Score

🔧 Repair Colony

Repairs damaged systems

Prevents Oxygen loss

Consumes Energy

Increases Score

🤖 Recharge Robots

Consumes Energy

Restores Robot efficiency

Improves resource collection

🍽 Eat Food

Consumes Food

Restores Energy

Improves Astronaut health

📅 Next Day

Advances to the next day

Triggers random events

Updates colony status

⚠️ Random Events
👽 Alien Attack

Possible enemies:

👾 Scout Alien

👾 Warrior Alien

👾 Alien Beast

Effects:

Decrease Energy

Damage Robots

Reduce Colony Health

💨 Oxygen Leakage

Causes:

Rapid Oxygen loss

Requires repairs

Reduces colony efficiency

☀️ Solar Storm

Effects:

Robot malfunction

Energy loss

Communication failure

🌌 Peaceful Day

No disaster occurs.

Resources remain safe.

👨‍🚀 Colony Characters
👨‍🚀 Astronaut

Collects resources

Explores nearby areas

Consumes Energy

👨‍🔧 Engineer

Repairs colony systems

Fixes oxygen leaks

Maintains equipment

🤖 Robot

Automates work

Collects resources

Requires Energy recharge

👽 Alien

Attacks the colony

Damages resources

Creates survival challenges

🏆 Win Condition
🏆 CONGRATULATIONS!

SPACE COLONY SURVIVED!

You successfully protected the colony
for 7 days.

Humanity has a new future.
💀 Game Over Conditions
💀 COLONY DESTROYED!

The game ends if:

🫁 Oxygen reaches 0

🍖 Food reaches 0

⚡ Energy reaches 0

🤖 All Robots are destroyed

🚀 Installation
Clone Repository
git clone https://github.com/yourusername/Space-Colony-Survival.git
Open Project Folder
cd Space-Colony-Survival
Run Program
python main.py
🗂️ Project Structure
Space-Colony-Survival/
│
├── main.py
├── README.md
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
📚 OOP Concepts Used
Concept	Usage
Abstraction	Character abstract class
Inheritance	Astronaut and Engineer inherit Human
Polymorphism	perform_duty() method implementation
Encapsulation	Oxygen, Food, Energy, Robot Status
Composition	SpaceColony contains Humans, Robots, and Aliens
Method Overriding	Child classes override perform_duty()
🧠 Learning Outcomes

This project demonstrates:

✅ Object-Oriented Programming

✅ Class Design

✅ Inheritance

✅ Polymorphism

✅ Encapsulation

✅ Abstraction

✅ Random Event Simulation

✅ Resource Management

✅ Simulation-Based Game Development

🔮 Future Improvements

✅ Inventory System

✅ More Alien Species

✅ Robot Upgrades

✅ Colony Expansion

✅ Weather & Planet Environment System

✅ Difficulty Levels

✅ Save/Load Game Feature

✅ GUI Version using Tkinter

✅ Multiplayer Colony Mode

✅ Achievement System
