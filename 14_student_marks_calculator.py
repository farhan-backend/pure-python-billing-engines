class MarksCalculator:

    def __init__(self, marathi, english, hindi, maths, science, social_science):
        self.marathi = marathi
        self.english = english
        self.hindi = hindi
        self.maths = maths
        self.science = science
        self.social_science = social_science
        self.total_marks = 600

    def calculate_total(self):
        return self.marathi + self.english + self.hindi + self.maths + self.science + self.social_science

    def calculate_percentage(self):
        return (self.calculate_total() / self.total_marks) * 100

    def get_result(self):
        percentage = self.calculate_percentage()
        total = self.calculate_total()

        print(f"\nTotal obtained marks = {total}")
        print(f"Total percentage = {percentage:.2f}%\n")

        if percentage >= 95:
            print("Grade = A+\nRemark = Perfect!\nStatus = You are promoted")
            
        elif percentage >= 90:
            print("Grade = A\nRemark = Excellent!\nStatus = You are promoted")
            
        elif percentage >= 80:
            print("Grade = B\nRemark = Very Good\nStatus = You are promoted")

        elif percentage >= 70:
            print("Grade = C\nRemark = Good\nStatus = You are promoted")

        elif percentage >= 50:
            print("Grade = D\nRemark = Bad, Need to improve\nStatus = You are promoted")

        elif percentage >= 35:
            print("Grade = E\nRemark = Very bad, Need to improve\nStatus = You are promoted")

        else:
            print("You are Failed\nStatus = You are detained")


# Driver code
while True:

    print("------------Marks Calculator------------")

    m = float(input("\nEnter marks obtained in Marathi: "))
    e = float(input("Enter marks obtained in English: "))
    h = float(input("Enter marks obtained in Hindi: "))
    ma = float(input("Enter marks obtained in Maths: "))
    sc = float(input("Enter marks obtained in Science: "))
    ss = float(input("Enter marks obtained in Social_Science: "))

    calc = MarksCalculator(m, e, h, ma, sc, ss)
    calc.get_result()

    print("\nDone")
    
    cont = input("Do you want to calculate for another student? (y/n): ").lower()
    if cont != 'y':
        break

 
