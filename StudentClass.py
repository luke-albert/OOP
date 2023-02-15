from datetime import date


"""
class Student:

    def __init__(self,i, n, d, c, r):
        self.id = i
        self.name = n
        self.dob = d
        self.classification = c
        self.age = 0
        self.registration = r


    def calc_age(self):
        self.dob = self.dob.split('/')
        self.dob.year = self.dob[2]
        self.age = year - self.dob.year
        
        

    def calc_registration(self):
        class_year = ['F','S','Jr','Sr']
        if self.classification in class_year:
            if self.classifiaction == 'F':
                self.registration = 'Freshman - 4/10 thru 4/12'
            elif self.classification == 'S':
                self.registration = 'Sophomores - 4/7 thru 4/9'
            elif self.classification == 'Jr':
                self.registration = 'Juniors - 4/4 thru 4/6'
            else:
                self.registration = 'Seniors 4/1 thru 4/3'
            


    def get_age(self):
        return self.age


    def get_registration(self):
        return self.registration

"""


class Student:
    def __init__(self, id, name, dob, classification):
        self.__studentid = id
        self.__name = name
        self.__dob = dob
        self.__classification = classification
        self.__age = 0
        self.__register = ""

    def calc_age(self):
        today = date.today()
        today_year = today.year
        dob = self.__dob.split("/")
        dob_year = int(dob[2])
        self.___age = today_year - dob_year

    def calc_register(self):
        if self.__classification == "senior":
            self.___register = "4/1 thru 4/3"
        elif self.__classification == "junior":
            self.___register = "4/4 thru 4/6"
        elif self.__classification == "sophomore":
            self.___register = "4/7 thru 4/9"
        elif self.__classification == "freshman":
            self.___register = "4/9 thru 4/12"
        else:
            self.__register = "classifiaction not found"

    def get_age(self):
        return self.__age

    def get_register(self):
        return self.__register
