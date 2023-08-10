from collections import deque

def main():
    #add code here
    foods = deque(maxlen=5)
    foods.append("STA001")
    ordered_foods = ["DES001", "ENT001", "ENT003", "STA004"]
    foods.extend(ordered_foods)
    foods.append("DES009")
    print(foods)
    return

if __name__ == "__main__":
    main()