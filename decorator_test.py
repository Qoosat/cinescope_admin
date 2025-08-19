'''
7. Для Warrior сделать метод, который будет менять стойку, всего у него их 2 - это "атакующая" и "защитная"
		- Если у Warrior защитная стойка - входящий урон снижается на 20%
		- Если у Warrior атакующая стойка - ничего не делать

8. Сделать так, чтобы один мог аттаковать другого:
		- Сделать метод attack так, чтобы на вход он принимал объект Hero, у которого вызовет метод take_damage нанося урон
        - Атакующая стойка Воина теперь увеличивает наносимый урон вдвое

покрыть тестами
'''


class Hero:
    def __init__(self, name, health, still_alive=True):
        self.name = name
        self._health = health
        self.still_alive = still_alive

    def take_damage(self, damage):
        if damage < 0:
            raise ValueError("Значение должно быть больше или равно нулю")
        self.health -= damage

    @property
    def health(self):
        # print("я попал в геттер")
        return self._health

    @health.setter
    def health(self, new_health):
        # print("я попал в сеттер")
        self._health = new_health
        # print("Установлено новое значение:", self._health)
        if self.health <= 0:
            self.still_alive = False


class Warrior(Hero):
    def __init__(self, name, health, stance):
        super().__init__(name, health)
        self.stance = stance


class Mage(Hero):
    def __init__(self, name, health, magic_shield):
        super().__init__(name, health)
        if 0 < magic_shield < 1:
            self.magic_shield = magic_shield
        else:
            raise ValueError("Значение должно быть от 0 до 1")

    def take_damage(self, damage):
        damage *= (1 - self.magic_shield)
        super().take_damage(damage)


# Проверить что при значении magic_shield 0.6 и значениях health=80 damage=10 урон составит 4 и уровень health будет 76

def test_mag():
    mag = Mage("max", 80, 0.6)
    mag.take_damage(10)
    assert mag.health == 76, f"Ожидается значение 76, но пришло {mag.health}"
    print("test_mag ✅")


def test_object_creation():
    my_hero = Hero(1, 30)
    war1 = Warrior(5, 100, 2)
    mag1 = Mage(7, 90, 0.6)
    print("test_object_creation ✅")


def test_take_damage_positive():
    my_hero = Hero(1, 30)
    my_hero.take_damage(10)
    assert my_hero.health == 20
    print("test_take_damage_positive ✅")


def test_take_damage_positive_0():
    my_hero = Hero(1, 30)
    my_hero.take_damage(30)
    assert my_hero.health == 0
    print("test_take_damage_positive ✅")


def test_take_damage_positive_pos1():
    my_hero = Hero(1, 30)
    my_hero.take_damage(50)
    assert my_hero.health == -20
    print("test_take_damage_positive ✅")


def test_take_damage_negative():
    """
    Тест проверяет, что значение урона не может быть отрицательным
    """
    my_hero = Hero(1, 90)
    war1 = Warrior(5, 100, 2)
    mag1 = Mage(7, 30, 0.5)
    Play = [my_hero, war1, mag1]
    for i in Play:
        hero_health = i.health
        try:
            i.take_damage(-30)
        except Exception as e:
            assert str(
                e) == "Значение должно быть больше или равно нулю", f"текст ошибки не соответствует, получили {e}"

        assert i.health == hero_health, f"Ожидается значение 30, но пришло {i.health}"
        print("test_take_damage_negative ✅")


def test_setter_positive():
    my_hero = Hero("TestHero", 30)
    my_hero.take_damage(30)
    assert my_hero.still_alive == False
    print("test_setter_positiv ✅")


def test_setter_positive1():
    my_hero = Hero("TestHero", 30)
    my_hero.take_damage(40)
    assert my_hero.still_alive == False
    print("test_setter_positiv1 ✅")


def test_setter_positive2():
    my_hero = Hero("TestHero", 30)
    my_hero.take_damage(20)
    assert my_hero.still_alive == True
    print("test_setter_positiv2 ✅")


def run_tests():
    test_object_creation()
    test_take_damage_positive()
    test_take_damage_positive_0()
    test_take_damage_positive_pos1()
    test_take_damage_negative()
    test_setter_positive()
    test_setter_positive1()
    test_setter_positive2()
    test_mag()


run_tests()

