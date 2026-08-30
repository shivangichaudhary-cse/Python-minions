class Room:
    """Represents a game location with search logic."""
    def __init__(self, name: str, clues: list, descriptions: list):
        self.name = name
        self.clues = clues
        self.descriptions = descriptions
        self.searched = False

    def search(self) -> list:
        self.searched = True
        print(f"\nYou search {self.name} and find:")
        for desc in self.descriptions:
            print(f"- {desc}")
        return self.clues


class Suspect:
    """Represents a suspect with statement logic and win condition function."""
    def __init__(self, name: str, key_name: str, quote: str, trait: str, win_condition):
        self.name = name
        self.key_name = key_name
        self.quote = quote
        self.trait = trait
        self.win_condition = win_condition  # Functional condition check

    def interview(self) -> str:
        print(f"\nYou interview {self.name}. They say:\n{self.quote}")
        return self.trait

    def evaluate(self, clues: set, state: dict) -> bool:
        """Executes the suspect's individual win condition function."""
        return self.win_condition(clues, state)


class DetectiveGame:
    """Master game engine managing functional execution flow."""
    def __init__(self):
        self.clues = set()
        self.interviewed = {}
        self.is_running = True

        # Pure Python Data Initialization
        self.rooms = {
            "1": Room("The Study", ["letter", "vase", "diary"], 
                      ["A strange letter to Mr. Black.", "A broken bloody vase.", "Torn diary pages."]),
            "2": Room("The Library", ["hidden passage", "poison book"], 
                      ["A hidden passage to the study.", "A book on poisons."]),
            "3": Room("The Kitchen", ["missing knife", "footprint"], 
                      ["A missing kitchen knife.", "A footprint in flour."]),
            "4": Room("The Garden", ["bloody glove", "trampled flowers"], 
                      ["A buried bloody glove.", "Trampled flowers."]),
            "5": Room("The Bedroom", ["fabric", "debts"], 
                      ["Torn fabric matching butler uniform.", "Debt documents."])
        }

        self.suspects = {
            "1": Suspect("The Butler", "butler", "'I saw the maid near the study!'", "nervous",
                         lambda clues, state: "fabric" in clues),
            "2": Suspect("The Maid", "maid", "'I was in the kitchen preparing dinner!'", "kitchen",
                         lambda clues, state: "missing knife" in clues and "footprint" in clues),
            "3": Suspect("The Gardener", "gardener", "'I heard raised voices earlier!'", "heard voices",
                         lambda clues, state: "bloody glove" in clues and "trampled flowers" in clues),
            "4": Suspect("The Chef", "chef", "'I was with the maid in the kitchen!'", "alibi for maid",
                         lambda clues, state: "poison book" in clues and "chef" in state)
        }

    # Modular action functions
    def search_room(self):
        print("\nWhich room would you like to search?")
        for key, room in self.rooms.items():
            status = " [Searched]" if room.searched else ""
            print(f"{key}. {room.name}{status}")
        
        choice = input("Choice: ").strip()
        if choice in self.rooms:
            found = self.rooms[choice].search()
            self.clues.update(found)
        else:
            print("Invalid room choice.")

    def interview_suspect(self):
        print("\nWhich suspect would you like to interview?")
        for key, suspect in self.suspects.items():
            print(f"{key}. {suspect.name}")

        choice = input("Choice: ").strip()
        if choice in self.suspects:
            s = self.suspects[choice]
            trait = s.interview()
            self.interviewed[s.key_name] = trait
        else:
            print("Invalid suspect choice.")

    def make_accusation(self):
        print("\nWho do you accuse?")
        for key, suspect in self.suspects.items():
            print(f"{key}. {suspect.name}")

        choice = input("Choice: ").strip()
        if choice in self.suspects:
            s = self.suspects[choice]
            if s.evaluate(self.clues, self.interviewed):
                print(f"\nYou accuse {s.name}. They confess! You solved the case! 🎉")
            else:
                print(f"\nYou accuse {s.name}, but lack sufficient evidence. The culprit escapes! 🕵️‍♂️")
            self.is_running = False
        else:
            print("Invalid choice.")

    def play(self):
        """Main game loop using function mapping dispatch."""
        print("Welcome to 'Mystery at the Manor'!")
        
        # Function dispatcher: maps inputs directly to functions
        actions = {
            "1": self.search_room,
            "2": self.interview_suspect,
            "3": self.make_accusation
        }

        while self.is_running:
            print("\n--------------------------------")
            print("1. Search a room\n2. Interview a suspect\n3. Make an accusation")
            choice = input("Enter choice (1-3): ").strip()
            
            action = actions.get(choice)
            if action:
                action()
            else:
                print("Invalid choice. Pick 1, 2, or 3.")

if __name__ == "__main__":
    game = DetectiveGame()
    game.play()
  
