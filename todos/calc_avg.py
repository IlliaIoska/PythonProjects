def calc_avg_from_file():
    with open("nums.txt", "r") as file:
        file_contents = [int(i) for i in file.read().split(" ")]
        sum = 0
        for i in file_contents:
            sum += i
        print(sum)
        print(len(file_contents))
        avg = sum / len(file_contents)
        return avg


print(calc_avg_from_file())
