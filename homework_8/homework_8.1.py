class Flower:
    def __init__(self, name, cost, time_to_life):
        self.name = name
        self.cost = cost
        self.time_to_life = time_to_life


class Bouquet:
    def __init__(self, *args):
        self.bouquet = list(args)
        self.final_cost = 0.0
        self.count_postcard = 0
        self.count_chocolate = 0
        self.count_strawberry = 0

    def sort(self):
        exchange = True
        while exchange:
            exchange = False
            for n in range(len(self.bouquet) - 1):
                if self.bouquet[n].cost > self.bouquet[n + 1].cost:
                    intermediate = self.bouquet[n]
                    self.bouquet[n] = self.bouquet[n + 1]
                    self.bouquet[n + 1] = intermediate
                    exchange = True
        print("\nЦветы отсортированы по стоимости:")
        for n in range(len(self.bouquet)):
            print(f"{n + 1}: {self.bouquet[n].name} - {self.bouquet[n].cost}Р")

    def average_time(self):
        total_time = 0.0
        for n in range(len(self.bouquet)):
            total_time += self.bouquet[n].time_to_life
        print(f"\nВремя увядания букета: {total_time / len(self.bouquet):.1f} дня(ей).")

    def search_flower(self, flower):
        for n in range(len(self.bouquet)):
            if flower == self.bouquet[n].name:
                print(f"\n{flower} содержится в букете.")
                return
        print(f"\n{flower} не содержится в букете.")

    def cost_count(self):
        self.final_cost = 0.0
        print(f"\nСостав букета:")
        for n in range(len(self.bouquet)):
            self.final_cost += self.bouquet[n].cost
            print(f"Цветок {self.bouquet[n].name} стоимостью {self.bouquet[n].cost}Р")

        if self.count_postcard != 0:
            print(f"Открытка: {self.count_postcard}шт стоимостью {self.count_postcard * 100}Р.")
            self.final_cost += self.count_postcard * 100

        if self.count_chocolate != 0:
            print(f"Шоколад: {self.count_chocolate}шт стоимостью {self.count_chocolate * 200}Р.")
            self.final_cost += self.count_chocolate * 200

        if self.count_strawberry != 0:
            print(f"Клубника: {self.count_strawberry}шт стоимостью {self.count_strawberry * 500}Р.")
            self.final_cost += self.count_strawberry * 500
        return self.final_cost

    def postcard(self, count=1):
        self.count_postcard += count

    def chocolate(self, count=1):
        self.count_chocolate += count

    def strawberry(self, count=1):
        self.count_strawberry += count


class Rose(Flower):
    def __init__(self, cost=200, time_to_life=5):
        super().__init__("Роза", cost, time_to_life)


class Chrysanthemum(Flower):
    def __init__(self, cost=90, time_to_life=3):
        super().__init__("Хризантема", cost, time_to_life)


class Pion(Flower):
    def __init__(self, cost=140, time_to_life=3.5):
        super().__init__("Пион", cost, time_to_life)


class Tulip(Flower):
    def __init__(self, cost=120, time_to_life=4):
        super().__init__("Тюльпан", cost, time_to_life)


rose1 = Rose()
rose2 = Rose(220)
chrysanthemum1 = Chrysanthemum()
chrysanthemum2 = Chrysanthemum(115)
pion1 = Pion()
pion2 = Pion(152, 7)
tulip1 = Tulip()
tulip2 = Tulip()

bouquet1 = Bouquet(rose1, rose2, chrysanthemum1, chrysanthemum2, pion1, pion2, tulip1, tulip2)
bouquet1.postcard()
bouquet1.chocolate()
bouquet1.strawberry(2)
bouquet1.sort()
bouquet1.average_time()
bouquet1.search_flower("Хризантема")
bouquet1.search_flower("Астра")
print(f"\nОбщая стоимость: {bouquet1.cost_count()}Р")
