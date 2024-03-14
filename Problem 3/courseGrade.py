''' Name: Brady Korsmo
    Date: Thursday @2 '''


def courseGrade():
    
    # TODO: Declare any necessary variables here. 
    filename = input()

      
    # TODO: Read a file name from the user and read the tsv file here. 
    file_names = ["StudentInfo.tsv", "StudentInfo1.tsv", "StudentInfo2.tsv"]

    for i, file_name in enumerate(file_names, start=1):
        with open(file_name, 'r') as file:
            lines = file.readlines()

    lastname = []
    firstname = []
    midterm1 = []
    midterm2 = []
    final = []

    for line in lines:
        columns = line.strip().split('\t')
        lastname.append(columns[0])
        firstname.append(columns[1])
        midterm1.append(float(columns[2]))
        midterm2.append(float(columns[3]))
        final.append(float(columns[4]))

    # TODO: Compute student grades and exam averages, then output results to a text file here. 
    
    average = []
    grade = []

    for j in range(len(lastname)):
        averagescore = (midterm1[j]+midterm2[j]+final[j])/3
        average.append(averagescore)
        if averagescore >=90:
            letter = 'A'
        elif 80 <= averagescore < 90:
            letter = "B"
        elif 70 <= averagescore < 80:
            letter = 'C'
        elif 60 <= averagescore <70:
            letter = 'D'
        else:
            letter = "F"
        grade.append(letter)
    
    avgmidterm1 = sum(midterm1)/len(midterm1)
    avgmidterm2 = sum(midterm2)/len(midterm2)
    avgfinal = sum(final)/len(final)
    
    with open(f'report{i}.txt', 'w') as report_file:
        for j in range(len(lastname)):
            report_file.write(f"{lastname[j]}\t{firstname[j]}\t{midterm1[j]}\t{midterm2[j]}\t{final[j]}\t{grade[j]}\n")

        report_file.write(f"\nAverages: midterm1 {avgmidterm1:.2f}, midterm2 {avgmidterm2:.2f}, final {avgfinal:.2f}\n")


if __name__ == "__main__":
    courseGrade()
    
    