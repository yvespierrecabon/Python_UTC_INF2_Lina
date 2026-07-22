class Date :
    def __init__ (self, j :int, m:int, a:int):
        self.j = j
        self.m = m
        self.a = a

    def get_jour(self)->int:
        return self.j

    def set_jour(self, j:int)->None :
        if 0 < j < 32:
            self.j = j

    def get_mois(self):
        return self.m

    def set_mois(self, m:int):
        if 0 < m < 13:
            self.m = m


    def get_annee(self):
        return self.a


    def set_annee(self, a:int):
        if 0 < a:
            self.a = a


    def lendemain(self) : # renvoie la date correspondant au lendemain de self
        new_date = Date(self.j+1, self.m, self.a)
        if new_date.m == 2 and new_date.j == 29:
            new_date.j = 1
            new_date.m = 3
        elif new_date.j == 31 and new_date.m not in (1,3,5,7,8,10,12):
            new_date.j = 1
            new_date.m += 1
        elif new_date.j == 32:
            new_date.j = 1
            if new_date.m < 12:
                new_date.m += 1
            else:
                new_date.m = 1
                new_date.a +=1
        return new_date

    def __str__(self) :
        return f'{self.j:02d}/{self.m:02d}/{self.a}'


def main():
    date = Date(1,1,2026)

    for _ in range(366):
        print(date, end = " ")
        date = date.lendemain()
        if date.j == 1:
            print()




if __name__ == "__main__":
    main()