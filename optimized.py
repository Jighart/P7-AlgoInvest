import csv
import time

start_time = time.time()


def optimized(file):
    stocks_list = read_csv(file)

    print(f"\nProcessing {len(stocks_list)} stocks:")

    best_combo = get_combos(stocks_list)

    print(best_combo)
    print(round(time.time() - start_time, 2), "seconds elapsed")


def read_csv(file):
    with open("data/" + file) as csvfile:
        stocks = []
        stocks_file = csv.reader(csvfile, delimiter=',')

        for row in stocks_file:
            if row[0] == "name" or float(row[1]) <= 0 or float(row[2]) <= 0:
                pass
            else:
                stock = (
                    row[0],
                    int(float(row[1]) * 100),
                    float(row[2])
                )
                stocks.append(stock)
        return stocks


def get_combos(stocks_list):
    cost = []
    profit = []
    best_combo = []
    stocks = len(stocks_list)
    available_money = int(500 * 100)

    for stock in stocks_list:
        cost.append(stock[1])
        profit.append(stock[1] * stock[2] / 100)

    table = [[0 for x in range(available_money + 1)] for x in range(stocks + 1)]

    for i in range(1, stocks + 1):
        for w in range(1, available_money + 1):
            if cost[i - 1] <= w:
                table[i][w] = max(profit[i - 1] + table[i - 1][w - cost[i - 1]], table[i - 1][w])
            else:
                table[i][w] = table[i - 1][w]

    while available_money >= 0 and stocks >= 0:

        if table[stocks][available_money] == \
                table[stocks-1][available_money - cost[stocks-1]] + profit[stocks-1]:

            best_combo.append(stocks_list[stocks-1])
            available_money -= cost[stocks-1]

        stocks -= 1

    return best_combo
