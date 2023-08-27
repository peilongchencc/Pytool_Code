with open("test.txt", "r") as file:
    lines = file.readlines()
    print(lines)
    for line in lines:
        print(line, end='')  # end=空，用来避免重复的换行