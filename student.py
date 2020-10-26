import pandas


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
            print("Problem z otwarciem pliku", err)

    def wyszukaj(self, parametr, nazwa):
        try:
            listaUczniow = []
            for i in range(len(self.students)):
                if parametr == "nazwisko":
                    if (nazwa == self.students[i][2]):
                        listaUczniow.append(self.students[i])
                elif parametr == "grupa":
                    if (nazwa == self.students[i][5]):
                        listaUczniow.append(self.students[i])
                elif parametr == "miasto":
                    if (nazwa == self.students[i][4]):
                        listaUczniow.append(self.students[i])
                else:
                    raise NameError(
                        "Taki parametr nie istnieje. Dostepne: nazwisko, grupa oraz miasto.")
            if len(listaUczniow) > 0:
                return listaUczniow
            else:
                return None
        except NameError as err:
            print("Bląd.", err)

    def statystykiStudentow(self):
        print("### STATYSTYKI STUDENTOW ###")
        print("Ilosc studentow w bazie: " + str(len(self.students)))
        # zakladajac, ze kazde imie kobiety konczy sie na "a" liczymy liczbe kobiet i mezczyzn
        kobiety = 0
        mezczyzni = 0
        for i in range(len(self.students)):
            if str(self.students[i][1])[-1] == 'a':
                kobiety += 1
            else:
                mezczyzni += 1
        print("Ilosc kobiet: ", str(kobiety),
              ", ilosc mezczyzn: ", str(mezczyzni))
        idGrup = set()
        for i in range(len(self.students)):
            idGrup.add(self.students[i][5])
        print("Ilosc grup: " + str(len(idGrup)))
        for grupa in idGrup:
            liczebnosc = len(list(
                filter(lambda name: grupa in name, self.students)))
            print("* ", grupa, "(liczaca "+str(liczebnosc)+" osob)")
        print("###")
