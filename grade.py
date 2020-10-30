import pandas


class Grade:
    grades = []
    fileName = "./data/grades.csv"
    df = ""

    def __init__(self):
        try:
            df = pandas.read_csv(self.fileName, header=0, delimiter=";", names=[
                'id', 'subject', 'grade'])
            self.df = df
            self.grades = df.values.tolist()
        except IOError as err:
            print("Wystapił problem z otwarciem pliku:", err)

    def dodaj(self, id, subject, grade):
        print(id, subject, grade)
        newGrade = [id, subject, grade]
        self.grades.append(newGrade)
        self.df = pandas.DataFrame(self.grades, columns=[
            'id', 'subject', 'grade'])
        try:
            with open(self.fileName, 'a+') as f:
                f.write(str(id)+';'+subject+';'+str(grade) + '\n')
                f.close()
        except:
            print("Blad przy zapisywaniu nowych ocen studenta do bazy")

    def usun(self, id):
        newGrades = []
        try:
            for i in range(len(self.grades)):
                if int(id) != self.grades[i][0]:
                    newGrades.append(self.grades[i])
            if len(self.grades) == len(newGrades):
                raise NameError("Brak studenta o podanym ID")
            self.df = pandas.DataFrame(newGrades, columns=[
                'id', 'subject', 'grade'])
            with open(self.fileName, 'w', encoding='utf8') as f:
                f.write('id;subject;grade'+'\n')
                for i in range(len(newGrades)):
                    f.write(
                        str(newGrades[i][0])+';'+newGrades[i][1]+';'+str(newGrades[i][2])+'\n')
                f.close()
        except NameError as err:
            print("Blad:", err)
        except:
            print("Blad przy usuwaniu ocen studenta z bazy")

    def statystykiOcen(self):
        # ilosc studentow ktorzy maja wystawiona przynajmniej jedna ocene
        # uzycie Set by uniknąc dupikatow
        print("### STATYSTYKI OCEN ###")
        idOfStudents = set()
        for i in range(len(self.grades)):
            idOfStudents.add(self.grades[i][0])
        print("Ilosc studentów, którym wpisano choćby jedną ocene: " +
              str(len(idOfStudents)))
        # srednia ocen
        print("Srednia ocen dla przedmiotów: ")
        print(self.df.groupby(['subject'])['grade'].mean())
        print("###")
