
import unittest

class RunnerTest(unittest.TestCase):
    is_frozen = False

    def skip_if_frozen(func):
        def wrapper(self, *args, **kwargs):
            if self.is_frozen:
                self.skipTest("Тесты в этом кейсе заморожены")
            return func(self, *args, **kwargs)
        return wrapper

    @skip_if_frozen
    def test_first_case(self):
        self.assertTrue(True)

    @skip_if_frozen
    def test_second_case(self):
        self.assertTrue(True)

class TournamentTest(unittest.TestCase):
    is_frozen = True

    def skip_if_frozen(func):
        def wrapper(self, *args, **kwargs):
            if self.is_frozen:
                self.skipTest("Тесты в этом кейсе заморожены")
            return func(self, *args, **kwargs)
        return wrapper

    @skip_if_frozen
    def test_first_tournament(self):
        self.assertTrue(True)

    @skip_if_frozen
    def test_second_tournament(self):
        self.assertTrue(True)

    @skip_if_frozen
    def test_third_tournament(self):
        self.assertTrue(True)

