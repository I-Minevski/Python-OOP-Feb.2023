class Integer:
    def __init__(self, value: int):
        self.value = value

    @classmethod
    def from_float(cls, float_value: float):
        if type(float_value) == float:
            return cls(int(float_value))
        else:
            return "value is not a float"

    @classmethod
    def from_roman(cls, value: str):

        roman_dict = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }

        result = 0
        previous_value = 0
        for num in value:
            current_value = roman_dict[num]
            if current_value > previous_value:
                result += current_value - 2 * previous_value
            else:
                result += current_value
            previous_value = current_value

        return cls(result)

    @classmethod
    def from_string(cls, value: str):
        if type(value) == str:
            return cls(int(value))
        else:
            return "wrong type"


first_num = Integer(10)
print(first_num.value)

second_num = Integer.from_roman("IV")
print(second_num.value)

print(Integer.from_float("2.6"))
print(Integer.from_string(2.6))
