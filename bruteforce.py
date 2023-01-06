from itertools import combinations
import csv
import time


def bruteforce(file):
    start_time = time.time()
    stocks_list = read_csv(file)

    print(f"\nProcessing {len(stocks_list)} stocks:")

    best_combo = get_combos(stocks_list)

    print(f"Best option selected: {len(best_combo[0])} stocks\n")
    for stock in best_combo[0]: print(f"{stock[0]}, ", end='')
    print(f"\n\nTotal cost: {best_combo[2] / 100}€")
    print(f"Total profit: {round(best_combo[1], 2)}€")
    print("Time spent:", round(time.time() - start_time, 2), "seconds")


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
    profit = 0
    best_combo = []
    best_cost = 0

    for i in range(len(stocks_list)):
        combos = combinations(stocks_list, i + 1)

        for combo in combos:
            total_cost = sum([stock[1] for stock in combo])

            if total_cost <= 50000:
                total_profit = sum([stock[1] * stock[2] / 10000 for stock in combo])

                if total_profit > profit:
                    profit = total_profit
                    best_combo = combo
                    best_cost = total_cost

    return best_combo, profit, best_cost
