def get_dict():
    dict = {
        '♠1': 's',
        '♠2': 'p',
        '♠3': 'a',
        '♠4': 'd',
        '♠5': 'e',
        '♥1': 'h',
        '♥2': 'e',
        '♥3': 'a',
        '♥4': 'r',
        '♥5': 't',
        '♣1': 'c',
        '♣2': 'l',
        '♣3': 'u',
        '♣4': 'b',
        '♦1': 'd',
        '♦2': 'i',
        '♦3': 'a',
        '♦4': 'm',
        '♦5': 'o',
        '♦6': 'n',
        '♦7': 'd'
    }
    return dict


def reverse_dict(dict):
    reverse_dict = {}
    for key, value in dict.items():
        reverse_dict.update({value: key})
    return reverse_dict


def pokercode(dict, string):
    for key, value in dict.items():
        string = string.replace(key, value)
    return string


def poker_to_letter(string):
    dict = {
        '♤': '♠',
        '♡': '♥',
        '♧': '♣',
        '♢': '♦',
        '黑桃': '♠',
        '红桃': '♥',
        '梅花': '♣',
        '方片': '♦',
    }
    for key, value in dict.items():
        string = string.replace(key, value)
    return pokercode(get_dict(), string)


def letter_to_poker(string):
    return pokercode(reverse_dict(get_dict()), string.lower())


def main():
    letter = 'abc,DEF,GHI'
    # letter = 'HISB.'
    poker = '♥1♢2,♠1♣4！'
    # poker = '红桃1方片2,♠1♣4！'
    print(letter_to_poker(letter))
    print(poker_to_letter(poker))


if __name__ == "__main__":
    main()
