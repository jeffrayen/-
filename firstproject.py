#剪刀石頭布互動遊戲,需要有計分板,詢問玩家是否繼續下去,需顯示玩家和電腦出什麼
import random

print("歡迎來到剪刀石頭布！ ")
name = input("請輸入您的名稱：")
fair_game = 0
youwin = 0
comwin = 0
player_list = ["剪刀", "石頭", "布"]    
computer_list = ["剪刀", "石頭", "布"]

while youwin < 2 and comwin < 2:
    while True:
        computer_hand = random.randint(0,2) #隨機產生整數
        player_hand = int(input(("請出拳： (0) 剪刀 (1) 石頭 (2) 布：")))
        if player_hand in [0, 1, 2]:
            break
        else:
            print("輸入錯誤,在輸入一次")
            continue

    if (player_hand == computer_hand) : #平手條件
        print("平手", name , player_list[player_hand],"電腦出" + computer_list[computer_hand])
        fair_game = fair_game + 1
    elif (player_hand - computer_hand) == 1 or (player_hand - computer_hand) == -2 : #玩家獲勝條件
        print("你贏了這把", name + "出" + player_list[player_hand],"電腦出" + computer_list[computer_hand])
        youwin = youwin + 1
        if youwin == 2:
            break
    else: #(computer_hand - player_hand) == 1 or (computer_hand - player_hand) == -2 : 玩家獲勝條件以外就是電腦獲勝條件
        print("電腦贏了這把",name + "出" + player_list[player_hand],"電腦出" + computer_list[computer_hand])
        comwin = comwin + 1
        if comwin == 2:
            break


print(name + "贏了" + str(youwin) + "把")
print("電腦贏了" + str(comwin) + "把")
print("平手" + str(fair_game) + "把")

if youwin == 2:
    print(name + " win this game")
if comwin == 2:
    print("computer win this game") 

def paperscissorsstonegame():
    import random
    print("歡迎來到剪刀石頭布！ ")
    name = input("請輸入您的名稱：")
    fair_game = 0
    youwin = 0
    comwin = 0
    player_list = ["剪刀", "石頭", "布"]    
    computer_list = ["剪刀", "石頭", "布"]

    while youwin < 2 and comwin < 2:
        while True:
            computer_hand = random.randint(0,2) #隨機產生整數
            player_hand = int(input(("請出拳： (0) 剪刀 (1) 石頭 (2) 布：")))
            if player_hand in [0, 1, 2]:
                break
            else:
                print("輸入錯誤,在輸入一次")
                continue

        if (player_hand == computer_hand) : #平手條件
            print("平手", name + "出" + player_list[player_hand],"電腦出" + computer_list[computer_hand])
            fair_game = fair_game + 1
        elif (player_hand - computer_hand) == 1 or (player_hand - computer_hand) == -2 : #玩家獲勝條件
            print("你贏了這把", name + "出" + player_list[player_hand],"電腦出" + computer_list[computer_hand])
            youwin = youwin + 1
            if youwin == 2:
                break
        else: #(computer_hand - player_hand) == 1 or (computer_hand - player_hand) == -2 : 玩家獲勝條件以外就是電腦獲勝條件
            print("電腦贏了這把",name + "出" + player_list[player_hand],"電腦出" + computer_list[computer_hand])
            comwin = comwin + 1
            if comwin == 2:
                break

    print(name + "贏了" + str(youwin) + "把")
    print("電腦贏了" + str(comwin) + "把")
    print("平手" + str(fair_game) + "把")

    if youwin == 2:
        print(name + " win this game")
    if comwin == 2:
        print("computer win this game")

    
while (1) :
    game_again = input('是否要重新開始新的一局？(y/n)')
    if game_again == "n":
        break 
    elif game_again == "y":
        print("開始新的一局！")
        paperscissorsstonegame()
    else:
        break
