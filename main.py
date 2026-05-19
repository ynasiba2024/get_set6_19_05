#3-masala
class Phone:
    def __init__(self, model, battery):
        self.model = model
        self.__battery = 0
        self.set_battery(battery)

    def get_battery(self):
        return self.__battery

    def set_battery(self, new_battery):
        if new_battery > 100:
            print("Batareya foizi noto'g'ri")
        else:
            self.__battery = new_battery


p1 = Phone("iPhone", 85)

print(p1.model)
print(p1.get_battery())
