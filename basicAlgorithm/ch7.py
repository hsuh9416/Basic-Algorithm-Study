"""
    Ch7 String searching(문자열 검색)
    * Skipped too simple examples

    * important notes
    1) String searching means to find pattern from the text
    2) Brute force method: Expanded method from linear search
        => Also called as 'Straightforward method'

"""


def bf_match(txt: str, pat: str) -> int:
    pt = 0  # Current index position of cursor
    pp = 0  # Current checking index order of pattern

    while pt != len(txt) and pp != len(pat):
        if txt[pt] == pat[pp]:  # Letter been matched
            pt += 1  # Increase index
            pp += 1  # Check next character
        else:
            pt = pt - pp + 1  # Redo the cursor
            pp = 0  # Initialized

    return pt - pp if pp == len(pat) else -1


def bf_match2(txt: str, pat: str) -> int:
    if pat in txt:
        idx = txt.find(pat, 0, len(txt))
        right_idx = txt.rfind(pat, 0, len(txt))  # Return biggest index matched
        # idx = txt.index(pat, 0, len(txt))
        # idx = txt.rindex(pat, 0, len(txt))  # Return biggest index matched
        if idx == right_idx:
            print('The pattern only included once!')
        else:
            print(f'The latest index that pattern included was range({right_idx},{right_idx+len(pat)-1})')
        if txt.startswith(pat, 0, len(txt)):  # Check if pattern was prefix
            print('The pattern was a prefix!')
        elif txt.endswith(pat, 0, len(txt)):  # Check if pattern was suffix
            print('The pattern was a suffix!')
        else:
            print('The pattern was in the middle!')
        return idx
    else:
        return -1


def string_searching_text():
    s1 = input('Enter the whole text to be searched: ')
    s2 = input('Enter the pattern string to use in searching: ')

    # idx = bf_match(s1, s2)
    idx = bf_match2(s1, s2)

    if idx == -1:
        print("There's no matching pattern in the text!")
    else:
        print(f'The pattern first matched in index range({idx},{idx + len(s2)-1})')


if __name__ == '__main__':
    string_searching_text()
