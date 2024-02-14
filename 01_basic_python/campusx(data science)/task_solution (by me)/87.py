class Instructor:

    def __init__(self,name,technology,experience,feedback):
        self.__name = name
        self.__technology = technology
        self.__experience = experience
        self.__feedback = feedback

    def check_eligibility(self):

        if self.__experience > 3 and self.__feedback >= 4.5:
            return True
        elif self.__experience <= 3 and self.__feedback >= 4:
            return True
        else:
            return False

    def allocate_course(self,tech):
        is_eligible = self.check_eligibility()

        if is_eligible:
            if tech in self.__technology:
                return 'Padha sakta hai'
            else:
                return 'Ye to usko aata hi nai hai'
        else:
            return 'acha nai padhata hai'

ins = Instructor('Nitish',['Data Science','Web Development'],5,4.9)
print(ins.allocate_course('Android Dev'))
