import os
import time
from time import sleep
import colorama
import pystyle
from pystyle import Colors

# Beta test

colorama.init(autoreset=True)

os.system("title TOKA MASTER ")

os.chdir(os.path.dirname(os.path.abspath(__file__)))



class pao:
    def __init__(self):
        print("     ")
        pystyle.Write.Print('''                        
                                   =¿ª=*=
                               ┬╥T²─┬╤╩ƒ
                         ┌,.xpr     ;q.
                      ⌐~⌐'ºT"=⌐"    º¼
                     ┘──]]╥╤╬┬╩═─` ▒`
                    ▒>pa;ÅÅm║╙:σ..<
                   ¬"4¬"ª"}▒4Pª""'
                  ─╤`╔═╥╦╩─┼╦╝─═─
                 σm ^gτπ;oo;π>τ░
               ~"▒    '"!⌐7⌐'"`
              ═╨╗╦, ╓╔╗─`
             :bτmzατp*
            =¿ª=*=
''', Colors.blue_to_purple, interval=0)
        sleep(0.3)
        os.system("cls")

        
pao()
class po:
    def __init__(self):
        print("     ")
        pystyle.Write.Print('''                        
                                   =¿ª=*=
                               ┬╥T²─┬╤╩ƒ
                         ┌,.xpr     ;q.
                      ⌐~⌐'ºT"=⌐"    º¼
                     ┘──]]╥╤╬┬╩═─` ▒`
                    ▒>pa;ÅÅm║╙:σ..<
                   ¬"4¬"ª"}▒4Pª""'
                  ─╤`╔═╥╦╩─┼╦╝─═─
                 σm ^gτπ;oo;π>τ░
               ~"▒    '"!⌐7⌐'"`
              ═╨╗╦, ╓╔╗─`
             :bτmzατp*
            =¿ª=*=
''', Colors.blue_to_cyan, interval=0)
        sleep(0.3)
        os.system("cls")


po()
class pa1o:
    def __init__(self):
        print("     ")
        pystyle.Write.Print('''                        
                                   =¿ª=*=
                               ┬╥T²─┬╤╩ƒ
                         ┌,.xpr     ;q.
                      ⌐~⌐'ºT"=⌐"    º¼
                     ┘──]]╥╤╬┬╩═─` ▒`
                    ▒>pa;ÅÅm║╙:σ..<
                   ¬"4¬"ª"}▒4Pª""'
                  ─╤`╔═╥╦╩─┼╦╝─═─
                 σm ^gτπ;oo;π>τ░
               ~"▒    '"!⌐7⌐'"`
              ═╨╗╦, ╓╔╗─`
             :bτmzατp*
            =¿ª=*=
''', Colors.cyan_to_green, interval=0)
        sleep(0.3)
        os.system("cls")

pa1o()
class po2:
    def __init__(self):
        print("     ")
        pystyle.Write.Print('''                        
                                   =¿ª=*=
                               ┬╥T²─┬╤╩ƒ
                         ┌,.xpr     ;q.
                      ⌐~⌐'ºT"=⌐"    º¼
                     ┘──]]╥╤╬┬╩═─` ▒`
                    ▒>pa;ÅÅm║╙:σ..<
                   ¬"4¬"ª"}▒4Pª""'
                  ─╤`╔═╥╦╩─┼╦╝─═─
                 σm ^gτπ;oo;π>τ░
               ~"▒    '"!⌐7⌐'"`
              ═╨╗╦, ╓╔╗─`
             :bτmzατp*
            =¿ª=*=
''', Colors.green_to_red, interval=0)
        sleep(0.3)
        os.system("cls")

po2()    


    
class interface:
    def __init__(self):   
        print("   ")
        pystyle.Write.Print("      ========TOKA MASTER========", Colors.blue_to_green, interval=0.03)
        print("        ")


interface()


class inp:
    def __init__(self):
        print("   ")
        Nom = pystyle.Write.Input("      [ ] Nom > ", Colors.cyan_to_green, interval=0.00)
        prenom = pystyle.Write.Input("      [ ] prenom > ", Colors.cyan_to_green, interval=0.00)
        domaine = pystyle.Write.Input("      [perso] domaine > ", Colors.cyan_to_green, interval=0.00)
        self.Nom = Nom
        self.prenom = prenom
        self.domaine = domaine


h1 = inp()


class fin:
    def __init__(self):
        os.system("cls")
        interface()
        print("    ")
        pystyle.Write.Print("      [ ] creation....", Colors.cyan_to_green, interval=0.00)
        time.sleep(0.5)
        os.system("cls")
        interface()
        print("    ")
        time.sleep(0.5)
        pystyle.Write.Print("       [ ] TERMINE....", Colors.cyan_to_green, interval=0.00)
        sleep(1)


fin()


class fichier:
    def __init__(self):
        fichier = open('{}'.format(h1.Nom) + "{}".format(h1.Nom) + ".txt", "w")
        fichier.write(f"\n ----------------------------------------------------------------------------------------------------------------------------------")
        fichier.write(f"\n  /$$$$$$$$ /$$$$$$  /$$   /$$  /$$$$$$        /$$      /$$  /$$$$$$   /$$$$$$  /$$$$$$$$ /$$$$$$$$ /$$$$$$$")
        fichier.write(f"\n |__  $$__//$$__  $$| $$  /$$/ /$$__  $$      | $$$    /$$$ /$$__  $$ /$$__  $$|__  $$__/| $$_____/| $$__  $$")
        fichier.write(f"\n    | $$  | $$  \ $$| $$ /$$/ | $$  \ $$      | $$$$  /$$$$| $$  \ $$| $$  \__/   | $$   | $$      | $$  \ $$")
        fichier.write(f"\n    | $$  | $$  | $$| $$$$$/  | $$$$$$$$      | $$ $$/$$ $$| $$$$$$$$|  $$$$$$    | $$   | $$$$$   | $$$$$$$/")
        fichier.write(f"\n    | $$  | $$  | $$| $$  $$  | $$__  $$      | $$  $$$| $$| $$__  $$ \____  $$   | $$   | $$__/   | $$__  $$")
        fichier.write(f"\n    | $$  | $$  | $$| $$\  $$ | $$  | $$      | $$\  $ | $$| $$  | $$ /$$  \ $$   | $$   | $$      | $$  \ $$")
        fichier.write(f"\n    | $$  |  $$$$$$/| $$ \  $$| $$  | $$      | $$ \/  | $$| $$  | $$|  $$$$$$/   | $$   | $$$$$$$$| $$  | $$")
        fichier.write(f"\n    |__/   \______/ |__/  \__/|__/  |__/      |__/     |__/|__/  |__/ \______/    |__/   |________/|__/  |__/")
        fichier.write(f"\n ----------------------------------------------------------------------------------------------------------------------------------")
        fichier.write(f"\n Discord :GREG PRIME !!!!!!!!#0001")
        fichier.write(f"\n            ")
        fichier.write("\n [DOMAINE PERSO] = " +'{}'.format(h1.Nom) + "@" + '{}'.format(h1.domaine))
        fichier.write("\n [DOMAINE PERSO] = " +'{}'.format(h1.prenom) + "@" + '{}'.format(h1.domaine))
        fichier.write("\n [DOMAINE PERSO] = " + '{}'.format(h1.prenom) +'{}'.format(h1.Nom) + "@" + '{}'.format(h1.domaine))
        fichier.write("\n [DOMAINE PERSO] = " + '{}'.format(h1.Nom) +'{}'.format(h1.prenom) + "@" + '{}'.format(h1.domaine))
        fichier.write("\n [DOMAINE PERSO] = " + '{}'.format(h1.prenom) +"." + '{}'.format(h1.Nom) + "@" + '{}'.format(h1.domaine))
        fichier.write("\n [DOMAINE PERSO] = " + '{}'.format(h1.Nom) +"." + '{}'.format(h1.prenom) + "@" + '{}'.format(h1.domaine))
        fichier.write("\n [DOMAINE PERSO] = " + '{}'.format(h1.Nom) + '{}'.format(h1.prenom) + "_" + "@" + '{}'.format(h1.domaine))
        fichier.write("\n [DOMAINE PERSO] = " + '{}'.format(h1.prenom) + '{}'.format(h1.Nom) + "_" + "@" + '{}'.format(h1.domaine))
        fichier.write("\n [DOMAINE PERSO] = " + '{}'.format(h1.Nom) + '{}'.format(h1.prenom) + "-" + "@" + '{}'.format(h1.domaine))
        fichier.write("\n [DOMAINE PERSO] = " + '{}'.format(h1.prenom) + '{}'.format(h1.Nom) + "-" + "@" + '{}'.format(h1.domaine))
        fichier.write(f"\n            ")
        fichier.write("\n [GMAIL] = " +'{}'.format(h1.Nom) + "@" + "gmail.com")
        fichier.write("\n [GMAIL] = " +'{}'.format(h1.prenom) + "@" + "gmail.com")
        fichier.write("\n [GMAIL] = " + '{}'.format(h1.prenom) +'{}'.format(h1.Nom) + "@" + "gmail.com")
        fichier.write("\n [GMAIL] = " + '{}'.format(h1.Nom) +'{}'.format(h1.prenom) + "@" + "gmail.com")
        fichier.write("\n [GMAIL] = " + '{}'.format(h1.prenom) +"." + '{}'.format(h1.Nom) + "@" + "gmail.com")
        fichier.write("\n [GMAIL] = " + '{}'.format(h1.Nom) +"." + '{}'.format(h1.prenom) + "@" + "gmail.com")
        fichier.write("\n [GMAIL] = " + '{}'.format(h1.Nom) + '{}'.format(h1.prenom) + "_" + "@" + "gmail.com")
        fichier.write("\n [GMAIL] = " + '{}'.format(h1.prenom) + '{}'.format(h1.Nom) + "_" + "@" + "gmail.com")
        fichier.write("\n [GMAIL] = " + '{}'.format(h1.Nom) + '{}'.format(h1.prenom) + "-" + "@" + "gmail.com")
        fichier.write("\n [GMAIL] = " + '{}'.format(h1.prenom) + '{}'.format(h1.Nom) + "-" + "@" + "gmail.com")
        fichier.write(f"\n            ")
        fichier.write("\n [ICLOUD] = " +'{}'.format(h1.Nom) + "@" + "icloud.com")
        fichier.write("\n [ICLOUD] = " +'{}'.format(h1.prenom) + "@" + "icloud.com")
        fichier.write("\n [ICLOUD] = " + '{}'.format(h1.prenom) +'{}'.format(h1.Nom) + "@" + "icloud.com")
        fichier.write("\n [ICLOUD] = " + '{}'.format(h1.Nom) +'{}'.format(h1.prenom) + "@" + "icloud.com")
        fichier.write("\n [ICLOUD] = " + '{}'.format(h1.prenom) +"." + '{}'.format(h1.Nom) + "@" + "icloud.com")
        fichier.write("\n [ICLOUD] = " + '{}'.format(h1.Nom) +"." + '{}'.format(h1.prenom) + "@" + "icloud.com")
        fichier.write("\n [ICLOUD] = " + '{}'.format(h1.Nom) + '{}'.format(h1.prenom) + "_" + "@" + "icloud.com")
        fichier.write("\n [ICLOUD] = " + '{}'.format(h1.prenom) + '{}'.format(h1.Nom) + "_" + "@" + "icloud.com")
        fichier.write("\n [ICLOUD] = " + '{}'.format(h1.Nom) + '{}'.format(h1.prenom) + "-" + "@" + "icloud.com")
        fichier.write("\n [ICLOUD] = " + '{}'.format(h1.prenom) + '{}'.format(h1.Nom) + "-" + "@" + "icloud.com")
        fichier.write(f"\n            ")
        fichier.write("\n [YAHOO] = " +'{}'.format(h1.Nom) + "@" + "yahoo.fr")
        fichier.write("\n [YAHOO] = " +'{}'.format(h1.prenom) + "@" + "yahoo.fr")
        fichier.write("\n [YAHOO] = " + '{}'.format(h1.prenom) +'{}'.format(h1.Nom) + "@" + "yahoo.fr")
        fichier.write("\n [YAHOO] = " + '{}'.format(h1.Nom) +'{}'.format(h1.prenom) + "@" + "yahoo.fr")
        fichier.write("\n [YAHOO] = " + '{}'.format(h1.prenom) +"." + '{}'.format(h1.Nom) + "@" + "yahoo.fr")
        fichier.write("\n [YAHOO] = " + '{}'.format(h1.Nom) +"." + '{}'.format(h1.prenom) + "@" + "")
        fichier.write("\n [YAHOO] = " + '{}'.format(h1.Nom) + '{}'.format(h1.prenom) + "_" + "@" + "yahoo.fr")
        fichier.write("\n [YAHOO] = " + '{}'.format(h1.prenom) + '{}'.format(h1.Nom) + "_" + "@" + "yahoo.fr")
        fichier.write("\n [YAHOO] = " + '{}'.format(h1.Nom) + '{}'.format(h1.prenom) + "-" + "@" + "yahoo.fr")
        fichier.write("\n [YAHOO] = " + '{}'.format(h1.prenom) + '{}'.format(h1.Nom) + "-" + "@" + "yahoo.fr")





fichier()
