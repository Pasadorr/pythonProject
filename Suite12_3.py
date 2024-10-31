
import unittest
from Tests12_3 import RunnerTest, TournamentTest  # Импортируем тестовые классы

# Создаем тестовый набор
suite = unittest.TestSuite()

# Добавляем тесты RunnerTest и TournamentTest
suite.addTest(unittest.makeSuite(RunnerTest))
suite.addTest(unittest.makeSuite(TournamentTest))

# Запускаем тесты с выводом
runner = unittest.TextTestRunner(verbosity=2)
runner.run(suite)
