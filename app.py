# app.py

from flask import Flask, render_template, request, jsonify
from tic_tac_toe import TicTacToe

app = Flask(__name__)
game = TicTacToe()
mode = None  # To store current game mode ('computer' or 'two-players')

@app.route('/')
def redirect_home():
    return render_template('home.html')

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/game')
def game_page():
    return render_template('index.html')

@app.route('/move', methods=['POST'])
def move():
    global mode
    position = int(request.form['position'])
    
    if position != -1:  # If position is not -1, it's a player's move
        if game.make_move(position):
            winner = game.check_winner()
            if winner:
                return jsonify({'board': game.board, 'winner': winner, 'current_player': game.current_player})

    if mode == 'computer' and game.current_player == 'O':  # Computer's turn
        game.ai_move()  # Make AI move using minimax algorithm
        winner = game.check_winner()
        if winner:
            return jsonify({'board': game.board, 'winner': winner, 'current_player': game.current_player})

    return jsonify({'board': game.board, 'current_player': game.current_player})

@app.route('/reset', methods=['POST'])
def reset():
    global mode
    game.reset_board()
    mode = None
    return jsonify({'board': game.board, 'current_player': game.current_player})

@app.route('/mode', methods=['POST'])
def set_mode():
    global mode
    mode = request.form['mode']
    game.reset_board()  # Reset board when mode changes

    if mode == 'computer' and game.current_player == 'O':  # Computer starts if mode is 'computer'
        game.ai_move()

    return jsonify({'mode': mode, 'board': game.board, 'current_player': game.current_player})

if __name__ == '__main__':
    app.run(debug=True)
