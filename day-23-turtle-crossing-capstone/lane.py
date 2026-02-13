from car import Car
import random

SPAWN_INTERVALS = [10, 15, 20, 25, 30, 40, 50, 70]
SPAWN_WEIGHTS = [5, 10, 20, 25, 20, 10, 5, 5]

SAFE_DISTANCE_BUFFER = 230

class Lane:
    def __init__(self, y_position, direction, speed, color):
        """Initializes a lane object. Supply the lanes y-coordinate position,
        direction (left or right), initial speed, and color."""
        self.y_position = y_position
        self.direction = direction
        self.speed = speed
        self.original_speed = speed
        self.color = color
        self.cars = []  # Each lane owns its cars!
        #this counts while loop iterations and is a helper variable for spawning cars
        self.frame_counter = 0
        # Randomly select a spawn interval from SPAWN_INTERVALS list,
        # using SPAWN_WEIGHTS to make some intervals more likely than others.
        # [0] extracts the single value from the returned list.
        self.next_spawn = random.choices(SPAWN_INTERVALS, weights=SPAWN_WEIGHTS)[0]

    def create_car(self):
        """Creates car objects under certain conditions. Cars can't spawn bumper to bumper.
        Randomizes which frame to spawn a car."""

        #there is at least one car in the cars list
        if len(self.cars) > 0 and self.frame_counter >= self.next_spawn:
            last_car = self.cars[-1]
            if self.direction == "left":
                #if too close, don't spawn
                if last_car.xcor() > SAFE_DISTANCE_BUFFER:
                    self.frame_counter = 0
                    self.next_spawn = random.choices(SPAWN_INTERVALS, weights=SPAWN_WEIGHTS)[0]
                else:
                    new_car = Car(self)
                    self.cars.append(new_car)
                    self.frame_counter = 0
                    self.next_spawn = random.choices(SPAWN_INTERVALS, weights=SPAWN_WEIGHTS)[0]
            #right direction
            else:
                # if too close, don't spawn
                if last_car.xcor() < -SAFE_DISTANCE_BUFFER:
                    self.frame_counter = 0
                    self.next_spawn = random.choices(SPAWN_INTERVALS, weights=SPAWN_WEIGHTS)[0]
                else:
                    new_car = Car(self)
                    self.cars.append(new_car)
                    self.frame_counter = 0
                    self.next_spawn = random.choices(SPAWN_INTERVALS, weights=SPAWN_WEIGHTS)[0]

        #this is the first car
        else:
            if self.frame_counter >= self.next_spawn:
                new_car = Car(self)
                self.cars.append(new_car)
                self.frame_counter = 0
                self.next_spawn = random.choices(SPAWN_INTERVALS, weights=SPAWN_WEIGHTS)[0]

    def move_cars(self):
        """Move all cars in the lane."""
        for car in self.cars:
            car.move()

    def cleanup_cars(self):
        """Remove cars that drive beyond the screen."""
        if len(self.cars) > 0:
            if self.direction == "right":
                if self.cars[0].xcor() > 280:
                    self.cars[0].hideturtle()
                    self.cars.pop(0)
            else:
                if self.cars[0].xcor() + 30 < -280:
                    self.cars[0].hideturtle()
                    self.cars.pop(0)

    def reset(self):
        """Remove all cars from the lane and reset spawn state."""
        for car in self.cars:
            car.hideturtle()
        self.cars.clear()
        self.frame_counter = 0
        self.speed = self.original_speed
        self.next_spawn = random.choices(SPAWN_INTERVALS, weights=SPAWN_WEIGHTS)[0]

    def update(self):
        """Increment the frame counter, create a car object, move and cleanup cars."""
        self.frame_counter += 1
        self.create_car()
        self.move_cars()
        self.cleanup_cars()
