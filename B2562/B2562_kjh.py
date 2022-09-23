l = list(map(int, open(0)))
print(f'{max(l)}\n{l.index(max(l))+1}')