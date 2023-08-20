from turtle import*
from random import*
from math import*
bgcolor("darkGreen")
ht()
karte_znakovi = ['2k','3k','4k','5k','6k','7k','8k','9k','Xk','Jk','Qk','Kk','Ak',
                 '2h','3h','4h','5h','6h','7h','8h','9h','Xh','Jh','Qh','Kh','Ah',
                 '2p','3p','4p','5p','6p','7p','8p','9p','Xp','Jp','Qp','Kp','Ap',
                 '2t','3t','4t','5t','6t','7t','8t','9t','Xt','Jt','Qt','Kt','At']

prepoznavanje_znaka = {'2':lambda x,y,z: dvojka(x,y,z),
                       '3':lambda x,y,z: trojka(x,y,z),
                       '4':lambda x,y,z: cetvorka(x,y,z),
                       '5':lambda x,y,z: petica(x,y,z),
                       '6':lambda x,y,z: sestica(x,y,z),
                       '7':lambda x,y,z: sedmica(x,y,z),
                       '8':lambda x,y,z: osmica(x,y,z),
                       '9':lambda x,y,z: devetka(x,y,z),
                       'X':lambda x,y,z: desetka(x,y,z),
                       'J':lambda x,y,z: decko(x,y,z),
                       'Q':lambda x,y,z: kraljica(x,y,z),
                       'K':lambda x,y,z: kralj(x,y,z),
                       'A':lambda x,y,z: kec(x,y,z)}
boje = {'k':'Red','h':'Red','p':'Black','t':'Black'}

prepoznavanje_boje = {'k':lambda:karo(),'h':lambda:herc(),'p':lambda:pik(),'t':lambda:tref()}

def karo():
    begin_fill()
    lt(45)
    for i in range(4):
        fd(5.75*sqrt(2))
        rt(90)

    end_fill()
    rt(45)

def pik():

    pu()
    fd(11.5)
    rt(180)
    pd()
    herc()

    fd(10)

    begin_fill()
    rt(15)
    fd(7.5)
    lt(180-75)
    fd(3.882)
    lt(180-75)
    fd(7.5)
    rt(15)
    end_fill()

def tref():
    bk(7.25)

    begin_fill()
    rt(90)
    fd(3.882/2)
    lt(180-75)
    fd(7.5)

    rt(185)
    circle(4, 270)

    rt(135)
    circle(4, 250)

    rt(135)
    circle(4, 270)

    end_fill()

    seth(90)
    fd(7.25)

def herc():
    begin_fill()
    lt(45)
    fd(5.75*sqrt(2))
    circle(-(5.75*sqrt(2))/2,180)
    lt(90)
    circle(-(5.75 * sqrt(2)) / 2, 180)
    fd(5.75 * sqrt(2))
    rt(45*3)
    end_fill()


def kec(x, y, z):
    pu()
    goto(-250 + 43 * y, -150 + z * 250)
    pd()
    blank()
    pencolor(boje[x])

    pu()
    tracer(True)
    rt(90)
    fd(11)
    ##fd(12.5)
    lt(90)
    fd(35 / 2)

    fd(140)

    pd()
    tracer(False)
    write('A', move=False, align='center', font=('Arial', 16, 'normal'))

    pu()
    bk(11.5)
    lt(90)
    fd(2)
    rt(90)
    pd()

    color(boje[x])
    prepoznavanje_boje[x]()

    pu()
    fd(11.5)
    rt(90)
    fd(2)
    lt(90)

    bk(140 + 37 / 2 + 8)
    rt(90)
    fd(120)
    lt(90)
    pd()

    write('A', move=False, align='center', font=('Arial', 16, 'normal'))

    pu()
    goto(-250 + y * 43 + 70.5, -150 + z * 250 + 175 / 2)
    bk(37.5)
    pd()

    write('A', move=False, align='center', font=('Arial', 50, 'normal'))

    pu()
    goto(-250 + 43 * y, -150 + z * 250)
    pd()


def dvojka(x,y,z):

    
    pu()
    goto(-250+43*y,-150+z*250)
    pd()
    blank()
    pencolor(boje[x])
    
    pu()
    tracer(True)
    rt(90)
    fd(11)
    ##fd(12.5)
    lt(90)
    fd(35/2)
    
    fd(140)

    pd()
    tracer(False)
    write(2, move=False, align='center', font=('Arial', 16, 'normal'))

    pu()
    bk(11.5)
    lt(90)
    fd(2)
    rt(90)
    pd()
    
    color(boje[x])
    prepoznavanje_boje[x]()

    pu()
    fd(11.5)
    rt(90)
    fd(2)
    lt(90)
    
    
    bk(140+37/2+8)
    rt(90)
    fd(120)
    lt(90)
    pd()

    write(2, move=False, align='center', font=('Arial', 16, 'normal'))

    pu()
    goto(-250+y*43 + 70.5,-150+ z*250+ 175/2)
    bk(37.5)
    pd()

    write(2, move=False, align='center', font=('Arial', 50, 'normal'))

    pu()
    goto(-250 + 43 * y, -150 + z * 250)
    pd()


def trojka(x, y, z):
    pu()
    goto(-250 + 43 * y, -150 + z * 250)
    pd()
    blank()
    pencolor(boje[x])

    pu()
    tracer(True)
    rt(90)
    fd(11)
    ##fd(12.5)
    lt(90)
    fd(35 / 2)

    fd(140)

    pd()
    tracer(False)
    write(3, move=False, align='center', font=('Arial', 16, 'normal'))

    pu()
    bk(11.5)
    lt(90)
    fd(2)
    rt(90)
    pd()

    color(boje[x])
    prepoznavanje_boje[x]()

    pu()
    fd(11.5)
    rt(90)
    fd(2)
    lt(90)

    bk(140 + 37 / 2 + 8)
    rt(90)
    fd(120)
    lt(90)
    pd()

    write(3, move=False, align='center', font=('Arial', 16, 'normal'))

    pu()
    goto(-250 + y * 43 + 70.5, -150 + z * 250 + 175 / 2)
    bk(37.5)
    pd()

    write(3, move=False, align='center', font=('Arial', 50, 'normal'))

    pu()
    goto(-250 + 43 * y, -150 + z * 250)
    pd()

def cetvorka(x, y, z):
    pu()
    goto(-250 + 43 * y, -150 + z * 250)
    pd()
    blank()
    pencolor(boje[x])

    pu()
    tracer(True)
    rt(90)
    fd(11)
    ##fd(12.5)
    lt(90)
    fd(35 / 2)

    fd(140)

    pd()
    tracer(False)
    write(4, move=False, align='center', font=('Arial', 16, 'normal'))

    pu()
    bk(11.5)
    lt(90)
    fd(2)
    rt(90)
    pd()

    color(boje[x])
    prepoznavanje_boje[x]()

    pu()
    fd(11.5)
    rt(90)
    fd(2)
    lt(90)

    bk(140 + 37 / 2 + 8)
    rt(90)
    fd(120)
    lt(90)
    pd()

    write(4, move=False, align='center', font=('Arial', 16, 'normal'))

    pu()
    goto(-250 + y * 43 + 70.5, -150 + z * 250 + 175 / 2)
    bk(37.5)
    pd()

    write(4, move=False, align='center', font=('Arial', 50, 'normal'))

    pu()
    goto(-250 + 43 * y, -150 + z * 250)
    pd()

def petica(x, y, z):
    pu()
    goto(-250 + 43 * y, -150 + z * 250)
    pd()
    blank()
    pencolor(boje[x])

    pu()
    tracer(True)
    rt(90)
    fd(11)
    ##fd(12.5)
    lt(90)
    fd(35 / 2)

    fd(140)

    pd()
    tracer(False)
    write(5, move=False, align='center', font=('Arial', 16, 'normal'))

    pu()
    bk(11.5)
    lt(90)
    fd(2)
    rt(90)
    pd()

    color(boje[x])
    prepoznavanje_boje[x]()

    pu()
    fd(11.5)
    rt(90)
    fd(2)
    lt(90)

    bk(140 + 37 / 2 + 8)
    rt(90)
    fd(120)
    lt(90)
    pd()

    write(5, move=False, align='center', font=('Arial', 16, 'normal'))

    pu()
    goto(-250 + y * 43 + 70.5, -150 + z * 250 + 175 / 2)
    bk(37.5)
    pd()

    write(5, move=False, align='center', font=('Arial', 50, 'normal'))

    pu()
    goto(-250 + 43 * y, -150 + z * 250)
    pd()


def sestica(x, y, z):
    pu()
    goto(-250 + 43 * y, -150 + z * 250)
    pd()
    blank()
    pencolor(boje[x])

    pu()
    tracer(True)
    rt(90)
    fd(11)
    ##fd(12.5)
    lt(90)
    fd(35 / 2)

    fd(140)

    pd()
    tracer(False)
    write(6, move=False, align='center', font=('Arial', 16, 'normal'))

    pu()
    bk(11.5)
    lt(90)
    fd(2)
    rt(90)
    pd()

    color(boje[x])
    prepoznavanje_boje[x]()

    pu()
    fd(11.5)
    rt(90)
    fd(2)
    lt(90)

    bk(140 + 37 / 2 + 8)
    rt(90)
    fd(120)
    lt(90)
    pd()

    write(6, move=False, align='center', font=('Arial', 16, 'normal'))

    pu()
    goto(-250 + y * 43 + 70.5, -150 + z * 250 + 175 / 2)
    bk(37.5)
    pd()

    write(6, move=False, align='center', font=('Arial', 50, 'normal'))

    pu()
    goto(-250 + 43 * y, -150 + z * 250)
    pd()

def sedmica(x, y, z):
    pu()
    goto(-250 + 43 * y, -150 + z * 250)
    pd()
    blank()
    pencolor(boje[x])

    pu()
    tracer(True)
    rt(90)
    fd(11)
    ##fd(12.5)
    lt(90)
    fd(35 / 2)

    fd(140)

    pd()
    tracer(False)
    write(7, move=False, align='center', font=('Arial', 16, 'normal'))

    pu()
    bk(11.5)
    lt(90)
    fd(2)
    rt(90)
    pd()

    color(boje[x])
    prepoznavanje_boje[x]()

    pu()
    fd(11.5)
    rt(90)
    fd(2)
    lt(90)

    bk(140 + 37 / 2 + 8)
    rt(90)
    fd(120)
    lt(90)
    pd()

    write(7, move=False, align='center', font=('Arial', 16, 'normal'))

    pu()
    goto(-250 + y * 43 + 70.5, -150 + z * 250 + 175 / 2)
    bk(37.5)
    pd()

    write(7, move=False, align='center', font=('Arial', 50, 'normal'))

    pu()
    goto(-250 + 43 * y, -150 + z * 250)
    pd()

def osmica(x, y, z):
    pu()
    goto(-250 + 43 * y, -150 + z * 250)
    pd()
    blank()
    pencolor(boje[x])

    pu()
    tracer(True)
    rt(90)
    fd(11)
    ##fd(12.5)
    lt(90)
    fd(35 / 2)

    fd(140)

    pd()
    tracer(False)
    write(8, move=False, align='center', font=('Arial', 16, 'normal'))

    pu()
    bk(11.5)
    lt(90)
    fd(2)
    rt(90)
    pd()

    color(boje[x])
    prepoznavanje_boje[x]()

    pu()
    fd(11.5)
    rt(90)
    fd(2)
    lt(90)

    bk(140 + 37 / 2 + 8)
    rt(90)
    fd(120)
    lt(90)
    pd()

    write(8, move=False, align='center', font=('Arial', 16, 'normal'))

    pu()
    goto(-250 + y * 43 + 70.5, -150 + z * 250 + 175 / 2)
    bk(37.5)
    pd()

    write(8, move=False, align='center', font=('Arial', 50, 'normal'))

    pu()
    goto(-250 + 43 * y, -150 + z * 250)
    pd()

def devetka(x, y, z):
    pu()
    goto(-250 + 43 * y, -150 + z * 250)
    pd()
    blank()
    pencolor(boje[x])

    pu()
    tracer(True)
    rt(90)
    fd(11)
    ##fd(12.5)
    lt(90)
    fd(35 / 2)

    fd(140)

    pd()
    tracer(False)
    write(9, move=False, align='center', font=('Arial', 16, 'normal'))

    pu()
    bk(11.5)
    lt(90)
    fd(2)
    rt(90)
    pd()

    color(boje[x])
    prepoznavanje_boje[x]()

    pu()
    fd(11.5)
    rt(90)
    fd(2)
    lt(90)

    bk(140 + 37 / 2 + 8)
    rt(90)
    fd(120)
    lt(90)
    pd()

    write(9, move=False, align='center', font=('Arial', 16, 'normal'))

    pu()
    goto(-250 + y * 43 + 70.5, -150 + z * 250 + 175 / 2)
    bk(37.5)
    pd()

    write(9, move=False, align='center', font=('Arial', 50, 'normal'))

    pu()
    goto(-250 + 43 * y, -150 + z * 250)
    pd()

def desetka(x, y, z):
    pu()
    goto(-250 + 43 * y, -150 + z * 250)
    pd()
    blank()
    pencolor(boje[x])

    pu()
    tracer(True)
    rt(90)
    fd(14)
    ##fd(12.5)
    lt(90)
    fd(35 / 2)

    fd(140)

    pd()
    tracer(False)
    write(10, move=False, align='center', font=('Arial', 16, 'normal'))

    pu()
    bk(11.5)
    lt(90)
    fd(2)
    rt(90)
    pd()

    color(boje[x])
    prepoznavanje_boje[x]()

    pu()
    fd(11.5)
    rt(90)
    fd(2)
    lt(90)

    bk(140 + 37 / 2 + 8)
    rt(90)
    fd(116)
    lt(90)
    pd()

    write(10, move=False, align='center', font=('Arial', 16, 'normal'))

    pu()
    goto(-250 + y * 43 + 70.5, -150 + z * 250 + 175 / 2)
    bk(37.5)
    pd()

    write(10, move=False, align='center', font=('Arial', 50, 'normal'))

    pu()
    goto(-250 + 43 * y, -150 + z * 250)
    pd()


def kralj(x, y, z):
    pu()
    goto(-250 + 43 * y, -150 + z * 250)
    pd()
    blank()
    pencolor(boje[x])

    pu()
    tracer(True)
    rt(90)
    fd(11)
    ##fd(12.5)
    lt(90)
    fd(35 / 2)

    fd(140)

    pd()
    tracer(False)
    write('K', move=False, align='center', font=('Arial', 16, 'normal'))

    pu()
    bk(11.5)
    lt(90)
    fd(2)
    rt(90)
    pd()

    color(boje[x])
    prepoznavanje_boje[x]()

    pu()
    fd(11.5)
    rt(90)
    fd(2)
    lt(90)

    bk(140 + 37 / 2 + 8)
    rt(90)
    fd(120)
    lt(90)
    pd()

    write('K', move=False, align='center', font=('Arial', 16, 'normal'))

    pu()
    goto(-250 + y * 43 + 70.5, -150 + z * 250 + 175 / 2)
    bk(25)


    rt(90)
    fd(50)
    lt(90)
    pd()
    pensize(3)
    fd(8.816)
    lt(100)
    fd(50.771)


    rt(20)
    fd(50.771)
    lt(100)
    fd(8.816)
    pu()

    goto(-250 + y * 43 + 70.5, -150 + z * 250 + 175 / 2)
    fd(10)
    rt(270)
    pd()

    fd(25)
    lt(90)
    fd(35)
    lt(150)
    fd(23.094)

    rt(120)
    fd(26.904)
    lt(120)
    fd(26.904)

    rt(120)
    fd(23.094)
    lt(150)
    fd(35)

    lt(90)
    fd(25)
    lt(90)

    pensize(1)
    pu()
    goto(-250 + 43 * y, -150 + z * 250)
    pd()

def kraljica(x, y, z):
    pu()
    goto(-250 + 43 * y, -150 + z * 250)
    pd()
    blank()
    pencolor(boje[x])

    pu()
    tracer(True)
    rt(90)
    fd(11)
    ##fd(12.5)
    lt(90)
    fd(35 / 2)

    fd(140)

    pd()
    tracer(False)
    write('Q', move=False, align='center', font=('Arial', 16, 'normal'))

    pu()
    bk(11.5)
    lt(90)
    fd(2)
    rt(90)
    pd()

    color(boje[x])
    prepoznavanje_boje[x]()

    pu()
    fd(11.5)
    rt(90)
    fd(2)
    lt(90)

    bk(140 + 37 / 2 + 8)
    rt(90)
    fd(120)
    lt(90)
    pd()

    write('Q', move=False, align='center', font=('Arial', 16, 'normal'))

    pu()
    goto(-250 + y * 43 + 70.5, -150 + z * 250 + 175 / 2)
    bk(35)
    pd()


    pensize(3)
    rt(90)
    fd(50)
    lt(180-63.435)
    fd(55.902)
    lt(90-26.565)

    fd(50)
    lt(90-26.565)
    fd(55.902)
    lt(180-63.435)
    fd(50)



    fd(50)
    lt(180-63.435)
    lt(30)



    fd(48.413)
    rt(90)
    fd(27.951)

    seth(180)
    fd(50)

    lt(90-26.565+60)
    fd(27.951)
    rt(90)
    fd(48.413)
    seth(0)

    fd(50)

    lt(90)

    pu()
    fd(60)
    pd()

    rt(90)
    fd(25)
    lt(90)
    fd(35)
    lt(150)
    fd(23.094)

    rt(120)
    fd(26.904)
    lt(120)
    fd(26.904)

    rt(120)
    fd(23.094)
    lt(150)
    fd(35)

    lt(90)
    fd(25)
    lt(90)

    pensize(1)
    tracer(True)
    tracer(False)

def decko(x, y, z):
    pu()
    goto(-250 + 43 * y, -150 + z * 250)
    pd()
    blank()
    pencolor(boje[x])

    pu()
    tracer(True)
    rt(90)
    fd(11)
    ##fd(12.5)
    lt(90)
    fd(35 / 2)

    fd(140)

    pd()
    tracer(False)
    write('J', move=False, align='center', font=('Arial', 16, 'normal'))

    pu()
    bk(11.5)
    lt(90)
    fd(2)
    rt(90)
    pd()

    color(boje[x])
    prepoznavanje_boje[x]()

    pu()
    fd(11.5)
    rt(90)
    fd(2)
    lt(90)

    bk(140 + 37 / 2 + 8)
    rt(90)
    fd(120)
    lt(90)
    pd()

    write('J', move=False, align='center', font=('Arial', 16, 'normal'))

    pu()
    goto(-250 + y * 43 + 70.5, -150 + z * 250 + 175 / 2)
    bk(25)
    pd()


    pensize(3)
    rt(90)
    fd(50)
    bk(100)
    fd(50)



    lt(90)
    pu()
    fd(25)
    rt(90)
    pd()

    fd(25)
    lt(60)
    fd(30)
    lt(120)
    fd(36)
    rt(90)
    circle(4,180)
    rt(90)
    fd(36)
    lt(120)
    fd(30)
    lt(60)
    fd(50)
    lt(90)



    pensize(1)
    pu()
    goto(-250 + 43 * y, -150 + z * 250)
    pd()

def blank():
    color('Black')
    fillcolor("White")
    begin_fill()
    for i in range(2):
        fd(175)
        circle(-8,90)
        fd(125)
        circle(-8,90)
    end_fill()
    color("Black")


def poledina():
    pu()
    rt(90)
    fd(8)
    lt(90)
    pd()
    begin_fill()
    fillcolor("firebrick")
    for i in range(2):
        fd(175)
        rt(90)
        fd(125)
        rt(90)
    end_fill()
    color("Black")


        
    rt(90)
    fd(12.5)
    lt(90)
    pu()
    color("red")
    fd(35/2)
    begin_fill()
    pd()
    for i in range(2):
        fd(140)
        rt(90)
        fd(100)
        rt(90)
    end_fill()

    pu()
    rt(90)
    fd(50)
    lt(90)
    fd(50)
    rt(45)
    pd()
    color("White")
    begin_fill()
    for i in range(4):
        fd(28.28)
        lt(90)

    end_fill()

    lt(45)
    pu()
    bk(50)
    lt(90)
    fd(62.5)
    lt(90)
    fd(35/2)
    rt(180)
    pd()
    color("Black")



    
def pocetak():
    
    lt(90)
    pu()
    goto(-250,-150)
    pd()
    
    blank()
    poledina()
    pu()
    
    rt(90)
    fd(35)
    lt(90)
    pd()
    blank()
    poledina()
    
    lt(90)
    pu()
    fd(51)
    rt(90)
    fd(250)
    pd()

    blank()
    poledina()
    pu()

    rt(90)
    fd(35)
    lt(90)
    pd()
    blank()
    poledina()

    pu()
    goto(-250,-150)
    pd()
    

def igra(dek_i,dek_d):
    pobjeda_igrac, vrijednost_igrac = igrac(dek_i,dek_d)

    if pobjeda_igrac:
        print('Pobijedili ste!')
        

        
    elif not pobjeda_igrac and not vrijednost_igrac:
        print("Izugbili ste, imate preko 21!")

        

    else:
        if vrijednost_igrac == 21:
                print('Dobili ste Blackjack!')
        else:        
            pobjeda_dealer, vrijednost_dealer = dealer(vrijednost_igrac,dek_d)

            if not pobjeda_dealer:
                print("Pobijedili ste!")
            
            elif pobjeda_dealer and vrijednost_dealer:
                print("Izjednačeno je!")
            else:
                print("Izgubili ste!")
        

        
     


def dealer(vrijednost,dek):
    brojac_dealer = 0
    zbroj_dealer = 0
    l = [0]
    for i in dek:

        if brojac_dealer>= 1:
            prepoznavanje_znaka[i[0]](i[1],brojac_dealer,1)


        if  brojac_dealer < 5 and zbroj_dealer < 17 and vrijednost >= zbroj_dealer:
            
            if i[0] in '23456789':
                l = [x + int(i[0]) for x in l]
            elif i[0] in 'XJQK':
                l = [x + 10 for x in l]
            else:
                l1 = l[::]
                l = [x + 1 for x in l] + [x + 11 for x in l1]

            for j in l:
                if j > 21:
                    l.remove(j)
            if l:
                zbroj_dealer = max(l)

                if brojac_dealer >= 1:
                    print("Vrijednost karata dealera: ", zbroj_dealer)


            else:
                if i[0] in 'XQJK':

                    print("Vrijednost karata dealera: ", zbroj_dealer + 10)
                else:
                    print("Vrijednost karata dealera: ", zbroj_dealer + int(i[0]))
                print('BUST Dealera')
                return False, 0



            if zbroj_dealer > vrijednost or brojac_dealer == 4:
                return True, 0
            elif zbroj_dealer == vrijednost and zbroj_dealer > 16:
                return True, vrijednost
            elif zbroj_dealer < vrijednost and zbroj_dealer > 16:
                return False, 0
            
            
        else:
            return False, 0
        brojac_dealer += 1

    
    

def igrac(dek_igrac,dealer):
    brojac_igrac = 0
    zbroj_igrac = 0
    l = [0]
    pro = 0
    for i in dek_igrac:
        pro = 0

        if brojac_igrac < 2:
            tracer(1)
            if brojac_igrac == 0:
                pitanje = input('Želite li krneuti? ')
                pro = 1
            a = '1'
            tracer(0)
            
        elif brojac_igrac < 5:
            print("Što želite sljedeće? \n 1. Hit \n 2. Stay")
            a = input("Vaš odabir: ")
        else:
            print("da")
            return True, 0

        if a in 'h1':

            prepoznavanje_znaka[i[0]](i[1],brojac_igrac,0)
            if pro == 1:
                prepoznavanje_znaka[dealer[0][0]](dealer[0][1], brojac_igrac, 1)

            if i[0] in '23456789':
                l = [x + int(i[0]) for x in l]
            elif i[0] in 'XJQK':
                l = [x + 10 for x in l]
            else:
                l1 = l[::]
                l = [x + 1 for x in l] + [x + 11 for x in l1]
            
            for j in l:
                if j > 21:
                    l.remove(j)
        
            if l:
                zbroj_igrac = max(l)
            
            else:
                print('BUST')
                return False, 0
            if brojac_igrac > 0:
                print("Vrijednost vaših karata: ", zbroj_igrac)
            
            if zbroj_igrac == 21:
                return False, 21

            if brojac_igrac == 4 and zbroj_igrac < 21:
                return True, 0
            
            
        else:
            print("Vrijednost vaših karata: ", zbroj_igrac)
            return False, zbroj_igrac 
        brojac_igrac += 1
        
            

        
        

        

            

def main():
    print('Dobrodošli u Blackjack!')
    tracer(False)
    pocetak()
    update()
    dek_igrac = sample(karte_znakovi,5)
    dek_dealer = sample(list(set(karte_znakovi) - set(dek_igrac)),5)

    ##print(dek_igrac,dek_dealer)
    igra(dek_igrac,dek_dealer)
    tracer(True)



main()    



tracer(True)
mainloop()
