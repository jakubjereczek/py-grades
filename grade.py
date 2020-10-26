import pandas


class Grade:
    grades = []
    fileName = "./data/grades.csv"
    df = ""

    def __init__(self):
        try:
            df = pandas.read_csv(self.fileName, header=0, delimiter=";", names=[
                'id', 'subject', 'grade'])
            print(df)
            self.df = df
            self.grades = df.values.tolist()
        except IOError as err:
            print("Problem z otwarciem pliku", err)

    def dodaj(self, id, subject, grade):
        print(id, subject, grade)
        nowaOcena = [id, subject, grade]
        self.grades.append(nowaOcena)
        self.df = pandas.DataFrame(self.grades, columns=[
            'id', 'subject', 'grade'])
        try:
            with open(self.fileName, 'a+') as f:
                f.write(str(id)+';'+subject+';'+str(grade) + '\n')
                f.close()
        except:
            print("Blad przy zapisywaniu nowych ocen studenta do bazy")

    def statystykiOcen(self):
        # ilosc studentow ktorzy maja wystawiona przynajmniej jedna ocene
        # uzycie Set by uniknąc dupikatow
        print("### STATYSTYKI OCEN ###")
        idStudentow = set()
        for i in range(len(self.grades)):
            idStudentow.add(self.grades[i][0])
        print("Ilosc studentów, którym wpisano choćby jedną ocene: " +
              str(len(idStudentow)))
        # srednia ocen
        print("Srednia ocen dla przedmiotów: ")
        print(self.df.groupby(['subject'])['grade'].mean())
        print("###")
