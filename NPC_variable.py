from os import name
from random import *
import pickle
import sys
sys.path.insert(0, r'C:\PycharmProjects\Game\chars')


class Character:

    def __init__(self, name):
        #Wir speichern den Namen in einer lokalen Variable, die zum Objekt gehört
        self.name = name
        #Standart Attribute
        self.mut = 7
        self.klugheit = 7
        self.charisma = 7
        self.geschick = 7
        self.koerperkraft = 7
        self.atacke = 10
        self.parade = 8
        self.bonustreffer = 0
        self.malustreffer = 0


    def wuerfelmut(self):
        ### Wuerfel der Attribute

        # Mut
        self.zmut = randint(1, 6)
        self.gmut = self.zmut + self.mut

    def wuerfelklugheit(self):

        #Klugheit
        self.zklug = randint(1, 6)
        self.gklug = self.zklug + self.klugheit

    def wuerfelcharisma(self):

        #Charisma
        self.zchar = randint(1, 6)
        self.gchar = self.zchar + self.charisma

    def wuerfelgeschick(self):

        # Geschick
        self.zges = randint(1, 6)
        self.gges = self.zges + self.geschick


    def wuerfelkraft(self):

        #Körperkraft
        self.zkoe = randint(1, 6)
        self.gkoe = self.zkoe + self.koerperkraft


    def sonderattribute(self):
        ### Sonderattribute - Bonus - Malus
        # Bonus Körperkraft > 13 = + 1 Trefferpunkt
        if self.gkoe == 13:
            self.bonustreffer = self.bonustreffer + 1
            print('Aufgrund deiner Koerperkraft erhöen sich deine Trefferpunkte um 1')

        # Malus Körperkraft == 8 = - 1 Trefferpunkt
        if self.gkoe == 8:
            self.malustreffer = self.malustreffer - 1
            print('Aufgrund deiner Koerperkraft verringern sich deine Trefferpunkte um 1')

        # Bonus Geschick > 13 = + 1 Attacke
        if self.gges == 13:
            self.atacke = self.atacke + 1
            print('Durch deine Geschicklichkeit erhöt sich deine Attacke um 1 auf :',self.atacke)

        # Malus Geschick == 8 = - 1 auf Attacke oder Parade
        if self.gges == 8:
            print('Aufgrund deines Geschicklichkeitswertes bekommt du einen Malus auf entweder Attacke oder Parrade \nWähle jetzt 1. Attacke oder 2. Parade')
            while True:
                malusgges = input()
                if malusgges == '1':
                    self.atacke = self.atacke - 1
                    print('Deine Attacke wurde um 1 verringert auf :',self.atacke)
                    break

                elif malusgges == '2':
                    self.parade = self.parade - 1
                    print('Deine Parade wurde um 1 verringert auf :',self.parade)
                    break
                else:
                    print('Bitte wähle Atacke oder Parade')
                    continue

    def abenteurer(self):
        self.magicelf = 0
        self.magichuman = 0
        self.ritterruestung = 0
        self.sruestung = 1
        self.zwehaender = 0
        self.leben = 30

    def krieger(self):
        self.magicelf = 0
        self.magichuman = 0
        self.ritterruestung = 1
        self.sruestung = 1
        self.zwehaender = 1
        self.leben = 30

    def zwerg(self):
        self.magicelf = 0
        self.magichuman = 0
        self.ritterruestung = 0
        self.sruestung = 1
        self.zwehaender = 0
        self.leben = 35

    def elf(self):
        self.magicelf = 1
        self.magichuman = 0
        self.ritterruestung = 0
        self.sruestung = 1
        self.zwehaender = 0
        self.leben = 25
        self.astral = 25

    def magier(self):
        self.magicelf = 0
        self.magichuman = 1
        self.ritterruestung = 0
        self.sruestung = 0
        self.zwehaender = 0
        self.leben = 20
        self.astral = 30


print('Bitte gebe jetzt deinen Spielernamen ein')
username = input('Name des Charakters:' )
user = Character(username)

#Auswürfeln der Attribute
print('Bitte Wuerfel deine Attribute aus')

input('Bitte drücke Enter um Mut zu Würfeln')
user.wuerfelmut()
print('Deine Mut ist:',user.gmut)

input('Bitte drücke Enter um Klugheit zu Würfeln')
user.wuerfelklugheit()
print('Deine Klugheit ist:',user.gklug)

input('Bitte drücke Enter um Charisma zu Würfeln')
user.wuerfelcharisma()
print('Dein Charisma ist:',user.gchar)

input('Bitte drücke Enter um Geschick zu Würfeln')
user.wuerfelgeschick()
print('Dein Geschick ist:',user.gges)

input('Bitte drücke Enter um Körperkraft zu Würfeln')
user.wuerfelkraft()
print('Deine Kraft ist:', user.gkoe)


print('Deine Attribute sind wie folgt:''\nMut:',user.gmut,'\nKlugheit:',user.gklug,'\nCharisma:',user.gchar,'\nGeschick:',user.gges,'\nKoerperkraft:',user.gkoe)
input('Weiter mit Enter..')
input('Mal schauen ob dein Charakter Attributs Bonus oder Malus erhält')

user.sonderattribute()



# Klassen




# Abenteurer - Keine Grundvoraussetzung

# Der Krieger - Mut und Körperkraft min 12 - Lebenspunkte 30
def checkkrieger():
    if user.gmut > 11:
        if user.gkoe > 11:
            return


# Der Zwerg - Körperkraft und Geschick min 12 - Lebenspunkte 35
def checkzwerg():
    if user.gkoe > 11:
        if user.gges > 11:
             return


# Der Elf - Klugheit und Geschick min 12 - Lebenspunkte 25 - Astralenergie 25 ASP
def checkelf():
    if user.gklug > 11:
        if user.gges > 11:
            return


# Der Magier - Klugheit und Charisma min 12 - Lebenspunkte 20 - Astralenergie 30 ASP
def checkmagier():
    if user.gklug > 11:
        if user.gchar > 11:
             return

print('Wähle jetzt eine klasse')


while True:
    print('1. Abenteurer \n2. Der Krieger \n3. Der Zwerg \n4. Der Elf \n5. Der Magier')
    klasseninput = input('Wähle Klasse: ')
    if klasseninput == '1':
        while True:
            print('1. Abenteurer als Klasse wählen')
            print('2. Mehr über Abenteurer erfahren')
            print('3 Zurück zur Klassenauswahl')
            abenteurerinput = input()
            if abenteurerinput == '1':
                user.abenteurer()
                print('Du hast als Klasse den Abenteurer gewählt')
                break
            elif abenteurerinput == '2':
                print('Der Abenteurer \nDas ist ein Mensch, der sich für ein gefahrvolles, spannungsgeladenes Leben entschieden hat, obwohl er vom Schicksal nicht mit außergewöhnlichen Gaben gesegnet wurde \nEs gibt keine Grundvorrausetzung für den Abenteurer \nBeschränkungen: Keine magische Begabung, darf keine Ritterrüstungen und keine Zweihänder-Waffen benutzen \nLebensenergie: 30 LP')
                input('Weiter mit Enter..')
                continue
            elif abenteurerinput == '3':
                break
            else:
                continue
        continue
    elif klasseninput == '2':
        while True:
            print('1. Den Krieger als Klasse wählen')
            print('2. Mehr über den Krieger erfahren')
            print('3 Zurück zur Klassenauswahl')
            kriegerinput = input()
            if kriegerinput == '1':
                while True:
                    if checkkrieger() is True:
                        user.krieger()
                        print('Du hast die Klasse Krieger gewählt')
                        break
                        break
                        break
                    else:
                        print('Du besitzt nicht genug Mut und Körperkraft für diese Klasse')
                        break
            elif kriegerinput == '2':
                print('Der Krieger \n Ein furchloser, starke Krieger! Er geht rein und tötet! \nGrundvoraussetzung: Mut und Körperkraft min 12 \nVorzüge: Darf alle Waffen und Rüstungen benutzen \nBeschränkungen: Keinerlei magische Begabung \n Lebensenergie bei der Entstehung: 30 LP ')
                input('Weiter mit Enter..')
                continue
            elif kriegerinput == '3':
                break
            else:
                continue
        continue


    elif klasseninput == '3':
        while True:
            print('1. Den Zwerg als Klasse wählen')
            print('2. Mehr über den Zwerg erfahren')
            print('3 Zurück zur Klassenauswahl')
            zwerginput = input()
            if zwerginput == '1':
                while True:
                    if checkzwerg() is True:
                        user.zwerg()
                        print('Du hast die Klasse Zwerg gewählt')
                    else:
                        print('Du besitzt nicht genug Geschick und Körperkraft für diese Klasse')
                        break
            elif zwerginput == '2':
                print('Der Zwerg \nEin kleinwüchsiger (1,40m) Berserker! Auch er geht rein und tötet! \nGrundvoraussetzungen: Körperkraft- und Geschicklichkeits-Wert mindestens 12 \nVorzüge: hohe Lebensenergie, Zwergeninstinkt \nBeschränkungen: Er verfügt weder über Magie noch Zweihänderwaffen oder eine Ritterrüstung \nLebensenergie: 35 LP bei der Entstehung ')
                input('Weiter mit Enter..')
                continue
            elif zwerginput == '3':
                break
            else:
                continue
        continue

    elif klasseninput == '4':
        while True:
            print('1. Den Elf als Klasse wählen')
            print('2. Mehr über den Elf erfahren')
            print('3 Zurück zur Klassenauswahl')
            elfinput = input()
            if elfinput == '1':
                while True:
                    if checkelf() is True:
                        user.elf()
                        print('Du hast die Klasse Elf gewählt')
                    else:
                        print('Du besitzt nicht genug Geschick und Klugheit für diese Klasse')
                        break
            elif elfinput == '2':
                print('Der Elf \nSchwules Zaubernedes wesen.... \nGrundvoraussetzungen: Klugheits- und Geschicklichkeits-Wert mindestens 12 \nVorzüge: Magiebegabung \nBeschränkungen: Der Elf beherrscht nur einen Teil der Zauberformeln. Keine Zweihänder-Waffen, keine Ritterrüstung \nLebensenergie: 25 LP bei der Entstehung \nAstralenergie: 25 ASP bei der Entstehung. ')
                input('Weiter mit Enter..')
                continue
            elif elfinput == '3':
                break
            else:
                continue
        continue

    elif klasseninput == '5':
        while True:
            print('1. Den Magier als Klasse wählen')
            print('2. Mehr über den Magier erfahren')
            print('3 Zurück zur Klassenauswahl')
            magierinput = input()
            if magierinput == '1':
                while True:
                    if checkmagier() is True:
                        user.magier()
                        print('Du hast die Klasse Magier gewählt')
                    else:
                        print('Du besitzt nicht genug Charisma und Klugheit für diese Klasse')
                        break
            elif magierinput == '2':
                print('Der Magier \nVerweichlichtes Mutterkind \nKann licht machen \nEventuell für irgendwas anderes nützlich... weiss keiner \nGrundvoraussetzungen: Klugheits- und Charisma-Wert mindestens 12 \nVorzüge: Magiebegabung, hohe Astralenergie \nBeschränkungen: Als Rüstung ist dem Magier bestenfalls ein wattierter Waffenrock (RS 2) erlaubt, als Waffe nur Dolch oder Zauberstab \nLebensenergie: 20 LP \nAstralenergie: 30 ASP.')
                continue
            elif magierinput == '3':
                break
            else:
                continue
        continue
    else:
        print('Wähle eine Klasse')
        continue
        

pickle_out = open(r'C:\PycharmProjects\Game\chars\%s' % username, 'wb')
pickle.dump(user, pickle_out)
pickle_out.close()

print('Dein Charakter wurde erfolgreich angelegt. Viel Spaß in Aventurien')