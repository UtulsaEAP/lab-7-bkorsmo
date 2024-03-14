''' Name: Brady Korsmo
    Date: Thursday @2 '''


def wordInRange():
    #Type your code here
    file_name = input()
    lower_bound = input()
    upper_bound = input()

    with open(file_name, 'r') as file:
        readit = file.readlines()

    new = [line.strip() for line in readit]
    print(new)

    for string in new:
        if lower_bound <= string <= upper_bound :
            print(f"{string} - in range.")
        else:
            print(f"{string} - not in range.")

if __name__ == '__main__':
    wordInRange()