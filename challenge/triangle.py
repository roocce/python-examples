"""kiwigamerromania's challenge

    Draw a triangle based on a given number,
    e.g. 3 in the form:
       1
      1 2
     1 2 3
"""

def draw_triangle_of_height(n):
    try:
        if n > 9:
            raise ValueError("Enter a number smaller than 9.")
        if n < 1:
            raise ValueError("Enter a number greater than 0.")
    except ValueError as err:
        print("Invalid number: "+ str(n))
        print(err)
    else:
        for row in range(1, n+1):
            data = list(range(1,row+1))
            text = ""
            for col in data:
                text = text + str(col)
                if col < len(data):
                    text = text + " "
            print(len(text))
            print(text.center(n*2))


if __name__ == "__main__":
    import sys
    draw_triangle_of_height(int(sys.argv[1]))
