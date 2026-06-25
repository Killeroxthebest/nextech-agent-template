#!/usr/bin/env python3
"""Simple single-player Gold Quest (beginner version).

Goal: reach 10,000 money.

Features:
- Collect money (random base) multiplied by your multiplier.
- Buy multiplier upgrades to increase earnings.
- Take disadvantages for instant cash but increases chance to lose money on collects.
"""
import random
import sys


GOAL = 10000


def fmt(n):
    return f"${n:,.0f}"


class Game:
    def __init__(self):
        self.money = 0
        self.multiplier = 1.0
        self.mult_level = 0
        self.disadvantages = 0

    def status(self):
        print(f"Money: {fmt(self.money)} | Multiplier: x{self.multiplier:.2f} | Disadvantages: {self.disadvantages}")

    def collect(self):
        base = random.randint(50, 150)
        gain = int(base * self.multiplier)

        # Each disadvantage adds a 10% independent chance to trigger a penalty
        penalty = 0
        for i in range(self.disadvantages):
            if random.random() < 0.10:
                # lose a portion of the gain
                lost = int(gain * 0.20)
                penalty += lost

        net = max(0, gain - penalty)
        self.money += net
        print(f"Collected {fmt(gain)}. Penalties {fmt(penalty)}. Net {fmt(net)}.")

    def cost_for_multiplier(self):
        # Cost grows with current mult level
        return 500 * (2 ** self.mult_level)

    def buy_multiplier(self):
        cost = self.cost_for_multiplier()
        if self.money < cost:
            print(f"Not enough money. Multiplier upgrade costs {fmt(cost)}.")
            return
        self.money -= cost
        self.mult_level += 1
        self.multiplier += 0.5
        print(f"Bought multiplier. New multiplier: x{self.multiplier:.2f}.")

    def take_disadvantage(self):
        # Tradeoff: get instant cash, but increase disadvantages
        reward = random.randint(300, 800)
        self.money += reward
        self.disadvantages += 1
        print(f"Took a disadvantage: +{fmt(reward)} now, but disadvantages increased to {self.disadvantages}.")

    def remove_disadvantage(self):
        if self.disadvantages <= 0:
            print("No disadvantages to remove.")
            return
        cost = 200 * self.disadvantages
        if self.money < cost:
            print(f"Not enough money to remove disadvantages. Cost {fmt(cost)}.")
            return
        self.money -= cost
        self.disadvantages -= 1
        print(f"Removed one disadvantage. Left: {self.disadvantages}.")


def print_help():
    print("Commands:")
    print("  collect    - Collect money (affected by multiplier/disadvantages)")
    print("  buy        - Buy a multiplier upgrade (cost increases)")
    print("  disadvantage - Take a disadvantage for instant cash")
    print("  remove     - Remove one disadvantage (costs money)")
    print("  status     - Show current money, multiplier, disadvantages")
    print("  help       - Show this help")
    print("  quit       - Exit game")


def main():
    game = Game()
    print("Welcome to Gold Quest (Beginner). Goal: reach $10,000.")
    print_help()

    while True:
        if game.money >= GOAL:
            print(f"Congratulations! You reached the goal with {fmt(game.money)}.")
            break

        cmd = input("\n> ").strip().lower()
        if not cmd:
            continue
        if cmd in ("collect", "c"):
            game.collect()
        elif cmd in ("buy", "b"):
            game.buy_multiplier()
        elif cmd in ("disadvantage", "d"):
            game.take_disadvantage()
        elif cmd in ("remove", "r"):
            game.remove_disadvantage()
        elif cmd in ("status", "s"):
            game.status()
        elif cmd in ("help", "h"):
            print_help()
        elif cmd in ("quit", "q", "exit"):
            print("Goodbye!")
            break
        else:
            print("Unknown command — type 'help' for commands.")


if __name__ == "__main__":
    try:
        main()
    except (KeyboardInterrupt, EOFError):
        print("\nGoodbye!")
        sys.exit(0)
#!/usr/bin/env python3
"""Simple single-player Gold Quest (beginner version).

Goal: reach 10,000 money.

Features:
- Collect money (random base) multiplied by your multiplier.
- Buy multiplier upgrades to increase earnings.
- Take disadvantages for instant cash but increases chance to lose money on collects.
"""
import random
import sys


GOAL = 10000


def fmt(n):
    return f"${n:,.0f}"


class Game:
    def __init__(self):
        self.money = 0
        self.multiplier = 1.0
        self.mult_level = 0
        self.disadvantages = 0

    def status(self):
        print(f"Money: {fmt(self.money)} | Multiplier: x{self.multiplier:.2f} | Disadvantages: {self.disadvantages}")

    def collect(self):
        base = random.randint(50, 150)
        gain = int(base * self.multiplier)

        # Each disadvantage adds a 10% independent chance to trigger a penalty
        penalty = 0
        for i in range(self.disadvantages):
            if random.random() < 0.10:
                # lose a portion of the gain
                lost = int(gain * 0.20)
                penalty += lost

        net = max(0, gain - penalty)
        self.money += net
        print(f"Collected {fmt(gain)}. Penalties {fmt(penalty)}. Net {fmt(net)}.")

    def cost_for_multiplier(self):
        # Cost grows with current mult level
        return 500 * (2 ** self.mult_level)

    def buy_multiplier(self):
        cost = self.cost_for_multiplier()
        if self.money < cost:
            print(f"Not enough money. Multiplier upgrade costs {fmt(cost)}.")
            return
        self.money -= cost
        self.mult_level += 1
        self.multiplier += 0.5
        print(f"Bought multiplier. New multiplier: x{self.multiplier:.2f}.")

    def take_disadvantage(self):
        # Tradeoff: get instant cash, but increase disadvantages
        reward = random.randint(300, 800)
        self.money += reward
        self.disadvantages += 1
        print(f"Took a disadvantage: +{fmt(reward)} now, but disadvantages increased to {self.disadvantages}.")

    def remove_disadvantage(self):
        if self.disadvantages <= 0:
            print("No disadvantages to remove.")
            return
        cost = 200 * self.disadvantages
        if self.money < cost:
            print(f"Not enough money to remove disadvantages. Cost {fmt(cost)}.")
            return
        self.money -= cost
        self.disadvantages -= 1
        print(f"Removed one disadvantage. Left: {self.disadvantages}.")


def print_help():
    print("Commands:")
    print("  collect    - Collect money (affected by multiplier/disadvantages)")
    print("  buy        - Buy a multiplier upgrade (cost increases)")
    print("  disadvantage - Take a disadvantage for instant cash")
    print("  remove     - Remove one disadvantage (costs money)")
    print("  status     - Show current money, multiplier, disadvantages")
    print("  help       - Show this help")
    print("  quit       - Exit game")


def main():
    game = Game()
    print("Welcome to Gold Quest (Beginner). Goal: reach $10,000.")
    print_help()

    while True:
        if game.money >= GOAL:
            print(f"Congratulations! You reached the goal with {fmt(game.money)}.")
            break

        cmd = input("\n> ").strip().lower()
        if not cmd:
            continue
        if cmd in ("collect", "c"):
            game.collect()
        elif cmd in ("buy", "b"):
            game.buy_multiplier()
        elif cmd in ("disadvantage", "d"):
            game.take_disadvantage()
        elif cmd in ("remove", "r"):
            game.remove_disadvantage()
        elif cmd in ("status", "s"):
            game.status()
        elif cmd in ("help", "h"):
            print_help()
        elif cmd in ("quit", "q", "exit"):
            print("Goodbye!")
            break
        else:
            print("Unknown command — type 'help' for commands.")


if __name__ == "__main__":
    try:
        main()
    except (KeyboardInterrupt, EOFError):
        print("\nGoodbye!")
        sys.exit(0)
