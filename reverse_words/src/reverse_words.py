def reverse_words(text):
    if not isinstance(text, str):
        raise TypeError("Вхідний параметр повинен бути рядком.")

    result = []
    words = text.split(" ")

    for word in words:
        letters = list(word)
        i, j = 0, len(letters) - 1

        while i < j:
            if not letters[i].isalpha():
                i += 1
            elif not letters[j].isalpha():
                j -= 1
            else:
                letters[i], letters[j] = letters[j], letters[i]
                i += 1
                j -= 1

        result.append("".join(letters))

    return " ".join(result)
