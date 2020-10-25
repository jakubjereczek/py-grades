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
