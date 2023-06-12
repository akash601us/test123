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

