import random
from abc import ABC, abstractmethod

class Hunt_The_Wumpus():
    def __init__(self, size):
        self.size = size
        self.player = Player()
        self.cave = []
        self.isWaitingForAction = False
        self.isWaitingForArrowDirection = False
        self.debug = False

    def init_game(self):
        self.player = Player()
        self.cave = []
        self.isWaitingForAction = False
        self.isWaitingForArrowDirection = False

        for _ in range(0, self.size):
            self.cave.append([None] * self.size)
        
        self.add_event(Gold())
        self.add_event(EscapeRope())
        self.add_event(Wumpus())
        self.add_event(Arrow())
        self.add_event(Arrow())
        self.add_event(BatSwarm())
        self.add_event(BatSwarm())
        self.add_event(Pit())
        self.add_event(Pit())

    def add_event(self, event):
        while True:
            roomX = random.randint(0, self.size - 1)
            roomY = random.randint(0, self.size - 1)

            if (event.get_symbol() == "R"):
                self.cave[self.player.y][self.player.x] = event
                break

            if (self.cave[roomY][roomX] == None) and (self.player.x != roomX and self.player.y != roomY):
                self.cave[roomY][roomX] = event
                break

    def play_game(self, action):
        if (self.isWaitingForAction and action != None):
            output = ""

            if (not self.is_valid_action(action)):
                return self.get_action_error(action)
            
            if (action == 'f' and not self.isWaitingForArrowDirection):
                self.isWaitingForArrowDirection = True
                return self.output_get_arrow_direction()
            
            if not self.isWaitingForArrowDirection:
                self.move(action)
            else:
                self.fire_arrow(action)

            output += self.get_encounter() + "\n"
            output += self.get_cave() + "\n"

            if self.check_lose() or self.check_win():
                if (self.check_lose()):
                    output += "You lost the game! Better luck next time.\n"
                else:
                    output += "Congradulations! You beat Hunt the Wumpus!\n"
                self.init_game()
                return output

            output += self.get_percepts() + "\n"
            output += self.output_get_action_choices()

            return output
        elif not self.isWaitingForAction:
            self.isWaitingForAction = True
            output = ""
            output += "Welcome to Hunt the Wumpus!\n\n"
        
            output += self.get_cave() + "\n"

            output += self.get_percepts() + "\n"
            output += self.output_get_action_choices()

            return output
        else:
            return "Enter a value to play the game!"

    def get_cave(self):
        cave = ""

        cave += f"Arrows Remaining: {self.player.numArrows} \n"
        row_border = "+"
        for _ in range(0, self.size):
            row_border += "--+"
        
        cave += row_border + "\n"

        for row in range(0, self.size):
            cave += "|"
            for column in range(0, self.size):

                #same pos as player
                if row == self.player.y and column == self.player.x:
                    cave += "P"
                else:
                    cave += " "
                #event in room
                
                if self.cave[row][column] != None and (self.debug or self.check_lose() or self.check_win()):
                    cave += self.cave[row][column].get_symbol()
                else:
                    cave += " "
                

                cave += "|"
            
            cave += f"\n{row_border}\n"


        return f'`{cave}`'
    
    def get_encounter(self): # todo
        event = self.cave[self.player.y][self.player.x]
        if (event != None):
            if event.encounter(self.player):
                self.cave[self.player.y][self.player.x] = None

        return ""

    def get_percepts(self):
        output = ""
        for i in range(-1 , 2):
            for j in range(-1, 2):
                if (i == 0 or j == 0) and (abs(i) != abs(j)):
                    if (self.player.y + i >= 0 and self.player.y + i < self.size and self.player.x + j >= 0 and self.player.x + j < self.size):
                        if (self.cave[self.player.y + i][self.player.x + j] != None):
                            output += self.cave[self.player.y + i][self.player.x + j].get_percept()
        
        return output
    
    def check_win(self):
        return self.player.hasWon
    
    def check_lose(self):
        return not self.player.isAlive
    
    def is_direction(self, c):
        return c == 'w' or c == 'a' or c == 's' or c == 'd'

    def get_random_direction(self):
        directions = ['a', 'w', 'd', 's']
        direction = ''

        while True:
            direction = directions[random.randint(0, len(directions) - 1)]
            if (self.can_move_in_direction(direction)):
                break
        
        return direction
    
    def to_lower(self, direction):
        if direction >= 'A' and direction <= 'Z':
            return direction + ('a' - 'A')
        return direction
    
    def can_move_in_direction(self, direction):
        return (direction == 'w' and self.player.y > 0) or (direction == 's' and self.player.y < self.size - 1) or (direction == 'a' and self.player.x > 0) or (direction == 'd' and self.player.x < self.size - 1)
    
    def is_valid_position(self, x, y):
        return x >= 0 and x < self.size and y >= 0 and y < self.size
    
    def is_valid_action(self, action):
        if self.is_direction(action):
            return self.can_move_in_direction(action)
        elif action == 'f':
            return self.player.numArrows > 0
        
        return False
    
    def get_action_error(self, action):
        if self.is_direction(action):
            return "You can't move in that direction!\n"
        elif action == 'f':
            return "You're out of arrows!\n"
        return "That's an invalid input!\n"
    
    def move(self, action):
        if self.player.isConfused:
            action = self.get_random_direction()
            self.player.isConfused = False

        if action == 'w':
            self.player.y -= 1
        elif action == 'a':
            self.player.x -= 1
        elif action == 's':
            self.player.y += 1
        elif action == 'd':
            self.player.x += 1

    def fire_arrow(self, action): # todo
        if self.player.isConfused:
            action = self.get_random_direction()
            self.player.isConfused = False

        if action == 'w':
            self.fire_arrow_in_direction(0, -1)
        elif action == 'a':
            self.fire_arrow_in_direction(-1, 0)
        elif action == 's':
            self.fire_arrow_in_direction(0, 1)
        elif action == 'd':
            self.fire_arrow_in_direction(1, 0)

    def fire_arrow_in_direction(self, xDir, yDir):
        for i in range(1, 4):
            roomX = self.player.x + (xDir * i)
            roomY = self.player.y + (yDir * i)

            if self.is_valid_position(roomX, roomY):
                if self.cave[roomY][roomX] != None:
                    if self.cave[roomY][roomX].get_symbol() == "W":
                        self.player.hasWon = True

    def output_get_arrow_direction(self):
        return "w: shoot up\na: shoot left\ns: shoot down\nd: shoot right\n"

    def output_get_action_choices(self):
        return "w: move up\na: move left\ns: move down\nd: move right\nf: fire an arrow\n"


    
class Player():
    def __init__(self):
        self.x = 0
        self.y = 0
        self.hasWon = False
        self.isAlive = True
        self.hasGold = False
        self.isConfused = False
        self.numArrows = 0
    
class Event(ABC):
    @abstractmethod
    def get_symbol(self):
        pass
    
    @abstractmethod
    def get_percept(self):
        pass

    @abstractmethod
    def encounter(self, player):
        pass

class Gold(Event):
    def get_symbol(self):
        return "G"

    def get_percept(self):
        return "You stub your toe on something heavy.\n"
    
    def encounter(self, player):
        player.hasGold = True

        return True
    
class Arrow(Event):
    def get_symbol(self):
        return "A"

    def get_percept(self):
        return ""
    
    def encounter(self, player):
        player.numArrows += 1

        return True
    
class Wumpus(Event):
    def get_symbol(self):
        return "W"
    
    def get_percept(self):
        return "The hairs stand up on the back of your neck.\n"
    
    def encounter(self, player):
        player.isAlive = False

        return False
    
class EscapeRope(Event):
    def get_symbol(self):
        return "R"
    
    def get_percept(self):
        return ""
    
    def encounter(self, player):
        if player.hasGold:
            player.hasWon = True

        return False
    
class Pit(Event):
    def get_symbol(self):
        return "P"
    
    def get_percept(self):
        return "You feel a breeze.\n"
    
    def encounter(self, player):
        die = random.randint(0, 3)
        if die == 0:
            player.isAlive = False

        return False
    
class BatSwarm(Event):
    def get_symbol(self):
        return "B"
    
    def get_percept(self):
        return "You hear screeching.\n"
    
    def encounter(self, player):
        player.isConfused = True

        return False