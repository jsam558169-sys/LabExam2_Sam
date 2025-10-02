from abc import ABC, abstractmethod

# report class
class Report(ABC):
    @abstractmethod
    def generate(self):
        pass

# gradeReport class
class gradeReport(Report):
    def __init__(self):

        # encapsulation
        self.__grades = []

    def add_grade(self, grade):
        if grade == -1:
            return False
        elif 0 <= grade <= 100:
            self.__grades.append(grade)
            return True
        else:
            print("Invalid grade!! Must be between 0 and 100.")
            return True

    def generate(self):
        if not self.__grades:
            return "No grades entered."

        avg = sum(self.__grades) / len(self.__grades)
        point = ((100 - avg) + 10) / 10

        # determine remarks based on average
        if avg < 0:
            remarks = "No such grade"
            point = 0.00
        elif avg < 50:
            remarks = "No such grade"
            point = 9.00
        elif avg < 75:
            remarks = "Dropped"
            point = 5.00
        elif avg < 80:
            remarks = "Failed"
        elif avg < 85:
            remarks = "Passed – Satisfactory"
        elif avg < 90:
            remarks = "Passed – Good"
        elif avg < 100:
            remarks = "Passed – Average"
        elif avg == 100:
            remarks = "Passed – Very Good"
        else:
            remarks = "Passed – Excellent (Out of range or Invalid)"

        return {
            "Average": round(avg, 2),
            "Point Grade": round(point, 2),
            "Remarks": remarks
        }

# main menu
if __name__ == "__main__":
    report = gradeReport()

    while True:
        try:
            grade = int(input("Input Grade: "))
            if not report.add_grade(grade):
                break
        except ValueError:
            print("Please enter a valid value.")

    result = report.generate()
    if isinstance(result, dict):
        for key, value in result.items():
            print(f"{key}: {value}")
    else:
        print(result)