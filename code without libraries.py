nc, dc, tc = {}, {}, {} #Создание переменных

with open('example.fasta') as f: # открытие файла
    while (a := f.readline().strip()):
        b = f.readline().strip() #Чтение строк файла
        f.readline(), f.readline()      

        for n in b: #Подсчет нуклеотидов
            nc[n] = nc.get(n, 0) + 1
        
        for i in range(len(b)-1): #Подсчет дуниклеотидов
            dc[b[i:i+2]] = dc.get(b[i:i+2], 0) + 1
        
        for i in range(len(b)-2): #Подсчет тринуклеотиды
            tc[b[i:i+3]] = tc.get(b[i:i+3], 0) + 1

for title, counts in [("Нуклеотиды", nc), ("Динуклеотиды", dc), ("Тринуклеотиды", tc)]: #Вывод текста
    print(f"\n{title}:")
    for k in sorted(counts):
        print(f"{k}: {counts[k]}")
