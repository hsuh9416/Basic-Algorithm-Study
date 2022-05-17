"""
    Ch7 String searching(문자열 검색)
    * Skipped too simple examples

    * important notes
    1) String searching means to find pattern from the text
    2) Brute force method: Expanded method from linear search
        => Also called as 'Straightforward method'
        => This is simple but has the worst efficiency
        => If pattern matching is failed, abandon the previous procedures and redo the process from the start
    3) KMP(Knuth-Morris-Pratt)
        => The method does not abandon the previous procedures
        => Write a skip table for KMP
           a> Find overlapping patterns within patten
           b> From a>, set the logic to the point to start over
           c> Execute search
        => KMP is a kind of adjustment of brute search method, so it is basically a linear searching method.
        => However, this algorithm is generally inferior to the Boyer-Moore method(So seldomly be used)
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


def kmp_match(txt: str, pat: str) -> int:
    pt = 1  # Current index position of cursor
    pp = 0  # Current checking index order of pattern
    skip = [0] * (len(pat) + 1)  # Skip table

    # Skip table setting ex> Pattern 'ABCABD'
    skip[pt] = 0  # [0,0,0,0,0,0,0]
    while pt != len(pat):  # There found some letters overlapped within pattern itself
        if pat[pt] == pat[pp]:
            pt += 1
            pp += 1
            skip[pt] = pp  # [0,0,0,1,2,0]
        elif pp == 0:  # For the very first position, do not determine of skipping
            pt += 1
            skip[pt] = pp
        else:  # No overlapped letter anymore, so turn to 0
            pp = skip[pp]

    # String Search ex> Text 'ABCABCABD'
    pt = pp = 0  # Initializing
    while pt != len(txt) and pp != len(pat):
        if txt[pt] == pat[pp]:  # Check if pattern matches
            pt += 1
            pp += 1
        elif pp == 0:  # No latter matched yet
            pt += 1
        else:  # Turned out the pattern was not totally matched -> apply skip table
            pp = skip[pp]  # For text[5] = 'C' -> pp = skip[pp] = 2 -> Start from scanning (2 + 1) letter of pattern

    return pt - pp if pp == len(pat) else -1


def string_searching_text():
    s1 = input('Enter the whole text to be searched: ')
    s2 = input('Enter the pattern string to use in searching: ')

    # idx = bf_match(s1, s2)
    # idx = bf_match2(s1, s2)
    idx = kmp_match(s1, s2)

    if idx == -1:
        print("There's no matching pattern in the text!")
    else:
        print(f'The pattern first matched in index range({idx},{idx + len(s2)-1})')


if __name__ == '__main__':
    string_searching_text()
