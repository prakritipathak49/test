def guess_weight(age, height):
    # A simple formula to guess weight
    weight = (height - 100 + age / 10) * 0.9
    return weight

def main():
    age = int(input("Enter your age: "))
    height = float(input("Enter your height in cm: "))
    
    weight = guess_weight(age, height)
    print(f"Based on your age and height, your guessed weight is: {weight:.2f} kg")

if __name__ == "__main__":
    main()
