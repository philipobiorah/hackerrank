import math


def create_door_mat(rows, columns):
    #Calculate the center position 
    center = columns // 2

    for i in range (rows):
        if i < rows // 2:
            #Top poart of the door mat
            patten = ".|." *(2 * i + 1)
        elif i == rows // 2:
            #Center line with  'WELCOME'
            patten = "WELCOME"

        else:
            # Botom part of the door mat(mirror of the top part)
            patten = ".|." * (2 * (rows - 1) - 1)

        #Calculate the padding on each side
        padding = (columns - len(patten)) // 2

        #Print the line with padding
        print('-' * padding + patten + '-' * padding)


if __name__ == "__main__":
    n, m = map(int, input("Enter size (N * M): ").split())
    create_door_mat(n,m)
    