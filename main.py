import csv
import numpy as np
def cal_avg(total):
    average = total/3
    return average
def display_result (name,total,average):
    print("Name:",name)
    print("Total Marks:",total)
    print("Average marks:",average)
def cal_stats(math_array,science_array,english_array):
    print("\nMaths Statistics")
    print("Class Maths Average:",np.mean(math_array))
    print("Standard deviation Maths:",np.std(math_array))
    print("Maths Range:",np.max(math_array)-np.min(math_array))
    print("Highest Maths Marks:",max(math_array))
    print("Lowest Maths Marks:",min(math_array))
    print("\nScience Statistics")
    print("Class Science Average:",np.mean(science_array))
    print("Standard deviation Science:",np.std(science_array))
    print("science Range:",np.max(science_array)-np.min(science_array))
    print("Highest Science Marks:",max(science_array))
    print("Lowest Science Marks:",min(science_array))
    print("\nEnglish Statistics")
    print("Class English Average:",np.mean(english_array))
    print("Standard deviation English:",np.std(english_array))
    print("English Range:",np.max(english_array)-np.min(english_array))
    print("Highest English Marks:",max(english_array))
    print("Lowest English Marks:",min(english_array))
def analyze_students():
    file = open("students.csv","r")
    data = csv.reader(file)
    math_marks=[]
    science_marks=[]
    english_marks=[]    
    for row in data :
        if row[0]=="Name":
            continue

        Maths = int(row[-3])
        Science = int(row[-2])
        English = int(row[-1])
        math_marks.append(Maths)
        science_marks.append(Science)
        english_marks.append(English)
        total=Maths+Science+English
        average=cal_avg(total)
        display_result(row[0],total,average)

    file.close()
    math_array=np.array(math_marks)
    science_array=np.array(science_marks)
    english_array=np.array(english_marks)
    cal_stats(math_array,science_array,english_array)
def main():
    analyze_students()
main()



