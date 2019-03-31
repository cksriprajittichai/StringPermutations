#!/usr/bin/env python3

import sys

# s: string
def print_permutations(s):
    visited = [False for i in range(0, len(s))]
    cur_s = [None for i in range(0, len(s))]
    print_permutations_helper(s, cur_s, visited)

# s: string
# cur_s: list of character
# visited: list of boolean
# ndx: int
def print_permutations_helper(s, cur_s, visited, ndx = 0):
    if ndx == len(s):
        print(''.join(cur_s))
        return
    
    for i in range(0, len(s)):
        if is_next_unvisited_char_instance(s, visited, i):
            visited[i] = True
            cur_s[ndx] = s[i]
            print_permutations_helper(s, cur_s, visited, ndx + 1)
            visited[i] = False

# s: string
# visited: list of boolean
# ndx: int
def is_next_unvisited_char_instance(s, visited, ndx):
    for i in range(0, ndx):
        if s[i] == s[ndx] and visited[i] is False:
            return False
    return visited[ndx] is False


if len(sys.argv) != 2:
    print('Incorrect number of arguments. This program takes one parameter.')
else:
    print_permutations(sys.argv[1])
