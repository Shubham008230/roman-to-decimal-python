from roman import roman_to_decimal

assert roman_to_decimal("III") == 3
assert roman_to_decimal("IV") == 4
assert roman_to_decimal("IX") == 9
assert roman_to_decimal("XIV") == 14
assert roman_to_decimal("LVIII") == 58
assert roman_to_decimal("MCMXCIV") == 1994
assert roman_to_decimal("mcmxciv") == 1994
assert roman_to_decimal("ABC") is None
assert roman_to_decimal("") is None

print("All tests passed")