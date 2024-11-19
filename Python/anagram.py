def is_anagram(s, t):
    letters = {}

    for c in s:
        if c in letters:
            letters[c] = letters[c] + 1
        else:
            letters[c] = 1

    for c in t:
        if c in letters:
            remaining = letters[c] - 1

            if remaining < 0:
                return False
            elif remaining == 0:
                del letters[c]
            else:
                letters[c] = remaining
        else:
            return False

    if len(letters) > 0:
        return False

    return True


print(is_anagram("anagram", "grammar"))