def draw_triangle():
    # Assign the height values using input()
    height = int(input("Enter the height of the triangle : "))
    
    # Draws the first row with spaces and a backslash
    print(" " * (height - 1) + "/" + " " * (height - 4) + "\\")

    # Draws the middle rows with spaces, forward slashes, underscores, and backslashes
    for i in range(height - 2):
        print(" " * (height - i - 2) + "/" + "  " * (2 * i) + "\\")
        
    # Draws the last row with underscores and forward slashes and backslashes
    print("/" + "_" * (2 * height - 2) + "\\")

draw_triangle()