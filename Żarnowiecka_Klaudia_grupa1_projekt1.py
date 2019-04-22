# -*- coding: utf-8 -*-
"""
Created on Mon Mar 18 09:08:12 2019
@author: Klaudia
"""
#import bibliotek
from PyQt5.QtWidgets import QWidget, QPushButton, QApplication, QLabel, QLineEdit, QGridLayout, QColorDialog, QMessageBox
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import sys
import matplotlib.pyplot as plt

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.title = 'Wyznaczenie punktu przecięcia dwóch odcinków'
        self.initInterface()
        
    def initInterface(self):
        self.setWindowTitle(self. title)

#okreslenie nazw przycisków
        self.button = QPushButton('Oblicz punkt przecięcia i narysuj wykres', self) 
        self.clrChoose=QPushButton('Zmień kolor',self)
        self.button2=QPushButton('Wyczysc dane', self)
        self.zapis=QPushButton('Zapisz', self)

#okreslenie nazw napisow
        self.polecenie=QLabel("PODAJ WSPÓŁRZĘDNE",self)
        self.polecenie2=QLabel("WSPÓŁRZĘDNE PUNKTU P:",self)
        self.punktLabel = QLabel("POŁOŻENIE PUNKTU P:", self)
        
#utworzenie pol w ktore bedziemy wpisywac wspolrzedne oraz etykiety do poszczegolnych wspolrzednych        
        self.xalabel = QLabel("Xa", self)
        self.xaEdit = QLineEdit()
        self.yalabel = QLabel("Ya", self)
        self.yaEdit = QLineEdit()
        
        self.xblabel = QLabel("Xb", self)
        self.xbEdit = QLineEdit()
        self.yblabel = QLabel("Yb", self)
        self.ybEdit = QLineEdit()
        
        self.xclabel = QLabel("Xc", self)
        self.xcEdit = QLineEdit()
        self.yclabel = QLabel("Yc", self)
        self.ycEdit = QLineEdit()
        
        self.xdlabel = QLabel("Xd", self)
        self.xdEdit = QLineEdit()
        self.ydlabel = QLabel("Yd", self)
        self.ydEdit = QLineEdit()
        
        self.xplabel = QLabel("Xp", self)
        self.xpEdit = QLineEdit()
        self.yplabel = QLabel("Yp", self)
        self.ypEdit = QLineEdit()
#utworzenie pola w ktorym bedzie wyswietlala sie lokalizacja punktu P        
        self.polozenie = QLineEdit() 
        
        #wykresy
        #podpięcie funkcji pod widżety 
        self.figure=plt.figure()
        self.canvas=FigureCanvas(self.figure)
    
#okreslenie lokalizacja poszczegolnych napisow i pol        
        layout =  QGridLayout(self)
        layout.addWidget(self.xalabel, 2, 1)
        layout.addWidget(self.xaEdit, 3, 2)
        layout.addWidget(self.yalabel, 2, 2)
        layout.addWidget(self.yaEdit, 3, 1)
        
        layout.addWidget(self.xblabel, 4, 1)
        layout.addWidget(self.xbEdit, 5, 2)
        layout.addWidget(self.yblabel, 4, 2)
        layout.addWidget(self.ybEdit, 5, 1)
        
        layout.addWidget(self.xclabel, 6, 1)
        layout.addWidget(self.xcEdit, 7, 2)
        layout.addWidget(self.yclabel, 6, 2)
        layout.addWidget(self.ycEdit, 7, 1)
        
        layout.addWidget(self.xdlabel, 8, 1)
        layout.addWidget(self.xdEdit, 9, 2)
        layout.addWidget(self.ydlabel, 8, 2)
        layout.addWidget(self.ydEdit, 9, 1)
        
        layout.addWidget(self.xplabel, 13, 1)
        layout.addWidget(self.xpEdit, 14, 2)
        layout.addWidget(self.yplabel, 13, 2)
        layout.addWidget(self.ypEdit, 14, 1)
        
        
        #lokalizacja "oblicz i narysuj wykres"
        layout.addWidget(self.button,10, 1, 1, 2)
         #lokalizacja "wyczysc pola"
        layout.addWidget(self.button2,15, 1, 1, 2)
        #lokalizacja "zapisz"
        layout.addWidget(self.zapis,16, 1, 1, 2)
        #lokalizacja "gdzie znajduje sie punkt"
        layout.addWidget(self.punktLabel, 1, 3, 1, 20)
        #lokalizacja okienka w ktorym bedzie wyswietlalo sie gdzie sie znajduje punkt
        layout.addWidget(self.polozenie, 1, 20, 1, 30)

        #definiowanie polozenia wykresu
        layout.addWidget(self.canvas, 3,3,15,50)
        #definiowanie polozenie napisu "wpisz wspolrzedne"
        layout.addWidget(self.polecenie,1,1)
        #lokalizacja napisu "wspolrzedne punktu p:"
        layout.addWidget(self.polecenie2,12,1)
        #definiowanie paska wyboru kolorow
        layout.addWidget(self.clrChoose, 11,1,1,2)
        
        #polaczenie przyciskow singal z akcja slot
        self.button.clicked.connect(self.handleButton) #podpiecie funkcji handlebutton pod przycisk button
        self.clrChoose.clicked.connect(self.clrChooseF) #podpiecie funkcji clrChooseF pod przycisk clrChoose
        self.button2.clicked.connect(self.czysc) #podpiecie funkcji czysc pod przycisk button2
        self.zapis.clicked.connect(self.zapisz) #podpiecie funkcji zapisz pod przycisk zapis
        
        
        
        

#funkcja sprawdzajaca poprawnosc wprowadzanych danych   
    def checkValues(self, element):
        if element.text().lstrip('-').replace('.','',1).isdigit():
            return float(element.text())
        else:
            element.setFocus()
            return None
        
#utworzenie funkcji definiujacej zmiane koloru jednego z odcinkow       
    def clrChooseF(self):
        color=QColorDialog.getColor()
        if color.isValid():
            print(color.name())
            self.rysuj(col=color.name())
        else:
            pass
    
            
        
    def handleButton(self):
        self.rysuj()
        
        
    def zapisz(self):           
        self.rysuj()

#funkcja definiujaca czyszczenie uzupelnionych danych za pomoca zdefiniowanego wyzej przycisku                
    def czysc(self):
        self.xaEdit.clear()
        self.yaEdit.clear()
        self.xbEdit.clear()
        self.ybEdit.clear()
        self.xcEdit.clear()
        self.ycEdit.clear()
        self.xdEdit.clear()
        self.ydEdit.clear()
        self.xpEdit.clear()
        self.ypEdit.clear()
        self.polozenie.clear()

#funkcja definiujaca rysowanie wykresu w zdefiniowanym kolorze        
    def rysuj(self, col='r'):
        Xa = self.checkValues(self.xaEdit)
        Ya = self.checkValues(self.yaEdit)
        Xb = self.checkValues(self.xbEdit)
        Yb = self.checkValues(self.ybEdit)
        Xc = self.checkValues(self.xcEdit)
        Yc = self.checkValues(self.ycEdit)
        Xd = self.checkValues(self.xdEdit)
        Yd = self.checkValues(self.ydEdit)
        
        
        if Xa or Xb or Xc or Xd !=None and Ya or Yb or Yc or Yd != None: 
            self.figure.clear() #czyszczenie 
            ax = self.figure.add_subplot(111)
            self.canvas.draw()
        else: #komunikat wyswietlajacy sie gdy wprowadzone dane są nieprawidlowe
            msg_err = QMessageBox()
            msg_err.setWindowTitle("Komunikat")
            msg_err.setStandardButtons(QMessageBox.Ok)
            msg_err.setText("Podałes błędne współrzędne!")
            msg_err.exec_()
            self.figure.clear()
            self.canvas.draw()
 #delty poszczegolnych wspolrzednych x i y           
        dXab = Xb - Xa
        dYab = Yb - Ya
        dXcd = Xd - Xc
        dYcd = Yd - Yc
        dXac = Xc - Xa
        dYac = Yc - Ya
        x = dXab*dYcd - dYab*dXcd    
            
 #obliczenia pozwalajaca okreslic lokalizacje punktu P           
        if x!= 0:
            t1 = (dXac*dYcd - dYac*dXcd)/x
            t2 = (dXac*dYab - dYac*dXab)/x
            if t1>=0 and t1<=1 and t2>=0 and t2<=1: #warunki sprawdzajace lokalizacje punktu P
                xp = Xa + t1*dXab #obliczenie wspolrzednych punktu P
                yp = Ya + t1*dYab #obliczenie wspolrzednych punktu P
                a = "{0:.3f}".format(xp) #zapisanie wspolrzednych z dokladnoscia 3 miejsc po przecinku
                b = "{0:.3f}".format(yp)#zapisanie wspolrzednych z dokladnoscia 3 miejsc po przecinku
                self.xpEdit.setText(str(a)) #podpiecie wyniku pod dane oknienko w aplikacji
                self.ypEdit.setText(str(b))#podpiecie wyniku pod dane oknienko w aplikacji
                self.polozenie.setText(str("Punkt P znajduje się na przecięciu odcinków"))
            elif 0 <= t1 <=1: #warunki sprawdzajace lokalizacje punktu P
                xp = Xa + t1*dXab#obliczenie wspolrzednych punktu P
                yp = Ya + t1*dYab#obliczenie wspolrzednych punktu P
                c = "{0:.3f}".format(xp)#zapisanie wspolrzednych z dokladnoscia 3 miejsc po przecinku
                d = "{0:.3f}".format(yp)#zapisanie wspolrzednych z dokladnoscia 3 miejsc po przecinku
                self.xpEdit.setText(str(c))
                self.ypEdit.setText(str(d))
                self.polozenie.setText(str("Punkt P znajduje się na przedłużeniu odcinka ab"))
                
            elif 0 <= t2 <=1: #warunki sprawdzajace lokalizacje punktu P
                xp = Xa + t1*dXab#obliczenie wspolrzednych punktu P
                yp = Ya + t1*dYab#obliczenie wspolrzednych punktu P
                e = "{0:.3f}".format(xp) #zapisanie wspolrzednych z dokladnoscia 3 miejsc po przecinku
                f = "{0:.3f}".format(yp) #zapisanie wspolrzednych z dokladnoscia 3 miejsc po przecinku
                self.xpEdit.setText(str(e))#podpiecie wyniku pod dane oknienko w aplikacji
                self.ypEdit.setText(str(f))#podpiecie wyniku pod dane oknienko w aplikacji
                self.polozenie.setText(str("Punkt P znajduje się na przedłużeniu odcinka bc"))
            else:
                xp = Xa + t1*dXab#obliczenie wspolrzednych punktu P
                yp = Ya + t1*dYab#obliczenie wspolrzednych punktu P
                g = "{0:.3f}".format(xp)#zapisanie wspolrzednych z dokladnoscia 3 miejsc po przecinku
                h = "{0:.3f}".format(yp)#zapisanie wspolrzednych z dokladnoscia 3 miejsc po przecinku
                self.xpEdit.setText(str(g))#podpiecie wyniku pod dane oknienko w aplikacji
                self.ypEdit.setText(str(h))#podpiecie wyniku pod dane oknienko w aplikacji
                self.polozenie.setText(str("Punkt P znajduje się na przedłużeniu obu odcinków"))
        elif x == 0: #warunki sprawdzajace lokalizacje punktu P
            self.polozenie.setText(str("Brak punktu P, odcinki są równoległe"))
                                        
        #zapisanie współrzędnych punktów do pliku
        plik = open('wyniki.txt','w')
        plik.write("|{:^15}|{:^15}|{:^15}|\n".format("Nazwa punktu", "X [m]", "Y [m]" )) #nazwy "naglowkow" oraz ich lokalizacja oraz sposob rozdzielania |
        #definiowanie lokalizacja wspolrzednych x,y poszczegolnych punktow; beda zapisane z dokladnoscia 3 miejsc po przecinku
        plik.write("|{:^15}|{:15.3f}|{:15.3f}|\n".format("A",Ya, Xa)) 
        plik.write("|{:^15}|{:15.3f}|{:15.3f}|\n".format("B",Yb, Xb))
        plik.write("|{:^15}|{:15.3f}|{:15.3f}|\n".format("C",Yc, Xc))
        plik.write("|{:^15}|{:15.3f}|{:15.3f}|\n".format("D",Yd, Xd))
        if self.xaEdit == None:
            plik.write("|{:^15.3f}|{:^15.3f}|{:^15.3f}|\n".format("P","brak", "brak")) #jezeli punkt nie istnieje to w miejscu wspolrzednych pojawi sie napis "brak"
        else:
            plik.write("|{:^15}|{:^15.3f}|{:^15.3f}|\n".format("P",yp,xp)) #wpisanie do pliku wspolrzednych punktu p
        
        plik.close() #zamkniecie pliku
        #wykres przedstwiający odcinki i punkt przecięcia odcinkóW
        self.figure.clear() #czyszczenie pozsotałowsci
        ax = self.figure.add_subplot(111)
        ax.plot([yp, Yb], [xp, Xb], 'go:')
        ax.plot([Ya, yp], [Xa, xp], 'go:')
        ax.plot([yp, Yd], [xp, Xd], 'go:')
        ax.plot([Yc, yp], [Xc, xp], 'go:')
        ax.plot([Ya, Yb], [Xa, Xb], 'bo-')
        ax.plot([Yc, Yd], [Xc, Xd], color=col, marker ='o') #kolor linii wraz z "koleczkami" na koncach
        ax.plot(yp, xp, color = 'blue', marker= 'o')
        
                #dodanie etykiet na wykresie, okreslenie rozmiaru oraz koloru czcionki dla każdego punktu
        ax.text(Ya, Xa, " A(" + str(round(Xa,3)) +";"+ str(round(Ya,3))+")", fontsize = 9, color = "black")
        ax.text(Yb, Xb, " B(" + str(round(Xb,3)) +";"+ str(round(Yb,3))+")", fontsize = 9, color = "black")
        ax.text(Yc, Xc, " C(" + str(round(Xc,3)) +";"+ str(round(Yc,3))+")", fontsize = 9, color = "black")
        ax.text(Yd, Xd, " D(" + str(round(Xd,3)) +";"+ str(round(Yd,3))+")", fontsize = 9, color = "black")
        ax.text(yp, xp, " P(" + str(round(xp,3)) +";"+ str(round(yp,3))+")", fontsize = 9, color = "black")
        self.canvas.draw()
    
   
        
if __name__ == '__main__':
    if not QApplication.instance():
        app=QApplication(sys.argv)
    else:
        app=QApplication.instance()
    window = Window()
    window.show()
    sys.exit(app.exec_())