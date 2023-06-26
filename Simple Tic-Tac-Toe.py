def print_board(rows):
    print('-' * 9)
    for row in rows:
        print("| " + " ".join(row) + " |")
    print('-' * 9)


def check_winner(rows):
    winning_combinations = [
                               # Rows
                               [rows[i][0], rows[i][1], rows[i][2]] for i in range(len(rows))] + [
                               # Columns
                               [rows[0][i], rows[1][i], rows[2][i]] for i in range(len(rows))] + [
                               # Diagonals
                               [rows[0][0], rows[1][1], rows[2][2]],
                               [rows[0][2], rows[1][1], rows[2][0]]
                           ]
    for combination in winning_combinations:
        if combination == ['X', 'X', 'X']:
            return 'X'
        elif combination == ['O', 'O', 'O']:
            return 'O'
    if all(cell != ' ' for row in rows for cell in row):
        return 'Draw'
    return None


inputs = [' '] * 9
rows = [inputs[i:i + 3] for i in range(0, len(inputs), 3)]

print_board(rows)

element = 0

while ' ' in inputs:
    try:
        a, b = map(int, input("Enter the coordinates: ").split())
        if a not in [1, 2, 3] or b not in [1, 2, 3]:
            print("Coordinates should be from 1 to 3!")
            continue
    except ValueError:
        print("You should enter numbers!")
        continue

    cell = 3 * (a - 1) + (b - 1)

    if inputs[cell] != ' ':
        print("This cell is occupied! Choose another one!")
        continue

    if element == 0:
        marker = 'X'
        element = 1
    else:
        marker = 'O'
        element = 0

    inputs[cell] = marker
    rows[a - 1][b - 1] = marker

    print_board(rows)

    winner = check_winner(rows)
    if winner:
        print(winner + " wins")
        break

if not winner:
    print("Draw")
