
# https://www.codewars.com/kata/51b66044bce5799a7f000003/train/python

class RomanNumerals:

    @staticmethod
    def to_roman(value):
        thousands = 'M' * (value // 1000)
        hundreds = ('C' * (value % 1000 // 100)).replace(9*'C', 'CM').replace(5*'C', 'D').replace(4*'C', 'CD')
        tens = ('X' * (value % 100 // 10)).replace(9*'X', 'XC').replace(5*'X', 'L').replace(4*'X', 'XL')
        units = ('I' * (value % 10)).replace(9*'I', 'IX').replace(5*'I', 'V').replace(4*'I', 'IV')

        return '{}{}{}{}'.format(thousands, hundreds, tens, units)

    @staticmethod
    def from_roman(value):
        values = [
            ('I', 1),
            ('V', 5),
            ('X', 10),
            ('L', 50),
            ('C', 100),
            ('D', 500),
            ('M', 1000),
        ]

        numeric_value = 0
        value = value.replace('IV', 4*'I').replace('IX', 9*'I').replace('XL', 4*'X').replace('XC', 9*'X').replace('CD', 4*'C').replace('CM', 9*'C')
        for k, v in dict(values).items():
            if k in value:
                numeric_value += v * value.count(k)

        return numeric_value

print(RomanNumerals.from_roman('XXI'))
print(RomanNumerals.from_roman('IV'))
