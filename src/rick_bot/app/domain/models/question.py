
class Question:
    def __init__(self, value: str):
        self._value = value.strip()

    def get_value(self) -> str:
        return self._value