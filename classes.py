man = {'Honda': ['accord', 'crv', 'hrv', 'civic'],
       'Maruti': ['Breeja', 'Alto']}
suv = ['crv', 'hrv']
hatchback = ['accord', 'civic']
class Car():

    def suv(self,abc): #abc='crv'
        if abc in suv:
            print("yes its a suv")
        else:
            print("Not its not")
        for i in man: #i =honda and Maruti
            print(i)
            if abc in man[i]:
                print("Manufacture is ",i)


        def hatchback(self, xyz):
            return True


xyz = Car()
xyz.suv("Alto")


Subject = {'Science': ['maths', 'physics', 'chemistry', 'biology'],
           'commerce': ['economics', 'business studies', 'financial management', 'policy'],
           'Arts': ['history', 'geography', 'political science']}

engineering = ['maths', 'physics']
medical = ['biology', 'chemistry']
accounting = ['business studies', 'policy']
journalism = ['history', 'political science']


class Stream():

    def engineering(self, abc):
        if abc in engineering:
            print("yes you are eligible for engineering")
        else:
            print("No You are not eligible for engineering")
        for i in subject:
            print
