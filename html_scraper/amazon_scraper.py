from datetime import datetime
import requests
import csv
import bs4


if __name__ == "__main__":
   with open('product_amazon.csv', newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        for row in reader:
            url = row[0]
            print(url)