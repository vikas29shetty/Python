class Student:
    def __init__(self, name, roll, marks):
        self._name = name
        self._roll = roll
        self._marks = marks

    def calculate_grade(self):
        if self._marks >= 90:
            return "A+"
        elif self._marks >= 75:
            return "A"
        elif self._marks >= 60:
            return "B"
        return "C"

    def display_details(self):
        print(self._name, self._roll, self._marks, self.calculate_grade())


class EngineeringStudent(Student):
    def __init__(self, name, roll, marks, branch):
        super().__init__(name, roll, marks)
        self.branch = branch

    def display_details(self):
        print("Engineering Student")
        super().display_details()
        print("Branch:", self.branch)


s = EngineeringStudent("Kapil", 101, 95, "CSE")
s.display_details()
