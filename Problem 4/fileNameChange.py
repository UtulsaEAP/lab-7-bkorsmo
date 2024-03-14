''' Name: Brady Korsmo
    Date: Thursday @2 '''


def fileNameChange():
    #type your code here
    file = input()


    output = []
    with open(file,'r') as z:
        for line in z :
            filename = line.strip()
            if 'photo.jpg' in filename:
                new = filename.replace('photo.jpg', 'info.txt')
                output.append(new)
            else:
                new = filename
                output.append(new)

    for file_name in output:
        print(file_name)

if __name__ == '__main__':
    fileNameChange()