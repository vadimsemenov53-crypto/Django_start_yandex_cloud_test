# # from .models import Student1, Grade
#
# class StudentService:
#
#     @staticmethod
#     def get_full_name(student_id):
#         student = Student1.objects.get(id=student_id)
#
#         return f'{student.first_name} {student.last_name}'
#
#     @staticmethod
#     def calculate_avg_score(student_id):
#         grades = Grade.objects.filter(student_id=student_id)
#
#         if not grades.exists():
#             return None
#
#         total_score = sum(grade.score for grade in grades)
#         avg_score = total_score / grades.count()
#
#         return avg_score
#
#     @staticmethod
#     def has_passed(student_id, passing_score=60):
#         avg_score = StudentService.calculate_avg_score(student_id)
#
#         if avg_score is None:
#             return None
#
#         return avg_score >= passing_score
