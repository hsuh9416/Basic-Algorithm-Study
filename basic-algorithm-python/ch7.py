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
        => However, this algorithm is generally inferior to the Boyer-Moor method(So seldom be used)
    4) Boyer-Moor method: The methods scans the text by pattern reversely to make much effective skipping
        => Known as much superior algorithm than KPM method
        => Enable to skip length of pattern
        => Skip table logic
           a> If the letter was not included in pattern
            => The skipping length == len(pattern)
           b> If the letter was included in pattern
            - If the latest index was k then -> the skipping length == len(pattern) - k - 1
            - If no latter was overlapped within pattern then -> the skipping length == len(n)
           c> The number of elements used in skip table is 256
    5> Time complexity of string searching algorithm
        * n: length of text m: length of pattern
        a> Brute force method: Theoretically O(mn) but actually O(n)
        b> KMP(Knuth-Morris-Pratt): O(n)
            => Good for file reading sequentially
        c> Boyer-Moor method: The worst case: O(n) In average: O(n / m)
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


def bm_match(txt: str, pat: str) -> int:
    skip = [None] * 256  # Skip table

    # Skip table
    for pt in range(256):  # Allocate number to skip as a length of pattern in all elements
        skip[pt] = len(pat)

    for pt in range(len(pat)):  # Relocate number to skip for which overlapped element(ASCII number of character)
        skip[ord(pat[pt])] = len(pat) - pt - 1

    # String searching
    while pt < len(txt):  # Checking within reversed pattern
        pp = len(pat) - 1  # Add up the index as [len(pattern) - 1]
        while txt[pt] == pat[pp]:
            if pp == 0:  # All the letter has been matched
                return pt
            pt -= 1
            pp -= 1
        # After pattern matching been failed
        pt += skip[ord(txt[pt])] if skip[ord(txt[pt])] > len(pat) - pp else len(pat) - pp

    return -1


def string_searching_text():
    s1 = input('Enter the whole text to be searched: ')
    s2 = input('Enter the pattern string to use in searching: ')

    # idx = bf_match(s1, s2)
    # idx = bf_match2(s1, s2)
    # idx = kmp_match(s1, s2)
    idx = bm_match(s1, s2)

    if idx == -1:
        print("There's no matching pattern in the text!")
    else:
        print(f'The pattern first matched in index range({idx},{idx + len(s2)-1})')


if __name__ == '__main__':
    string_searching_text()
