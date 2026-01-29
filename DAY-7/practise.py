class StudentInfo:
    def __init__(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no

    def display_info(self):
        print(f"Name    : {self.name}")
        print(f"Roll No : {self.roll_no}")


class AcademicMarks:
    def __init__(self, start, mid, end):
        try:
            if start < 0 or mid < 0 or end < 0:
                raise ValueError("Academic marks cannot be negative")

            self.start = start
            self.mid = mid
            
            self.end = end

        except ValueError as e:
            print("Academic Marks Error:", e)
            self.start = self.mid = self.end = 0

    def display_academics(self):
        print("Start Exam :", self.start)
        print("Mid Exam   :", self.mid)
        print("End Exam   :", self.end)


class InterviewMarks:
    def __init__(self, technical, hr):
        try:
            if technical > 50 or hr > 50:
                raise ValueError("Interview marks should be between 0 and 50")

            self.technical = technical
            self.hr = hr

        except ValueError as e:
            print("Interview Marks Error:", e)
            self.technical = self.hr = 0

    def result(self):
        return "PASS" if self.technical >= 25 and self.hr >= 25 else "FAIL"

try:
    student = StudentInfo("Satheesh", 42)
    academics = AcademicMarks(25, 30, 35)
    interview = InterviewMarks(technical=30, hr=40)

    print("\n--- Student Information ---")
    student.display_info()

    print("\n--- Academic Marks ---")
    academics.display_academics()

    print("\n--- Interview Marks ---")
    print("Technical :", interview.technical)
    print("HR        :", interview.hr)

    print("\n--- Interview Result ---")
    if interview.result() == "PASS":
        print("Result : PASS")
        print(" You got the job!")
    else:
        print("Result : FAIL")
        print(" Better luck next time.")

except Exception as e:
    print("Unexpected Error:", e)






