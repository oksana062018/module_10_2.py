import threading
import time   #чтобы выводилось время

class Knight(threading.Thread):
   def __init__(self, name, power):
        threading.Thread.__init__(self)
        self.name = name
        self.power = power
        self.enemies = 100  # Начальное количество врагов
        self.days = 0
        print(f'{self.name},  на нас напали!"')

   def run(self):
       print(f'{self.name}, на нас напали!"')
       while self.enemies >0:
           time.sleep(1) # (1 день)
           self.days +=1
           self.enemies-= self.power
           if self.enemies < 0:
               self.enemies = 0
           print(f"{self.name} сражается {self.days}..., осталось {self.enemies} воинов.")
       print(f"{self.name} одержал победу спустя {self.days} {'дней' if self.days > 1 else 'день'}!")

# Создаем и запускаем два потока рыцарей
first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)

first_knight.start()
second_knight.start()

# Ждем завершения обоих потоков
first_knight.join()
second_knight.join()

print("Битвы окончены.")