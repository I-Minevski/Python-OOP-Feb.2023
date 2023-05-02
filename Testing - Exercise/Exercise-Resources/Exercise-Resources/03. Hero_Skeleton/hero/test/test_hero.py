from project.hero import Hero
import unittest


class HeroTest(unittest.TestCase):
    def setUp(self) -> None:
        self.hero = Hero("Gancho", 50, 100, 25)

    def test_init(self):
        self.assertEqual(self.hero.username, "Gancho")
        self.assertEqual(self.hero.level, 50)
        self.assertEqual(self.hero.health, 100)
        self.assertEqual(self.hero.damage, 25)

    def test_battle_same_username_exception(self):
        enemy = Hero("Gancho", 50, 100, 25)
        with self.assertRaises(Exception) as context:
            self.hero.battle(enemy)
        self.assertEqual(str(context.exception), "You cannot fight yourself")

    def test_battle_rest_error(self):
        self.hero.health = 0
        enemy = Hero("Stancho", 50, 100, 25)
        with self.assertRaises(ValueError) as context:
            self.hero.battle(enemy)
        self.assertEqual(str(context.exception), "Your health is lower than or equal to 0. You need to rest")

    def test_battle_enemy_rest_error(self):
        enemy = Hero("Stancho", 50, 100, 25)
        enemy.health = 0
        with self.assertRaises(ValueError) as context:
            self.hero.battle(enemy)
        self.assertEqual(str(context.exception), "You cannot fight Stancho. He needs to rest")

    def test_battle_draw(self):
        enemy = Hero("Stancho", 50, 100, 25)
        self.assertEqual(self.hero.battle(enemy), "Draw")
        self.assertEqual(self.hero.health, -1150)
        self.assertEqual(enemy.health, -1150)

    def test_battle_win(self):
        enemy = Hero("Stancho", 30, 100, 1)
        self.assertEqual(self.hero.battle(enemy), "You win")
        self.assertEqual(self.hero.level, 51)
        self.assertEqual(self.hero.health, 75)
        self.assertEqual(self.hero.damage, 30)

    def test_battle_lose(self):
        enemy = Hero("Stancho", 300, 10000, 100)
        self.assertEqual(self.hero.battle(enemy), "You lose")
        self.assertEqual(enemy.level, 301)
        self.assertEqual(enemy.health, 8755)
        self.assertEqual(enemy.damage, 105)

    def test_str(self):
        self.assertEqual(str(self.hero), "Hero Gancho: 50 lvl\n"
                                         "Health: 100\n"
                                         "Damage: 25\n")


if __name__ == "__main__":
    unittest.main()
