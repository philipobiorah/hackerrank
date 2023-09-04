def create_door_mat(rows, columns):
    # Calculate the center position
    center = columns // 2

    for i in range(rows):
        if i < rows // 2:
            # Top part of the door mat
            pattern = ".|." * (2 * i + 1)
        elif i == rows // 2:
            # Center line with 'WELCOME'
            pattern = "WELCOME"
        else:
            # Bottom part of the door mat (mirror of the top part)
            pattern = ".|." * (2 * (rows - i) - 1)
        
        # Calculate the padding on each side
        padding = (columns - len(pattern)) // 2
        
        # Print the line with padding
        print('-' * padding + pattern + '-' * padding)

if __name__ == "__main__":
    n, m = map(int, input("Enter size (N x M): ").split())
    create_door_mat(n, m)
