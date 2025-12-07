from src.model import AppModel


class TestAppModel:
    def test_initialization(self):
        model = AppModel()
        assert model.counter == 0

    def test_initialization_with_value(self):
        model = AppModel(counter=10)
        assert model.counter == 10

    def test_increment(self):
        model = AppModel(counter=5)
        new_value = model.increment()
        assert new_value == 6
        assert model.counter == 6

    def test_increment_multiple_times(self):
        model = AppModel()
        model.increment()
        model.increment()
        model.increment()
        assert model.counter == 3

    def test_reset(self):
        model = AppModel(counter=42)
        new_value = model.reset()
        assert new_value == 0
        assert model.counter == 0

    def test_increment_then_reset(self):
        model = AppModel()
        model.increment()
        model.increment()
        assert model.counter == 2

        model.reset()
        assert model.counter == 0
