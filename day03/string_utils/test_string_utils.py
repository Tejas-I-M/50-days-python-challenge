from string_utils import is_palindrome, camel_to_snake, validate_email

print("Testing is_palindrome...")
assert is_palindrome("A man, a plan, a canal: Panama")
assert is_palindrome("racecar")
assert is_palindrome("No lemon, no melon")
assert not is_palindrome("hello")

print("Testing camel_to_snake...")
assert camel_to_snake("camelCase") == "camel_case"
assert camel_to_snake("PascalCase") == "pascal_case"
assert camel_to_snake("XML") == "x_m_l"  

print("Testing validate_email...")
assert validate_email("user@example.com")
assert not validate_email("bad-email@.com")
assert not validate_email("noatsymbol.com")

print("All tests passed!")
