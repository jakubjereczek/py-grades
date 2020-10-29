from student import Student
from grade import Grade
import pandas


student = Student()
# WYSWIETLANIE DANYCH DLA STUDENTOW, OCEN ORAZ INDYWIDUALNYCH STATYSTYK DLA STUDNETOW, OCEN.
# wysz1 = student.wyszukaj("nazwisko", "Kamińska")
# wysz2 = student.wyszukaj("grupa", "A03")
# wysz3 = student.wyszukaj("miasto", "Gdynia")

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

# grade.statystykiOcen()
# student.statystykiStudentow()


def dodajStudenta(id, name, surname, age, city, group, **grades):
    print("Dodawanie nowego studenta")
    student.dodaj(id, name, surname, age, city, group)
    for arg in grades:
        subject = str(arg)
        g = int(grades[arg])
        grade.dodaj(id, subject, g)

# lastId = int(student.students[len(student.students) - 1][0]) + 1
# dodajStudenta(lastId, "Jan", "Kowalski", 21, "Gdansk", "A01", biology=5,
#             physics = 5, it = 5, english = 4, science = 4, math = 5)


def usunStudenta(id):
    print("Usuwanie nowego studenta")
    student.usun(id)
    grade.usun(id)


# usunStudenta("100001")

polaczonePliki = (student.df).merge(grade.df, on='id', how='inner')

# statystyki grupowe (z uzyciem students oraz grades)
# srednia dla grup
print("Srednie dla grup: ")
print(polaczonePliki.groupby(['group'])['grade'].mean())

# najlepsze 5 osob z (stypendia)
# pogrupowanie indeksow wraz ze srednia
studenciWedlugSredniej = (polaczonePliki.groupby(['id', 'group'])[
    'grade'].mean().sort_values()).sort_values(ascending=False).head(5)
print(studenciWedlugSredniej)

# osoby majace oceny zagrazające (2)
zagrozeni = set()
iloscZagrozen = 0
for i in range(len(grade.grades)):
    if (grade.grades[i][2] < 3):
        iloscZagrozen += 1
        zagrozeni.add(grade.grades[i][0])
print("Zagrozeni uczniowie: ", str(len(zagrozeni)))
for zagrozony in zagrozeni:
    student2 = student.wyszukaj("id", zagrozony)
    print("* "+student2[0][1]+" "+student2[0][2]+" z grupy "+student2[0][5])
print("Ilosc ocen niedostatecznych: "+str(iloscZagrozen))
