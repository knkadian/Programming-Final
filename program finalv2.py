#Source of reference: Sam, official python website

import math
#different variable types


t=True
class Star():
    def __init__(self, x, y, name):
        self.x = x
        self.y = y
        self.name = name

    def distance(self, otherStar):
        return math.sqrt((otherStar.x - self.x)**2 + (otherStar.y - self.y)**2)

def main():
    stars = []  # Initialize array to store

    # Input loop
    for i in range(2):
        starName=input(f"Enter the name of star {i+1}:")
        while t:
            try:
                x = float(input(f"Enter the x-coordinate of star {i+1}: "))
                y = float(input(f"Enter the y-coordinate of star {i+1}: "))
                
                break  # Exit the loop
            except ValueError:
                print("Invalid input. ENTER NUMBERS!?!?!?")
        stars.append(Star(x, y, starName))

    # Unpack

    star1 = stars[0]
    star2 = stars[1]

    # Calculate distance
    calc_distance = star1.distance(star2)

    # Display the result
    print(f"{calc_distance} is the distance between", star1.name, ",", star2.name)


#displaying the array

#Calling function main
if __name__ == "__main__":
    main()