class Score:
    def __init__(self, grade, weight):
        self.grade = grade
        self.weight = weight


class CourseGrade:
    def __init__(self, name, score = 0):
        self.name = name
        self.weight = 0
        self.score = score

    def add_score(self, score):
        if type(score) == Score and score.weight != 0 and self.weight + score.weight <= 100:
            self.score = self.score * self.weight + score.grade * score.weight
            self.weight += score.weight
            self.score /= (self.weight)

    def add_scores(self, scores):
        for score in scores:
            self.add_score(score)

    def __str__(self):
        letter_grade_dict = {100: "A+", 95: "A+", 90: "A+", 85: "A.", 80: "A-", 75: "B+", 70: "B.", 65: "B-", 60: "C+", 55: "C.", 50: "C-"}
        if self.score < 50:
            return "{}: {} for a letter score of: F\n".format(self.name, self.score)
        else:
            return "{}: {} for a letter score of: {}\n".format(self.name, self.score, letter_grade_dict[self.score - self.score % 5])
    
    def pure_string(self):
        letter_grade_dict = {90: "A+", 85: "A.", 80: "A-", 75: "B+", 70: "B.", 65: "B-", 60: "C+", 55: "C.", 50: "C-"}
        return "{} {} {}".format(self.name, self.score, letter_grade_dict[self.score - self.score % 5])
        

class GPA:
    def __init__(self):
        self.courses = []
        self.grade = 0
        self.num_courses = 0
        
    def __str__(self):
        output = str(self.courses[0])
        for course in self.courses[1:]:
            output += str(course)
        return output

    def pure_string(self):
        output = self.courses[0].pure_string()
        for course in self.courses[1:]:
            output += "\n" + course.pure_string()
        return output

    def append(self, course):
        self.courses.append(course)
        grade_dict = {100: 9, 95: 9, 90: 9, 85: 8, 80: 7, 75: 6, 70: 5, 65: 4, 60: 3, 55: 2, 50: 1}
        if type(course) != CourseGrade:
            return
        grade = course.score - course.score % 5
        if grade < 50:
            grade = 0
        else: 
            grade = grade_dict[grade]
        self.grade = self.grade * self.num_courses + grade
        self.num_courses += 1
        self.grade /= self.num_courses

    def show(self):
        letter_grade_dict = {9: 'A+', 8: 'A.', 7: 'A-', 6: 'B+', 5: 'B.', 4: 'B-', 3: 'C+', 2: 'C.', 1: 'C-', 0: "F"}
        grade = self.grade - (self.grade % 1)
        print("After {} courses, your current GPA is {}".format(self.num_courses, letter_grade_dict[grade]))
        print(self)

    def save(self):
        filename = input("Enter the file to save to:\n")
        save_file = open(filename, 'w')
        save_file.write(self.pure_string())
        print(self.pure_string())
        save_file.close()

    def load(self):
        filename = input("Enter the file to load from:\n")
        input_file = open(filename, 'r')
        contents = input_file.read()
        input_file.close()
        for course in contents.split("\n"):
            course = course.split(" ")
            print(course)
            print(course[0], course[1])
            course = CourseGrade(course[0], float(course[1]))
            self.append(course)

def main():
    gpa = get_load()
    if gpa == False:
        gpa = GPA()
    do_continue = True
    while do_continue:
        course = get_course_grades()
        gpa.append(course)
        gpa.show()
        do_continue = get_continue()
    do_save(gpa)

def get_load():
    load = input("Do you want to load?\n")
    while load not in ["Y", "N"]:
        load = input("Do you want to load?\n")
    if load != "Y":
        return False
    else:
        gpa = GPA()
        gpa.load()
    return gpa

def do_save(gpa):
    save = input("Do you want to save?\n")
    while save not in ["Y", "N"]:
        save = input("Do you want to save?\n")
    if save != "Y":
        return
    else:
        gpa.save()
    

def get_course_grades():
    course = CourseGrade(input("Enter the courses name: "))
    calculate_course_grades(course)
    show_required_grades(course)
    return course

def calculate_course_grades(course):
    score = get_score(course)
    course.add_score(score)
    needs_more = get_continue(course)
    print("{}: current grade: {}, current weight: {}".format(course.name, course.score, course.weight))
    while needs_more:
        score = get_score(course)
        course.add_score(score)
        needs_more = get_continue(course)
        print("{}: current grade: {}, current weight: {}".format(course.name, course.score, course.weight))
        

def get_score(course):
    grade = input("Enter the score you got\n")
    while not is_valid(grade):
        print('invalid grade')
        grade = input("Enter the score you got\n")
    weight = input("Enter the weight of that score\n")
    while not is_valid(weight):
        print('invalid weight')
        weight = input("Enter the weight of that score\n")
    weight = float(weight)
    grade = float(grade)
    if weight + course.weight > 100:
        return
    return Score(grade, weight)

def is_valid(number):
    letters = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '.']
    for digit in number:
        if digit not in letters:
            return False
    return True

def get_continue(course=True):
    if course != True:
        if course.weight == 100:
            return False
    while True:
        do_continue = input("Do you want to continue (Y / N)? ")
        if do_continue == 'Y':
            return True
        if do_continue == 'N':
            return False

def show_required_grades(course):
    if course.weight == 100:
        print("Your grade is:", course.score)
        return
    expected_grade = get_expected()
    remaining_weight = 100 - course.weight
    final_grade = ((100 * expected_grade) - course.score * course.weight) / remaining_weight
    if final_grade > 100:
        max_grade = (course.score * course.weight + 100 * remaining_weight) / 100
        print("Sorry, but this grade is impossible.")
        print("Your maximum grade is {}".format(max_grade))
    else:
        print("To get {} in {} you will need to have an average grade of {}".format(expected_grade, course.name, final_grade))
    

def get_expected():
    letter_grade_dict = {"A+": 90, "A.": 85, "A-": 80, "B+": 75, "B.": 70, "B-": 65, "C+": 60, "C.": 55, "C-": 50}
    while True:
        expected = input("What grade are you aiming for?\nEnter a number or a letter grade using '.' for an average\n")
        if expected.isnumeric():
            return float(expected)
        if expected in letter_grade_dict:
            return letter_grade_dict[expected]
            

main()











        
