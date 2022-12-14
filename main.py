from itertools import combinations
import csv
import time

start_time = time.time()


def main():
    stocks_list = read_csv()

    print(f"\nProcessing {len(stocks_list)} shares:")

    best_combo = set_combos(stocks_list)

    print(best_combo)
    print(time.time() - start_time, "seconds")


def read_csv():
    with open("data/test.csv") as csvfile:
        stocks_file = csv.reader(csvfile, delimiter=',')

        stocks = []
        for row in stocks_file:
            stocks.append(
                (row[0], float(row[1]), float(row[2]))
            )
        return stocks


def set_combos(stocks_list):
    profit = 0
    best_combo = []
    best_cost = 0

    for i in range(len(stocks_list)):
        combos = combinations(stocks_list, i + 1)

        for combo in combos:
            total_cost = sum([stock[1] for stock in combo])

            if total_cost <= 500:
                total_profit = sum([stock[1] * stock[2] / 100 for stock in combo])

                if total_profit > profit:
                    profit = total_profit
                    best_combo = combo
                    best_cost = total_cost

    return best_combo, profit, best_cost


main()