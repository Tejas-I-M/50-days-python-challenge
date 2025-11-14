"""
Day 03 - Simple String Utilities

"""

def is_palindrome(s: str) -> bool:
    if s is None:
        return False

    cleaned = ""
    for ch in s:
        if ch.isalnum():
            cleaned += ch.lower()

    return cleaned == cleaned[::-1]


def camel_to_snake(s: str) -> str:
    if s is None:
        return ""

    result = ""
    for ch in s:
        if ch.isupper():
            if result != "":
                result += "_"
            result += ch.lower()
        else:
            result += ch
    return result


def validate_email(s: str) -> bool:
    if s is None:
        return False

    if s.count("@") != 1:
        return False

    local, domain = s.split("@")

    if local == "" or domain == "":
        return False

    if "." not in domain:
        return False

    domain_parts = domain.split(".")
    if any(part == "" for part in domain_parts):
        return False

    return True
