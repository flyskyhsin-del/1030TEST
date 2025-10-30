import random
import time

WORDS = [
    'apple', 'banana', 'cherry', 'dog', 'elephant', 'frog', 'grape', 'house', 'island', 'jungle',
    'king', 'lemon', 'monkey', 'notebook', 'orange', 'pencil', 'queen', 'rabbit', 'sun', 'tree',
    'umbrella', 'violin', 'water', 'xylophone', 'yogurt', 'zebra'
]

ROUND = 5  # 題數可依需求修改

print("歡迎來到英打小遊戲！共{}題，請盡快並正確輸入出現的英文單字。".format(ROUND))
input("按下 Enter 開始...\n")

total_time = 0
for i in range(1, ROUND + 1):
    word = random.choice(WORDS)
    print(f"第{i}題. 請輸入：{word}")
    start = time.time()
    while True:
        answer = input('> ')
        if answer == word:
            elapsed = time.time() - start
            print(f"正確！用時：{elapsed:.2f} 秒\n")
            total_time += elapsed
            break
        else:
            print("錯誤，請再試一次！")

avg_time = total_time / ROUND
print(f"遊戲結束！平均每題用時：{avg_time:.2f} 秒")
