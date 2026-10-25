def calculate_marks():
    mark1 = float(input("Enter Tamil marks: "))
    mark2 = float(input("Enter English marks: "))
    mark3 = float(input("Enter Maths marks: "))
    mark4 = float(input("Enter Science marks: "))
    mark5 = float(input("Enter Social Science marks: "))

    total = mark1 + mark2 + mark3 + mark4 + mark5
    average = total / 5

    print("\n----- MARKS REPORT -----")
    print("Tamil:", mark1)
    print("English:", mark2)
    print("Maths:", mark3)
    print("Science:", mark4)
    print("Social Science:", mark5)
    print("Total Marks (TOT):", total)
    print("Average Marks (AVG):", average)

    if __name__ == "__main__":
        calculate_marks()