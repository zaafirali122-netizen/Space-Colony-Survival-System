from abc import ABC, abstractmethod
import random


# ======================================
# ABSTRACT CLASS
# ======================================

class ColonyMember(ABC):

    @abstractmethod
    def perform_duty(self):
        pass


# ======================================
# HUMAN CLASS
# ======================================

class Human(ColonyMember):

    def __init__(self, name):

        self.name = name
        self.health = 100
        self.energy = 100

    def rest(self):

        self.energy += 25

        if self.energy > 100:
            self.energy = 100

        print(f"{self.name} rested and restored energy.")

    def show_status(self):

        print(f"""
Name: {self.name}
Health: {self.health}
Energy: {self.energy}
""")


# ======================================
# ASTRONAUT CLASS
# ======================================

class Astronaut(Human):

    def __init__(self, name):

        super().__init__(name)

    def explore(self, colony):

        if self.energy < 20:

            print("Not enough energy to explore.")
            return

        found_food = random.randint(10, 30)

        colony.food += found_food

        self.energy -= 20

        print(f"{self.name} explored planet.")
        print(f"Food Found: {found_food}")

    # Polymorphism
    def perform_duty(self):
        pass


# ======================================
# ENGINEER CLASS
# ======================================

class Engineer(Human):

    def __init__(self, name):

        super().__init__(name)

    def repair_system(self, colony):

        if self.energy < 15:

            print("Not enough energy to repair.")
            return

        repair = random.randint(10, 25)

        colony.oxygen += repair
        colony.energy_supply += repair

        self.energy -= 15

        print(f"{self.name} repaired colony systems.")
        print(f"Oxygen Restored: {repair}")

    # Polymorphism
    def perform_duty(self):
        pass


# ======================================
# ROBOT CLASS
# ======================================

class Robot(ColonyMember):

    def __init__(self, model):

        self.model = model
        self.power = 100

    def mine_resources(self, colony):

        if self.power < 20:

            print("Robot needs recharge.")
            return

        resources = random.randint(15, 35)

        colony.energy_supply += resources

        self.power -= 20

        print(f"Robot {self.model} mined resources.")
        print(f"Energy Gained: {resources}")

    def recharge(self):

        self.power += 30

        if self.power > 100:
            self.power = 100

        print(f"Robot {self.model} recharged.")

    def show_status(self):

        print(f"""
Robot Model: {self.model}
Power: {self.power}
""")

    # Polymorphism
    def perform_duty(self):
        pass


# ======================================
# SPACE COLONY CLASS
# ======================================

class SpaceColony:

    def __init__(self, name):

        self.name = name

        self.food = 100
        self.oxygen = 100
        self.energy_supply = 100

        self.day = 1
        self.max_days = 10

    def next_day(self, astronaut, engineer):

        print("\n================================")
        print(f"DAY {self.day}")
        print("================================")

        # Daily resource consumption
        self.food -= 15
        self.oxygen -= 10
        self.energy_supply -= 5

        astronaut.health -= 5
        engineer.health -= 5

        # Random event
        event = random.choice([
            "Alien Attack",
            "Solar Storm",
            "Oxygen Leak",
            "Safe Day"
        ])

        print(f"\nEvent: {event}")

        if event == "Alien Attack":

            damage = random.randint(10, 20)

            astronaut.health -= damage
            engineer.health -= damage

            print("Aliens attacked the colony!")

        elif event == "Solar Storm":

            self.energy_supply -= 20

            print("Solar storm damaged systems.")

        elif event == "Oxygen Leak":

            self.oxygen -= 20

            print("Oxygen leak occurred.")

        else:

            print("Everything is stable today.")

        # Prevent negative values
        self.food = max(0, self.food)
        self.oxygen = max(0, self.oxygen)
        self.energy_supply = max(0, self.energy_supply)

        astronaut.health = max(0, astronaut.health)
        engineer.health = max(0, engineer.health)

        self.day += 1

    def show_colony_status(self):

        print(f"""
================================
SPACE COLONY: {self.name}

Day: {self.day}/{self.max_days}

Food: {self.food}
Oxygen: {self.oxygen}
Energy Supply: {self.energy_supply}
================================
""")

    def game_over(self, astronaut, engineer):

        if self.food <= 0:
            print("\nGame Over! Food finished.")
            return True

        if self.oxygen <= 0:
            print("\nGame Over! Oxygen finished.")
            return True

        if self.energy_supply <= 0:
            print("\nGame Over! No energy remaining.")
            return True

        if astronaut.health <= 0:
            print("\nGame Over! Astronaut died.")
            return True

        if engineer.health <= 0:
            print("\nGame Over! Engineer died.")
            return True

        return False

    def win_game(self):

        if self.day > self.max_days:

            print("\n🏆 CONGRATULATIONS!")
            print("You survived on Planet Titan.")
            return True

        return False


# ======================================
# CREATE OBJECTS
# ======================================

colony = SpaceColony("Titan Base")

astronaut = Astronaut("Alex")
engineer = Engineer("David")
robot = Robot("XR-7")


# ======================================
# MAIN GAME LOOP
# ======================================

while True:

    print("\n========== SPACE COLONY ==========")
    print("1. Show Colony Status")
    print("2. Show Crew Status")
    print("3. Explore Planet")
    print("4. Repair Systems")
    print("5. Mine Resources")
    print("6. Rest Crew")
    print("7. Recharge Robot")
    print("8. Next Day")
    print("9. Exit")

    choice = input("\nEnter Choice: ")

    # ==================================

    if choice == "1":

        colony.show_colony_status()

    elif choice == "2":

        astronaut.show_status()
        engineer.show_status()
        robot.show_status()

    elif choice == "3":

        astronaut.explore(colony)

    elif choice == "4":

        engineer.repair_system(colony)

    elif choice == "5":

        robot.mine_resources(colony)

    elif choice == "6":

        astronaut.rest()
        engineer.rest()

    elif choice == "7":

        robot.recharge()

    elif choice == "8":

        colony.next_day(
            astronaut,
            engineer
        )

        # Check Game Over
        if colony.game_over(
            astronaut,
            engineer
        ):
            break

        # Check Win
        if colony.win_game():
            break

    elif choice == "9":

        print("\nExiting Game...")
        break

    else:

        print("\nInvalid Choice.")