from student import Student
from grade import Grade
import pandas


student = Student()
# Metoda wyszukaj() przyjmuję parametry:
# parametr - nazwisko, grupa, miast
# nazwa - treść na ktorej podstawie szukamy
# Zwraca liste uczniów. a przypadku gdy jest pusta None.
# wysz1 = student.wyszukaj("nazwisko", "Kamińska")
# wysz2 = student.wyszukaj("grupa", "A03")
# wysz3 = student.wyszukaj("miasto", "Gdynia")

# print(wysz1)

# print("Uczennice o nazwisku Kaminska: ")
# for i in range(len(wysz1)):
#     print("* "+wysz1[i][1]+" "+wysz1[i][2]+" z grupy "+wysz1[i][5])

# print("Uczniowie z grupy A03: ")
# for i in range(len(wysz2)):
#     print("* "+wysz2[i][1]+" "+wysz2[i][2])

# print("Uczniowie zamieszkujacy miasto Gdynia: ")
# for i in range(len(wysz3)):
#     print("* "+wysz3[i][1]+" "+wysz3[i][2])

grade = Grade()

# student.df.id.astype(int)
# grade.df.id.astype(int)

# print(grade.df)
polaczonePliki = (student.df).merge(grade.df, on='id', how='inner')
# print(polaczonePliki)

# grade.statystykiOcen()
# student.statystykiStudentow()


def dodajStudenta(id, name, surname, age, city, group, **grades):
    print("Dodawanie nowego studenta")
    student.dodaj(id, name, surname, age, city, group)
    for arg in grades:
        subject = str(arg)
        g = int(grades[arg])
        grade.dodaj(id, subject, g)


#lastId = int(student.students[len(student.students) - 1][0]) + 1
# dodajStudenta(lastId, "Jan", "Kowalski", 21, "Gdansk", "A01", biology=5,
#             physics = 5, it = 5, english = 4, science = 4, math = 5)


def usunStudenta(id):
    print("Usuwanie nowego studenta")
    student.usun(id)
    grade.usun(id)


usunStudenta("100001")

# statystyki grupowe (z uzyciem students oraz grades)
# najlepsze 5 osob z danej grupy (stypendia)

# osoby majace oceny zagrazające (2)

# srednie względem grupy ()
