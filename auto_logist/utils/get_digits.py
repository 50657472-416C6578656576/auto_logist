def get_all(string: str) -> list:
    answer = []
    separators = (',', '.')
    previous = ''
    for el in string:
        if el.isdigit():
            if previous in separators:
                answer.append(previous)
            answer.append(el)
            previous = el
        elif el in separators and previous.isdigit():
            previous = el
        else:
            previous = ''
    return answer


def get_value(string: str) -> float | None:
    try:
        return float(''.join(get_all(string)))
    except ValueError:
        return None
