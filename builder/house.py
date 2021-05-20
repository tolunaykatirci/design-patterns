

class House:

    def __init__(self):
        self.walls: int = 6
        self.doors: int = 3
        self.rooms: int = 2
        self.has_garage: bool = False
        self.has_garden: bool = False
        self.has_swim_pool: bool = False

    def specifications(self):
        specs = '\nWalls: {}\nDoors: {}\nRooms: {}\nHas Garage: {}\nHas Garden: {}\nHas Swim Pool: {}'.format(
            self.rooms, self.doors, self.rooms, self.has_garage, self.has_garden, self.has_swim_pool)
        return specs

    '''
    Tricky solution to Builder pattern in Python
    '''

    def additional_init(self, walls=6, doors=3, rooms=2, has_garage=False, has_garden=False, has_swim_pool=False):
        self.walls = walls
        self.doors = doors
        self.rooms = rooms
        self.has_garage = has_garage
        self.has_garden = has_garden
        self.has_swim_pool = has_swim_pool


class HouseBuilder:

    def __init__(self) -> None:
        self.house = House()

    def set_walls(self, wall_count):
        self.house.walls = wall_count

    def set_doors(self, door_count):
        self.house.doors = door_count

    def set_rooms(self, room_count):
        self.house.rooms = room_count

    def add_garage(self):
        self.house.has_garage = True

    def add_garden(self):
        self.house.has_garden = True

    def add_swim_pool(self):
        self.house.has_swim_pool = True

    def build(self) -> House:
        return self.house

    def reset(self):
        self.house = House()
