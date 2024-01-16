from flask import Flask, render_template
from flask_socketio import SocketIO, emit
from flask_cors import CORS
from ConnectFourBoard import ConnectFourBoard
from Play import Play

app = Flask(__name__)
# socketio = SocketIO(app)
CORS(app)
socketio = SocketIO(app, cors_allowed_origins="*")

games = {}

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('connect')
def handle_connect():
    print('Client connected')

@socketio.on('disconnect')
def handle_disconnect():
    print('Client disconnected')

@socketio.on('start_game')
def handle_start_game(data):
    game_id = str(data['game_id'])
    games[game_id] = ConnectFourBoard()
    print("Game started! Game ID: " + game_id)
    # emit('update_board', {'board': games[game_id].board})



@socketio.on('human_turn1')
def human_turn1(data):
    game_id = str(data['game_id'])
    board = games[game_id]
    column = data['column']['columnIndex']
    player = data['player']
    print("player" + str(player))
    if column in board.getPossibleMoves():
        for i in range(5, -1, -1):
            if board.board[i][column] == 0:
                board.makeMove(i, column, player)
                break
        emit('update_board', {'board': board.board, 'player': player})
        print("updatd board" + str(board.board))
        # emit('ai1_turn', {'game_id': game_id})
        #check if the game is over
        check_game_over(board)

    else:
        emit('invalid_column', {'game_id': game_id})
    
# Computer's turn
@socketio.on('ai1_turn')
def ai1_turn(data):
    print("computer playing")
    game_id = str(data['game_id'])
    player = data['player']
    print("Game id : " + game_id)
    board = games[game_id]
    play = Play(board)
    column = play.AIbot1()
    for i in range(5, -1, -1):
        if board.board[i][column] == 0:
            board.makeMove(i, column, player)
            break
    emit('update_board', {'board': board.board, 'player': player})
    check_game_over(board)


# Computer's turn
@socketio.on('ai2_turn')
def ai2_turn(data):
    print("computer playing")
    game_id = str(data['game_id'])
    player = data['player']
    print("Game id : " + game_id)
    board = games[game_id]
    play = Play(board)
    column = play.AIbot2()
    for i in range(5, -1, -1):
        if board.board[i][column] == 0:
            board.makeMove(i, column, 2)
            break
    emit('update_board', {'board': board.board, 'player': player})
    check_game_over(board)

def check_game_over(board):
    if board.gameOver():
        print("Game over!")
        winner = 1 if board.win(1) else 2 if board.win(2) else 0
        emit('game_over', {'winner': winner})
        emit('disconnect')




if __name__ == '__main__':
    socketio.run(app, debug=True)