
with open("game_stat.txt", "r") as i:
    print(i)
    k = []
    for line in i:
        lines = line.split('\n')
        pr = lines[0].split('\t')
        k.append(pr)
        print(k)
    for l in k:
        print(l[0], '|', l[1], '|', l[2], '|', l[3], '|', l[4], end="*\n")
        # for m in l:
        #print(m, end=" | ")
        print()
