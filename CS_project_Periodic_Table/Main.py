import tkinter
from tkinter import *
from tkinter import messagebox

#Window size

gui = Tk(className=' Periodic Table')
gui.geometry('865x800')
gui.resizable(False,False)

global counter
counter = 1

#Font

text = Text(gui,height=15, font=('calibri'))

#All Groups

group1 = StringVar()
Group1 = Label(gui,textvariable=group1)
group1.set('1')
Group1.place(x=52,y=15)

group2 = StringVar()
Group2 = Label(gui,textvariable=group2)
group2.set('2')
Group2.place(x=96,y=70)

group3 = StringVar()
Group3 = Label(gui,textvariable=group3)
group3.set('3')
Group3.place(x=140,y=180)

group4 = StringVar()
Group4 = Label(gui,textvariable=group4)
group4.set('4')
Group4.place(x=184,y=180)

group5 = StringVar()
Group5 = Label(gui,textvariable=group5)
group5.set('5')
Group5.place(x=228,y=180)

group6 = StringVar()
Group6 = Label(gui,textvariable=group6)
group6.set('6')
Group6.place(x=272,y=180)

group7 = StringVar()
Group7 = Label(gui,textvariable=group7)
group7.set('7')
Group7.place(x=316,y=180)

group8 = StringVar()
Group8 = Label(gui,textvariable=group8)
group8.set('8')
Group8.place(x=360,y=180)

group9 = StringVar()
Group9 = Label(gui,textvariable=group9)
group9.set('9')
Group9.place(x=404,y=180)

group10 = StringVar()
Group10 = Label(gui,textvariable=group10)
group10.set('10')
Group10.place(x=444,y=180)

group11 = StringVar()
Group11 = Label(gui,textvariable=group11)
group11.set('11')
Group11.place(x=488,y=180)

group12 = StringVar()
Group12 = Label(gui,textvariable=group12)
group12.set('12')
Group12.place(x=532,y=180)

group13 = StringVar()
Group13 = Label(gui,textvariable=group13)
group13.set('13')
Group13.place(x=576,y=70)

group14 = StringVar()
Group14 = Label(gui,textvariable=group14)
group14.set('14')
Group14.place(x=620,y=70)

group15 = StringVar()
Group15 = Label(gui,textvariable=group15)
group15.set('15')
Group15.place(x=664,y=70)

group16 = StringVar()
Group16 = Label(gui,textvariable=group16)
group16.set('16')
Group16.place(x=708,y=70)

group17 = StringVar()
Group17 = Label(gui,textvariable=group17)
group17.set('17')
Group17.place(x=752,y=70)

group18 = StringVar()
Group18 = Label(gui,textvariable=group18)
group18.set('18')
Group18.place(x=796,y=15)

#All Periods 

period1 = StringVar()
Period1 = Label(gui,textvariable=period1)
period1.set('1')
Period1.place(x=20,y=52)

period2 = StringVar()
Period2 = Label(gui,textvariable=period2)
period2.set('2')
Period2.place(x=20,y=108)

period3 = StringVar()
Period3 = Label(gui,textvariable=period3)
period3.set('3')
Period3.place(x=20,y=162)

period4 = StringVar()
Period4 = Label(gui,textvariable=period4)
period4.set('4')
Period4.place(x=20,y=218)

period5 = StringVar()
Period5 = Label(gui,textvariable=period5)
period5.set('5')
Period5.place(x=20,y=272)

period6 = StringVar()
Period6 = Label(gui,textvariable=period6)
period6.set('6')
Period6.place(x=20,y=328)

period7 = StringVar()
Period7 = Label(gui,textvariable=period7)
period7.set('7')
Period7.place(x=20,y=382)

period6 = StringVar()
Period6 = Label(gui,textvariable=period6)
period6.set('6')
Period6.place(x=150,y=463)

period7 = StringVar()
Period7 = Label(gui,textvariable=period7)
period7.set('7')
Period7.place(x=150,y=518)

#Subcategory Names

line1 = StringVar()
Line1 = Label(gui,textvariable=line1,font=(text,10))
line1.set('Alkali Metals')
Line1.place(x=204,y=575)

line2 = StringVar()
Line2 = Label(gui,textvariable=line2,font=(text,10))
line2.set('Alkaline Earth Metals')
Line2.place(x=380,y=575)

line3 = StringVar()
Line3 = Label(gui,textvariable=line3,font=(text,10))
line3.set('Transition Metals')
Line3.place(x=556,y=575)

line4 = StringVar()
Line4 = Label(gui,textvariable=line4,font=(text,10))
line4.set('Post-Transition Metals')
Line4.place(x=204,y=630)

line5 = StringVar()
Line5 = Label(gui,textvariable=line5,font=(text,10))
line5.set('Metalloids')
Line5.place(x=380,y=630)

line6 = StringVar()
Line6 = Label(gui,textvariable=line6,font=(text,10))
line6.set('Reactive Non-Metals')
Line6.place(x=556,y=630)

line7 = StringVar()
Line7 = Label(gui,textvariable=line7,font=(text,10))
line7.set('Noble Gases')
Line7.place(x=204,y=685)

line8 = StringVar()
Line8 = Label(gui,textvariable=line8,font=(text,10))
line8.set('Lanthanides')
Line8.place(x=380,y=685)

line9 = StringVar()
Line9 = Label(gui,textvariable=line9,font=(text,10))
line9.set('Actinides')
Line9.place(x=556,y=685)

line10 = StringVar()
Line10 = Label(gui,textvariable=line10,font=(text,10))
line10.set('Unknown properties')
Line10.place(x=380,y=740)

#Extra

lanthanides = StringVar()
Lanthanides = Label(gui,textvariable=lanthanides,font=(text,10))
lanthanides.set('Lanthanides')
Lanthanides.place(x=65,y=463)

line10 = StringVar()
Line10 = Label(gui,textvariable=line10,font=(text,10))
line10.set('Actinides')
Line10.place(x=80,y=518)

#Subcategories

def alkali_metals():
        S = Toplevel()
        s = StringVar()
        sub = Label(S,textvariable=s,justify=LEFT,font=(text,14),bg='#339665')
        s.set('The alkali metals consist of the chemical elements lithium, \nsodium, potassium, rubidium, caesium, and francium. \nTogether with hydrogen they constitute group 1, which lies \nin the s-block of the periodic table.')
        sub.place(x=0,y=0)
        S.title('Alkali_Metals')
        S.geometry("500x150")
        S.configure(bg='#339665')
        S.resizable(False,False)
        exit_button = tkinter.Button(S, text="Close", command=S.destroy, height=2,width=4,bg='#cc0000',activebackground='#8e0000')
        exit_button.place(x=230,y=100)

Alkali_metals = tkinter.Button(gui,command=alkali_metals,width=1,height=1,bg='#339665',activebackground='#2e7e68')

Alkali_metals.place(x=184,y=575)

def alkaline_earth_metals():
        S = Toplevel()
        s = StringVar()
        sub = Label(S,textvariable=s,justify=LEFT,font=(text,14),bg='#ff0000')
        s.set('The alkaline earth metals are six chemical elements in \ngroup 2 of the periodic table. They are beryllium, \nmagnesium, calcium, strontium, barium, and radium. The \nelements have very similar properties: they are all shiny, \nsilvery-white, somewhat reactive metals at standard \ntemperature and pressure.')
        sub.place(x=0,y=0)
        S.title('Alkaline Earth Metals')
        S.geometry("500x200")
        S.configure(bg='#ff0000')
        S.resizable(False,False)
        exit_button = tkinter.Button(S, text="Close", command=S.destroy, height=2,width=4,bg='#cc0000',activebackground='#8e0000')
        exit_button.place(x=230,y=150)

Alkaline_earth_metals = tkinter.Button(gui,command=alkaline_earth_metals,width=1,height=1,bg='#ff0000',activebackground='#b10000')

Alkaline_earth_metals.place(x=360,y=575)

def transition_metals():
        S = Toplevel()
        s = StringVar()
        sub = Label(S,textvariable=s,justify=LEFT,font=(text,14),bg='#7d2cff')
        s.set('In chemistry, a transition metal is a chemical element in the \nd-block of the periodic table, though the elements of group \n12 are sometimes excluded. The lanthanide and actinide \nelements are called inner transition metals and are \nsometimes considered to be transition metals as well.')
        sub.place(x=0,y=0)
        S.title('Transition Metals')
        S.geometry("500x175")
        S.configure(bg='#7d2cff')
        S.resizable(False,False)
        exit_button = tkinter.Button(S, text="Close", command=S.destroy, height=2,width=4,bg='#cc0000',activebackground='#8e0000')
        exit_button.place(x=230,y=125)

Transition_metals = tkinter.Button(gui,command=transition_metals,width=1,height=1,bg='#7d2cff',activebackground='#6223c9')

Transition_metals.place(x=536,y=575)

def post_transition_metals():
        S = Toplevel()
        s = StringVar()
        sub = Label(S,textvariable=s,justify=LEFT,font=(text,14),bg='#54ce00')
        s.set('The metallic elements in the periodic table located \nbetween the transition metals to their left and the \nchemically weak nonmetallic metalloids to their right have \nreceived many names in the literature, such as \npost-transition metals, poor metals, other metals, p-block \nmetals and chemically weak metals.')
        sub.place(x=0,y=0)
        S.title('Post Transition Metals')
        S.geometry("500x200")
        S.configure(bg='#54ce00')
        S.resizable(False,False)
        exit_button = tkinter.Button(S, text="Close", command=S.destroy, height=2,width=4,bg='#cc0000',activebackground='#8e0000')
        exit_button.place(x=230,y=150)

Post_transition_metals = tkinter.Button(gui,command=post_transition_metals,width=1,height=1,bg='#54ce00',activebackground='#54aa00')

Post_transition_metals.place(x=184,y=630)

def metalloids():
        S = Toplevel()
        s = StringVar()
        sub = Label(S,textvariable=s,justify=LEFT,font=(text,14),bg='#b46f02')
        s.set('A metalloid is a type of chemical element which has a \npreponderance of properties in between, or that are a \nmixture of, those of metals and nonmetals. There is no \nstandard definition of a metalloid and no complete \nagreement on which elements are metalloids.')
        sub.place(x=0,y=0)
        S.title('Metalloids')
        S.geometry("500x175")
        S.configure(bg='#b46f02')
        S.resizable(False,False)
        exit_button = tkinter.Button(S, text="Close", command=S.destroy, height=2,width=4,bg='#cc0000',activebackground='#8e0000')
        exit_button.place(x=230,y=125)

Metalloids = tkinter.Button(gui,command=metalloids,width=1,height=1,bg='#b46f02',activebackground='#995e00')

Metalloids.place(x=360,y=630)

def reactive_non_metals():
        S = Toplevel()
        s = StringVar()
        sub = Label(S,textvariable=s,justify=LEFT,font=(text,14),bg='#7f96ff')
        s.set('A nonmetal is a chemical element generally characterized \nby low density and high electronegativity. They range from \ncolorless gases like hydrogen to shiny solids like the \ngraphite form of carbon. Nonmetals are often poor \nconductors of heat and electricity, and when solid tend to \nbe brittle or crumbly.')
        sub.place(x=0,y=0)
        S.title('Reactive Non-Metals')
        S.geometry("500x200")
        S.configure(bg='#7f96ff')
        S.resizable(False,False)
        exit_button = tkinter.Button(S, text="Close", command=S.destroy, height=2,width=4,bg='#cc0000',activebackground='#8e0000')
        exit_button.place(x=230,y=150)

Reactive_non_metals = tkinter.Button(gui,command=reactive_non_metals,width=1,height=1,bg='#7f96ff',activebackground='#687bd1')

Reactive_non_metals.place(x=536,y=630)

def noble_gases():
        S = Toplevel()
        s = StringVar()
        sub = Label(S,textvariable=s,justify=LEFT,font=(text,14),bg='#e90076')
        s.set('The noble gases make up a class of chemical elements \nwith similar properties; under standard conditions, they are \nall odorless, colorless, monatomic gases with very low \nchemical reactivity. The six naturally occurring noble gases \nare helium, neon, argon, krypton, xenon, and the \nradioactive radon.')
        sub.place(x=0,y=0)
        S.title('Noble Gases')
        S.geometry("500x200")
        S.configure(bg='#e90076')
        S.resizable(False,False)
        exit_button = tkinter.Button(S, text="Close", command=S.destroy, height=2,width=4,bg='#cc0000',activebackground='#8e0000')
        exit_button.place(x=230,y=150)

Noble_gases = tkinter.Button(gui,command=noble_gases,width=1,height=1,bg='#e90076',activebackground='#b90076')

Noble_gases.place(x=184,y=685)

def lanthanides():
        S = Toplevel()
        s = StringVar()
        sub = Label(S,textvariable=s,justify=LEFT,font=(text,14),bg='#2986cc')
        s.set('The lanthanide or lanthanoid series of chemical elements \ncomprises the 15 metallic chemical elements with atomic \nnumbers 57-71, from lanthanum through lutetium. These \nelements, along with the chemically similar elements \nscandium and yttrium, are often collectively known as the \nrare-earth elements or rare-earth metals.')
        sub.place(x=0,y=0)
        S.title('Lanthanides')
        S.geometry("500x200")
        S.configure(bg='#2986cc')
        S.resizable(False,False)
        exit_button = tkinter.Button(S, text="Close", command=S.destroy, height=2,width=4,bg='#cc0000',activebackground='#8e0000')
        exit_button.place(x=230,y=150)

Lanthanides = tkinter.Button(gui,command=lanthanides,width=1,height=1,bg='#2986cc',activebackground='#226fa9')

Lanthanides.place(x=360,y=685)

def actinides():
        S = Toplevel()
        s = StringVar()
        sub = Label(S,textvariable=s,justify=LEFT,font=(text,14),bg='#ed7d08')
        s.set('The actinide or actinoid series encompasses the 15 \nmetallic chemical elements with atomic numbers from 89 \nto 103, actinium through lawrencium. The actinide series \nderives its name from the first element in the series, \nactinium.')
        sub.place(x=0,y=0)
        S.title('Actinides')
        S.geometry("500x175")
        S.configure(bg='#ed7d08')
        S.resizable(False,False)
        exit_button = tkinter.Button(S, text="Close", command=S.destroy, height=2,width=4,bg='#cc0000',activebackground='#8e0000')
        exit_button.place(x=230,y=125)

Actinides = tkinter.Button(gui,command=actinides,width=1,height=1,bg='#ed7d08',activebackground='#cf6d07')

Actinides.place(x=536,y=685)

def unknown_properties():
        S = Toplevel()
        s = StringVar()
        sub = Label(S,textvariable=s,justify=LEFT,font=(text,14),bg='#bcbcbc')
        s.set('* Meitnerium\n* Darmstadtium\n* Roentgenium\n* Copernicium\n* Nihonium\n* Flerovium\n* Moscovium\n* Livermorium\n* Tennessine\n* Oganesson')
        sub.place(x=0,y=0)
        S.title('Unknown properties')
        S.geometry("150x275")
        S.configure(bg='#bcbcbc')
        S.resizable(False,False)
        exit_button = tkinter.Button(S, text="Close", command=S.destroy, height=2,width=4,bg='#cc0000',activebackground='#8e0000')
        exit_button.place(x=55,y=225)

Unknown_properties = tkinter.Button(gui,command=unknown_properties,width=1,height=1,bg='#bcbcbc',activebackground='#8a8a8a')

Unknown_properties.place(x=360,y=740)

#Elements of Group-1

def hydrogen():
        E = Toplevel()
        e = StringVar()
        ele = Label(E,textvariable=e,justify=LEFT,font=(text,14),bg='#7f96ff')
        e.set('Hydrogen is the chemical element with the symbol H and \natomic number 1. Hydrogen is the lightest element. \nAt standard conditions hydrogen is a gas of diatomic \nmolecules having the formula H₂. It is colorless, odorless, \ntasteless, non-toxic, and highly combustible.\n\n\n Atomic number: 1                              Atomic mass: 1.007 u\n Boiling point: -252.9 °C                     Atomic Radius: 53 pm')
        ele.place(x=0,y=0)
        E.title('Hydrogen')
        E.geometry("500x265")
        E.configure(bg='#7f96ff')
        E.resizable(False,False)
        exit_button = tkinter.Button(E, text="Close", command=E.destroy, height=2,width=4,bg='#cc0000',activebackground='#8e0000')
        exit_button.place(x=230,y=215)
        
Hydrogen = tkinter.Button(gui,text='H',command=hydrogen,width=5,height=3,bg='#7f96ff',activebackground='#687bd1')

Hydrogen.place(x=35,y=35)

def lithium():
        E = Toplevel()
        e = StringVar()
        ele = Label(E,textvariable=e,justify=LEFT,font=(text,14),bg='#339665')       
        e.set('Lithium is a chemical element with the symbol Li and \natomic number 3. It is a soft, silvery-white alkali metal. \nUnder standard conditions, it is the least dense metal and \nthe least dense solid element.\n\n\n Atomic number: 3                              Atomic mass: 6.941 u\n Melting point: 180.5 °C                   Atomic Radius: 167 pm')
        ele.place(x=0,y=0)
        E.title('Lithium')
        E.geometry("500x265")
        E.configure(bg='#339665')
        E.resizable(False,False)
        exit_button = tkinter.Button(E, text="Close", command=E.destroy, height=2,width=4,bg='#cc0000',activebackground='#8e0000')
        exit_button.place(x=230,y=215)

Lithum = tkinter.Button(gui,text='Li',command=lithium,width=5,height=3,bg='#339665',activebackground='#2e7e68')

Lithum.place(x=35,y=90)

def sodium():
        E = Toplevel()
        e = StringVar()
        ele = Label(E,textvariable=e,justify=LEFT,font=(text,14),bg='#339665')
        e.set('Sodium is a chemical element with the symbol Na and \natomic number 11. It is a soft, silvery-white, highly reactive \nmetal. Sodium is an alkali metal, being in group 1 of the \nperiodic table. Its only stable isotope is ²³Na. The free \nmetal does not occur in nature, and must be prepared from \ncompounds.\n\n Atomic number: 11                          Atomic mass: 22.989 u\n Melting point: 97.79 °C                   Atomic Radius: 190 pm')
        ele.place(x=0,y=0)
        E.title('Sodium')
        E.geometry("500x265")
        E.configure(bg='#339665')
        E.resizable(False,False)
        exit_button = tkinter.Button(E, text="Close", command=E.destroy, height=2,width=4,bg='#cc0000',activebackground='#8e0000')
        exit_button.place(x=230,y=215)

Sodium = tkinter.Button(gui,text='Na',command=sodium,width=5,height=3,bg='#339665',activebackground='#2e7e68')

Sodium.place(x=35,y=145)

def potassium():
        E = Toplevel()
        e = StringVar()
        ele = Label(E,textvariable=e,justify=LEFT,font=(text,14),bg='#339665')
        e.set('Potassium is the chemical element with the symbol K and \natomic number 19. It is a silvery white metal that is soft \nenough to easily cut with a knife. Potassium metal reacts \nrapidly with atmospheric oxygen to form flaky white \npotassium peroxide in only seconds of exposure.\n\n\n Atomic number: 19                          Atomic mass: 39.098 u\n Melting point: 63.5 °C                        Atomic Radius: 98 pm')
        ele.place(x=0,y=0)
        E.title('Potassium')
        E.geometry("500x265")
        E.configure(bg='#339665')
        E.resizable(False,False)
        exit_button = tkinter.Button(E, text="Close", command=E.destroy, height=2,width=4,bg='#cc0000',activebackground='#8e0000')
        exit_button.place(x=230,y=215)
        
Potassium = tkinter.Button(gui,text='K',command=potassium,width=5,height=3,bg='#339665',activebackground='#2e7e68')

Potassium.place(x=35,y=200)

def rubidium():    
        E = Toplevel()
        e = StringVar()
        ele = Label(E,textvariable=e,justify=LEFT,font=(text,14),bg='#339665')
        e.set('Rubidium is the chemical element with the symbol Rb and \natomic number 37. It is a very soft, whitish-grey solid in the \nalkali metal group, similar to potassium and caesium. \nRubidium is the first alkali metal in the group to have a \ndensity higher than water.\n\n\n Atomic number: 37                          Atomic mass: 85.467 u\n Melting point: 39.48 °C                   Atomic Radius: 265 pm')
        ele.place(x=0,y=0)
        E.title('Rubidium')
        E.geometry("500x265")
        E.configure(bg='#339665')
        E.resizable(False,False)
        exit_button = tkinter.Button(E, text="Close", command=E.destroy, height=2,width=4,bg='#cc0000',activebackground='#8e0000')
        exit_button.place(x=230,y=215)
        
Rubidium = tkinter.Button(gui,text='Rb',command=rubidium,width=5,height=3,bg='#339665',activebackground='#2e7e68')

Rubidium.place(x=35,y=255)

def caesium():
        E = Toplevel()
        e = StringVar()
        ele = Label(E,textvariable=e,justify=LEFT,font=(text,14),bg='#339665')
        e.set('Caesium is a chemical element with the symbol Cs and \natomic number 55. It is a soft, silvery-golden alkali metal \nwith a melting point of 28.5 °C, which makes it one of only \nfive elemental metals that are liquid at or near room \ntemperature.\n\n\n Atomic number: 55                        Atomic mass: 132.905 u\n Melting point: 28.44 °C                   Atomic Radius: 298 pm')
        ele.place(x=0,y=0)
        E.title('Caesium')
        E.geometry("500x265")
        E.configure(bg='#339665')
        E.resizable(False,False)
        exit_button = tkinter.Button(E, text="Close", command=E.destroy, height=2,width=4,bg='#cc0000',activebackground='#8e0000')
        exit_button.place(x=230,y=215)
        
Caesium = tkinter.Button(gui,text='Cs',command=caesium,width=5,height=3,bg='#339665',activebackground='#2e7e68')

Caesium.place(x=35,y=310)

def francium():
        E = Toplevel()
        e = StringVar()
        ele = Label(E,textvariable=e,justify=LEFT,font=(text,14),bg='#339665')
        e.set('Francium is a chemical element with the symbol Fr and \natomic number 87. It is extremely radioactive; its most \nstable isotope, francium-223, has a half-life of only 22 \nminutes. It is the second-most electropositive element, \nbehind only caesium, and is the second rarest naturally \noccurring element.\n\n Atomic number: 87                        Atomic mass: 223.000 u\n Melting point: 27.00 °C                          Atomic Radius: N/A')
        ele.place(x=0,y=0)
        E.title('Francium')
        E.geometry("500x265")
        E.configure(bg='#339665')
        E.resizable(False,False)
        exit_button = tkinter.Button(E, text="Close", command=E.destroy, height=2,width=4,bg='#cc0000',activebackground='#8e0000')
        exit_button.place(x=230,y=215)

Francium = tkinter.Button(gui,text='Fr',command=francium,width=5,height=3,bg='#339665',activebackground='#2e7e68')

Francium.place(x=35,y=365)

#Elements of Group-2

def beryllium():
        E = Toplevel()
        e = StringVar()
        ele = Label(E,textvariable=e,justify=LEFT,font=(text,14),bg='#ff0000')
        e.set('Beryllium is a chemical element with the symbol Be and \natomic number 4. It is a steel-gray, strong, lightweight and \nbrittle alkaline earth metal. It is a divalent element that \noccurs naturally only in combination with other elements to \nform minerals. Notable gemstones high in beryllium include \nberyl and chrysoberyl.\n\n Atomic number: 4                               Atomic mass: 9.012 u\n Melting point: 1287 °C                    Atomic Radius: 112 pm')
        ele.place(x=0,y=0)
        E.title('Beryllium')
        E.geometry("500x265")
        E.configure(bg='#ff0000')
        E.resizable(False,False)
        exit_button = tkinter.Button(E, text="Close", command=E.destroy, height=2,width=4,bg='#cc0000',activebackground='#8e0000')
        exit_button.place(x=230,y=215)

Beryllium = tkinter.Button(gui,text='Be',command=beryllium,width=5,height=3,bg='#ff0000',activebackground='#b10000')

Beryllium.place(x=79,y=90)

def magnesium():
        E = Toplevel()
        e = StringVar()
        ele = Label(E,textvariable=e,justify=LEFT,font=(text,14),bg='#ff0000')
        e.set('Magnesium is a chemical element with the symbol Mg and \natomic number 12. It is a shiny gray metal having a low \ndensity, low melting point and high chemical reactivity. Like \nthe other alkaline earth metals it occurs naturally only in \ncombination with other elements and it almost always has \nan oxidation state of +2.\n\n Atomic number: 12                          Atomic mass: 24.305 u\n Melting point: 650 °C                      Atomic Radius: 145 pm')
        ele.place(x=0,y=0)
        E.title('Magnesium')
        E.geometry("500x265")
        E.configure(bg='#ff0000')
        E.resizable(False,False)
        exit_button = tkinter.Button(E, text="Close", command=E.destroy, height=2,width=4,bg='#cc0000',activebackground='#8e0000')
        exit_button.place(x=230,y=215)

Magnesium = tkinter.Button(gui,text='Mg',command=magnesium,width=5,height=3,bg='#ff0000',activebackground='#b10000')

Magnesium.place(x=79,y=145)

def calcium():
        E = Toplevel()
        e = StringVar()
        ele = Label(E,textvariable=e,justify=LEFT,font=(text,14),bg='#ff0000')
        e.set('Calcium is a chemical element with the symbol Ca and \natomic number 20. As an alkaline earth metal, calcium is a \nreactive metal that forms a dark oxide-nitride layer when \nexposed to air. Its physical and chemical properties are \nmost similar to its heavier homologues strontium and \nbarium.\n\n Atomic number: 20                          Atomic mass: 40.078 u\n Melting point: 842 °C                      Atomic Radius: 194 pm')
        ele.place(x=0,y=0)
        E.title('Calcium')
        E.geometry("500x265")
        E.configure(bg='#ff0000')
        E.resizable(False,False)
        exit_button = tkinter.Button(E, text="Close", command=E.destroy, height=2,width=4,bg='#cc0000',activebackground='#8e0000')
        exit_button.place(x=230,y=215)

Calcium = tkinter.Button(gui,text='Ca',command=calcium,width=5,height=3,bg='#ff0000',activebackground='#b10000')

Calcium.place(x=79,y=200)

def strontium():
        E = Toplevel()
        e = StringVar()
        ele = Label(E,textvariable=e,justify=LEFT,font=(text,14),bg='#ff0000')
        e.set('Strontium is the chemical element with the symbol Sr and \natomic number 38. An alkaline earth metal, strontium is a \nsoft silver-white yellowish metallic element that is highly \nchemically reactive. The metal forms a dark oxide layer \nwhen it is exposed to air.\n\n\n Atomic number: 38                          Atomic mass: 87.620 u\n Melting point: 777 °C                      Atomic Radius: 219 pm')
        ele.place(x=0,y=0)
        E.title('Strontium')
        E.geometry("500x265")
        E.configure(bg='#ff0000')
        E.resizable(False,False)
        exit_button = tkinter.Button(E, text="Close", command=E.destroy, height=2,width=4,bg='#cc0000',activebackground='#8e0000')
        exit_button.place(x=230,y=215)

Strontium = tkinter.Button(gui,text='Sr',command=strontium,width=5,height=3,bg='#ff0000',activebackground='#b10000')

Strontium.place(x=79,y=255)

def barium():
        E = Toplevel()
        e = StringVar()
        ele = Label(E,textvariable=e,justify=LEFT,font=(text,14),bg='#ff0000')
        e.set('Barium is a chemical element with the symbol Ba and \natomic number 56. It is the fifth element in group 2 and is a \nsoft, silvery alkaline earth metal. Because of its high \nchemical reactivity, barium is never found in nature as a \nfree element. The most common minerals of barium are \nbaryte and witherite.\n\n Atomic number: 56                        Atomic mass: 137.327 u\n Melting point: 727 °C                      Atomic Radius: 253 pm')
        ele.place(x=0,y=0)
        E.title('Barium')
        E.geometry("500x265")
        E.configure(bg='#ff0000')
        E.resizable(False,False)
        exit_button = tkinter.Button(E, text="Close", command=E.destroy, height=2,width=4,bg='#cc0000',activebackground='#8e0000')
        exit_button.place(x=230,y=215)

Barium = tkinter.Button(gui,text='Ba',command=barium,width=5,height=3,bg='#ff0000',activebackground='#b10000')

Barium.place(x=79,y=310)

def radium():
        E = Toplevel()
        e = StringVar()
        ele = Label(E,textvariable=e,justify=LEFT,font=(text,14),bg='#ff0000')
        e.set('Radium is a chemical element with the symbol Ra and \natomic number 88. It is the sixth element in group 2 of the \nperiodic table, also known as the alkaline earth metals. \nPure radium is silvery-white, but it readily reacts with \nnitrogen upon exposure to air, forming a black surface \nlayer of radium nitride.\n\n Atomic number: 88                        Atomic mass: 226.000 u\n Melting point: 700 °C                             Atomic Radius: N/A')
        ele.place(x=0,y=0)
        E.title('Radium')
        E.geometry("500x265")
        E.configure(bg='#ff0000')
        E.resizable(False,False)
        exit_button = tkinter.Button(E, text="Close", command=E.destroy, height=2,width=4,bg='#cc0000',activebackground='#8e0000')
        exit_button.place(x=230,y=215)

Radium = tkinter.Button(gui,text='Ra',command=radium,width=5,height=3,bg='#ff0000',activebackground='#b10000')

Radium.place(x=79,y=365)

#Elements of Group-3

def scandium():
        E = Toplevel()
        e = StringVar()
        ele = Label(E,textvariable=e,justify=LEFT,font=(text,14),bg='#7d2cff')
        e.set('Scandium is a chemical element with the symbol Sc and \natomic number 21. It is a silvery-white metallic d-block \nelement. Historically, it has been classified as a rare-earth \nelement, together with yttrium and the lanthanides.\n\n\n\n Atomic number: 21                          Atomic mass: 44.955 u\n Melting point: 1541 °C                    Atomic Radius: 184 pm')
        ele.place(x=0,y=0)
        E.title('Scandium')
        E.geometry("500x265")
        E.configure(bg='#7d2cff')
        E.resizable(False,False)
        exit_button = tkinter.Button(E, text="Close", command=E.destroy, height=2,width=4,bg='#cc0000',activebackground='#8e0000')
        exit_button.place(x=230,y=215)

Scandium = tkinter.Button(gui,text='Sc',command=scandium,width=5,height=3,bg='#7d2cff',activebackground='#6223c9')

Scandium.place(x=123,y=200)

def yttrium():
        E = Toplevel()
        e = StringVar()
        ele = Label(E,textvariable=e,justify=LEFT,font=(text,14),bg='#7d2cff')
        e.set('Yttrium is a chemical element with the symbol Y and atomic \nnumber 39. It is a silvery-metallic transition metal \nchemically similar to the lanthanides and has often been \nclassified as a "rare-earth element".\n\n\n\n Atomic number: 39                          Atomic mass: 88.905 u\n Melting point: 1526 °C                    Atomic Radius: 212 pm')
        ele.place(x=0,y=0)
        E.title('Yttrium')
        E.geometry("500x265")
        E.configure(bg='#7d2cff')
        E.resizable(False,False)
        exit_button = tkinter.Button(E, text="Close", command=E.destroy, height=2,width=4,bg='#cc0000',activebackground='#8e0000')
        exit_button.place(x=230,y=215)

Yttrium = tkinter.Button(gui,text='Y',command=yttrium,width=5,height=3,bg='#7d2cff',activebackground='#6223c9')

Yttrium.place(x=123,y=255)

def lanthanum():
        E = Toplevel()
        e = StringVar()
        ele = Label(E,textvariable=e,justify=LEFT,font=(text,14),bg='#2986cc')
        e.set('Lanthanum is a chemical element with the symbol La and \natomic number 57. It is a soft, ductile, silvery-white metal \nthat tarnishes slowly when exposed to air.\n\n\n\n\n Atomic number: 57                        Atomic mass: 138.905 u\n Melting point: 920 °C                             Atomic Radius: N/A')
        ele.place(x=0,y=0)
        E.title('Lanthanum')
        E.geometry("500x265")
        E.configure(bg='#2986cc')
        E.resizable(False,False)
        exit_button = tkinter.Button(E, text="Close", command=E.destroy, height=2,width=4,bg='#cc0000',activebackground='#8e0000')
        exit_button.place(x=230,y=215)

Lanthanum = tkinter.Button(gui,text='La',command=lanthanum,width=5,height=3,bg='#2986cc',activebackground='#226fa9')

Lanthanum.place(x=123,y=310)

def actinium():
        E = Toplevel()
        e = StringVar()
        ele = Label(E,textvariable=e,justify=LEFT,font=(text,14),bg='#ed7d08')
        e.set('Actinium is a chemical element with the symbol Ac and \natomic number 89. It was first isolated by Friedrich Oskar \nGiesel in 1902, who gave it the name emanium; the \nelement got its name by being wrongly identified with a \nsubstance André-Louis Debierne found in 1899 and called \nactinium.\n\n Atomic number: 89                        Atomic mass: 227.000 u\n Melting point: 1050 °C                           Atomic Radius: N/A')
        ele.place(x=0,y=0)
        E.title('Actinium')
        E.geometry("500x265")
        E.configure(bg='#ed7d08')
        E.resizable(False,False)
        exit_button = tkinter.Button(E, text="Close", command=E.destroy, height=2,width=4,bg='#cc0000',activebackground='#8e0000')
        exit_button.place(x=230,y=215)

Actinium = tkinter.Button(gui,text='Ac',command=actinium,width=5,height=3,bg='#ed7d08',activebackground='#cf6d07')

Actinium.place(x=123,y=365)

#Elements of Group-4

def titanium():
        E = Toplevel()
        e = StringVar()
        ele = Label(E,textvariable=e,justify=LEFT,font=(text,14),bg='#7d2cff')
        e.set('Titanium is a chemical element with the symbol Ti and \natomic number 22. Found in nature only as an oxide, it can \nbe reduced to produce a lustrous transition metal with a \nsilver color, low density, and high strength, resistant to \ncorrosion in sea water, aqua regia, and chlorine.\n\n\n Atomic number: 22                          Atomic mass: 47.867 u\n Melting point: 1668 °C                    Atomic Radius: 176 pm')
        ele.place(x=0,y=0)
        E.title('Titanium')
        E.geometry("500x265")
        E.configure(bg='#7d2cff')
        E.resizable(False,False)
        exit_button = tkinter.Button(E, text="Close", command=E.destroy, height=2,width=4,bg='#cc0000',activebackground='#8e0000')
        exit_button.place(x=230,y=215)
        
Titanium = tkinter.Button(gui,text='Ti',command=titanium,width=5,height=3,bg='#7d2cff',activebackground='#6223c9')

Titanium.place(x=167,y=200)

def zirconium():
        E = Toplevel()
        e = StringVar()
        ele = Label(E,textvariable=e,justify=LEFT,font=(text,14),bg='#7d2cff')
        e.set('Zirconium is a chemical element with the symbol Zr and \natomic number 40. The name zirconium is derived from the \nname of the mineral zircon, the most important source of \nzirconium. The word is related to Persian zargun.\n\n\n Atomic number: 40                          Atomic mass: 91.224 u\n Melting point: 1854.85 °C               Atomic Radius: 206 pm')
        ele.place(x=0,y=0)
        E.title('Zirconium')
        E.geometry("500x265")
        E.configure(bg='#7d2cff')
        E.resizable(False,False)
        exit_button = tkinter.Button(E, text="Close", command=E.destroy, height=2,width=4,bg='#cc0000',activebackground='#8e0000')
        exit_button.place(x=230,y=215)
        
Zirconium = tkinter.Button(gui,text='Zr',command=zirconium,width=5,height=3,bg='#7d2cff',activebackground='#6223c9')

Zirconium.place(x=167,y=255)

def hafnium():
        E = Toplevel()
        e = StringVar()
        ele = Label(E,textvariable=e,justify=LEFT,font=(text,14),bg='#7d2cff')
        e.set('Hafnium is a chemical element with the symbol Hf and \natomic number 72. A lustrous, silvery gray, tetravalent \ntransition metal, hafnium chemically resembles zirconium \nand is found in many zirconium minerals.\n\n\n Atomic number: 72                          Atomic mass: 178.49 u\n Melting point: 2227 °C                    Atomic Radius: 208 pm')
        ele.place(x=0,y=0)
        E.title('Hafnium')
        E.geometry("500x265")
        E.configure(bg='#7d2cff')
        E.resizable(False,False)
        exit_button = tkinter.Button(E, text="Close", command=E.destroy, height=2,width=4,bg='#cc0000',activebackground='#8e0000')
        exit_button.place(x=230,y=215)
        
Hafnium = tkinter.Button(gui,text='Hf',command=hafnium,width=5,height=3,bg='#7d2cff',activebackground='#6223c9')

Hafnium.place(x=167,y=310)

def rutherfordium():
        E = Toplevel()
        e = StringVar()
        ele = Label(E,textvariable=e,justify=LEFT,font=(text,14),bg='#7d2cff')
        e.set('Rutherfordium is a chemical element with the symbol Rf \nand atomic number 104, named after physicist Ernest \nRutherford. As a synthetic element, it is not found in nature \nand can only be made in a particle accelerator.\n\n\n Atomic number: 104                             Atomic mass: 267 u\n Melting point: 2100 °C                           Atomic Radius: N/A')
        ele.place(x=0,y=0)
        E.title('Rutherfordium')
        E.geometry("500x265")
        E.configure(bg='#7d2cff')
        E.resizable(False,False)
        exit_button = tkinter.Button(E, text="Close", command=E.destroy, height=2,width=4,bg='#cc0000',activebackground='#8e0000')
        exit_button.place(x=230,y=215)
        
Rutherfordium = tkinter.Button(gui,text='Rf',command=rutherfordium,width=5,height=3,bg='#7d2cff',activebackground='#6223c9')

Rutherfordium.place(x=167,y=365)

#Elements of Group-5

def vanadium():
        E = Toplevel()
        e = StringVar()
        ele = Label(E,textvariable=e,justify=LEFT,font=(text,14),bg='#7d2cff')
        e.set('Vanadium is a chemical element with the symbol V and \natomic number 23. It is a hard, silvery-grey, malleable \ntransition metal. The elemental metal is rarely found in \nnature, but once isolated artificially, the formation of an \noxide layer somewhat stabilizes the free metal against \nfurther oxidation.\n\n Atomic number: 23                          Atomic mass: 50.941 u\n Melting point: 1910 °C                    Atomic Radius: 171 pm')
        ele.place(x=0,y=0)
        E.title('Vanadium')
        E.geometry("500x265")
        E.configure(bg='#7d2cff')
        E.resizable(False,False)
        exit_button = tkinter.Button(E, text="Close", command=E.destroy, height=2,width=4,bg='#cc0000',activebackground='#8e0000')
        exit_button.place(x=230,y=215)
        
Vanadium = tkinter.Button(gui,text='V',command=vanadium,width=5,height=3,bg='#7d2cff',activebackground='#6223c9')

Vanadium.place(x=211,y=200)

def niobium():
        E = Toplevel()
        e = StringVar()
        ele = Label(E,textvariable=e,justify=LEFT,font=(text,14),bg='#7d2cff')
        e.set('Niobium is a chemical element with chemical symbol Nb \nand atomic number 41. It is a light grey, crystalline, and \nductile transition metal. Pure niobium has a Mohs hardness \nrating similar to pure titanium, and it has similar ductility to \niron.\n\n\n Atomic number: 41                          Atomic mass: 92.906 u\n Melting point: 2477 °C                    Atomic Radius: 198 pm')
        ele.place(x=0,y=0)
        E.title('Niobium')
        E.geometry("500x265")
        E.configure(bg='#7d2cff')
        E.resizable(False,False)
        exit_button = tkinter.Button(E, text="Close", command=E.destroy, height=2,width=4,bg='#cc0000',activebackground='#8e0000')
        exit_button.place(x=230,y=215)
        
Niobium = tkinter.Button(gui,text='Nb',command=niobium,width=5,height=3,bg='#7d2cff',activebackground='#6223c9')

Niobium.place(x=211,y=255)

def tantalum():
        E = Toplevel()
        e = StringVar()
        ele = Label(E,textvariable=e,justify=LEFT,font=(text,14),bg='#7d2cff')
        e.set('Tantalum is a chemical element with the symbol Ta and \natomic number 73. Previously known as tantalium, it is \nnamed after Tantalus, a figure in Greek mythology. \nTantalum is a very hard, ductile, lustrous, blue-gray \ntransition metal that is highly corrosion-resistant.\n\n\n Atomic number: 73                          Atomic mass: 180.94 u\n Melting point: 3020 °C                    Atomic Radius: 200 pm')
        ele.place(x=0,y=0)
        E.title('Tantalum')
        E.geometry("500x265")
        E.configure(bg='#7d2cff')
        E.resizable(False,False)
        exit_button = tkinter.Button(E, text="Close", command=E.destroy, height=2,width=4,bg='#cc0000',activebackground='#8e0000')
        exit_button.place(x=230,y=215)
        
Tantalum = tkinter.Button(gui,text='Ta',command=tantalum,width=5,height=3,bg='#7d2cff',activebackground='#6223c9')

Tantalum.place(x=211,y=310)

def dubnium():
        E = Toplevel()
        e = StringVar()
        ele = Label(E,textvariable=e,justify=LEFT,font=(text,14),bg='#7d2cff')
        e.set('Dubnium is a synthetic chemical element with the symbol \nDb and atomic number 105. It is highly radioactive: the \nmost stable known isotope, dubnium-268, has a half-life of \nabout 16 hours. This greatly limits extended research on \nthe element. Dubnium does not occur naturally on Earth \nand is produced artificially.\n\n Atomic number: 105                             Atomic mass: 262 u\n Melting point: 3020 °C                           Atomic Radius: N/A')
        ele.place(x=0,y=0)
        E.title('Dubnium')
        E.geometry("500x265")
        E.configure(bg='#7d2cff')
        E.resizable(False,False)
        exit_button = tkinter.Button(E, text="Close", command=E.destroy, height=2,width=4,bg='#cc0000',activebackground='#8e0000')
        exit_button.place(x=230,y=215)
        
Dubnium = tkinter.Button(gui,text='Db',command=dubnium,width=5,height=3,bg='#7d2cff',activebackground='#6223c9')

Dubnium.place(x=211,y=365)

#Elements of Group-6

def chromium():
        E = Toplevel()
        e = StringVar()
        ele = Label(E,textvariable=e,justify=LEFT,font=(text,14),bg='#7d2cff')
        e.set('Chromium is a chemical element with the symbol Cr and \natomic number 24. It is the first element in group 6. It is a \nsteely-grey, lustrous, hard, and brittle transition metal. \nChromium metal is valued for its high corrosion resistance \nand hardness.\n\n\n Atomic number: 24                          Atomic mass: 51.996 u\n Melting point: 1907 °C                    Atomic Radius: 166 pm')
        ele.place(x=0,y=0)
        E.title('Chromium')
        E.geometry("500x265")
        E.configure(bg='#7d2cff')
        E.resizable(False,False)
        exit_button = tkinter.Button(E, text="Close", command=E.destroy, height=2,width=4,bg='#cc0000',activebackground='#8e0000')
        exit_button.place(x=230,y=215)
        
Chromium = tkinter.Button(gui,text='Cr',command=chromium,width=5,height=3,bg='#7d2cff',activebackground='#6223c9')

Chromium.place(x=255,y=200)

def molybdenum():
        E = Toplevel()
        e = StringVar()
        ele = Label(E,textvariable=e,justify=LEFT,font=(text,14),bg='#7d2cff')
        e.set('Molybdenum is a chemical element with the symbol Mo and \natomic number 42 which is located in period 5 and group 6. \nThe name is from Neo-Latin molybdaenum, which is based \non Ancient Greek Μόλυβδος molybdos, meaning lead, \nsince its ores were confused with lead ores.\n\n\n Atomic number: 42                          Atomic mass: 95.955 u\n Melting point: 2623 °C                    Atomic Radius: 190 pm')
        ele.place(x=0,y=0)
        E.title('Molybdenum')
        E.geometry("500x265")
        E.configure(bg='#7d2cff')
        E.resizable(False,False)
        exit_button = tkinter.Button(E, text="Close", command=E.destroy, height=2,width=4,bg='#cc0000',activebackground='#8e0000')
        exit_button.place(x=230,y=215)
        
Molybdenum = tkinter.Button(gui,text='Mo',command=molybdenum,width=5,height=3,bg='#7d2cff',activebackground='#6223c9')

Molybdenum.place(x=255,y=255)

def tungsten():
        E = Toplevel()
        e = StringVar()
        ele = Label(E,textvariable=e,justify=LEFT,font=(text,14),bg='#7d2cff')
        e.set('Tungsten is a chemical element with the symbol W and \natomic number 74. Tungsten is a rare metal found naturally \non Earth almost exclusively as compounds with other \nelements. It was identified as a new element in 1781 and \nfirst isolated as a metal in 1783.\n\n\n Atomic number: 74                          Atomic mass: 183.84 u\n Melting point: 3422 °C                    Atomic Radius: 193 pm')
        ele.place(x=0,y=0)
        E.title('Tungsten')
        E.geometry("500x265")
        E.configure(bg='#7d2cff')
        E.resizable(False,False)
        exit_button = tkinter.Button(E, text="Close", command=E.destroy, height=2,width=4,bg='#cc0000',activebackground='#8e0000')
        exit_button.place(x=230,y=215)
        
Tungsten = tkinter.Button(gui,text='W',command=tungsten,width=5,height=3,bg='#7d2cff',activebackground='#6223c9')

Tungsten.place(x=255,y=310)

def seaborgium():
        E = Toplevel()
        e = StringVar()
        ele = Label(E,textvariable=e,justify=LEFT,font=(text,14),bg='#7d2cff')
        e.set('Seaborgium is a synthetic chemical element with the \nsymbol Sg and atomic number 106. It is named after the \nAmerican nuclear chemist Glenn T. Seaborg. As a \nsynthetic element, it can be created in a laboratory but is \nnot found in nature.\n\n\n Atomic number: 106                             Atomic mass: 269 u\n Melting point: N/A                                   Atomic Radius: N/A')
        ele.place(x=0,y=0)
        E.title('Seaborgium')
        E.geometry("500x265")
        E.configure(bg='#7d2cff')
        E.resizable(False,False)
        exit_button = tkinter.Button(E, text="Close", command=E.destroy, height=2,width=4,bg='#cc0000',activebackground='#8e0000')
        exit_button.place(x=230,y=215)
        
Seaborgium = tkinter.Button(gui,text='Sg',command=seaborgium,width=5,height=3,bg='#7d2cff',activebackground='#6223c9')

Seaborgium.place(x=255,y=365)

#Elements of Group-7

def manganese():
        E = Toplevel()
        e = StringVar()
        ele = Label(E,textvariable=e,justify=LEFT,font=(text,14),bg='#7d2cff')
        e.set('Manganese is a chemical element with the symbol Mn and \natomic number 25. It is a hard, brittle, silvery metal, often \nfound in minerals in combination with iron. Manganese is a \ntransition metal with a multifaceted array of industrial alloy \nuses, particularly in stainless steels.\n\n\n Atomic number: 25                          Atomic mass: 54.938 u\n Melting point: 1246 °C                    Atomic Radius: 161 pm')
        ele.place(x=0,y=0)
        E.title('Manganese')
        E.geometry("500x265")
        E.configure(bg='#7d2cff')
        E.resizable(False,False)
        exit_button = tkinter.Button(E, text="Close", command=E.destroy, height=2,width=4,bg='#cc0000',activebackground='#8e0000')
        exit_button.place(x=230,y=215)
        
Manganese = tkinter.Button(gui,text='Mn',command=manganese,width=5,height=3,bg='#7d2cff',activebackground='#6223c9')

Manganese.place(x=299,y=200)

def technetium():
        E = Toplevel()
        e = StringVar()
        ele = Label(E,textvariable=e,justify=LEFT,font=(text,14),bg='#7d2cff')
        e.set('Technetium is a chemical element with the symbol Tc and \natomic number 43. It is the lightest element whose \nisotopes are all radioactive. All available technetium is \nproduced as a synthetic element.\n\n\n Atomic number: 43                                  Atomic mass: 98 u\n Melting point: 2204 °C                    Atomic Radius: 183 pm')
        ele.place(x=0,y=0)
        E.title('Technetium')
        E.geometry("500x265")
        E.configure(bg='#7d2cff')
        E.resizable(False,False)
        exit_button = tkinter.Button(E, text="Close", command=E.destroy, height=2,width=4,bg='#cc0000',activebackground='#8e0000')
        exit_button.place(x=230,y=215)
        
Technetium = tkinter.Button(gui,text='Tc',command=technetium,width=5,height=3,bg='#7d2cff',activebackground='#6223c9')

Technetium.place(x=299,y=255)

def rhenium():
        E = Toplevel()
        e = StringVar()
        ele = Label(E,textvariable=e,justify=LEFT,font=(text,14),bg='#7d2cff')
        e.set("Rhenium is a chemical element with the symbol Re and \natomic number 75. It is a silvery-gray, heavy, third-row \ntransition metal in group 7 of the periodic table. With an \nestimated average concentration of 1 part per billion, \nrhenium is one of the rarest elements in the Earth's crust.\n\n\n Atomic number: 75                          Atomic mass: 186.20 u\n Melting point: 3182 °C                    Atomic Radius: 188 pm")
        ele.place(x=0,y=0)
        E.title('Rhenium')
        E.geometry("500x265")
        E.configure(bg='#7d2cff')
        E.resizable(False,False)
        exit_button = tkinter.Button(E, text="Close", command=E.destroy, height=2,width=4,bg='#cc0000',activebackground='#8e0000')
        exit_button.place(x=230,y=215)
        
Rhenium = tkinter.Button(gui,text='Re',command=rhenium,width=5,height=3,bg='#7d2cff',activebackground='#6223c9')

Rhenium.place(x=299,y=310)

def bohrium():
        E = Toplevel()
        e = StringVar()
        ele = Label(E,textvariable=e,justify=LEFT,font=(text,14),bg='#7d2cff')
        e.set('Bohrium is a synthetic chemical element with the symbol Bh \nand atomic number 107. It is named after Danish physicist \nNiels Bohr. As a synthetic element, it can be created in \nparticle accelerators but is not found in nature.\n\n\n Atomic number: 107                             Atomic mass: 264 u\n Melting point: N/A                                   Atomic Radius: N/A')
        ele.place(x=0,y=0)
        E.title('Bohrium')
        E.geometry("500x265")
        E.configure(bg='#7d2cff')
        E.resizable(False,False)
        exit_button = tkinter.Button(E, text="Close", command=E.destroy, height=2,width=4,bg='#cc0000',activebackground='#8e0000')
        exit_button.place(x=230,y=215)
        
Bohrium = tkinter.Button(gui,text='Bh',command=bohrium,width=5,height=3,bg='#7d2cff',activebackground='#6223c9')

Bohrium.place(x=299,y=365)

#Elements of Group-8

def iron():
        E = Toplevel()
        e = StringVar()
        ele = Label(E,textvariable=e,justify=LEFT,font=(text,14),bg='#7d2cff')
        e.set("Iron is a chemical element with the symbol Fe and atomic \nnumber 26. It is a metal that belongs to the first transition \nseries and group 8 of the periodic table. It is, by mass, the \nmost common element on Earth, just ahead of oxygen, \nforming much of Earth's outer and inner core.\n\n\n Atomic number: 26                          Atomic mass: 55.845 u\n Melting point: 1538 °C                    Atomic Radius: 156 pm")
        ele.place(x=0,y=0)
        E.title('Iron')
        E.geometry("500x265")
        E.configure(bg='#7d2cff')
        E.resizable(False,False)
        exit_button = tkinter.Button(E, text="Close", command=E.destroy, height=2,width=4,bg='#cc0000',activebackground='#8e0000')
        exit_button.place(x=230,y=215)
        
Iron = tkinter.Button(gui,text='Fe',command=iron,width=5,height=3,bg='#7d2cff',activebackground='#6223c9')

Iron.place(x=343,y=200)

def ruthenium():
        E = Toplevel()
        e = StringVar()
        ele = Label(E,textvariable=e,justify=LEFT,font=(text,14),bg='#7d2cff')
        e.set('Ruthenium is a chemical element with the symbol Ru and \natomic number 44. It is a rare transition metal belonging to \nthe platinum group of the periodic table. Like the other \nmetals of the platinum group, ruthenium is inert to most \nother chemicals.\n\n\n Atomic number: 44                          Atomic mass: 101.07 u\n Melting point: 2334 °C                    Atomic Radius: 178 pm')
        ele.place(x=0,y=0)
        E.title('Ruthenium')
        E.geometry("500x265")
        E.configure(bg='#7d2cff')
        E.resizable(False,False)
        exit_button = tkinter.Button(E, text="Close", command=E.destroy, height=2,width=4,bg='#cc0000',activebackground='#8e0000')
        exit_button.place(x=230,y=215)
        
Ruthenium = tkinter.Button(gui,text='Ru',command=ruthenium,width=5,height=3,bg='#7d2cff',activebackground='#6223c9')

Ruthenium.place(x=343,y=255)

def osmium():
        E = Toplevel()
        e = StringVar()
        ele = Label(E,textvariable=e,justify=LEFT,font=(text,14),bg='#7d2cff')
        e.set('Osmium is a chemical element with the symbol Os and \natomic number 76. It is a hard, brittle, bluish-white transition \nmetal in the platinum group that is found as a trace element \nin alloys, mostly in platinum ores. Osmium is the densest \nnaturally occurring element.\n\n\n Atomic number: 76                          Atomic mass: 190.23 u\n Melting point: 3033 °C                    Atomic Radius: 185 pm')
        ele.place(x=0,y=0)
        E.title('Osmium')
        E.geometry("500x265")
        E.configure(bg='#7d2cff')
        E.resizable(False,False)
        exit_button = tkinter.Button(E, text="Close", command=E.destroy, height=2,width=4,bg='#cc0000',activebackground='#8e0000')
        exit_button.place(x=230,y=215)
        
Osmium = tkinter.Button(gui,text='Os',command=osmium,width=5,height=3,bg='#7d2cff',activebackground='#6223c9')

Osmium.place(x=343,y=310)

def hassium():
        E = Toplevel()
        e = StringVar()
        ele = Label(E,textvariable=e,justify=LEFT,font=(text,14),bg='#7d2cff')
        e.set('Hassium is a chemical element with the symbol Hs and the \natomic number 108. Hassium is highly radioactive; its most \nstable known isotopes have half-lives of approximately ten \nseconds.\n\n\n Atomic number: 108                             Atomic mass: 269 u\n Melting point: N/A                                   Atomic Radius: N/A')
        ele.place(x=0,y=0)
        E.title('Hassium')
        E.geometry("500x265")
        E.configure(bg='#7d2cff')
        E.resizable(False,False)
        exit_button = tkinter.Button(E, text="Close", command=E.destroy, height=2,width=4,bg='#cc0000',activebackground='#8e0000')
        exit_button.place(x=230,y=215)
        
Hassium = tkinter.Button(gui,text='Hs',command=hassium,width=5,height=3,bg='#7d2cff',activebackground='#6223c9')

Hassium.place(x=343,y=365)

#Elements of Group-9

def cobalt():
        E = Toplevel()
        e = StringVar()
        ele = Label(E,textvariable=e,justify=LEFT,font=(text,14),bg='#7d2cff')
        e.set("Cobalt is a chemical element with the symbol Co and \natomic number 27. As with nickel, cobalt is found in the \nEarth's crust only in a chemically combined form, save for \nsmall deposits found in alloys of natural meteoric iron. The \nfree element, produced by reductive smelting, is a hard, \nlustrous, silvery metal.\n\n Atomic number: 27                          Atomic mass: 58.933 u\n Melting point: 1495 °C                    Atomic Radius: 152 pm")
        ele.place(x=0,y=0)
        E.title('Cobalt')
        E.geometry("500x265")
        E.configure(bg='#7d2cff')
        E.resizable(False,False)
        exit_button = tkinter.Button(E, text="Close", command=E.destroy, height=2,width=4,bg='#cc0000',activebackground='#8e0000')
        exit_button.place(x=230,y=215)
        
Cobalt = tkinter.Button(gui,text='Co',command=cobalt,width=5,height=3,bg='#7d2cff',activebackground='#6223c9')

Cobalt.place(x=387,y=200)

def rhodium():
        E = Toplevel()
        e = StringVar()
        ele = Label(E,textvariable=e,justify=LEFT,font=(text,14),bg='#7d2cff')
        e.set("Rhodium is a chemical element with the symbol Rh and \natomic number 45. It is a very rare, silvery-white, hard, \ncorrosion-resistant transition metal. It is a noble metal and a \nmember of the platinum group. It has only one naturally \noccurring isotope: ¹⁰³Rh.\n\n\n Atomic number: 45                          Atomic mass: 102.90 u\n Melting point: 1963 °C                    Atomic Radius: 173 pm")
        ele.place(x=0,y=0)
        E.title('Rhodium')
        E.geometry("500x265")
        E.configure(bg='#7d2cff')
        E.resizable(False,False)
        exit_button = tkinter.Button(E, text="Close", command=E.destroy, height=2,width=4,bg='#cc0000',activebackground='#8e0000')
        exit_button.place(x=230,y=215)
        
Rhodium = tkinter.Button(gui,text='Rh',command=rhodium,width=5,height=3,bg='#7d2cff',activebackground='#6223c9')

Rhodium.place(x=387,y=255)

def iridium():
        E = Toplevel()
        e = StringVar()
        ele = Label(E,textvariable=e,justify=LEFT,font=(text,14),bg='#7d2cff')
        e.set("Iridium is a chemical element with the symbol Ir and atomic \nnumber 77. A very hard, brittle, silvery-white transition metal \nof the platinum group, it is considered the second-densest \nnaturally occurring metal with a density of 22.56 g/cm³ as \ndefined by experimental X-ray crystallography.\n\n\n Atomic number: 77                          Atomic mass: 192.21 u\n Melting point: 2446 °C                    Atomic Radius: 180 pm")
        ele.place(x=0,y=0)
        E.title('Iridium')
        E.geometry("500x265")
        E.configure(bg='#7d2cff')
        E.resizable(False,False)
        exit_button = tkinter.Button(E, text="Close", command=E.destroy, height=2,width=4,bg='#cc0000',activebackground='#8e0000')
        exit_button.place(x=230,y=215)
        
Iridium = tkinter.Button(gui,text='Ir',command=iridium,width=5,height=3,bg='#7d2cff',activebackground='#6223c9')

Iridium.place(x=387,y=310)

def meitnerium():
        E = Toplevel()
        e = StringVar()
        ele = Label(E,textvariable=e,justify=LEFT,font=(text,14),bg='#bcbcbc')
        e.set("Meitnerium is a synthetic chemical element with the symbol \nMt and atomic number 109. It is an extremely radioactive \nsynthetic element. The most stable known isotope, \nmeitnerium-278, has a half-life of 4.5 seconds, although \nthe unconfirmed meitnerium-282 may have a longer \nhalf-life of 67 seconds.\n\n\n Atomic number: 109                             Atomic mass: 278 u\n Melting point: N/A                                   Atomic Radius: N/A")
        ele.place(x=0,y=0)
        E.title('Meitnerium')
        E.geometry("500x265")
        E.configure(bg='#bcbcbc')
        E.resizable(False,False)
        exit_button = tkinter.Button(E, text="Close", command=E.destroy, height=2,width=4,bg='#cc0000',activebackground='#8e0000')
        exit_button.place(x=230,y=215)
        
Meitnerium = tkinter.Button(gui,text='Mt',command=meitnerium,width=5,height=3,bg='#bcbcbc',activebackground='#8a8a8a')

Meitnerium.place(x=387,y=365)

#Elements of Group-10

def nickel():
        E = Toplevel()
        e = StringVar()
        ele = Label(E,textvariable=e,justify=LEFT,font=(text,14),bg='#7d2cff')
        e.set("Nickel is a chemical element with symbol Ni and atomic \nnumber 28. It is a silvery-white lustrous metal with a slight \ngolden tinge. Nickel is a hard and ductile transition metal.\n\n\n Atomic number: 28                          Atomic mass: 58.693 u\n Melting point: 1455 °C                    Atomic Radius: 149 pm")
        ele.place(x=0,y=0)
        E.title('Nickel')
        E.geometry("500x265")
        E.configure(bg='#7d2cff')
        E.resizable(False,False)
        exit_button = tkinter.Button(E, text="Close", command=E.destroy, height=2,width=4,bg='#cc0000',activebackground='#8e0000')
        exit_button.place(x=230,y=215)
        
Nickel = tkinter.Button(gui,text='Ni',command=nickel,width=5,height=3,bg='#7d2cff',activebackground='#6223c9')

Nickel.place(x=431,y=200)

def palladium():
        E = Toplevel()
        e = StringVar()
        ele = Label(E,textvariable=e,justify=LEFT,font=(text,14),bg='#7d2cff')
        e.set("Palladium is a chemical element with the symbol Pd and \natomic number 46. It is a rare and lustrous silvery-white \nmetal discovered in 1803 by the English chemist William \nHyde Wollaston.\n\n\n Atomic number: 46                          Atomic mass: 106.42 u\n Melting point: 1555 °C                    Atomic Radius: 169 pm")
        ele.place(x=0,y=0)
        E.title('Palladium')
        E.geometry("500x265")
        E.configure(bg='#7d2cff')
        E.resizable(False,False)
        exit_button = tkinter.Button(E, text="Close", command=E.destroy, height=2,width=4,bg='#cc0000',activebackground='#8e0000')
        exit_button.place(x=230,y=215)
        
Palladium = tkinter.Button(gui,text='Pd',command=palladium,width=5,height=3,bg='#7d2cff',activebackground='#6223c9')

Palladium.place(x=431,y=255)

def platinum():
        E = Toplevel()
        e = StringVar()
        ele = Label(E,textvariable=e,justify=LEFT,font=(text,14),bg='#7d2cff')
        e.set('Platinum is a chemical element with the symbol Pt and \natomic number 78. It is a dense, malleable, ductile, highly \nunreactive, precious, silverish-white transition metal. Its \nname originates from Spanish platina, a diminutive of plata \n"silver".\n\n\n Atomic number: 78                          Atomic mass: 195.08 u\n Melting point: 1768 °C                    Atomic Radius: 177 pm')
        ele.place(x=0,y=0)
        E.title('Platinum')
        E.geometry("500x265")
        E.configure(bg='#7d2cff')
        E.resizable(False,False)
        exit_button = tkinter.Button(E, text="Close", command=E.destroy, height=2,width=4,bg='#cc0000',activebackground='#8e0000')
        exit_button.place(x=230,y=215)
        
Platinum = tkinter.Button(gui,text='Pt',command=platinum,width=5,height=3,bg='#7d2cff',activebackground='#6223c9')

Platinum.place(x=431,y=310)

def darmstadtium():
        E = Toplevel()
        e = StringVar()
        ele = Label(E,textvariable=e,justify=LEFT,font=(text,14),bg='#bcbcbc')
        e.set("Darmstadtium is a chemical element with the symbol Ds \nand atomic number 110. It is an extremely radioactive \nsynthetic element. The most stable known isotope, \ndarmstadtium-281, has a half-life of approximately 14 \nseconds.\n\n\n Atomic number: 110                             Atomic mass: 281 u\n Melting point: N/A                                   Atomic Radius: N/A")
        ele.place(x=0,y=0)
        E.title('Darmstadtium')
        E.geometry("500x265")
        E.configure(bg='#bcbcbc')
        E.resizable(False,False)
        exit_button = tkinter.Button(E, text="Close", command=E.destroy, height=2,width=4,bg='#cc0000',activebackground='#8e0000')
        exit_button.place(x=230,y=215)
        
Darmstadtium = tkinter.Button(gui,text='Ds',command=darmstadtium,width=5,height=3,bg='#bcbcbc',activebackground='#8a8a8a')

Darmstadtium.place(x=431,y=365)

#Elements of Group-11

def copper():
        E = Toplevel()
        e = StringVar()
        ele = Label(E,textvariable=e,justify=LEFT,font=(text,14),bg='#7d2cff')
        e.set("Copper is a chemical element with the symbol Cu and \natomic number 29. It is a soft, malleable, and ductile metal \nwith very high thermal and electrical conductivity. A freshly \nexposed surface of pure copper has a pinkish-orange \ncolor.\n\n\n Atomic number: 29                          Atomic mass: 63.546 u\n Melting point: 1085 °C                    Atomic Radius: 145 pm")
        ele.place(x=0,y=0)
        E.title('Copper')
        E.geometry("500x265")
        E.configure(bg='#7d2cff')
        E.resizable(False,False)
        exit_button = tkinter.Button(E, text="Close", command=E.destroy, height=2,width=4,bg='#cc0000',activebackground='#8e0000')
        exit_button.place(x=230,y=215)
        
Copper = tkinter.Button(gui,text='Cu',command=copper,width=5,height=3,bg='#7d2cff',activebackground='#6223c9')

Copper.place(x=475,y=200)

def silver():
        E = Toplevel()
        e = StringVar()
        ele = Label(E,textvariable=e,justify=LEFT,font=(text,14),bg='#7d2cff')
        e.set("Silver is a chemical element with the symbol Ag and atomic \nnumber 47. A soft, white, lustrous transition metal, it \nexhibits the highest electrical conductivity, thermal \nconductivity, and reflectivity of any metal.\n\n\n Atomic number: 47                          Atomic mass: 107.86 u\n Melting point: 961.8 °C                   Atomic Radius: 165 pm")
        ele.place(x=0,y=0)
        E.title('Silver')
        E.geometry("500x265")
        E.configure(bg='#7d2cff')
        E.resizable(False,False)
        exit_button = tkinter.Button(E, text="Close", command=E.destroy, height=2,width=4,bg='#cc0000',activebackground='#8e0000')
        exit_button.place(x=230,y=215)
        
Silver = tkinter.Button(gui,text='Ag',command=silver,width=5,height=3,bg='#7d2cff',activebackground='#6223c9')

Silver.place(x=475,y=255)

def gold():
        E = Toplevel()
        e = StringVar()
        ele = Label(E,textvariable=e,justify=LEFT,font=(text,14),bg='#7d2cff')
        e.set("Gold is a chemical element with the symbol Au and atomic \nnumber 79. It is a bright, slightly orange-yellow, dense, soft, \nmalleable, and ductile metal in pure form. Chemically, gold \nis a transition metal and a group 11 element. It is one of the \nleast reactive chemical elements and is solid under \nstandard conditions.\n\n Atomic number: 79                          Atomic mass: 196.96 u\n Melting point: 1064 °C                    Atomic Radius: 174 pm")
        ele.place(x=0,y=0)
        E.title('Gold')
        E.geometry("500x265")
        E.configure(bg='#7d2cff')
        E.resizable(False,False)
        exit_button = tkinter.Button(E, text="Close", command=E.destroy, height=2,width=4,bg='#cc0000',activebackground='#8e0000')
        exit_button.place(x=230,y=215)
        
Gold = tkinter.Button(gui,text='Au',command=gold,width=5,height=3,bg='#7d2cff',activebackground='#6223c9')

Gold.place(x=475,y=310)

def roentgenium():
        E = Toplevel()
        e = StringVar()
        ele = Label(E,textvariable=e,justify=LEFT,font=(text,14),bg='#bcbcbc')
        e.set("Roentgenium is a chemical element with the symbol Rg \nand atomic number 111. It is an extremely radioactive \nsynthetic element that can be created in a laboratory but is \nnot found in nature.\n\n\n Atomic number: 111                             Atomic mass: 282 u\n Melting point: N/A                                   Atomic Radius: N/A")
        ele.place(x=0,y=0)
        E.title('Roentgenium')
        E.geometry("500x265")
        E.configure(bg='#bcbcbc')
        E.resizable(False,False)
        exit_button = tkinter.Button(E, text="Close", command=E.destroy, height=2,width=4,bg='#cc0000',activebackground='#8e0000')
        exit_button.place(x=230,y=215)
        
Roentgenium = tkinter.Button(gui,text='Rg',command=roentgenium,width=5,height=3,bg='#bcbcbc',activebackground='#8a8a8a')

Roentgenium.place(x=475,y=365)

#Elements of Group-12

def zinc():
        E = Toplevel()
        e = StringVar()
        ele = Label(E,textvariable=e,justify=LEFT,font=(text,14),bg='#7d2cff')
        e.set("Zinc is a chemical element with the symbol Zn and atomic \nnumber 30. Zinc is a slightly brittle metal at room \ntemperature and has a shiny-greyish appearance when \noxidation is removed. It is the first element in group 12 of \nthe periodic table.\n\n\n Atomic number: 30                             Atomic mass: 65.38 u\n Melting point: 419.5 °C                    Atomic Radius: 142 pm")
        ele.place(x=0,y=0)
        E.title('Zinc')
        E.geometry("500x265")
        E.configure(bg='#7d2cff')
        E.resizable(False,False)
        exit_button = tkinter.Button(E, text="Close", command=E.destroy, height=2,width=4,bg='#cc0000',activebackground='#8e0000')
        exit_button.place(x=230,y=215)
        
Zinc = tkinter.Button(gui,text='Zn',command=zinc,width=5,height=3,bg='#7d2cff',activebackground='#6223c9')

Zinc.place(x=519,y=200)

def cadmium():
        E = Toplevel()
        e = StringVar()
        ele = Label(E,textvariable=e,justify=LEFT,font=(text,14),bg='#7d2cff')
        e.set("Cadmium is a chemical element with the symbol Cd and \natomic number 48. This soft, silvery-white metal is \nchemically similar to the two other stable metals in group \n12, zinc and mercury.\n\n\n Atomic number: 48                          Atomic mass: 112.41 u\n Melting point: 321.1 °C                   Atomic Radius: 161 pm")
        ele.place(x=0,y=0)
        E.title('cadmium')
        E.geometry("500x265")
        E.configure(bg='#7d2cff')
        E.resizable(False,False)
        exit_button = tkinter.Button(E, text="Close", command=E.destroy, height=2,width=4,bg='#cc0000',activebackground='#8e0000')
        exit_button.place(x=230,y=215)
        
Cadmium = tkinter.Button(gui,text='Cd',command=cadmium,width=5,height=3,bg='#7d2cff',activebackground='#6223c9')

Cadmium.place(x=519,y=255)

def mercury():
        E = Toplevel()
        e = StringVar()
        ele = Label(E,textvariable=e,justify=LEFT,font=(text,14),bg='#7d2cff')
        e.set("Mercury is a chemical element with the symbol Hg and \natomic number 80. It is also known as quicksilver and was \nformerly named hydrargyrum from the Greek words hydro \nand argyros.\n\n\n Atomic number: 80                          Atomic mass: 200.59 u\n Melting point: -38.83 °C                  Atomic Radius: 171 pm")
        ele.place(x=0,y=0)
        E.title('Mercury')
        E.geometry("500x265")
        E.configure(bg='#7d2cff')
        E.resizable(False,False)
        exit_button = tkinter.Button(E, text="Close", command=E.destroy, height=2,width=4,bg='#cc0000',activebackground='#8e0000')
        exit_button.place(x=230,y=215)
        
Mercury = tkinter.Button(gui,text='Hg',command=mercury,width=5,height=3,bg='#7d2cff',activebackground='#6223c9')

Mercury.place(x=519,y=310)

def copernicium():
        E = Toplevel()
        e = StringVar()
        ele = Label(E,textvariable=e,justify=LEFT,font=(text,14),bg='#bcbcbc')
        e.set("Copernicium is a synthetic chemical element with the \nsymbol Cn and atomic number 112. Its known isotopes are \nextremely radioactive, and have only been created in a \nlaboratory. The most stable known isotope, \ncopernicium-285, has a half-life of approximately 30 \nseconds.\n\n Atomic number: 112                             Atomic mass: 285 u\n Melting point: N/A                                   Atomic Radius: N/A")
        ele.place(x=0,y=0)
        E.title('Copernicium')
        E.geometry("500x265")
        E.configure(bg='#bcbcbc')
        E.resizable(False,False)
        exit_button = tkinter.Button(E, text="Close", command=E.destroy, height=2,width=4,bg='#cc0000',activebackground='#8e0000')
        exit_button.place(x=230,y=215)
        
Copernicium = tkinter.Button(gui,text='Cn',command=copernicium,width=5,height=3,bg='#bcbcbc',activebackground='#8a8a8a')

Copernicium.place(x=519,y=365)

#Elements of Group-13

def boron():
        E = Toplevel()
        e = StringVar()
        ele = Label(E,textvariable=e,justify=LEFT,font=(text,14),bg='#b46f02')
        e.set('Boron is a chemical element with the symbol B and atomic \nnumber 5. In its crystalline form it is a brittle, dark, lustrous \nmetalloid; in its amorphous form it is a brown powder.\n\n\n Atomic number: 5                            Atomic mass: 10.811 u\n Melting point: 2076 °C                      Atomic Radius: 87 pm')
        ele.place(x=0,y=0)
        E.title('Boron')
        E.geometry("500x265")
        E.configure(bg='#b46f02')
        E.resizable(False,False)
        exit_button = tkinter.Button(E, text="Close", command=E.destroy, height=2,width=4,bg='#cc0000',activebackground='#8e0000')
        exit_button.place(x=230,y=215)

Boron = tkinter.Button(gui,text='B',command=boron,width=5,height=3,bg='#b46f02',activebackground='#995e00')

Boron.place(x=563,y=90)

def aluminium():
        E = Toplevel()
        e = StringVar()
        ele = Label(E,textvariable=e,justify=LEFT,font=(text,14),bg='#54ce00')
        e.set("Aluminium (aluminum in North American English) is a \nchemical element with the symbol Al and atomic number \n13. Aluminium has a density lower than those of other \ncommon metals; about one-third that of steel.\n\n\n Atomic number: 13                          Atomic mass: 26.982 u\n Melting point: 660.3 °C                   Atomic Radius: 118 pm")
        ele.place(x=0,y=0)
        E.title('Aluminium')
        E.geometry("500x265")
        E.configure(bg='#54ce00')
        E.resizable(False,False)
        exit_button = tkinter.Button(E, text="Close", command=E.destroy, height=2,width=4,bg='#cc0000',activebackground='#8e0000')
        exit_button.place(x=230,y=215)
        
Aluminium = tkinter.Button(gui,text='Al',command=aluminium,width=5,height=3,bg='#54ce00',activebackground='#54aa00')

Aluminium.place(x=563,y=145)

def gallium():
        E = Toplevel()
        e = StringVar()
        ele = Label(E,textvariable=e,justify=LEFT,font=(text,14),bg='#54ce00')
        e.set("Gallium is a chemical element with the symbol Ga and \natomic number 31. Discovered by the French chemist \nPaul-Émile Lecoq de Boisbaudran in 1875, gallium is in \ngroup 13 of the periodic table and is similar to the other \nmetals of the group.\n\n\n Atomic number: 31                          Atomic mass: 69.723 u\n Melting point: 29.76 °C                   Atomic Radius: 136 pm")
        ele.place(x=0,y=0)
        E.title('Gallium')
        E.geometry("500x265")
        E.configure(bg='#54ce00')
        E.resizable(False,False)
        exit_button = tkinter.Button(E, text="Close", command=E.destroy, height=2,width=4,bg='#cc0000',activebackground='#8e0000')
        exit_button.place(x=230,y=215)
        
Gallium = tkinter.Button(gui,text='Ga',command=gallium,width=5,height=3,bg='#54ce00',activebackground='#54aa00')

Gallium.place(x=563,y=200)

def indium():
        E = Toplevel()
        e = StringVar()
        ele = Label(E,textvariable=e,justify=LEFT,font=(text,14),bg='#54ce00')
        e.set("Indium is a chemical element with the symbol In and \natomic number 49. Indium is the softest metal that is not an \nalkali metal. It is a silvery-white metal that resembles tin in \nappearance. It is a post-transition metal that makes up 0.21 \nparts per million of the Earth's crust.\n\n\n Atomic number: 49                          Atomic mass: 114.82 u\n Melting point: 156.63 °C                 Atomic Radius: 156 pm")
        ele.place(x=0,y=0)
        E.title('Indium')
        E.geometry("500x265")
        E.configure(bg='#54ce00')
        E.resizable(False,False)
        exit_button = tkinter.Button(E, text="Close", command=E.destroy, height=2,width=4,bg='#cc0000',activebackground='#8e0000')
        exit_button.place(x=230,y=215)
        
Indium = tkinter.Button(gui,text='In',command=indium,width=5,height=3,bg='#54ce00',activebackground='#54aa00')

Indium.place(x=563,y=255)

def thallium():
        E = Toplevel()
        e = StringVar()
        ele = Label(E,textvariable=e,justify=LEFT,font=(text,14),bg='#54ce00')
        e.set("Thallium is a chemical element with the symbol Tl and \natomic number 81. It is a gray post-transition metal that is \nnot found free in nature. When isolated, thallium resembles \ntin, but discolors when exposed to air.\n\n\n Atomic number: 81                          Atomic mass: 204.38 u\n Melting point: 303.83 °C                  Atomic Radius: 156 pm")
        ele.place(x=0,y=0)
        E.title('Thallium')
        E.geometry("500x265")
        E.configure(bg='#54ce00')
        E.resizable(False,False)
        exit_button = tkinter.Button(E, text="Close", command=E.destroy, height=2,width=4,bg='#cc0000',activebackground='#8e0000')
        exit_button.place(x=230,y=215)
        
Thallium = tkinter.Button(gui,text='Tl',command=thallium,width=5,height=3,bg='#54ce00',activebackground='#54aa00')

Thallium.place(x=563,y=310)

def nihonium():
        E = Toplevel()
        e = StringVar()
        ele = Label(E,textvariable=e,justify=LEFT,font=(text,14),bg='#bcbcbc')
        e.set("Nihonium is a synthetic chemical element with the \nsymbol Nh and atomic number 113. It is extremely \nradioactive; its most stable known isotope, nihonium-286, \nhas a half-life of about 10 seconds. In the periodic table, \nnihonium is a transactinide element in the p-block. It is a \nmember of period 7 and group 13.\n\n Atomic number: 113                             Atomic mass: 286 u\n Melting point: N/A                                   Atomic Radius: N/A")
        ele.place(x=0,y=0)
        E.title('Nihonium')
        E.geometry("500x265")
        E.configure(bg='#bcbcbc')
        E.resizable(False,False)
        exit_button = tkinter.Button(E, text="Close", command=E.destroy, height=2,width=4,bg='#cc0000',activebackground='#8e0000')
        exit_button.place(x=230,y=215)
        
Nihonium = tkinter.Button(gui,text='Nh',command=nihonium,width=5,height=3,bg='#bcbcbc',activebackground='#8a8a8a')

Nihonium.place(x=563,y=365)

#Elements of Group-14

def carbon():
        E = Toplevel()
        e = StringVar()
        ele = Label(E,textvariable=e,justify=LEFT,font=(text,14),bg='#7f96ff')
        e.set("Carbon is a chemical element with the symbol C and \natomic number 6. It is nonmetallic and tetravalent—its atom \nmaking four electrons available to form covalent chemical \nbonds. It belongs to group 14 of the periodic table. Carbon \nmakes up about 0.025 percent of Earth's crust.\n\n\n Atomic number: 6                            Atomic mass: 12.011 u\n Melting point: 3550 °C                      Atomic Radius: 67 pm")
        ele.place(x=0,y=0)
        E.title('Carbon')
        E.geometry("500x265")
        E.configure(bg='#7f96ff')
        E.resizable(False,False)
        exit_button = tkinter.Button(E, text="Close", command=E.destroy, height=2,width=4,bg='#cc0000',activebackground='#8e0000')
        exit_button.place(x=230,y=215)

Carbon = tkinter.Button(gui,text='C',command=carbon,width=5,height=3,bg='#7f96ff',activebackground='#687bd1')

Carbon.place(x=607,y=90)

def silicon():
        E = Toplevel()
        e = StringVar()
        ele = Label(E,textvariable=e,justify=LEFT,font=(text,14),bg='#b46f02')
        e.set('Silicon is a chemical element with the symbol Si and atomic \nnumber 14. It is a hard, brittle crystalline solid with a \nblue-grey metallic luster, and is a tetravalent metalloid and \nsemiconductor. It is a member of group 14 in the periodic \ntable: carbon is above it; and germanium, tin, lead, and \nflerovium are below it.\n\n Atomic number: 14                          Atomic mass: 28.085 u\n Melting point: 1410  °C                   Atomic Radius: 111 pm')
        ele.place(x=0,y=0)
        E.title('Silicon')
        E.geometry("500x265")
        E.configure(bg='#b46f02')
        E.resizable(False,False)
        exit_button = tkinter.Button(E, text="Close", command=E.destroy, height=2,width=4,bg='#cc0000',activebackground='#8e0000')
        exit_button.place(x=230,y=215)

Silicon = tkinter.Button(gui,text='Si',command=silicon,width=5,height=3,bg='#b46f02',activebackground='#995e00')

Silicon.place(x=607,y=145)

def germanium():
        E = Toplevel()
        e = StringVar()
        ele = Label(E,textvariable=e,justify=LEFT,font=(text,14),bg='#b46f02')
        e.set('Germanium is a chemical element with the symbol Ge and \natomic number 32. It is lustrous, hard-brittle, grayish-white \nand similar in appearance to silicon. It is a metalloid in the \ncarbon group that is chemically similar to its group \nneighbors silicon and tin.\n\n\n Atomic number: 32                            Atomic mass: 72.64 u\n Melting point: 938.2 °C                   Atomic Radius: 125 pm')
        ele.place(x=0,y=0)
        E.title('Germanium')
        E.geometry("500x265")
        E.configure(bg='#b46f02')
        E.resizable(False,False)
        exit_button = tkinter.Button(E, text="Close", command=E.destroy, height=2,width=4,bg='#cc0000',activebackground='#8e0000')
        exit_button.place(x=230,y=215)

Germanium = tkinter.Button(gui,text='Ge',command=germanium,width=5,height=3,bg='#b46f02',activebackground='#995e00')

Germanium.place(x=607,y=200)

def tin():
        E = Toplevel()
        e = StringVar()
        ele = Label(E,textvariable=e,justify=LEFT,font=(text,14),bg='#54ce00')
        e.set("Tin is a chemical element with the symbol Sn and atomic \nnumber 50. A silvery-coloured metal, tin is soft enough to \nbe cut with little force, and a bar of tin can be bent by hand \nwith little effort.\n\n\n Atomic number: 50                          Atomic mass: 118.71 u\n Melting point: 231.9 °C                   Atomic Radius: 145 pm")
        ele.place(x=0,y=0)
        E.title('Tin')
        E.geometry("500x265")
        E.configure(bg='#54ce00')
        E.resizable(False,False)
        exit_button = tkinter.Button(E, text="Close", command=E.destroy, height=2,width=4,bg='#cc0000',activebackground='#8e0000')
        exit_button.place(x=230,y=215)
        
Tin = tkinter.Button(gui,text='Sn',command=tin,width=5,height=3,bg='#54ce00',activebackground='#54aa00')

Tin.place(x=607,y=255)

def lead():
        E = Toplevel()
        e = StringVar()
        ele = Label(E,textvariable=e,justify=LEFT,font=(text,14),bg='#54ce00')
        e.set("Lead is a chemical element with the symbol Pb and atomic \nnumber 82. It is a heavy metal that is denser than most \ncommon materials. Lead is soft and malleable, and also \nhas a relatively low melting point. When freshly cut, lead is \na shiny gray with a hint of blue. It tarnishes to a dull gray \ncolor when exposed to air.\n\n Atomic number: 82                            Atomic mass: 207.2 u\n Melting point: 327.5 °C                   Atomic Radius: 154 pm")
        ele.place(x=0,y=0)
        E.title('Lead')
        E.geometry("500x265")
        E.configure(bg='#54ce00')
        E.resizable(False,False)
        exit_button = tkinter.Button(E, text="Close", command=E.destroy, height=2,width=4,bg='#cc0000',activebackground='#8e0000')
        exit_button.place(x=230,y=215)
        
Lead = tkinter.Button(gui,text='Pb',command=lead,width=5,height=3,bg='#54ce00',activebackground='#54aa00')

Lead.place(x=607,y=310)

def flerovium():
        E = Toplevel()
        e = StringVar()
        ele = Label(E,textvariable=e,justify=LEFT,font=(text,14),bg='#bcbcbc')
        e.set("Flerovium is a superheavy chemical element with symbol Fl \nand atomic number 114. It is an extremely radioactive \nsynthetic element. It is named after the Flerov Laboratory \nof Nuclear Reactions of the Joint Institute for Nuclear \nResearch in Dubna, Russia, where the element was \ndiscovered in 1999.\n\n Atomic number: 114                             Atomic mass: 289 u\n Melting point: N/A                                   Atomic Radius: N/A")
        ele.place(x=0,y=0)
        E.title('Flerovium')
        E.geometry("500x265")
        E.configure(bg='#bcbcbc')
        E.resizable(False,False)
        exit_button = tkinter.Button(E, text="Close", command=E.destroy, height=2,width=4,bg='#cc0000',activebackground='#8e0000')
        exit_button.place(x=230,y=215)
        
Flerovium = tkinter.Button(gui,text='Fl',command=flerovium,width=5,height=3,bg='#bcbcbc',activebackground='#8a8a8a')

Flerovium.place(x=607,y=365)

#Elements of Group-15

def nitrogen():
        E = Toplevel()
        e = StringVar()
        ele = Label(E,textvariable=e,justify=LEFT,font=(text,14),bg='#7f96ff')
        e.set("Nitrogen is the chemical element with the symbol N and \natomic number 7. Nitrogen is a nonmetal and the lightest \nmember of group 15 of the periodic table, often called the \npnictogens. It is a common element in the universe, \nestimated at seventh in total abundance in the Milky Way \nand the Solar System.\n\n Atomic number: 7                            Atomic mass: 14.006 u\n Melting point: -210.1 °C                    Atomic Radius: 56 pm")
        ele.place(x=0,y=0)
        E.title('Nitrogen')
        E.geometry("500x265")
        E.configure(bg='#7f96ff')
        E.resizable(False,False)
        exit_button = tkinter.Button(E, text="Close", command=E.destroy, height=2,width=4,bg='#cc0000',activebackground='#8e0000')
        exit_button.place(x=230,y=215)

Nitrogen = tkinter.Button(gui,text='N',command=nitrogen,width=5,height=3,bg='#7f96ff',activebackground='#687bd1')

Nitrogen.place(x=651,y=90)

def phosphorus():
        E = Toplevel()
        e = StringVar()
        ele = Label(E,textvariable=e,justify=LEFT,font=(text,14),bg='#7f96ff')
        e.set("Phosphorus is a chemical element with the symbol P and \natomic number 15. Elemental phosphorus exists in two \nmajor forms, white phosphorus and red phosphorus, but \nbecause it is highly reactive, phosphorus is never found as \na free element on Earth.\n\n\n Atomic number: 15                          Atomic mass: 30.973 u\n Melting point: 44.2 °C                        Atomic Radius: 98 pm")
        ele.place(x=0,y=0)
        E.title('Phosphorus')
        E.geometry("500x265")
        E.configure(bg='#7f96ff')
        E.resizable(False,False)
        exit_button = tkinter.Button(E, text="Close", command=E.destroy, height=2,width=4,bg='#cc0000',activebackground='#8e0000')
        exit_button.place(x=230,y=215)

Phosphorus = tkinter.Button(gui,text='P',command=phosphorus,width=5,height=3,bg='#7f96ff',activebackground='#687bd1')

Phosphorus.place(x=651,y=145)

def arsenic():
        E = Toplevel()
        e = StringVar()
        ele = Label(E,textvariable=e,justify=LEFT,font=(text,14),bg='#b46f02')
        e.set('Arsenic is a chemical element with the symbol As and \natomic number 33. Arsenic occurs in many minerals, \nusually in combination with sulfur and metals, but also as a \npure elemental crystal. Arsenic is a metalloid.\n\n\n Atomic number: 33                          Atomic mass: 74.921 u\n Melting point: 816.8 °C                   Atomic Radius: 114 pm')
        ele.place(x=0,y=0)
        E.title('Arsenic')
        E.geometry("500x265")
        E.configure(bg='#b46f02')
        E.resizable(False,False)
        exit_button = tkinter.Button(E, text="Close", command=E.destroy, height=2,width=4,bg='#cc0000',activebackground='#8e0000')
        exit_button.place(x=230,y=215)

Arsenic = tkinter.Button(gui,text='As',command=arsenic,width=5,height=3,bg='#b46f02',activebackground='#995e00')

Arsenic.place(x=651,y=200)

def antimony():
        E = Toplevel()
        e = StringVar()
        ele = Label(E,textvariable=e,justify=LEFT,font=(text,14),bg='#b46f02')
        e.set('Antimony is a chemical element with the symbol Sb and \natomic number 51. A lustrous gray metalloid, it is found in \nnature mainly as the sulfide mineral stibnite. Antimony \ncompounds have been known since ancient times and \nwere powdered for use as medicine and cosmetics, often \nknown by the Arabic name kohl.\n\n Atomic number: 51                          Atomic mass: 121.76 u\n Melting point: 630.6 °C                   Atomic Radius: 133 pm')
        ele.place(x=0,y=0)
        E.title('Antimony')
        E.geometry("500x265")
        E.configure(bg='#b46f02')
        E.resizable(False,False)
        exit_button = tkinter.Button(E, text="Close", command=E.destroy, height=2,width=4,bg='#cc0000',activebackground='#8e0000')
        exit_button.place(x=230,y=215)

Antimony = tkinter.Button(gui,text='Sb',command=antimony,width=5,height=3,bg='#b46f02',activebackground='#995e00')

Antimony.place(x=651,y=255)

def bismuth():
        E = Toplevel()
        e = StringVar()
        ele = Label(E,textvariable=e,justify=LEFT,font=(text,14),bg='#54ce00')
        e.set("Bismuth is a chemical element with the symbol Bi and \natomic number 83. It is a post-transition metal and one of \nthe pnictogens, with chemical properties resembling its \nlighter group 15 siblings arsenic and antimony. Elemental \nbismuth occurs naturally, and its sulfide and oxide forms \nare important commercial ores.\n\n Atomic number: 83                            Atomic mass: 271.4 u\n Melting point: 271.4 °C                   Atomic Radius: 143 pm")
        ele.place(x=0,y=0)
        E.title('Bismuth')
        E.geometry("500x265")
        E.configure(bg='#54ce00')
        E.resizable(False,False)
        exit_button = tkinter.Button(E, text="Close", command=E.destroy, height=2,width=4,bg='#cc0000',activebackground='#8e0000')
        exit_button.place(x=230,y=215)
        
Bismuth = tkinter.Button(gui,text='Bi',command=bismuth,width=5,height=3,bg='#54ce00',activebackground='#54aa00')

Bismuth.place(x=651,y=310)

def moscovium():
        E = Toplevel()
        e = StringVar()
        ele = Label(E,textvariable=e,justify=LEFT,font=(text,14),bg='#bcbcbc')
        e.set("Moscovium is a synthetic element with the symbol Mc and \natomic number 115. It was first synthesized in 2003 by a \njoint team of Russian and American scientists at the Joint \nInstitute for Nuclear Research in Dubna, Russia.\n\n\n Atomic number: 115                             Atomic mass: 289 u\n Melting point: N/A                                   Atomic Radius: N/A")
        ele.place(x=0,y=0)
        E.title('Moscovium')
        E.geometry("500x265")
        E.configure(bg='#bcbcbc')
        E.resizable(False,False)
        exit_button = tkinter.Button(E, text="Close", command=E.destroy, height=2,width=4,bg='#cc0000',activebackground='#8e0000')
        exit_button.place(x=230,y=215)
        
Moscovium = tkinter.Button(gui,text='Mc',command=moscovium,width=5,height=3,bg='#bcbcbc',activebackground='#8a8a8a')

Moscovium.place(x=651,y=365)

#Elements of Group-16

def oxygen():
        E = Toplevel()
        e = StringVar()
        ele = Label(E,textvariable=e,justify=LEFT,font=(text,14),bg='#7f96ff')
        e.set("Oxygen is the chemical element with the symbol O and \natomic number 8. It is a member of the chalcogen group in \nthe periodic table, a highly reactive nonmetal, and an \noxidizing agent that readily forms oxides with most \nelements as well as with other compounds.\n\n\n Atomic number: 8                            Atomic mass: 15.999 u\n Melting point: -218.3 °C                    Atomic Radius: 48 pm")
        ele.place(x=0,y=0)
        E.title('Oxygen')
        E.geometry("500x265")
        E.configure(bg='#7f96ff')
        E.resizable(False,False)
        exit_button = tkinter.Button(E, text="Close", command=E.destroy, height=2,width=4,bg='#cc0000',activebackground='#8e0000')
        exit_button.place(x=230,y=215)

Oxygen = tkinter.Button(gui,text='O',command=oxygen,width=5,height=3,bg='#7f96ff',activebackground='#687bd1')

Oxygen.place(x=695,y=90)

def sulfur():
        E = Toplevel()
        e = StringVar()
        ele = Label(E,textvariable=e,justify=LEFT,font=(text,14),bg='#7f96ff')
        e.set("Sulfur is a chemical element with the symbol S and atomic \nnumber 16. It is abundant, multivalent and nonmetallic. \nUnder normal conditions, sulfur atoms form cyclic \noctatomic molecules with a chemical formula S₈. Elemental \nsulfur is a bright yellow, crystalline solid at room \ntemperature.\n\n Atomic number: 16                          Atomic mass: 32.065 u\n Melting point: 112.8 °C                     Atomic Radius: 87 pm")
        ele.place(x=0,y=0)
        E.title('Sulfur')
        E.geometry("500x265")
        E.configure(bg='#7f96ff')
        E.resizable(False,False)
        exit_button = tkinter.Button(E, text="Close", command=E.destroy, height=2,width=4,bg='#cc0000',activebackground='#8e0000')
        exit_button.place(x=230,y=215)

Sulfur = tkinter.Button(gui,text='S',command=sulfur,width=5,height=3,bg='#7f96ff',activebackground='#687bd1')

Sulfur.place(x=695,y=145)

def selenium():
        E = Toplevel()
        e = StringVar()
        ele = Label(E,textvariable=e,justify=LEFT,font=(text,14),bg='#7f96ff')
        e.set("Selenium is a chemical element with the symbol Se and \natomic number 34. It is a metalloid with properties that are \nintermediate between the elements above and below in the \nperiodic table, sulfur and tellurium, and also has similarities \nto arsenic.\n\n\n Atomic number: 34                            Atomic mass: 78.96 u\n Melting point: 221 °C                      Atomic Radius: 103 pm")
        ele.place(x=0,y=0)
        E.title('Selenium')
        E.geometry("500x265")
        E.configure(bg='#7f96ff')
        E.resizable(False,False)
        exit_button = tkinter.Button(E, text="Close", command=E.destroy, height=2,width=4,bg='#cc0000',activebackground='#8e0000')
        exit_button.place(x=230,y=215)

Selenium = tkinter.Button(gui,text='Se',command=selenium,width=5,height=3,bg='#7f96ff',activebackground='#687bd1')

Selenium.place(x=695,y=200)

def tellurium():
        E = Toplevel()
        e = StringVar()
        ele = Label(E,textvariable=e,justify=LEFT,font=(text,14),bg='#b46f02')
        e.set('Tellurium (Te) is a chemical element with atomic number \n52, discovered by Franz muller Von Reichenstein in the \nyear 1782. It is a rare, brittle, mildly toxic and silvery-white \nmetalloid. Tellurium gives a greenish-blue flame when \nburnt in the air.\n\n\n Atomic number: 52                            Atomic mass: 127.6 u\n Melting point: 449.5 °C                   Atomic Radius: 123 pm')
        ele.place(x=0,y=0)
        E.title('Tellurium')
        E.geometry("500x265")
        E.configure(bg='#b46f02')
        E.resizable(False,False)
        exit_button = tkinter.Button(E, text="Close", command=E.destroy, height=2,width=4,bg='#cc0000',activebackground='#8e0000')
        exit_button.place(x=230,y=215)

Tellurium = tkinter.Button(gui,text='Te',command=tellurium,width=5,height=3,bg='#b46f02',activebackground='#995e00')

Tellurium.place(x=695,y=255)

def polonium():
        E = Toplevel()
        e = StringVar()
        ele = Label(E,textvariable=e,justify=LEFT,font=(text,14),bg='#54ce00')
        e.set("Polonium is the chemical element with the symbol Po and \natomic number 84 in the periodic table. This element was \ndiscovered by Marie Sklodowska Curie and Pierre Curie \nin 1898.\n\n\n Atomic number: 84                               Atomic mass: 209 u\n Melting point: 253.8 °C                   Atomic Radius: 135 pm")
        ele.place(x=0,y=0)
        E.title('Polonium')
        E.geometry("500x265")
        E.configure(bg='#54ce00')
        E.resizable(False,False)
        exit_button = tkinter.Button(E, text="Close", command=E.destroy, height=2,width=4,bg='#cc0000',activebackground='#8e0000')
        exit_button.place(x=230,y=215)
        
Polonium = tkinter.Button(gui,text='Po',command=polonium,width=5,height=3,bg='#54ce00',activebackground='#54aa00')

Polonium.place(x=695,y=310)

def livermorium():
        E = Toplevel()
        e = StringVar()
        ele = Label(E,textvariable=e,justify=LEFT,font=(text,14),bg='#bcbcbc')
        e.set("Livermorium is a synthetic chemical element with the \nsymbol Lv and has an atomic number of 116. It is an \nextremely radioactive element that has only been created \nin a laboratory setting and has not been observed in nature.\n\n\n Atomic number: 116                             Atomic mass: 293 u\n Melting point: N/A                                   Atomic Radius: N/A")
        ele.place(x=0,y=0)
        E.title('Livermorium')
        E.geometry("500x265")
        E.configure(bg='#bcbcbc')
        E.resizable(False,False)
        exit_button = tkinter.Button(E, text="Close", command=E.destroy, height=2,width=4,bg='#cc0000',activebackground='#8e0000')
        exit_button.place(x=230,y=215)
        
Livermorium = tkinter.Button(gui,text='Lv',command=livermorium,width=5,height=3,bg='#bcbcbc',activebackground='#8a8a8a')

Livermorium.place(x=695,y=365)

#Elements of Group-17

def fluorine():
        E = Toplevel()
        e = StringVar()
        ele = Label(E,textvariable=e,justify=LEFT,font=(text,14),bg='#7f96ff')
        e.set("Fluorine is a chemical element with the symbol F and \natomic number 9. It is the lightest halogen and exists at \nstandard conditions as a highly toxic, pale yellow diatomic \ngas. As the most electronegative reactive element, it is \nextremely reactive, as it reacts with all other elements \nexcept for the light inert gases.\n\n Atomic number: 9                            Atomic mass: 18.998 u\n Melting point: -219.6 °C                    Atomic Radius: 42 pm")
        ele.place(x=0,y=0)
        E.title('Fluorine')
        E.geometry("500x265")
        E.configure(bg='#7f96ff')
        E.resizable(False,False)
        exit_button = tkinter.Button(E, text="Close", command=E.destroy, height=2,width=4,bg='#cc0000',activebackground='#8e0000')
        exit_button.place(x=230,y=215)

Fluorine = tkinter.Button(gui,text='F',command=fluorine,width=5,height=3,bg='#7f96ff',activebackground='#687bd1')

Fluorine.place(x=739,y=90)

def chlorine():
        E = Toplevel()
        e = StringVar()
        ele = Label(E,textvariable=e,justify=LEFT,font=(text,14),bg='#7f96ff')
        e.set("Chlorine is a chemical element with the symbol Cl and \natomic number 17. The second-lightest of the halogens, it \nappears between fluorine and bromine in the periodic table \nand its properties are mostly intermediate between them. \nChlorine is a yellow-green gas at room temperature.\n\n\n Atomic number: 17                          Atomic mass: 35.453 u\n Melting point: -101.5 °C                    Atomic Radius: 79 pm")
        ele.place(x=0,y=0)
        E.title('Chlorine')
        E.geometry("500x265")
        E.configure(bg='#7f96ff')
        E.resizable(False,False)
        exit_button = tkinter.Button(E, text="Close", command=E.destroy, height=2,width=4,bg='#cc0000',activebackground='#8e0000')
        exit_button.place(x=230,y=215)

Chlorine = tkinter.Button(gui,text='Cl',command=chlorine,width=5,height=3,bg='#7f96ff',activebackground='#687bd1')

Chlorine.place(x=739,y=145)

def bromine():
        E = Toplevel()
        e = StringVar()
        ele = Label(E,textvariable=e,justify=LEFT,font=(text,14),bg='#7f96ff')
        e.set("Bromine is a chemical element with the symbol Br and \natomic number 35. It is a volatile red-brown liquid at room \ntemperature that evaporates readily to form a similarly \ncoloured vapour. Its properties are intermediate between \nthose of chlorine and iodine.\n\n\n Atomic number: 35                          Atomic mass: 79.904 u\n Melting point: -7.2 °C                         Atomic Radius: 94 pm")
        ele.place(x=0,y=0)
        E.title('Bromine')
        E.geometry("500x265")
        E.configure(bg='#7f96ff')
        E.resizable(False,False)
        exit_button = tkinter.Button(E, text="Close", command=E.destroy, height=2,width=4,bg='#cc0000',activebackground='#8e0000')
        exit_button.place(x=230,y=215)

Bromine = tkinter.Button(gui,text='Br',command=bromine,width=5,height=3,bg='#7f96ff',activebackground='#687bd1')

Bromine.place(x=739,y=200)

def iodine():
        E = Toplevel()
        e = StringVar()
        ele = Label(E,textvariable=e,justify=LEFT,font=(text,14),bg='#7f96ff')
        e.set("Iodine is a chemical element with the symbol I and atomic \nnumber 53. The heaviest of the stable halogens, it exists at \nstandard conditions as a semi-lustrous, non-metallic solid \nthat melts to form a deep violet liquid at 114 °C (237 °F), \nand boils to a violet gas at 184 °C (363 °F).\n\n\n Atomic number: 53                          Atomic mass: 126.90 u\n Melting point: 113.7 °C                   Atomic Radius: 115 pm")
        ele.place(x=0,y=0)
        E.title('Iodine')
        E.geometry("500x265")
        E.configure(bg='#7f96ff')
        E.resizable(False,False)
        exit_button = tkinter.Button(E, text="Close", command=E.destroy, height=2,width=4,bg='#cc0000',activebackground='#8e0000')
        exit_button.place(x=230,y=215)

Iodine = tkinter.Button(gui,text='I',command=iodine,width=5,height=3,bg='#7f96ff',activebackground='#687bd1')

Iodine.place(x=739,y=255)

def astatine():
        E = Toplevel()
        e = StringVar()
        ele = Label(E,textvariable=e,justify=LEFT,font=(text,14),bg='#54ce00')
        e.set("Astatine is a chemical element with the symbol At and \natomic number 85. It is the rarest naturally occurring \nelement in the Earth's crust, occurring only as the decay \nproduct of various heavier elements. All of astatine's \nisotopes are short-lived; the most stable is astatine-210, \nwith a half-life of 8.1 hours.\n\n Atomic number: 85                               Atomic mass: 210 u\n Melting point: 302 °C                      Atomic Radius: 127 pm")
        ele.place(x=0,y=0)
        E.title('Astatine')
        E.geometry("500x265")
        E.configure(bg='#54ce00')
        E.resizable(False,False)
        exit_button = tkinter.Button(E, text="Close", command=E.destroy, height=2,width=4,bg='#cc0000',activebackground='#8e0000')
        exit_button.place(x=230,y=215)
        
Astatine = tkinter.Button(gui,text='At',command=astatine,width=5,height=3,bg='#54ce00',activebackground='#54aa00')

Astatine.place(x=739,y=310)

def tennessine():
        E = Toplevel()
        e = StringVar()
        ele = Label(E,textvariable=e,justify=LEFT,font=(text,14),bg='#bcbcbc')
        e.set("Tennessine is a synthetic chemical element with the \nsymbol Ts and atomic number 117. It is the \nsecond-heaviest known element and the penultimate \nelement of the 7th period of the periodic table.\n\n\n Atomic number: 117                             Atomic mass: 294 u\n Melting point: N/A                                   Atomic Radius: N/A")
        ele.place(x=0,y=0)
        E.title('Tennessine')
        E.geometry("500x265")
        E.configure(bg='#bcbcbc')
        E.resizable(False,False)
        exit_button = tkinter.Button(E, text="Close", command=E.destroy, height=2,width=4,bg='#cc0000',activebackground='#8e0000')
        exit_button.place(x=230,y=215)
        
Tennessine = tkinter.Button(gui,text='Ts',command=tennessine,width=5,height=3,bg='#bcbcbc',activebackground='#8a8a8a')

Tennessine.place(x=739,y=365)

#Elements of Group-18

def helium():
        E = Toplevel()
        e = StringVar()
        ele = Label(E,textvariable=e,justify=LEFT,font=(text,14),bg='#e90076')
        e.set('Helium is a chemical element with the symbol He and \natomic number 2. It is a colorless, odorless, tasteless, \nnon-toxic, inert, monatomic gas and the first in the noble \ngas group in the periodic table. Its boiling point is the \nlowest among all the elements, and it does not have a \nmelting point at standard pressure.\n\n Atomic number: 2                              Atomic mass: 4.002 u\n Boiling point: -268.9 °C                     Atomic Radius: 31 pm')
        ele.place(x=0,y=0)
        E.title('Helium')
        E.geometry("500x265")
        E.configure(bg='#e90076')
        E.resizable(False,False)
        exit_button = tkinter.Button(E, text="Close", command=E.destroy, height=2,width=4,bg='#cc0000',activebackground='#8e0000')
        exit_button.place(x=230,y=215)
        
Helium = tkinter.Button(gui,text='He',command=helium,width=5,height=3,bg='#e90076',activebackground='#b90076')

Helium.place(x=783,y=35)

def neon():
        E = Toplevel()
        e = StringVar()
        ele = Label(E,textvariable=e,justify=LEFT,font=(text,14),bg='#e90076')
        e.set("Neon is a chemical element with the symbol Ne and atomic \nnumber 10. It is a noble gas. Neon is a colorless, odorless, \ninert monatomic gas under standard conditions, with about \ntwo-thirds the density of air.\n\n\n Atomic number: 10                          Atomic mass: 20.179 u\n Melting point: -248.5 °C                    Atomic Radius: 38 pm")
        ele.place(x=0,y=0)
        E.title('Neon')
        E.geometry("500x265")
        E.configure(bg='#e90076')
        E.resizable(False,False)
        exit_button = tkinter.Button(E, text="Close", command=E.destroy, height=2,width=4,bg='#cc0000',activebackground='#8e0000')
        exit_button.place(x=230,y=215)

Neon = tkinter.Button(gui,text='Ne',command=neon,width=5,height=3,bg='#e90076',activebackground='#b90076')

Neon.place(x=783,y=90)

def argon():
        E = Toplevel()
        e = StringVar()
        ele = Label(E,textvariable=e,justify=LEFT,font=(text,14),bg='#e90076')
        e.set("Argon is a chemical element with the symbol Ar and atomic \nnumber 18. It is in group 18 of the periodic table and is a \nnoble gas. Argon is the third-most abundant gas in Earth's \natmosphere, at 0.934%.\n\n\n Atomic number: 18                          Atomic mass: 39.948 u\n Melting point: -189.4 °C                    Atomic Radius: 71 pm")
        ele.place(x=0,y=0)
        E.title('Argon')
        E.geometry("500x265")
        E.configure(bg='#e90076')
        E.resizable(False,False)
        exit_button = tkinter.Button(E, text="Close", command=E.destroy, height=2,width=4,bg='#cc0000',activebackground='#8e0000')
        exit_button.place(x=230,y=215)

Argon = tkinter.Button(gui,text='Ar',command=argon,width=5,height=3,bg='#e90076',activebackground='#b90076')

Argon.place(x=783,y=145)

def krypton():
        E = Toplevel()
        e = StringVar()
        ele = Label(E,textvariable=e,justify=LEFT,font=(text,14),bg='#e90076')
        e.set("Krypton is a chemical element with the symbol Kr and \natomic number 36. It is a colorless, odorless, tasteless \nnoble gas that occurs in trace amounts in the atmosphere \nand is often used with other rare gases in fluorescent \nlamps. Krypton is chemically inert.\n\n\n Atomic number: 36                          Atomic mass: 83.798 u\n Melting point: -157.3 °C                    Atomic Radius: 87 pm")
        ele.place(x=0,y=0)
        E.title('Krypton')
        E.geometry("500x265")
        E.configure(bg='#e90076')
        E.resizable(False,False)
        exit_button = tkinter.Button(E, text="Close", command=E.destroy, height=2,width=4,bg='#cc0000',activebackground='#8e0000')
        exit_button.place(x=230,y=215)

Krypton = tkinter.Button(gui,text='Kr',command=krypton,width=5,height=3,bg='#e90076',activebackground='#b90076')

Krypton.place(x=783,y=200)

def xenon():
        E = Toplevel()
        e = StringVar()
        ele = Label(E,textvariable=e,justify=LEFT,font=(text,14),bg='#e90076')
        e.set("Xenon is a chemical element with the symbol Xe and \natomic number 54. It is a dense, colorless, odorless noble \ngas found in Earth's atmosphere in trace amounts.\n\n\n Atomic number: 54                          Atomic mass: 131.29 u\n Melting point: -111.8 °C                  Atomic Radius: 108 pm")
        ele.place(x=0,y=0)
        E.title('Xenon')
        E.geometry("500x265")
        E.configure(bg='#e90076')
        E.resizable(False,False)
        exit_button = tkinter.Button(E, text="Close", command=E.destroy, height=2,width=4,bg='#cc0000',activebackground='#8e0000')
        exit_button.place(x=230,y=215)

Xenon = tkinter.Button(gui,text='Xe',command=xenon,width=5,height=3,bg='#e90076',activebackground='#b90076')

Xenon.place(x=783,y=255)

def radon():
        E = Toplevel()
        e = StringVar()
        ele = Label(E,textvariable=e,justify=LEFT,font=(text,14),bg='#e90076')
        e.set("Radon is a chemical element with the symbol Rn and \natomic number 86. It is a radioactive, colourless, \nodourless, noble gas.\n\n\n Atomic number: 86                               Atomic mass: 222 u\n Melting point: -71 °C                       Atomic Radius: 120 pm")
        ele.place(x=0,y=0)
        E.title('Radon')
        E.geometry("500x265")
        E.configure(bg='#e90076')
        E.resizable(False,False)
        exit_button = tkinter.Button(E, text="Close", command=E.destroy, height=2,width=4,bg='#cc0000',activebackground='#8e0000')
        exit_button.place(x=230,y=215)
        
Radon = tkinter.Button(gui,text='Rn',command=radon,width=5,height=3,bg='#e90076',activebackground='#b90076')

Radon.place(x=783,y=310)

def oganesson():
        E = Toplevel()
        e = StringVar()
        ele = Label(E,textvariable=e,justify=LEFT,font=(text,14),bg='#bcbcbc')
        e.set("Oganesson is a synthetic chemical element with the \nsymbol Og and atomic number 118. It was first synthesized \nin 2002 at the Joint Institute for Nuclear Research in Dubna, \nnear Moscow, Russia, by a joint team of Russian and \nAmerican scientists.\n\n\n Atomic number: 118                             Atomic mass: 294 u\n Melting point: N/A                                   Atomic Radius: N/A")
        ele.place(x=0,y=0)
        E.title('Oganesson')
        E.geometry("500x265")
        E.configure(bg='#bcbcbc')
        E.resizable(False,False)
        exit_button = tkinter.Button(E, text="Close", command=E.destroy, height=2,width=4,bg='#cc0000',activebackground='#8e0000')
        exit_button.place(x=230,y=215)
        
Oganesson = tkinter.Button(gui,text='Og',command=oganesson,width=5,height=3,bg='#bcbcbc',activebackground='#8a8a8a')

Oganesson.place(x=783,y=365)

#Elements of Lanthanides

def cerium():
        E = Toplevel()
        e = StringVar()
        ele = Label(E,textvariable=e,justify=LEFT,font=(text,14),bg='#2986cc')
        e.set('Cerium is a chemical element with the symbol Ce and \natomic number 58. Cerium is a soft, ductile, and \nsilvery-white metal that tarnishes when exposed to air.\n\n\n\n\n Atomic number: 58                        Atomic mass: 140.116 u\n Melting point: 795 °C                             Atomic Radius: N/A')
        ele.place(x=0,y=0)
        E.title('Cerium')
        E.geometry("500x265")
        E.configure(bg='#2986cc')
        E.resizable(False,False)
        exit_button = tkinter.Button(E, text="Close", command=E.destroy, height=2,width=4,bg='#cc0000',activebackground='#8e0000')
        exit_button.place(x=230,y=215)

Cerium = tkinter.Button(gui,text='Ce',command=cerium,width=5,height=3,bg='#2986cc',activebackground='#226fa9')

Cerium.place(x=167,y=447)

def praseodymium():
        E = Toplevel()
        e = StringVar()
        ele = Label(E,textvariable=e,justify=LEFT,font=(text,14),bg='#2986cc')
        e.set('Praseodymium is a chemical element with the symbol Pr \nand the atomic number 59. It is the third member of the \nlanthanide series and is considered one of the rare-earth \nmetals. It is a soft, silvery, malleable and ductile metal, \nvalued for its magnetic, electrical, chemical, and optical \nproperties.\n\n Atomic number: 59                        Atomic mass: 140.907 u\n Melting point: 930.8 °C                    Atomic Radius: 247 pm')
        ele.place(x=0,y=0)
        E.title('Praseodymium')
        E.geometry("500x265")
        E.configure(bg='#2986cc')
        E.resizable(False,False)
        exit_button = tkinter.Button(E, text="Close", command=E.destroy, height=2,width=4,bg='#cc0000',activebackground='#8e0000')
        exit_button.place(x=230,y=215)

Praseodymium = tkinter.Button(gui,text='Pr',command=praseodymium,width=5,height=3,bg='#2986cc',activebackground='#226fa9')

Praseodymium.place(x=211,y=447)

def neodymium():
        E = Toplevel()
        e = StringVar()
        ele = Label(E,textvariable=e,justify=LEFT,font=(text,14),bg='#2986cc')
        e.set('Neodymium is a chemical element with the symbol Nd and \natomic number 60. It is the fourth member of the lanthanide \nseries and is considered to be one of the rare-earth metals. \nIt is a hard, slightly malleable, silvery metal that quickly \ntarnishes in air and moisture.\n\n\n Atomic number: 60                        Atomic mass: 144.242 u\n Melting point: 1,021 °C                   Atomic Radius: 206 pm')
        ele.place(x=0,y=0)
        E.title('Neodymium')
        E.geometry("500x265")
        E.configure(bg='#2986cc')
        E.resizable(False,False)
        exit_button = tkinter.Button(E, text="Close", command=E.destroy, height=2,width=4,bg='#cc0000',activebackground='#8e0000')
        exit_button.place(x=230,y=215)

Neodymium = tkinter.Button(gui,text='Nd',command=neodymium,width=5,height=3,bg='#2986cc',activebackground='#226fa9')

Neodymium.place(x=255,y=447)

def promethium():
        E = Toplevel()
        e = StringVar()
        ele = Label(E,textvariable=e,justify=LEFT,font=(text,14),bg='#2986cc')
        e.set("Promethium is a chemical element with the symbol Pm and \natomic number 61. All of its isotopes are radioactive; it is \nextremely rare, with only about 500-600 grams naturally \noccurring in Earth's crust at any given time.\n\n\n Atomic number: 61                               Atomic mass: 145 u\n Melting point: 1,042 °C                   Atomic Radius: 205 pm")
        ele.place(x=0,y=0)
        E.title('Promethium')
        E.geometry("500x265")
        E.configure(bg='#2986cc')
        E.resizable(False,False)
        exit_button = tkinter.Button(E, text="Close", command=E.destroy, height=2,width=4,bg='#cc0000',activebackground='#8e0000')
        exit_button.place(x=230,y=215)

Promethium = tkinter.Button(gui,text='Pm',command=promethium,width=5,height=3,bg='#2986cc',activebackground='#226fa9')

Promethium.place(x=299,y=447)

def samarium():
        E = Toplevel()
        e = StringVar()
        ele = Label(E,textvariable=e,justify=LEFT,font=(text,14),bg='#2986cc')
        e.set('Samarium is a chemical element with symbol Sm and \natomic number 62. It is a moderately hard silvery metal that \nslowly oxidizes in air. Being a typical member of the \nlanthanide series, samarium usually has the oxidation \nstate +3.\n\n\n Atomic number: 62                          Atomic mass: 150.36 u\n Melting point: 1,072 °C                   Atomic Radius: 238 pm')
        ele.place(x=0,y=0)
        E.title('Samarium')
        E.geometry("500x265")
        E.configure(bg='#2986cc')
        E.resizable(False,False)
        exit_button = tkinter.Button(E, text="Close", command=E.destroy, height=2,width=4,bg='#cc0000',activebackground='#8e0000')
        exit_button.place(x=230,y=215)

Samarium = tkinter.Button(gui,text='Sm',command=samarium,width=5,height=3,bg='#2986cc',activebackground='#226fa9')

Samarium.place(x=343,y=447)

def europium():
        E = Toplevel()
        e = StringVar()
        ele = Label(E,textvariable=e,justify=LEFT,font=(text,14),bg='#2986cc')
        e.set('Europium is a chemical element with the symbol Eu and \natomic number 63. Europium is a silvery-white metal of the \nlanthanide series that reacts readily with air to form a dark \noxide coating. It is the most chemically reactive, least \ndense, and softest of the lanthanide elements.\n\n\n Atomic number: 63                        Atomic mass: 151.964 u\n Melting point: 826 °C                       Atomic Radius: 231 pm')
        ele.place(x=0,y=0)
        E.title('Europium')
        E.geometry("500x265")
        E.configure(bg='#2986cc')
        E.resizable(False,False)
        exit_button = tkinter.Button(E, text="Close", command=E.destroy, height=2,width=4,bg='#cc0000',activebackground='#8e0000')
        exit_button.place(x=230,y=215)

Europium = tkinter.Button(gui,text='Eu',command=europium,width=5,height=3,bg='#2986cc',activebackground='#226fa9')

Europium.place(x=387,y=447)

def gadolinium():
        E = Toplevel()
        e = StringVar()
        ele = Label(E,textvariable=e,justify=LEFT,font=(text,14),bg='#2986cc')
        e.set('Gadolinium is a chemical element with the symbol Gd and \natomic number 64. Gadolinium is a silvery-white metal \nwhen oxidation is removed. It is a malleable and ductile \nrare-earth element. Gadolinium reacts with atmospheric \noxygen or moisture slowly to form a black coating.\n\n\n Atomic number: 64                          Atomic mass: 157.25 u\n Melting point: 1,312 °C                   Atomic Radius: 231 pm')
        ele.place(x=0,y=0)
        E.title('Gadolinium')
        E.geometry("500x265")
        E.configure(bg='#2986cc')
        E.resizable(False,False)
        exit_button = tkinter.Button(E, text="Close", command=E.destroy, height=2,width=4,bg='#cc0000',activebackground='#8e0000')
        exit_button.place(x=230,y=215)

Gadolinium = tkinter.Button(gui,text='Gd',command=gadolinium,width=5,height=3,bg='#2986cc',activebackground='#226fa9')

Gadolinium.place(x=431,y=447)

def terbium():
        E = Toplevel()
        e = StringVar()
        ele = Label(E,textvariable=e,justify=LEFT,font=(text,14),bg='#2986cc')
        e.set('Terbium is a chemical element with the symbol Tb and \natomic number 65. It is a silvery-white, rare earth metal that \nis malleable, and ductile. The ninth member of the \nlanthanide series, terbium is a fairly electropositive metal \nthat reacts with water, evolving hydrogen gas.\n\n\n Atomic number: 65                        Atomic mass: 158.925 u\n Melting point: 1,356 °C                   Atomic Radius: 222 pm')
        ele.place(x=0,y=0)
        E.title('Terbium')
        E.geometry("500x265")
        E.configure(bg='#2986cc')
        E.resizable(False,False)
        exit_button = tkinter.Button(E, text="Close", command=E.destroy, height=2,width=4,bg='#cc0000',activebackground='#8e0000')
        exit_button.place(x=230,y=215)

Terbium = tkinter.Button(gui,text='Tb',command=terbium,width=5,height=3,bg='#2986cc',activebackground='#226fa9')

Terbium.place(x=475,y=447)

def dysprosium():
        E = Toplevel()
        e = StringVar()
        ele = Label(E,textvariable=e,justify=LEFT,font=(text,14),bg='#2986cc')
        e.set('Dysprosium is the chemical element with the symbol Dy \nand atomic number 66. It is a rare-earth element in the \nlanthanide series with a metallic silver luster. Dysprosium is \nnever found in nature as a free element, though, like other \nlanthanides, it is found in various minerals, such as \nxenotime.\n\n Atomic number: 66                            Atomic mass: 162.5 u\n Melting point: 1,412 °C                   Atomic Radius: 228 pm')
        ele.place(x=0,y=0)
        E.title('Dysprosium')
        E.geometry("500x265")
        E.configure(bg='#2986cc')
        E.resizable(False,False)
        exit_button = tkinter.Button(E, text="Close", command=E.destroy, height=2,width=4,bg='#cc0000',activebackground='#8e0000')
        exit_button.place(x=230,y=215)

Dysprosium = tkinter.Button(gui,text='Dy',command=dysprosium,width=5,height=3,bg='#2986cc',activebackground='#226fa9')

Dysprosium.place(x=519,y=447)

def holmium():
        E = Toplevel()
        e = StringVar()
        ele = Label(E,textvariable=e,justify=LEFT,font=(text,14),bg='#2986cc')
        e.set('Holmium is a chemical element with the symbol Ho and \natomic number 67. It is a rare-earth element and the \neleventh member of the lanthanide series. It is a relatively \nsoft, silvery, fairly corrosion-resistant and malleable metal.\n\n\n\n Atomic number: 67                        Atomic mass: 164.930 u\n Melting point: 1,474 °C                   Atomic Radius: 226 pm')
        ele.place(x=0,y=0)
        E.title('Holmium')
        E.geometry("500x265")
        E.configure(bg='#2986cc')
        E.resizable(False,False)
        exit_button = tkinter.Button(E, text="Close", command=E.destroy, height=2,width=4,bg='#cc0000',activebackground='#8e0000')
        exit_button.place(x=230,y=215)

Holmium = tkinter.Button(gui,text='Ho',command=holmium,width=5,height=3,bg='#2986cc',activebackground='#226fa9')

Holmium.place(x=563,y=447)

def erbium():
        E = Toplevel()
        e = StringVar()
        ele = Label(E,textvariable=e,justify=LEFT,font=(text,14),bg='#2986cc')
        e.set('Erbium is a chemical element with the symbol Er and \natomic number 68. A silvery-white solid metal when \nartificially isolated, natural erbium is always found in \nchemical combination with other elements.\n\n\n\n Atomic number: 68                        Atomic mass: 167.259 u\n Melting point: 1,529 °C                   Atomic Radius: 226 pm')
        ele.place(x=0,y=0)
        E.title('Erbium')
        E.geometry("500x265")
        E.configure(bg='#2986cc')
        E.resizable(False,False)
        exit_button = tkinter.Button(E, text="Close", command=E.destroy, height=2,width=4,bg='#cc0000',activebackground='#8e0000')
        exit_button.place(x=230,y=215)

Erbium = tkinter.Button(gui,text='Er',command=erbium,width=5,height=3,bg='#2986cc',activebackground='#226fa9')

Erbium.place(x=607,y=447)

def thulium():
        E = Toplevel()
        e = StringVar()
        ele = Label(E,textvariable=e,justify=LEFT,font=(text,14),bg='#2986cc')
        e.set('Thulium is a chemical element with the symbol Tm and \natomic number 69. It is the thirteenth and third-last element \nin the lanthanide series. Like the other lanthanides, the \nmost common oxidation state is +3, seen in its oxide, \nhalides and other compounds; however, the +2 oxidation \nstate can also be stable.\n\n Atomic number: 69                        Atomic mass: 168.934 u\n Melting point: 1,545 °C                   Atomic Radius: 222 pm')
        ele.place(x=0,y=0)
        E.title('Thulium')
        E.geometry("500x265")
        E.configure(bg='#2986cc')
        E.resizable(False,False)
        exit_button = tkinter.Button(E, text="Close", command=E.destroy, height=2,width=4,bg='#cc0000',activebackground='#8e0000')
        exit_button.place(x=230,y=215)

Thulium = tkinter.Button(gui,text='Tm',command=thulium,width=5,height=3,bg='#2986cc',activebackground='#226fa9')

Thulium.place(x=651,y=447)

def ytterbium():
        E = Toplevel()
        e = StringVar()
        ele = Label(E,textvariable=e,justify=LEFT,font=(text,14),bg='#2986cc')
        e.set('Ytterbium is a chemical element with the symbol Yb and \natomic number 70. It is a metal, the fourteenth and \npenultimate element in the lanthanide series, which is the \nbasis of the relative stability of its +2 oxidation state.\n\n\n\n Atomic number: 70                        Atomic mass: 173.045 u\n Melting point: 819 °C                      Atomic Radius: 222 pm')
        ele.place(x=0,y=0)
        E.title('Ytterbium')
        E.geometry("500x265")
        E.configure(bg='#2986cc')
        E.resizable(False,False)
        exit_button = tkinter.Button(E, text="Close", command=E.destroy, height=2,width=4,bg='#cc0000',activebackground='#8e0000')
        exit_button.place(x=230,y=215)

Ytterbium = tkinter.Button(gui,text='Yb',command=ytterbium,width=5,height=3,bg='#2986cc',activebackground='#226fa9')

Ytterbium.place(x=695,y=447)

def lutetium():
        E = Toplevel()
        e = StringVar()
        ele = Label(E,textvariable=e,justify=LEFT,font=(text,14),bg='#2986cc')
        e.set('Lutetium is a chemical element with the symbol Lu and \natomic number 71. It is a silvery white metal, which resists \ncorrosion in dry air, but not in moist air.\n\n\n\n\n Atomic number: 71                        Atomic mass: 174.967 u\n Melting point: 1,663 °C                   Atomic Radius: 217 pm')
        ele.place(x=0,y=0)
        E.title('Lutetium')
        E.geometry("500x265")
        E.configure(bg='#2986cc')
        E.resizable(False,False)
        exit_button = tkinter.Button(E, text="Close", command=E.destroy, height=2,width=4,bg='#cc0000',activebackground='#8e0000')
        exit_button.place(x=230,y=215)

Lutetium = tkinter.Button(gui,text='Lu',command=lutetium,width=5,height=3,bg='#2986cc',activebackground='#226fa9')

Lutetium.place(x=739,y=447)

#Elements of Actinides

def thorium():
        E = Toplevel()
        e = StringVar()
        ele = Label(E,textvariable=e,justify=LEFT,font=(text,14),bg='#ed7d08')
        e.set('Thorium is a weakly radioactive metallic chemical element \nwith the symbol Th and atomic number 90. Thorium is light \nsilver and tarnishes olive gray when it is exposed to air, \nforming thorium dioxide; it is moderately soft and malleable \nand has a high melting point.\n\n\n Atomic number: 90                        Atomic mass: 232.038 u\n Melting point: 1755 °C                           Atomic Radius: N/A')
        ele.place(x=0,y=0)
        E.title('Thorium')
        E.geometry("500x265")
        E.configure(bg='#ed7d08')
        E.resizable(False,False)
        exit_button = tkinter.Button(E, text="Close", command=E.destroy, height=2,width=4,bg='#cc0000',activebackground='#8e0000')
        exit_button.place(x=230,y=215)

Thorium = tkinter.Button(gui,text='Th',command=thorium,width=5,height=3,bg='#ed7d08',activebackground='#cf6d07')

Thorium.place(x=167,y=502)

def protactinium():
        E = Toplevel()
        e = StringVar()
        ele = Label(E,textvariable=e,justify=LEFT,font=(text,14),bg='#ed7d08')
        e.set('Protactinium is a radioactive chemical element with the \nsymbol Pa and atomic number 91. It is a dense, \nsilvery-gray actinide metal which readily reacts with oxygen, \nwater vapor and inorganic acids\n\n\n\n Atomic number: 91                        Atomic mass: 231.035 u\n Melting point: 1568 °C                           Atomic Radius: N/A')
        ele.place(x=0,y=0)
        E.title('Protactinium')
        E.geometry("500x265")
        E.configure(bg='#ed7d08')
        E.resizable(False,False)
        exit_button = tkinter.Button(E, text="Close", command=E.destroy, height=2,width=4,bg='#cc0000',activebackground='#8e0000')
        exit_button.place(x=230,y=215)

Protactinium = tkinter.Button(gui,text='Pa',command=protactinium,width=5,height=3,bg='#ed7d08',activebackground='#cf6d07')

Protactinium.place(x=211,y=502)

def uranium():
        E = Toplevel()
        e = StringVar()
        ele = Label(E,textvariable=e,justify=LEFT,font=(text,14),bg='#ed7d08')
        e.set('Uranium is a chemical element with symbol U and atomic \nnumber 92. It is a silvery-grey metal in the actinide series \nof the periodic table. A uranium atom has 92 protons and \n92 electrons, of which 6 are valence electrons. Uranium \nradioactively decays by emitting an alpha particle.\n\n\n Atomic number: 92                        Atomic mass: 238.028 u\n Melting point: 1132 °C                           Atomic Radius: N/A')
        ele.place(x=0,y=0)
        E.title('Uranium')
        E.geometry("500x265")
        E.configure(bg='#ed7d08')
        E.resizable(False,False)
        exit_button = tkinter.Button(E, text="Close", command=E.destroy, height=2,width=4,bg='#cc0000',activebackground='#8e0000')
        exit_button.place(x=230,y=215)

Uranium = tkinter.Button(gui,text='U',command=uranium,width=5,height=3,bg='#ed7d08',activebackground='#cf6d07')

Uranium.place(x=255,y=502)

def neptunium():
        E = Toplevel()
        e = StringVar()
        ele = Label(E,textvariable=e,justify=LEFT,font=(text,14),bg='#ed7d08')
        e.set('Neptunium is a chemical element with the symbol Np and \natomic number 93. A radioactive actinide metal, neptunium \nis the first transuranic element. Its position in the periodic \ntable just after uranium, named after the planet Uranus, led \nto it being named after Neptune, the next planet beyond \nUranus.\n\n Atomic number: 93                        Atomic mass: 237.048 u\n Melting point: 644 °C                             Atomic Radius: N/A')
        ele.place(x=0,y=0)
        E.title('Neptunium')
        E.geometry("500x265")
        E.configure(bg='#ed7d08')
        E.resizable(False,False)
        exit_button = tkinter.Button(E, text="Close", command=E.destroy, height=2,width=4,bg='#cc0000',activebackground='#8e0000')
        exit_button.place(x=230,y=215)

Neptunium = tkinter.Button(gui,text='Np',command=neptunium,width=5,height=3,bg='#ed7d08',activebackground='#cf6d07')

Neptunium.place(x=299,y=502)

def plutonium():
        E = Toplevel()
        e = StringVar()
        ele = Label(E,textvariable=e,justify=LEFT,font=(text,14),bg='#ed7d08')
        e.set('Plutonium is a radioactive chemical element with the \nsymbol Pu and atomic number 94. It is an actinide metal of \nsilvery-gray appearance that tarnishes when exposed to air, \nand forms a dull coating when oxidized. The element \nnormally exhibits six allotropes and four oxidation states.\n\n\n Atomic number: 94                        Atomic mass: 244.000 u\n Melting point: 639.4 °C                          Atomic Radius: N/A')
        ele.place(x=0,y=0)
        E.title('Plutonium')
        E.geometry("500x265")
        E.configure(bg='#ed7d08')
        E.resizable(False,False)
        exit_button = tkinter.Button(E, text="Close", command=E.destroy, height=2,width=4,bg='#cc0000',activebackground='#8e0000')
        exit_button.place(x=230,y=215)

Plutonium = tkinter.Button(gui,text='Pu',command=plutonium,width=5,height=3,bg='#ed7d08',activebackground='#cf6d07')

Plutonium.place(x=343,y=502)

def americium():
        E = Toplevel()
        e = StringVar()
        ele = Label(E,textvariable=e,justify=LEFT,font=(text,14),bg='#ed7d08')
        e.set('Americium is a synthetic radioactive chemical element with \nthe symbol Am and atomic number 95. It is a transuranic \nmember of the actinide series, in the periodic table located \nunder the lanthanide element europium and was thus \nnamed after the United States by analogy.\n\n\n Atomic number: 95                        Atomic mass: 243.000 u\n Melting point: 1176 °C                           Atomic Radius: N/A')
        ele.place(x=0,y=0)
        E.title('Americium')
        E.geometry("500x265")
        E.configure(bg='#ed7d08')
        E.resizable(False,False)
        exit_button = tkinter.Button(E, text="Close", command=E.destroy, height=2,width=4,bg='#cc0000',activebackground='#8e0000')
        exit_button.place(x=230,y=215)

Americium = tkinter.Button(gui,text='Am',command=americium,width=5,height=3,bg='#ed7d08',activebackground='#cf6d07')

Americium.place(x=387,y=502)

def curium():
        E = Toplevel()
        e = StringVar()
        ele = Label(E,textvariable=e,justify=LEFT,font=(text,14),bg='#ed7d08')
        e.set('Curium is a transuranic, radioactive chemical element with \nthe symbol Cm and atomic number 96. This actinide \nelement was named after eminent scientists Marie and \nPierre Curie, both known for their research on radioactivity.\n\n\n\n Atomic number: 96                        Atomic mass: 247.000 u\n Melting point: 1347 °C                           Atomic Radius: N/A')
        ele.place(x=0,y=0)
        E.title('Curium')
        E.geometry("500x265")
        E.configure(bg='#ed7d08')
        E.resizable(False,False)
        exit_button = tkinter.Button(E, text="Close", command=E.destroy, height=2,width=4,bg='#cc0000',activebackground='#8e0000')
        exit_button.place(x=230,y=215)

Curium = tkinter.Button(gui,text='Cm',command=curium,width=5,height=3,bg='#ed7d08',activebackground='#cf6d07')

Curium.place(x=431,y=502)

def berkelium():
        E = Toplevel()
        e = StringVar()
        ele = Label(E,textvariable=e,justify=LEFT,font=(text,14),bg='#ed7d08')
        e.set('Berkelium is a transuranic radioactive chemical element \nwith the symbol Bk and atomic number 97. It is a member \nof the actinide and transuranium element series. It is \nnamed after the city of Berkeley, California, the location of \nthe Lawrence Berkeley National Laboratory where it was \ndiscovered in December 1949.\n\n Atomic number: 97                        Atomic mass: 247.000 u\n Melting point: 984.4 °C                          Atomic Radius: N/A')
        ele.place(x=0,y=0)
        E.title('Berkelium')
        E.geometry("500x265")
        E.configure(bg='#ed7d08')
        E.resizable(False,False)
        exit_button = tkinter.Button(E, text="Close", command=E.destroy, height=2,width=4,bg='#cc0000',activebackground='#8e0000')
        exit_button.place(x=230,y=215)

Berkelium = tkinter.Button(gui,text='Bk',command=berkelium,width=5,height=3,bg='#ed7d08',activebackground='#cf6d07')

Berkelium.place(x=475,y=502)

def californium():
        E = Toplevel()
        e = StringVar()
        ele = Label(E,textvariable=e,justify=LEFT,font=(text,14),bg='#ed7d08')
        e.set('Californium is a radioactive chemical element with the \nsymbol Cf and atomic number 98. The element was first \nsynthesized in 1950 at Lawrence Berkeley National \nLaboratory, by bombarding curium with alpha particles.\n\n\n\n Atomic number: 98                        Atomic mass: 251.000 u\n Melting point: 898.8 °C                          Atomic Radius: N/A')
        ele.place(x=0,y=0)
        E.title('Californium')
        E.geometry("500x265")
        E.configure(bg='#ed7d08')
        E.resizable(False,False)
        exit_button = tkinter.Button(E, text="Close", command=E.destroy, height=2,width=4,bg='#cc0000',activebackground='#8e0000')
        exit_button.place(x=230,y=215)

Californium = tkinter.Button(gui,text='Cf',command=californium,width=5,height=3,bg='#ed7d08',activebackground='#cf6d07')

Californium.place(x=519,y=502)

def einsteinium():
        E = Toplevel()
        e = StringVar()
        ele = Label(E,textvariable=e,justify=LEFT,font=(text,14),bg='#ed7d08')
        e.set('Einsteinium is a synthetic element with the symbol Es and \natomic number 99. Einsteinium is a member of the actinide \nseries and it is the seventh transuranium element. It was \nnamed in honor of Albert Einstein. Einsteinium was \ndiscovered as a component of the debris of the first \nhydrogen bomb explosion in 1952.\n\n Atomic number: 99                        Atomic mass: 252.000 u\n Melting point: 860 °C                             Atomic Radius: N/A')
        ele.place(x=0,y=0)
        E.title('Einsteinium')
        E.geometry("500x265")
        E.configure(bg='#ed7d08')
        E.resizable(False,False)
        exit_button = tkinter.Button(E, text="Close", command=E.destroy, height=2,width=4,bg='#cc0000',activebackground='#8e0000')
        exit_button.place(x=230,y=215)

Einsteinium = tkinter.Button(gui,text='Es',command=einsteinium,width=5,height=3,bg='#ed7d08',activebackground='#cf6d07')

Einsteinium.place(x=563,y=502)

def fermium():
        E = Toplevel()
        e = StringVar()
        ele = Label(E,textvariable=e,justify=LEFT,font=(text,14),bg='#ed7d08')
        e.set('Fermium is a synthetic element with the symbol Fm and \natomic number 100. It is an actinide and the heaviest \nelement that can be formed by neutron bombardment of \nlighter elements, and hence the last element that can be \nprepared in macroscopic quantities, although pure fermium \nmetal has not yet been prepared.\n\n Atomic number: 100                      Atomic mass: 257.000 u\n Melting point: 1527 °C                           Atomic Radius: N/A')
        ele.place(x=0,y=0)
        E.title('Fermium')
        E.geometry("500x265")
        E.configure(bg='#ed7d08')
        E.resizable(False,False)
        exit_button = tkinter.Button(E, text="Close", command=E.destroy, height=2,width=4,bg='#cc0000',activebackground='#8e0000')
        exit_button.place(x=230,y=215)

Fermium = tkinter.Button(gui,text='Fm',command=fermium,width=5,height=3,bg='#ed7d08',activebackground='#cf6d07')

Fermium.place(x=607,y=502)

def mendelevium():
        E = Toplevel()
        e = StringVar()
        ele = Label(E,textvariable=e,justify=LEFT,font=(text,14),bg='#ed7d08')
        e.set('Mendelevium is a synthetic element with the symbol Md \nand atomic number 101. A metallic radioactive \ntransuranium element in the actinide series, it is the first \nelement by atomic number that currently cannot be \nproduced in macroscopic quantities by neutron \nbombardment of lighter elements.\n\n Atomic number: 101                      Atomic mass: 258.000 u\n Melting point: 826.8 °C                          Atomic Radius: N/A')
        ele.place(x=0,y=0)
        E.title('Mendelevium')
        E.geometry("500x265")
        E.configure(bg='#ed7d08')
        E.resizable(False,False)
        exit_button = tkinter.Button(E, text="Close", command=E.destroy, height=2,width=4,bg='#cc0000',activebackground='#8e0000')
        exit_button.place(x=230,y=215)

Mendelevium = tkinter.Button(gui,text='Md',command=mendelevium,width=5,height=3,bg='#ed7d08',activebackground='#cf6d07')

Mendelevium.place(x=651,y=502)

def nobelium():
        E = Toplevel()
        e = StringVar()
        ele = Label(E,textvariable=e,justify=LEFT,font=(text,14),bg='#ed7d08')
        e.set('Nobelium is a synthetic chemical element with the symbol \nNo and atomic number 102. It is named in honor of Alfred \nNobel, the inventor of dynamite and benefactor of science. \nA radioactive metal, it is the tenth transuranic element and \nis the penultimate member of the actinide series.\n\n\n Atomic number: 102                      Atomic mass: 259.000 u\n Melting point: 826.8 °C                          Atomic Radius: N/A')
        ele.place(x=0,y=0)
        E.title('Nobelium')
        E.geometry("500x265")
        E.configure(bg='#ed7d08')
        E.resizable(False,False)
        exit_button = tkinter.Button(E, text="Close", command=E.destroy, height=2,width=4,bg='#cc0000',activebackground='#8e0000')
        exit_button.place(x=230,y=215)

Nobelium = tkinter.Button(gui,text='No',command=nobelium,width=5,height=3,bg='#ed7d08',activebackground='#cf6d07')

Nobelium.place(x=695,y=502)

def lawrencium():
        E = Toplevel()
        e = StringVar()
        ele = Label(E,textvariable=e,justify=LEFT,font=(text,14),bg='#ed7d08')
        e.set('Lawrencium is a synthetic chemical element with the \nsymbol Lr and atomic number 103. It is named in honor of \nErnest Lawrence, inventor of the cyclotron, a device that \nwas used to discover many artificial radioactive elements.\n\n\n\n Atomic number: 103                      Atomic mass: 262.000 u\n Melting point: 1627 °C                           Atomic Radius: N/A')
        ele.place(x=0,y=0)
        E.title('Lawrencium')
        E.geometry("500x265")
        E.configure(bg='#ed7d08')
        E.resizable(False,False)
        exit_button = tkinter.Button(E, text="Close", command=E.destroy, height=2,width=4,bg='#cc0000',activebackground='#8e0000')
        exit_button.place(x=230,y=215)

Lawrencium = tkinter.Button(gui,text='Lr',command=lawrencium,width=5,height=3,bg='#ed7d08',activebackground='#cf6d07')

Lawrencium.place(x=739,y=502)

gui.mainloop()