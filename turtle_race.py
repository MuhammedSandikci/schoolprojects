from swampy.TurtleWorld import *

print("||| WELCOME TO SEHIR TURTLE CUP |||")

def start_game():
    global Firstscore
    global Secondscore
    global FirstTurtle
    global SecondTurtle
    global world
    global player1_info
    global player2_info
    print "--- First Turtle ---"

    world = TurtleWorld()

    FirstTurtle = Turtle()                                  #Bu dort satirda ilk ve ikinci turtlelarin calismasini sagladik ve hizlarini yukselttik.
    SecondTurtle = Turtle()
    FirstTurtle.set_delay(0.1)
    SecondTurtle.set_delay(0.1)

    x =  raw_input("What is the name of first Turtle ?\n")
    print "Welcome " + x
    player1_info = [FirstTurtle,x]

    while True:
        color = raw_input("Please select color for your Turtle red-blue-yellow\n")   #burada kullaniciya renk sectiriyor ve sectgi renk yanlissa hata veriyor.
        if color == "red" or color == "blue" or color == "yellow":
            print "Your color is " + color
            FirstTurtle.set_color(color)
            FirstTurtle.set_pen_color("White")
            bk(FirstTurtle,100)
            print x + " is ready to go"
            break
        else:
            print color, "is not a valid color, please select one of red-blue-yellow colors"

    print "\n--- Second Turtle"
    y = raw_input("What is the name of second Turtle ?\n")
    print "Welcome " + y

    while True:                                                         #burada while true kodu ile turtle isimlerinin ayni olmasi durumunda tekrar isim cektiriyoruz.
        if y == x:
            print y + " is taken choose another name"
            y = raw_input("What is the name of second Turtle ?\n")
        else:
            break
    player2_info = [SecondTurtle, y]
    while True:
        colorsec = raw_input("Please select color for your Turtle red-blue-yellow\n")           #Burada ikinci turtle icin renk cektiriyoruz eger ilk turtle ile ikinci turtle in rengi ayni secilirse hata verip tekrar sectiriyor.
        if colorsec == color:
            print colorsec + " is already taken, please choose another color"
        elif colorsec == "red" or colorsec == "blue" or colorsec == "yellow":
            print "Your color is " + colorsec
            SecondTurtle.set_color(colorsec)                                                   #Burada turtlelari baslangic noktasina aliyoruz ve gectikleri yerleri beyaz yapiyoruz ki baslangica geldiklerinde oyun hartiasinda renk gozukmesin.
            SecondTurtle.set_pen_color("White")

            rt(SecondTurtle,90)
            fd(SecondTurtle,90)
            rt(SecondTurtle,90)
            fd(SecondTurtle,100)
            rt(SecondTurtle,90)
            rt(SecondTurtle,90)
            print y + " is ready to go"
            break
        else:
            print colorsec + "is not a valid color, please select one of red-blue-yellow colors"
    print "||| Lets Start |||"

start_game()
import random
kickoff = random.randint(1,2)

players = [player1_info,player2_info]                                 #Burada liste yontemi ile playerlari tanimliyoruz ayrica burada oyuna ilk kimin baslayacagini bilgisayara
startwith_info = random.choice(players)                               #rasgele bir sekilde sectiriyoruz.
players.remove(startwith_info)
later_info = players[0]                                               #Burada ustte tanimladigimiz players listsindeki 0 inci yani listedeki ilk tanimi later_info olarak tanimliyoruz.
startwith = startwith_info[0]                                         #Burada bilgisayarin rasgele sectigi yani 1. oyuncuyu startwith seklinde tanimliyoruz.
later = later_info[0]                                                 #Burada da oyuna 2. baslayan turte i later seklinde tanimliyoruz.
startwith_name = startwith_info[1]                                    #Burada listedeki 1. yani aslinda 2. olan tanimi kullanip (x,y) turtlelarin bazi durumlarda hata vermeden calisabilmesi icin bu tanimi kullaniyoruz.
later_name = later_info[1]
Firstscore = 0                                                        #Burada skorlari 0 diye tanitip her el kullanicinin yazdigi sayi ile toplanip eklenmesi icin fonksiyonun icinde bunu tanimliyoruz.
Secondscore = 0
FirstTurtle.set_pen_color("Black")
SecondTurtle.set_pen_color("Black")
round_no = 0

def movement1(turtle,dist):                                            #Burada merdiven hareketini tanimliyoruz 2 ser kere for loop kullanarak kodu kisaltiyoruz.
    fd(turtle, dist / 5)
    for i in range(2):
        lt(turtle, 90)
        fd(turtle, dist / 5)
        rt(turtle, 90)
        fd(turtle, dist / 5)
    for x in range(2):
        rt(turtle, 90)
        fd(turtle, dist / 5)
        lt(turtle, 90)
        fd(turtle, dist / 5)

def movement2(turtle,dist):                                        #Burada duz gitme hareketini tanimliyoruz.
    fd(turtle, dist)

def movement3(turtle,dist):                                        #Burada yarim daire hareketini tanimliyoruz. Su sekilde tanimliyoruz
                                                                   #Oncelikle turtle i oyuna baslarken geri cektigimiz sayi ile hareketi yaptirdiktan sonraki konumunun farkini bulup bunu tam sayi seklinde boldugumuzde yarim daire hareketini pixel olarak tam sekilde yapiyor.
    turtle.set_delay(0.0001)
    cap = float(float(dist)/110.0)
    lt(turtle,90)
    for i in range(180):
        fd(turtle,cap)
        rt(turtle,1)
    lt(turtle,90)



def game():                                                     #Burada oyunu def fonksiyonu icine de tanimladik ve roundlar ve skorlarin toplanarak gitmesini sagladik
    global FirstTurtle
    global Firstscore
    global SecondTurtle
    global round_no
    round_no = round_no + 1
    print "||| Round " + str(round_no) + " |||"
    print startwith_name + "'s score = " + str(Firstscore)
    print later_name + "'s score = " + str(Secondscore)
    print startwith_name + " plays"
    E = int(raw_input("How many steps would you like to take ?\n"))         #Burada kullaniciya bir deger girmesini istiyoruz.
    Sans = 100 - E                                                          #Burada bir sans degiskeni tanimliyoruz bu degisken 100 den adamin sectigi sayiyi cikariyor.
    randompc = random.randint(0, 100)                                       #Burada bilgisayar rastgele 1 ile 100 arasinda bir sayi seciyor.
    while True:
        if E >= 100:                                                        #Burada eger kullanicinin girdigi sayi 100 den buyukse tekrar sorduruyor
            print "Choose another number between 1-100"
            E = input("How many steps would you like to take ?\n")
            continue
        if E < 100:
            if randompc <= Sans:                                            #Burada eger bilgisayarin sectigi random sayi bizim belirledigimiz sans degiskeninden kucukse basarili bir sekilde hareketi yapiyor.
                print "Succes :)"
                startwith.set_pen_color("Black")
                Firstscore = Firstscore + E
                x = [1,2,3]
                x = random.choice(x)
                if x == 1:
                    movement1(startwith,E)
                elif x == 2:
                    movement2(startwith,E)
                elif x == 3:
                    movement3(startwith,E)
                break
            else:
                print "You Failed :("
                break

def game2():
    global Secondscore
    global round_no
    round_no = round_no + 1
    print "||| Round " + str(round_no) + " |||"
    print startwith_name + "'s score = " + str(Firstscore)
    print later_name + "'s score = " + str(Secondscore)
    print later_name + " plays"
    E = int(raw_input("How many steps would you like to take ?\n"))
    Sans = (100 - E)
    randompc = random.randint(0, 100)
    while True:
        if E >= 100:
            print "Choose another number between 1-100"
            E = input("How many steps would you like to take ?\n")
            continue
        if E < 100:
            if randompc <= Sans:
                print "Succes :)"
                Secondscore = Secondscore + E
                later.set_pen_color("Black")
                x = [1, 2,3]
                x = random.choice(x)
                if x == 1:
                    movement1(later, E)
                elif x == 2:
                    movement2(later, E)
                elif x == 3:
                    movement3(later, E)
                break
            else:
                print "You Failed :("
                break
while True:
    game()
    if Firstscore >= 200:                                                      #Burada eger skor 200 u gecerse oyun bitiyor ve tekrar oynama sorusu soruluyor
        print startwith_name, "wins"
        sonsoru = raw_input("Do you want to play again ?(Yes/No)\n")
        if sonsoru == "Yes":                                                    #Verilen cevap yes ise oyun tekrar basliyor.

            start_game()
            print " "
            players = [player1_info,
                       player2_info]  # Burada liste yontemi ile playerlari tanimliyoruz ayrica burada oyuna ilk kimin baslayacagini bilgisayara
            startwith_info = random.choice(players)  # rasgele bir sekilde sectiriyoruz.
            players.remove(startwith_info)
            later_info = players[
                0]  # Burada ustte tanimladigimiz players listsindeki 0 inci yani listedeki ilk tanimi later_info olarak tanimliyoruz.
            startwith = startwith_info[
                0]  # Burada bilgisayarin rasgele sectigi yani 1. oyuncuyu startwith seklinde tanimliyoruz.
            later = later_info[0]  # Burada da oyuna 2. baslayan turte i later seklinde tanimliyoruz.
            startwith_name = startwith_info[
                1]  # Burada listedeki 1. yani aslinda 2. olan tanimi kullanip (x,y) turtlelarin bazi durumlarda hata vermeden calisabilmesi icin bu tanimi kullaniyoruz.
            later_name = later_info[1]
            Firstscore = 0  # Burada skorlari 0 diye tanitip her el kullanicinin yazdigi sayi ile toplanip eklenmesi icin fonksiyonun icinde bunu tanimliyoruz.
            Secondscore = 0
            FirstTurtle.set_pen_color("Black")
            SecondTurtle.set_pen_color("Black")
            round_no = 0

            continue
        else:
            break
    game2()
    if Secondscore >= 200:                                                     #Burada ikinci oyun kazanirsa tekrar oynama sorusu soruluyor ve oyun tekrar basliyor.
        print later_name, "wins"
        sonsoru = raw_input("Do you want to play again ?(Yes/No) ")
        while True:
            if sonsoru == "Yes":

                start_game()
                print " "
                players = [player1_info,
                           player2_info]  # Burada liste yontemi ile playerlari tanimliyoruz ayrica burada oyuna ilk kimin baslayacagini bilgisayara
                startwith_info = random.choice(players)  # rasgele bir sekilde sectiriyoruz.
                players.remove(startwith_info)
                later_info = players[
                    0]  # Burada ustte tanimladigimiz players listsindeki 0 inci yani listedeki ilk tanimi later_info olarak tanimliyoruz.
                startwith = startwith_info[
                    0]  # Burada bilgisayarin rasgele sectigi yani 1. oyuncuyu startwith seklinde tanimliyoruz.
                later = later_info[0]  # Burada da oyuna 2. baslayan turte i later seklinde tanimliyoruz.
                startwith_name = startwith_info[
                    1]  # Burada listedeki 1. yani aslinda 2. olan tanimi kullanip (x,y) turtlelarin bazi durumlarda hata vermeden calisabilmesi icin bu tanimi kullaniyoruz.
                later_name = later_info[1]
                Firstscore = 0  # Burada skorlari 0 diye tanitip her el kullanicinin yazdigi sayi ile toplanip eklenmesi icin fonksiyonun icinde bunu tanimliyoruz.
                Secondscore = 0
                FirstTurtle.set_pen_color("Black")
                SecondTurtle.set_pen_color("Black")
                round_no = 0

                continue
            else:
                break






wait_for_user()