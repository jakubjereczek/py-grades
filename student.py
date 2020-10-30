import pandas
import csv


class Student:
    students = []
    fileName = "./data/students.csv"
    df = ""

    def __init__(self):
        try:
            df = pandas.read_csv(self.fileName, header=0, delimiter=";", names=[
                'id', 'name', 'surname', 'age', 'city', 'group'])
            self.df = df
            self.students = df.values.tolist()
        except IOError as err:
            print("Wystapił problem z otwarciem pliku:", err)

    def dodaj(self, id, name, surname, age, city, group):
        nowyStudent = [id, name, surname, age, city, group]
        try:
            self.students.append(nowyStudent)
            self.df = pandas.DataFrame(self.students, columns=[
                'id', 'name', 'surname', 'age', 'city', 'group'])
            with open(self.fileName, 'a+') as f:
                f.write(str(id)+';'+name+';'+surname+';' +
                        str(age)+';'+city+';'+group+'\n')
                f.close()
        except:
            print("Blad przy zapisywaniu nowego studenta do bazy")

    def usun(self, id):
        newStudents = []
        try:
            for i in range(len(self.students)):
                if int(id) != self.students[i][0]:
                    newStudents.append(self.students[i])
            if len(self.students) == len(newStudents):
                raise NameError("Brak studenta o podanym ID")
            # z tablicy students nadpisanie pliku (wykluczajac danego studenta) oraz aktualizacja df by miec aktualne statystyki
            self.df = pandas.DataFrame(newStudents, columns=[
                'id', 'name', 'surname', 'age', 'city', 'group'])
            with open(self.fileName, 'w', encoding='utf8') as f:
                f.write('id;name;surname;age;city;group'+'\n')
                for i in range(len(newStudents)):
                    f.write(str(newStudents[i][0])+';'+newStudents[i][1]+';'+newStudents[i][2]+';' +
                            str(newStudents[i][3])+';'+newStudents[i][4]+';'+newStudents[i][5]+'\n')
                f.close()
        except NameError as err:
            print("Blad: ", err)
        except:
            print("Blad przy usuwaniu studenta z bazy")

    def wyszukaj(self, parametr, arg):
        try:
            studentsList = []
            for i in range(len(self.students)):
                if parametr == "nazwisko":
                    if (arg == self.students[i][2]):
                        studentsList.append(self.students[i])
                elif parametr == "grupa":
                    if (arg == self.students[i][5]):
                        studentsList.append(self.students[i])
                elif parametr == "miasto":
                    if (arg == self.students[i][4]):
                        studentsList.append(self.students[i])
                elif parametr == "id":
                    if (arg == self.students[i][0]):
                        studentsList.append(self.students[i])
                else:
                    raise NameError(
                        "Taki parametr nie istnieje. Dostepne: nazwisko, grupa oraz miasto.")
            if len(studentsList) > 0:
                return studentsList
            else:
                return None
        except NameError as err:
            print("Bląd: ", err)

    def statystykiStudentow(self):
        print("### STATYSTYKI STUDENTOW ###")
        print("Ilosc studentow w bazie: " + str(len(self.students)))
        # zakladajac, ze kazde imie kobiety konczy sie na "a" liczymy liczbe kobiet i mezczyzn
        woman = 0
        men = 0
        for i in range(len(self.students)):
            if str(self.students[i][1])[-1] == 'a':
                woman += 1
            else:
                men += 1
        print("Ilosc kobiet: ", str(woman),
              ", ilosc mezczyzn: ", str(men))
        idOfGroups = set()
        for i in range(len(self.students)):
            idOfGroups.add(self.students[i][5])
        print("Ilosc grup: " + str(len(idOfGroups)))
        for group in idOfGroups:
            length = len(list(
                filter(lambda name: group in name, self.students)))
            print("* ", group, "(liczaca "+str(length)+" osob)")
        print("###")
