def draw_rectangle():
    # Assign the width and height values using input()
    width = int(input("Enter the width of the rectangle: "))
    height = int(input("Enter the height of the rectangle: "))

    # Draw the rectangle
    print("|" + "-" * (width - 2) + "|")
    for i in range(height - 2):
        print("|" + " " * (width - 2) + "|")
    print("|" + "-" * (width - 2) + "|")

# Call the draw_rectangle() function to create a rectangle
draw_rectangle()
