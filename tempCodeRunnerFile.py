from student import Student
from grade import Grade

student = Student()
# Metoda wyszukaj() przyjmuję parametry:
# parametr - nazwisko, grupa, miast
# nazwa - treść na ktorej podstawie szukamy
# Zwraca liste uczniów. a przypadku gdy jest pusta None.
print(student.wyszukaj("nazwisko", "Kamińska"))
print(student.wyszukaj("grupa", "A03"))
print(student.wyszukaj("miasto", "Gdynia"))

grade = Grade()
print(grade.grades)
