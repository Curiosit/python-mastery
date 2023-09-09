def portfolio_cost(filename):
    total = 0
    with open(filename,'r') as f:
        
        for line in f:
            print(line)
            stock = line.split()
            print(stock)
            try:
                partialresult = int(stock[1]) * float(stock[2])
            except:
                print("An exception has occured")
            print(partialresult)
            total += partialresult
        print("Total:")
        print(total)
    return total
    
if __name__ == '__main__':
    print(portfolio_cost('portfolio3.dat'))