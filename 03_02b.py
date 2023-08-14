import csv
from collections import namedtuple

def main():
    #add code here
    #read data/Customer.csv
    with open("data/Customer.csv", "r") as customers:
        csv_reader = csv.reader(customers, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                Customer = namedtuple("Customer", ",".join(row))
            else:
                customer = Customer(*row)
                print(customer)
            line_count += 1
    #Create workable objects with each line
    
    return

if __name__ == "__main__":
    main()