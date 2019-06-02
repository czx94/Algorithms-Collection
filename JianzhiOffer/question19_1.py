'''
Regular expression
'''

def solution1(pair):
    s, p = pair

    # Initialize the table with False. The first row is satisfied.
    table = [[False] * (len(s) + 1) for _ in range(len(p) + 1)]

    # Update the corner case of matching two empty strings.
    table[0][0] = True

    # Update the corner case of when s is an empty string but p is not.
    # Since each '*' can eliminate the charter before it, the table is
    # vertically updated by the one before previous. [test_symbol_0]
    for i in range(2, len(p) + 1):
        table[i][0] = table[i - 2][0] and p[i - 1] == '*'

    for i in range(1, len(p) + 1):
        for j in range(1, len(s) + 1):
            if p[i - 1] != "*":
                # Update the table by referring the diagonal element.
                table[i][j] = table[i - 1][j - 1] and \
                              (p[i - 1] == s[j - 1] or p[i - 1] == '.')
            else:
                # Eliminations (referring to the vertical element)
                # Either refer to the one before previous or the previous.
                # I.e. * eliminate the previous or count the previous.
                # [test_symbol_1]
                table[i][j] = table[i - 2][j] or table[i - 1][j]

                # Propagations (referring to the horizontal element)
                # If p's previous one is equal to the current s, with
                # helps of *, the status can be propagated from the left.
                # [test_symbol_2]
                if p[i - 2] == s[j - 1] or p[i - 2] == '.':
                    table[i][j] |= table[i][j - 1]

    return table[-1][-1]




if __name__ == '__main__':
    pairs = [['aab', 'c*a*b'], ['a.a', 'aa.a'], ['', ''], ['aaa', 'aa']]
    for pair in pairs:
        print(pair, solution1(pair))