Subject = {'Science': ['maths', 'physics', 'chemistry', 'biology'],
           'commerce': ['economics', 'business studies', 'financial management', 'policy'],
           'Arts': ['history', 'geography', 'political science']}

engineering = ['maths', 'physics']
medical = ['biology', 'chemistry']
accounting = ['business studies', 'policy']
journalism = ['history', 'political science']


class Stream():

    def engineering(self, abc):
        for i in Subject:
            if abc in Subject[i]:
                print("Your stream is", i)
        if abc in engineering:
            print("Yes, you are eligible for Engineering")
        else:
            print("No, You are not eligible for Engineering")

    # def med(self, bca):
    #     for i in Subject:
    #         if bca in Subject[i]:
    #             print("Your stream is", i)
    #     while bca in medical:
    #         print("yes, you are eligible for Medical ")
    #     else:
    #         print("No, You are not eligible for Medical")


xyz = Stream()
xyz.engineering("maths")

# zxa = Stream()
# zxa.med("biology")

