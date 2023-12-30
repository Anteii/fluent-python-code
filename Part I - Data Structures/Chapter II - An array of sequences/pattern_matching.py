import random


STATES = ("STAY", "BEEP", "FORWARD", "BACKWARD")
STATIONS = ("Alpha", "Bravo", "Gamma")


class InvalidCommand(Exception):
    pass


class Robot:
    _cur_position: float
    _start_position: float
    
    def __init__(self, position: float = 0) -> None:
        self._start_position = self._cur_position = position
    
    def move(self, direction: str, distance: float) -> None:
        if direction == "FORWARD":
            self._cur_position += distance
        else:
            self._cur_position -= distance
    
    def message_distance(self, station: str) -> None:
        dist = abs(self._start_position - self._cur_position)
        print(f"Message to {station}. Distance from the starting point it {dist}")


class Commander:
    
    _error_chance: float = 0.2
    
    def get_command(self) -> tuple:
        if random.random() < self._error_chance:
            return ("JUMP",)
        command = random.choice(STATES)
        if command == "STAY":
            return (command,)
        elif command == "BEEP":
            return (command, random.choice(STATIONS))
        else:
            return (command, 10 * random.random())


# Simple match case
robot = Robot()
commander = Commander()

steps = 100

for i_step in range(steps):
    command = commander.get_command()
    
    match command:
        case ("STAY",):
            pass
        case ("BEEP", station_name):
            robot.message_distance(station_name)
        case (direction, distance):
            robot.move(direction, distance)
        case _:
            print("Invalid command!")


# Match case with guard
robot = Robot()
commander = Commander()

steps = 100

for i_step in range(steps):
    command = commander.get_command()
    
    match command:
        case ("STAY",):
            pass
        case ("BEEP", station_name):
            robot.message_distance(station_name)
        case (direction, distance) if abs(distance) > 1e-5: # e.g. there's noise in values
            robot.move(direction, distance)
        case _:
            print("Invalid command!")


# Match case with as keyword
robot = Robot()
commander = Commander()

steps = 100

for i_step in range(steps):
    command = commander.get_command()
    
    match command:
        case ("STAY",):
            pass
        case ("BEEP", station_name):
            robot.message_distance(station_name)
        case (direction, distance) as coords if abs(distance) > 1e-5:
            robot.move(*coords)
        case _:
            print("Invalid command!")

# Match case with type info
robot = Robot()
commander = Commander()

steps = 100

for i_step in range(steps):
    command = commander.get_command()
    
    match command:
        case ("STAY",):
            pass
        case ("BEEP", str(station_name)):
            robot.message_distance(station_name)
        case (str(direction), float(distance)) as coords if abs(distance) > 1e-5:
            robot.move(*coords)
        case _:
            print("Invalid command!")

# NOTE 1: [] <=> ()
# NOTE 2: can't use match with str, bytes, bytearray. Workaround is convert to tuple
# NOTE 2: in stdlib these types compatible with match
#   list    tuple           memoryview
#   range   array.array     collections.deque
# NOTE 3: _ matched to any item, but it's never bound to it