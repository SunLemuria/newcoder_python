# 应该用trie树再实现一遍,偷懒调用API


while True:
    try:
        n = int(input())
        words = [input() for i in range(n)]
        for w in sorted(words):
            print(w)
    except:
        break