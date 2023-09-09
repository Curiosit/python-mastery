with open('portfolio.dat','r') as f:
    total = 0
    for line in f:
        print(line)
        stock = line.split()
        print(stock)
        partialresult = int(stock[1]) * float(stock[2])
        print(partialresult)
        total += partialresult
    print("Total:")
    print(total)