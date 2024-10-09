from threading import Thread
import time

class Knight(Thread):
    def __init__(self, name, power):
        super().__init__()
        self.name = name
        self.power = power

    def run(self):
        self.total_enemies = 100
        self.days = 0
        print(f"{self.name}, на нас напали!")
        while self.total_enemies > 0:
            time.sleep(1)
            self.days += 1
            self.total_enemies -= self.power
            day = "дней" if self.days > 4 else "дня(день)"
            print(f"{self.name}, сражается {self.days} {day}..., осталось {self.total_enemies} воинов.")

        print(f"{self.name} одержал победу спустя {self.days} {day}!")

first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)

first_knight.start()
second_knight.start()

first_knight.join()
second_knight.join()

print("Все битвы закончились!")