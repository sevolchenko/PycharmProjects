def get_text(filename):
    with open(filename, 'r') as file:
        return file.read()


def solve(text):
    res_text = text
    i = 0
    while i < len(res_text):
        ch = res_text[i]
        if ch == '(':
            index = find_bracket_from(res_text, i)
            if index != -1:
                sec = res_text[(index - len(res_text) + 1):] if index - len(res_text) + 1 != 0 else ''
                res_text = res_text[:i] + sec
        i += 1
    return res_text


def find_bracket_from(text, index_from):
    i = index_from + 1
    counter = 1
    while i < len(text):
        ch = text[i]
        if ch == ')':
            counter -= 1
        if counter == 0:
            return i
        if ch == '(':
            counter += 1
        i += 1
    return -1


if __name__ == '__main__':
    print(solve(get_text('input.txt')))
