from project.student import Student
import unittest


class StudentTest(unittest.TestCase):
    def setUp(self) -> None:
        self.student = Student("Pesho")
        self.student_with_course = Student(
            "Gosho"
            , {"math": ["note"]}
        )

    def test_init(self):
        self.assertEqual(self.student.name, "Pesho")
        self.assertEqual(self.student.courses, {})

        self.assertEqual(self.student_with_course.name, "Gosho")
        self.assertEqual(self.student_with_course.courses, {"math": ["note"]})

    def test_enroll_in_existing_course(self):
        result = self.student_with_course.enroll("math", ["another note"])
        self.assertEqual(result, "Course already added. Notes have been updated.")
        self.assertEqual(self.student_with_course.courses["math"], ["note", "another note"])

    def test_enroll_in_new_course_without_extra_parameter(self):
        result = self.student.enroll("physics", ["note"])
        self.assertEqual(result, "Course and course notes have been added.")
        self.assertEqual(self.student.courses["physics"], ["note"])

    def test_enroll_in_new_course_with_extra_parameter(self):
        result = self.student.enroll("physics", ["note"], "Y")
        self.assertEqual(result, "Course and course notes have been added.")
        self.assertEqual(self.student.courses["physics"], ["note"])

    def test_enroll_in_new_course_without_notes(self):
        result = self.student.enroll("physics", ["note"], "X")
        self.assertEqual(result, "Course has been added.")
        self.assertEqual(self.student.courses["physics"], [])

    def test_add_notes_to_existing_course(self):
        result = self.student_with_course.add_notes("math", "another note")
        self.assertEqual(result, "Notes have been updated")
        self.assertEqual(self.student_with_course.courses["math"], ["note", "another note"])

    def test_add_notes_to_non_existent_course(self):
        with self.assertRaises(Exception) as context:
            self.student.add_notes("math", "note")
        self.assertEqual(str(context.exception), "Cannot add notes. Course not found.")

    def test_leave_existing_course(self):
        result = self.student_with_course.leave_course("math")
        self.assertEqual(result, "Course has been removed")
        self.assertEqual(self.student_with_course.courses, {})

    def test_leave_non_existent_course(self):
        with self.assertRaises(Exception) as context:
            self.student.leave_course("math")
        self.assertEqual(str(context.exception), "Cannot remove course. Course not found.")


if __name__ == "__main__":
    unittest.main()