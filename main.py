import pandas
from student import Student
from grade import Grade

student = Student()

# Statystyki wyłącznie dla dla studentow (nieuzględniając ocen)
student.statystykiStudentow()

# Wyswietlenie danych dla studentów wyszukanych według okreslonych parametrów (przefiltrowanie). Zwraca liste z studentami. W przypadku braku elementów None.


def showStudents(students):
    for i in range(len(students)):
        print("* "+students[i][1]+" "+students[i]
              [2]+" grupa: "+students[i][5]+", miasto: "+students[i][4])


Kaminska = student.wyszukaj("nazwisko", "Kamińska")
print("Uczennice o nazwisku Kaminska: ")
showStudents(Kaminska)

A03 = student.wyszukaj("grupa", "A03")
print("Uczniowie z grupy A03: ")
showStudents(A03)

Gdynia = student.wyszukaj("miasto", "Gdynia")
print("Uczniowie zamieszkujacy miasto Gdynia: ")
showStudents(Gdynia)

###

grade = Grade()

# Statystyki wyłącznie dla dla ocen (nieuzględniając studentow)
grade.statystykiOcen()

# Dodawanie nowego studenta wraz z ocenami do bazy (do pliku csv oraz do aktualnej listy students oraz grades)


def dodajStudenta(id, name, surname, age, city, group, **grades):
    print("Dodawanie nowego studenta")
    student.dodaj(id, name, surname, age, city, group)
    for arg in grades:
        subject = str(arg)
        g = int(grades[arg])
        grade.dodaj(id, subject, g)


lastId = int(student.students[len(student.students) - 1][0]) + 1
# dodajStudenta(lastId, "Jan", "Kowalski", 21, "Gdansk", "A01", biology=5,
#             physics = 5, it = 5, english = 4, science = 4, math = 5)

# Usunie cie nowego studenta wraz z ocenami z bazy (z pliku csv oraz z aktulanej listy students oraz grades)


def usunStudenta(id):
    print("Usuwanie nowego studenta")
    student.usun(id)
    grade.usun(id)

# usunStudenta("100001")


# STATYSTYKI DLA LĄCZĄCZONYCH ZBIORÓW DANYCH (z uzyciem students oraz grades)
polaczonePliki = (student.df).merge(grade.df, on='id', how='inner')

# Srednia dla poszczegolnych z grup
print("Srednie dla grup: ")
print(polaczonePliki.groupby(['group'])['grade'].mean())

# Wyswietlnie najlepszych 5 osob z wszystkich grup (mozliwe zastosowanie: stypendia)
# pogrupowanie indeksow wraz ze srednia
studenciWedlugSredniej = (polaczonePliki.groupby(['id', 'group'])[
    'grade'].mean().sort_values()).sort_values(ascending=False).head(5)
print(studenciWedlugSredniej)

# Wyswietlenie osob posiadajacych minum jedna ocene nieumazliwiajaca niezaliczenie (2). Zliczenie ocen zagrazajacych.

uczniowieZagrozeni = set()
iloscZagrozen = 0

for i in range(len(grade.grades)):
    if (grade.grades[i][2] < 3):
        iloscZagrozen += 1
        uczniowieZagrozeni.add(grade.grades[i][0])
print("Zagrozeni uczniowie: ", str(len(uczniowieZagrozeni)))

for zagrozony in uczniowieZagrozeni:
    wyszukanyStudent = student.wyszukaj("id", zagrozony)
    showStudents(wyszukanyStudent)
print("Ilosc ocen niedostatecznych: "+str(iloscZagrozen))
