global board


def new_board():
    return [
        ['-', '-', '-'],
        ['-', '-', '-'],
        ['-', '-', '-']
    ]


def print_board(message='', new_line=True):
    pad_screen()
    output = "╭───────╮\n"
    for row in board:
        output += "│ "
        for val in row:
            output += val + ' '
        output += '│\n'
    output += "╰───────╯"
    output += str('\n' + message) if message != '' else ''
    print(output, end='\n' if new_line else '')


def pad_screen():
    i = 0
    while i < 100:
        print()
        i += 1


def main():
    global board
    board = new_board()
    print_board(turn_loop())


def turn_loop():
    # TODO True will be replaced with a function that checks for a winner, which will break the loop.
    is_player1 = True
    message = ''
    while True:
        print_board(message +
                    ('\n' if message != '' else '') +
                    "[ " + ("X" if is_player1 else "O") +
                    " ] Select your next move")

        message = mark_board(input("ROW COLUMN | "), 'X' if is_player1 else 'O')

        if message == 'X Wins' or message == 'O Wins':
            return message
        elif message == '':
            is_player1 = not is_player1


def mark_board(coords_string, player):
    try:
        vals = coords_string.replace(',', '').split(' ')
        row = int(vals[0])
        col = int(vals[1])

        if not 0 < row * col < 10:
            raise ValueError

        if board[row - 1][col - 1] != '-':
            return ("----------------------------------------------------\n" +
                    "  I'm sorry, that space is already taken!\n" +
                    "  Please select an empty space to place your mark.\n" +
                    "----------------------------------------------------\n")

        board[row - 1][col - 1] = player
        return check_winner()
    except ValueError:
        return ("====================================================\n" +
                "  I'm sorry, I didn't recognize your input!\n" +
                "  Please specify a number 1-3 for the ROW and COLUMN\n" +
                "====================================================\n")


def check_winner():
    win_string = ('|' + board[0][0] + board[0][1] + board[0][2] + '|' +
                  '|' + board[1][0] + board[1][1] + board[1][2] + '|' +
                  '|' + board[2][0] + board[2][1] + board[2][2] + '|' +
                  '|' + board[0][0] + board[1][0] + board[2][0] + '|' +
                  '|' + board[0][1] + board[1][1] + board[2][1] + '|' +
                  '|' + board[0][2] + board[1][2] + board[2][2] + '|' +
                  '|' + board[0][0] + board[1][1] + board[2][2] + '|' +
                  '|' + board[2][0] + board[1][1] + board[0][2] + '|')

    try:
        if win_string.index('|XXX|') > -1:
            return "X Wins"
    except ValueError:
        try:
            if win_string.index("|OOO|") > -1:
                return "O Wins"
        except ValueError:
            return ''


main()
