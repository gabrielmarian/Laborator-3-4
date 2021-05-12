Class Student:

Numar_studenti = 0
def __init__(self, nume, prenume, medie):
Self.nume = nume
Self.prenume = prenume
Self.medie = medie
Print “Initializare student: ”,self.nume,self.prenume
Student.numar_studenti += 1

def test_bursier(self):
If self.medie>=9.50:
Print “Bursa de merit”
Elif 8.50<=self.medie<9.50:
Print “Bursa de studiu”

def nr_studenti():
Print “Exista”, Student.numar_studenti, “instante.”
Nr_studenti = staticmethod(nr_studenti)

Studenti1 = Student (‘Bucur’,’Tudor’,10)
Student1.test_bursier()
Student.nr_studenti()

Student2 = student(‘Enache’,’Stefan’,8)
Student2.test_bursier()
Student.nr_studenti()