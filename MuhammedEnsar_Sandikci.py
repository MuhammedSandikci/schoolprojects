import random
print "Welcome to Sehir Hadi"
adminnumber = "**"
setprize = [10000]

class Ques1:                                                                                    #bu kisimda calss olusturup bu classlarin icine soru ve cevaplarimizi self kodunu kullarak classimizin icine tanimladik
    def __init__(self, Question1,answer1,answer2,answer3):
        self.Question1 = Question1
        self.answer1 = answer1
        self.answer2 = answer2
        self.answer3 = answer3

Q1 = Ques1("Q1-:What color are zebras","1-:Black with white stripes","2-:white with black stripes","3-:Black with blue stripes")
class Ques2:
    def __init__(self, Question2, answer4, answer5, answer6):
        self.Question2 = Question2
        self.answer4 = answer4
        self.answer5 = answer5
        self.answer6 = answer6

Q2 = Ques2("Q2-Where was the old campus of Sehir Univercity","1-Levent","2-Altunizade","3-Maltepe")


class New_question:
    def __init__(self,New_question,New_answer1,New_answer2,New_answer3):
        self.New_question = New_question
        self.New_answer1 = New_answer1
        self.New_answer2 = New_answer2
        self.New_answer3 = New_answer3


class User:                                                   # burada kullanicilar adli class olusurup kullanicilarin bilgilerini olusturduk
    def __init__(self,name,balance,phone_number):
        self.is_qualified = False
        self.name = name
        self.balances = balance
        self.phone_number = phone_number
users = User("['apo','pelin','elif','defne','esra','onder','can','mami','ender','berk']",[2.4,5.2,0.2,9.2,11.2,17.2,37.3,23.5,32.2,334.2],["5577","5540","5322","5302","5244","551","5442","5441","5436","966"])


Question3 = {}

class Admincoment:              # burada classlar ve diger ogrendigimiz kodlardan bazilarini kullanarak admin menusunu olusturduk
    def __init__(self,A,B,C,D,E,F):
        self.A = A
        self.B = B
        self.C = C
        self.D = D
        self.E = E
        self.F = F
ac = Admincoment("1-Set prize for the next competetion","2-Display question for the next competetion","3-Add new question to the next competetion","4-Delete a question from next competetion","5-See users data","6-Log out")



def adminmenu():
    print ac.A
    print ac.B
    print ac.C
    print ac.D
    print ac.E
    print ac.F
    admin_coment = input("Select one of the orders:")
    if admin_coment == 1:                                    # burada admine ait bi bolum olusturduk
        adminprize = raw_input("Please type the total prize of the next competition:\n")
        del setprize[0]
        setprize.append(int(adminprize))
        print "Setting prize..."
        print "\nPrize is " + str(setprize)
        adminmenu()
    if admin_coment == 4:
        deletef = input("which question would you like to delete(1-2-3):")
        if deletef == 1:
            print "Deleting first question..."
            print "\n" + Q2.Question2
            print Q2.answer4
            print Q2.answer5
            print Q2.answer6 + "\n"
            for key, values in Question3.items():
                print key
                print values[0]
                print values[1]
                print values[2]
        elif deletef == 2:
            print "Deleting second question..."
            print Q1.Question1
            print Q1.answer1
            print Q1.answer2
            print Q1.answer3
            for key, values in Question3.items():
                print key
                print values[0]
                print values[1]
                print values[2]
        elif deletef == 3:
            print "Deleting third question..."
            print Q1.Question1
            print Q1.answer1
            print Q1.answer2
            print Q1.answer3
            print "\n" + Q2.Question2
            print Q2.answer4
            print Q2.answer5
            print Q2.answer6 + "\n"
        else:
            print Q1.Question1
            print Q1.answer1
            print Q1.answer2
            print Q1.answer3
            print "\n" + Q2.Question2
            print Q2.answer4
            print Q2.answer5
            print Q2.answer6 + "\n"
            for key, values in Question3.items():
                print key
                print values[0]
                print values[1]
                print values[2]
        adminmenu()

    if admin_coment == 2:
        print Q1.Question1
        print Q1.answer1
        print Q1.answer2
        print Q1.answer3
        print "\n" + Q2.Question2
        print Q2.answer4
        print Q2.answer5
        print Q2.answer6 + "\n"
        for key, values in Question3.items():
            print key
            print values[0]
            print values[1]
            print values[2]
        adminmenu()
    if admin_coment == 3:
        nq = raw_input("Please type the new question for the next competition")
        na1 = raw_input("Please type the correct answer for the next competition")
        na2 = raw_input("Please type the incorrect answer 1 for the next competition")
        na3 = raw_input("Please type the incorrect answer 2 for the next competition")
        Question3["Q3-"+nq] = ["1-"+na1,"2-"+na2,"3-"+na3]
        adminmenu()


    if admin_coment == 5:
        print users.name
        print users.balances
        print users.phone_number
        adminmenu()


    if admin_coment == 6:
        print "See you soon"
        game()
def game():                       # burada hadi oyunumuzu olusturduk
    print "Competition will start soon ..Be ready :>"
    print "Today prize is " + str(setprize)
    print "******************Total Players 10**********************"
    print Q1.Question1
    print Q1.answer1
    print Q1.answer2
    print Q1.answer3
    q1 = raw_input("What is your answer [1-2-3]?")
    if q1 == "1":
        print "You loose the game"
    elif q1 == "2":
        print "Your answer correct :)"
        while True:
            random_pc1 = random.randint(0,9)          # burada bilgisaara 3 adet rastgele sayi buldurduk ve bu sayilar sayesinde raund bitimlerindeki cevap siklarinin dagilimlerini belirledik
            random_pc2 = random.randint(0,9)
            random_pc3 = random.randint(0,9)
            random_pc4 = random.randint(0, random_pc2)
            random_pc5 = random.randint(0, random_pc2 + 1)
            random_pc6 = random.randint(0, random_pc2)
            if random_pc1 + random_pc2 + random_pc3 == 9:

                print Q1.answer1 + " False " + "Total answers:" + str(random_pc1)
                print Q1.answer2 + " True " + "Total answers:" + str(random_pc2+1)
                print Q1.answer3 + " False " + "Total answers:" + str(random_pc3)
                print "\n------TOTAL PLAYERS " + str(random_pc2+1) + "----------"

                print Q2.Question2
                print Q2.answer4
                print Q2.answer5
                print Q2.answer6
                q2 = raw_input("what is your answer [1-2-3]?")
                if q2 == "1":
                    print "You lose the competition"
                if q2 == "2":
                    print "your answer correct"
                    random_pc4 = random.randint(0,random_pc2)
                    random_pc5 = random.randint(0,random_pc2+1)
                    random_pc6 = random.randint(0,random_pc2)

                if random_pc4 + random_pc5 + random_pc6 == random_pc2+1:

                    print Q2.answer4 + " False "+ "Total answers:" + str(random_pc4)
                    print Q2.answer5 + " True "+ "Total answers:" + str(random_pc5+1)
                    print Q2.answer6 + " False "+ "Total answers:" + str(random_pc6)
                    print "\n------TOTAL WINNERS " + str(random_pc5) + "----------"
                    print "\n------Total distributed prize:" + str(setprize)
                    if random_pc5 -1> 0:

                        print "Done..."
                        break
                    break
                elif q2 == "3":
                    print "You lose the competition"
    elif q1 == "3":
        print "You lose the competition"





def hadigame():     # bu kisimda kullanici admin degilse onun hangi siradan kullanici oldugunu belirledik ve ayarli oyuna girmesini sagladik

    password = raw_input("Please type your student number")
    if password == "5577" or password == "5540" or password == "5322" or password == "5302" or password == "5244" or password == "551" or password == "5442" or password == "5441" or password == "5436" or password == "966":
        print "Welcome to the Sehir Hadi game "
        game()

    elif password == "**":
        adminmenu()
    else:
        hadigame()

hadigame()
