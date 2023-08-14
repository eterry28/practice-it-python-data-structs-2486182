from collections import namedtuple

def can_take_order(driver, num_packages):
    return driver.car_capacity >= num_packages

def main():
    #add code here
    #create a driver with a name, car type, and car capacity
    Driver = namedtuple("driver", ["name", "car_type", "car_capacity"])
    #an example you can use to practice: "Iris", "Toyota Prius", 7
    iris = Driver("Iris", "Prius", 7)
    mickey = Driver("Micky", "Tucson", 15)
    woody = Driver("Woody", "Hummer", 26)
    #check if they can take a certain order, given their car's capacity.
    print(can_take_order(woody, 3))
    print(can_take_order(mickey, 20))
    print(can_take_order(iris, 10))
    return

if __name__ == "__main__":
    main()