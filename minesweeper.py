from posixpath import split
from pydoc import cli
import random

def display():
    arr = [i for i in range(0, columns)]
    print('\033[91m   ' + arr.__str__().replace("'", '').replace(',',' ').replace(']','').replace('[', ''))
    for i in range(0, rows):
        print('\033[91m' + f"{i}" + '\033[0m' + display_plane[i].__str__().replace("'", '').replace(',',' ').replace(']','').replace('[', '  '))

def click(i , j):
    global open
    value = plane[i][j]
    if value == '*':
        return
    display_plane[i][j] = value
    open += 1
    if value != 0:
        return
    if i-1 >= 0:
        if display_plane[i-1][j] == '#':
            click(i-1, j)
        if j-1 >= 0 and display_plane[i-1][j-1] == '#':
            click(i-1, j-1)
        if j+1 < columns and display_plane[i-1][j+1] == '#':
            click(i-1, j+1)
    if i+1 < rows:
        if display_plane[i+1][j] == '#':
            click(i+1, j)
        if j-1 >= 0 and display_plane[i+1][j-1] == '#':
            click(i+1, j-1)
        if j+1 < columns and display_plane[i+1][j+1] == '#':
            click(i+1, j+1)
    if j-1 >= 0 and display_plane[i][j-1] == '#':
        click(i, j-1)
    if j+1 < columns and display_plane[i][j+1] == '#':
        click(i, j+1)

rows, columns, mines = 9, 9, 10
plane = [[0 for _ in range(0, columns)] for __ in range(0, rows)]
display_plane = [['#' for _ in range(0, columns)] for __ in range(0, rows)]

mines_planted = 0
while mines_planted < mines:
    row = random.randint(0, rows - 1)
    column = random.randint(0, columns - 1)
    if plane[row][column] == 0:
        plane[row][column] = '*'
        mines_planted += 1

for i in range(0, rows):
    for j in range(0, columns):
        if plane[i][j] == '*':
            if i-1 >= 0:
                if plane[i-1][j] != '*':
                    plane[i-1][j] += 1
                if j-1 >= 0 and plane[i-1][j-1] != '*':
                    plane[i-1][j-1] += 1
                if j+1 < columns and plane[i-1][j+1] != '*':
                    plane[i-1][j+1] += 1
            if i+1 < rows:
                if plane[i+1][j] != '*':
                    plane[i+1][j] += 1
                if j-1 >= 0 and plane[i+1][j-1] != '*':
                    plane[i+1][j-1] += 1
                if j+1 < columns and plane[i+1][j+1] != '*':
                    plane[i+1][j+1] += 1
            if j-1 >= 0 and plane[i][j-1] != '*':
                plane[i][j-1] += 1
            if j+1 < columns and plane[i][j+1] != '*':
                plane[i][j+1] += 1

# print(plane.__str__().replace('],', '\n').replace("'", ''))

open = 0
while True:
    display()
    in_str = input('Click in [row column] format, flag and unflag in [f row column] format: ').strip(' ').split(' ')
    length = len(in_str)
    if length > 3 or length < 2 or (length == 3 and in_str[0] != 'f'):
        print('Wrong input')
        continue
    if length == 3:
        i, j = map(int, in_str[1:])
        if display_plane[i][j] != '#' and display_plane[i][j] != '?':
            print('Cant flag this cell.')
        elif display_plane[i][j] == '#':
            display_plane[i][j] = '?'
        else:
            display_plane[i][j] = '#'
    if length == 2:
        i, j = map(int, in_str)
        if display_plane[i][j] == '?':
            print('Cant click a flagged cell. Try unflagging.')
        elif display_plane[i][j] != '#':
            print('Cell already clicked.')
        elif plane[i][j] == '*':
            print('You lost!')
            break
        else: 
            click(i, j)
    if open == rows * columns - mines:
        display()
        print('You won!')
        break
