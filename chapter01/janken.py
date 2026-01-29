import random, sys

print('ROCK, PAPER, SCISSORS')

# 勝ち、負け、引き分けの数を記録する
wins = 0
losses = 0
ties = 0

while True:  # メインのゲームループ
    print(str(wins) + ' Wins, ' + str(losses) + ' Losses, ' + str(ties) + ' Ties')

    # プレイヤーの入力ループ
    while True:
        print('Enter your move: (r)ock (p)aper (s)cissors or (q)uit')
        player_move = input()

        if player_move == 'q':
            sys.exit()  # プログラム終了

        if player_move in ('r', 'p', 's'):
            break  # 正しい入力 → ループ抜ける

        print('Type one of r, p, s, or q.')

    # プレイヤーの手を表示
    if player_move == 'r':
        print('ROCK versus...')
    elif player_move == 'p':
        print('PAPER versus...')
    elif player_move == 's':
        print('SCISSORS versus...')

    # コンピュータの手を作る
    random_number = random.randint(1, 3)
    if random_number == 1:
        computer_move = 'r'
        print('ROCK')
    elif random_number == 2:
        computer_move = 'p'
        print('PAPER')
    else:
        computer_move = 's'
        print('SCISSORS')

    # 勝敗を判定する
    if player_move == computer_move:
        print('It is a tie!')
        ties += 1

    elif player_move == 'r' and computer_move == 's':
        print('You win!')
        wins += 1
    elif player_move == 'p' and computer_move == 'r':
        print('You win!')
        wins += 1
    elif player_move == 's' and computer_move == 'p':
        print('You win!')
        wins += 1

    elif player_move == 'r' and computer_move == 'p':
        print('You lose!')
        losses += 1
    elif player_move == 'p' and computer_move == 's':
        print('You lose!')
        losses += 1
    elif player_move == 's' and computer_move == 'r':
        print('You lose!')
        losses += 1
