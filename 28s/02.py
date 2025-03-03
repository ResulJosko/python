class Car:
    def __init__(self, model, color, year, speed):
        self.model = model
        self.color = color
        self.year = year
        self.speed = speed

    def show_info(self):
        print(f"Model:", {self.model})
        print(f"Color:", {self.color})
        print(f"Year:", {self.year})
        print(f"Speed:", {self.speed})
        print("*" * 15)

    def speed_up(self,amount):
        self.speed = amount

    def increase(self):
        self.speed += 10
        print("Speed", self.speed)
        print("*" * 20)

car1 = Car(
    input("Write the car's model: "),
    input("Write the car's year: "),
    input("Write the car's color: "),
    int(input("Write the car's speed: "))
)

car1.show_info()
car1.increase()