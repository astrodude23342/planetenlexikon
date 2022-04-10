import tkinter as tk
from tkinter import ttk
from tkinter import *
import PIL
from PIL import ImageTk, Image

FULL_EARTH_DESC = 'Unser Heimatplanet ist der dritte Planet von der Sonne\n und der einzige uns bisher bekannte Ort, der \nvon Lebewesen bewohnt wird.\n\n\nWährend die Erde nur der fünftgrößte Planet\nim Sonnensystem ist, ist sie die einzige Welt\nin unserem Sonnensystem mit flüssigem Wasser auf der Oberfläche.\nNur ein bisschen größer als die Venus. Die Erde ist\nder größte der vier sonnennächsten Planeten,\ndie alle aus Gestein und Metall bestehen.\n\n\nDer Name Erde ist mindestens 1.000 Jahre alt.\nAlle Planeten außer der Erde waren benannt nach griechischen\nund römischen Göttern und Göttinnen.\nDer Name Erde ist jedoch ein germanisches Wort,\nwelches einfach "der Boden" bedeutet.'
EARTH_FACT = 'Die Erde ist der einzige Planet im Sonnensystem mit nur einem Mond.'

FULL_JUPITER_DESC = 'Jupiter hat eine lange Geschichte, die \nWissenschaftler überraschte – bis zurück ins Jahr 1610, als Galileo Galilei \ndie ersten Monde jenseits der Erde entdeckte. \n\n\nDer Jupiter, der fünfte in der Sonnenlinie, \nist bei weitem der größte Planet im Sonnensystem, \nmehr als doppelt so massiv wie alle anderen Planeten \nzusammen .\n\n\nJupiters vertraute Streifen \nund Wirbel sind eigentlich kalte, windige Wolken \naus Ammoniak und Wasser, die in einer Atmosphäre aus \nWasserstoff und Helium schweben. Jupiters ikonischer Großer Roter Fleck ist ein riesiger Sturm, der größer als die Erde ist und seit Hunderten von Jahren wütet.'
JUPITER_FACT = 'Ein Raumschiff – der Juno-Orbiter der NASA – erkundet derzeit diese riesige Welt.'

FULL_NEPTUNE_DESC = 'Dunkel, kalt und von Überschallwinden gepeitscht, ist der \n Riese Neptun der achte und am weitesten entfernte \nPlanet in unserem Sonnensystem.\n\n\nMehr als 30 Mal so weit von der Sonne entfernt als die Erde, \nist Neptun der erste Planet, der von der Physik \nvor seiner Entdeckung vorhergesagt wurde. Im Jahr 2011\nbrach Neptun seinen ersten 165-Jährigen \nOrbit seit seiner Entdeckung im Jahr 1846 ab.\n\n\n Voyager 2 der NASA ist das einzige Raumschiff, \ndas Neptun aus nächster Nähe beobachtet hat. Es flog 1989 auf seinem Weg aus dem Sonnensystem vorbei.'
NEPTUNE_FACT = 'Neptun hat 14 Monde. \nDer interessanteste Mond ist Triton, eine gefrorene Welt, die unter ihrer Oberfläche Stickstoffeis und Staubpartikel ausstößt.\nWahrscheinlich wurde sie von der Anziehungskraft des Neptun eingefangen. Es ist wahrscheinlich die kälteste Welt im Sonnensystem.'

FULL_MARS_DESC = 'Der vierte Planet \nMars, ist eine staubige, kalte Wüstenwelt mit einer sehr dünnen Atmosphäre.\n\n\nDieser dynamische Planet hat Jahreszeiten, \npolare Eiskappen und Wetter sowie Schluchten und \nnicht mehr aktive Vulkane.\n\n\n Der Mars ist einer der am besten erforschten Planeten \nin unserem Sonnensystem und er ist der einzige Planet, \nauf dem wir Rover geschickt haben, um die Landschaft\nzu durchstreifen. Nasa, Indien und die ESA haben Raumfahrzeuge im Orbit über dem Mars.\nDiese "Roboterforscher" haben viele Hinweise darauf gefunden, \ndass der Mars viel feuchter und wärmer war \nund eine viel dickere Atmosphäre hatte, vor \nMilliarden von Jahren.'
MARS_FACT = 'Die neueste Robotermission der NASA zum Roten Planeten, Perseverance Rover, \nzielt darauf ab, zukünftigen Astronauten zu helfen, dieser unwirtlichen Landschaft zu trotzen.'

FULL_SATURN_DESC = 'Saturn ist der sechste Planet von der Sonne \nund der zweitgrößte Planet in unserem Sonnensystem.\n\n\nGeschmückt mit Tausenden wunderschöner Ringe\n ist Saturn einzigartig unter den Planeten. Es ist\nnicht der einzige Planet, der Ringe hat, die \naus Eis- und Gesteinsbrocken bestehen, aber keiner \nist so spektakulär, wie der von Saturn.\n\n\n Wie der andere Gasriese Jupiter ist auch Saturn ein massiver \nBall, der hauptsächlich aus Wasserstoff und Helium besteht.'
SATURN_FACT = 'Neun Erden nebeneinander würden fast den Durchmesser des Saturn überspannen.'

FULL_VENUS_DESC = 'Venus ist der zweite Planet von der Sonne und unser nächster planetarischer Nachbar. \nÄhnlich in Struktur und Größe wie \ndie Erde dreht sich die Venus langsam in die entgegengesetzte Richtung von \nden meisten Planeten. Ihre dichte Atmosphäre fängt Wärme in einem unkontrollierten \nTreibhauseffekt ein und macht sie zum heißesten Planeten \nin unserem Sonnensystem mit Oberflächentemperaturen, die heiß genug sind \num Blei schmelzen. Blicke unter die Wolken \nenthüllen Vulkane und verformte Berge.\n\n\n Die Venus ist nach der antiken römischen Göttin der Liebe\nund Schönheit benannt, die den alten Griechen als Aphrodite \nbekannt war.'
VENUS_FACT = 'Mit einem Radius von 3.760 Meilen hat die Venus ungefähr die gleiche Größe wie die Erde – nur etwas kleiner'

FULL_URANUS_DESC = 'Der erste mit Hilfe eines Teleskops gefundene Planet\nUranus wurde 1781 vom Astronomen William Herschel entdeckt,\n obwohl er ursprünglich dachte, es sei entweder ein Komet oder ein Stern.\n\n\nZwei Jahre später war das Objekt nun allgemein als neuer Planet akzeptiert, \nteilweise aufgrund von Beobachtungen des Astronomen Johann Elert Bode.\nHerschel versuchte erfolglos, seine Entdeckung \nGeorgium Sidus nach König Georg III. zu benennen. Stattdessen akzeptierte die \nwissenschaftliche Gemeinschaft Bodes Vorschlag, \n Uranus, den griechischen Gott des Himmels, \nals Vorschlag von Bode zu nennen.'
URANUS_FACT = 'Uranus ist als „Sidewaysplanet“ bekannt, weil er sich auf der Seite dreht.'

FULL_MERCURY_DESC = 'Merkur, der kleinste Planet in unserem Sonnensystem und \nder Sonne am nächsten, ist nur \netwas größer als der Mond der Erde.\n\n\n Von der Oberfläche des Merkur würde die Sonne \nmehr als dreimal so groß erscheinen, \nals von der Erde aus betrachtet,\nund das Sonnenlicht wäre bis zu \nsiebenmal heller. Trotz seiner \nNähe zur Sonne ist Merkur nicht der heißeste \nPlanet in unserem Sonnensystem \ndieser Titel gehört dank ihrer dichten Atmosphäre \nzur Venus.'
MERCURY_FACT = 'Es ist der sonnennächste Planet in einer Entfernung von etwa 36 Millionen Meilen (58 Millionen Kilometer)'

FULL_PLUTO_DESC = 'Pluto - kleiner als der Erdmond\nhat einen herzförmigen Gletscher von der Größe Texas.\nDiese faszinierende Welt hat einen blauen Himmel, \nMonde, Berge so hoch wie die Rocky Mountains\nund es schneit - aber der Schnee ist rot.\n\n\n Plutos Atmosphäre ist dünn und besteht \nhauptsächlich aus Stickstoff, Methan und Kohlenstoffmonoxid.'
PLUTO_FACT = 'Pluto (Zwergplanetenbezeichnung: 134340 Pluto) ist ein eisiger Zwergplanet im Kuipergürtel, einem Asteroidengürtel jenseits der Neptunbahn'

HEIGHT = 1000
WIDTH = 1500

root = tk.Tk()
root.title('Planeten App')

def planet(event):
    planet_type = clicked.get()

    if planet_type == option[0]:                                           
        image = Image.open("mercury.png")
        basewidth = 400

        canvas2 = tk.Canvas(root, height=400, width=400, bg='#171717',bd=0, highlightthickness=0, relief='ridge')
        wpercent = (basewidth / float(image.size[0]))
        hsize = int((float(image.size[1]) * float(wpercent)))
        image = image.resize((basewidth, hsize), PIL.Image.ANTIALIAS)
        photo = ImageTk.PhotoImage(image)
        item4 = canvas2.create_image(225, 210, image=photo)

        canvas2.place(relx=0.05, rely=0.1, relheight=0.6, relwidth=0.5)

        for widget in desc_frame.winfo_children():
            widget.destroy()

        for widget in fact_frame.winfo_children():
            widget.destroy()


        earth_label = tk.Label(desc_frame, text=FULL_MERCURY_DESC, font=('Poppins', 9), bg='#121212', fg='white')
        earth_label.pack()

        earth_fact = tk.Label(fact_frame, text=MERCURY_FACT,font=('Poppins', 16), bg='#121212', fg='white')
        earth_fact.pack(side='left')

        item4.pack()

    if planet_type == option[1]:                                            
        image = Image.open("venus.png")
        basewidth = 400

        canvas2 = tk.Canvas(root, height=400, width=400, bg='#171717',bd=0, highlightthickness=0, relief='ridge')
        wpercent = (basewidth / float(image.size[0]))
        hsize = int((float(image.size[1]) * float(wpercent)))
        image = image.resize((basewidth, hsize), PIL.Image.ANTIALIAS)
        photo = ImageTk.PhotoImage(image)
        item4 = canvas2.create_image(225, 210, image=photo)

        canvas2.place(relx=0.05, rely=0.1, relheight=0.6, relwidth=0.5)

        for widget in desc_frame.winfo_children():
            widget.destroy()

        for widget in fact_frame.winfo_children():
            widget.destroy()

        planet_label = tk.Label(desc_frame, text=FULL_VENUS_DESC, font=('Poppins', 9), bg='#121212', fg='white')
        planet_label.pack()

        planet_fact = tk.Label(fact_frame, text=VENUS_FACT,font=('Poppins', 16), bg='#121212', fg='white')
        planet_fact.pack(side='left')

        item4.pack()

    if planet_type == option[2]:                                           
        image = Image.open("earth.png")
        basewidth = 400

        canvas2 = tk.Canvas(root, height=400, width=400, bg='#171717',bd=0, highlightthickness=0, relief='ridge')
        wpercent = (basewidth / float(image.size[0]))
        hsize = int((float(image.size[1]) * float(wpercent)))
        image = image.resize((basewidth, hsize), PIL.Image.ANTIALIAS)
        photo = ImageTk.PhotoImage(image)
        item4 = canvas2.create_image(225, 210, image=photo)

        canvas2.place(relx=0.05, rely=0.1, relheight=0.6, relwidth=0.5)

        for widget in desc_frame.winfo_children():
            widget.destroy()

        for widget in fact_frame.winfo_children():
            widget.destroy()

        planet_label = tk.Label(desc_frame, text=FULL_EARTH_DESC, font=('Poppins', 9), bg='#121212', fg='white')
        planet_label.pack()

        planet_fact = tk.Label(fact_frame, text=EARTH_FACT,font=('Poppins', 13), bg='#121212', fg='white')
        planet_fact.pack(side='left')

        item4.pack()

    if planet_type == option[3]:                                          
        image = Image.open("mars.png")
        basewidth = 400

        canvas2 = tk.Canvas(root, height=400, width=400, bg='#171717',bd=0, highlightthickness=0, relief='ridge')
        wpercent = (basewidth / float(image.size[0]))
        hsize = int((float(image.size[1]) * float(wpercent)))
        image = image.resize((basewidth, hsize), PIL.Image.ANTIALIAS)
        photo = ImageTk.PhotoImage(image)
        item4 = canvas2.create_image(225, 210, image=photo)

        canvas2.place(relx=0.05, rely=0.1, relheight=0.6, relwidth=0.5)

        for widget in desc_frame.winfo_children():
            widget.destroy()

        for widget in fact_frame.winfo_children():
            widget.destroy()

        planet_label = tk.Label(desc_frame, text=FULL_MARS_DESC, font=('Poppins', 9), bg='#121212', fg='white')
        planet_label.pack()

        planet_fact = tk.Label(fact_frame, text=MARS_FACT,font=('Poppins', 16), bg='#121212', fg='white')
        planet_fact.pack(side='left')

        item4.pack()

    if planet_type == option[4]:                                            
        image = Image.open("jupiter.png")
        basewidth = 400

        canvas2 = tk.Canvas(root, height=400, width=400, bg='#171717',bd=0, highlightthickness=0, relief='ridge')
        wpercent = (basewidth / float(image.size[0]))
        hsize = int((float(image.size[1]) * float(wpercent)))
        image = image.resize((basewidth, hsize), PIL.Image.ANTIALIAS)
        photo = ImageTk.PhotoImage(image)
        item4 = canvas2.create_image(225, 210, image=photo)

        canvas2.place(relx=0.05, rely=0.1, relheight=0.6, relwidth=0.5)

        for widget in desc_frame.winfo_children():
            widget.destroy()

        for widget in fact_frame.winfo_children():
            widget.destroy()

        earth_label = tk.Label(desc_frame, text=FULL_JUPITER_DESC, font=('Poppins', 9), bg='#121212', fg='white')
        earth_label.pack()

        earth_fact = tk.Label(fact_frame, text=JUPITER_FACT,font=('Poppins', 16), bg='#121212', fg='white')
        earth_fact.pack(side='left')

        item4.pack()

    if planet_type == option[5]:                                            
        image = Image.open("saturn.png")
        basewidth = 400

        canvas2 = tk.Canvas(root, height=400, width=400, bg='#171717',bd=0, highlightthickness=0, relief='ridge')
        wpercent = (basewidth / float(image.size[0]))
        hsize = int((float(image.size[1]) * float(wpercent)))
        image = image.resize((basewidth, hsize), PIL.Image.ANTIALIAS)
        photo = ImageTk.PhotoImage(image)
        item4 = canvas2.create_image(225, 210, image=photo)

        canvas2.place(relx=0.05, rely=0.1, relheight=0.6, relwidth=0.5)

        for widget in desc_frame.winfo_children():
            widget.destroy()

        for widget in fact_frame.winfo_children():
            widget.destroy()

        earth_label = tk.Label(desc_frame, text=FULL_SATURN_DESC, font=('Poppins', 9), bg='#121212', fg='white')
        earth_label.pack()

        earth_fact = tk.Label(fact_frame, text=SATURN_FACT,font=('Poppins', 16), bg='#121212', fg='white')
        earth_fact.pack(side='left')

        item4.pack()

    if planet_type == option[6]:                                           
        image = Image.open("uranus.png")
        basewidth = 400

        canvas2 = tk.Canvas(root, height=400, width=400, bg='#171717',bd=0, highlightthickness=0, relief='ridge')
        wpercent = (basewidth / float(image.size[0]))
        hsize = int((float(image.size[1]) * float(wpercent)))
        image = image.resize((basewidth, hsize), PIL.Image.ANTIALIAS)
        photo = ImageTk.PhotoImage(image)
        item4 = canvas2.create_image(225, 210, image=photo)

        canvas2.place(relx=0.05, rely=0.1, relheight=0.6, relwidth=0.5)

        for widget in desc_frame.winfo_children():
            widget.destroy()

        for widget in fact_frame.winfo_children():
            widget.destroy()

        earth_label = tk.Label(desc_frame, text=FULL_URANUS_DESC, font=('Poppins', 9), bg='#121212', fg='white')
        earth_label.pack()

        earth_fact = tk.Label(fact_frame, text=URANUS_FACT,font=('Poppins', 16), bg='#121212', fg='white')
        earth_fact.pack(side='left')

        item4.pack()

    if planet_type == option[7]:                                            
        image = Image.open("neptune.png")
        basewidth = 400

        canvas2 = tk.Canvas(root, height=400, width=400, bg='#171717',bd=0, highlightthickness=0, relief='ridge')
        wpercent = (basewidth / float(image.size[0]))
        hsize = int((float(image.size[1]) * float(wpercent)))
        image = image.resize((basewidth, hsize), PIL.Image.ANTIALIAS)
        photo = ImageTk.PhotoImage(image)
        item4 = canvas2.create_image(225, 210, image=photo)

        canvas2.place(relx=0.05, rely=0.1, relheight=0.6, relwidth=0.5)

        for widget in desc_frame.winfo_children():
            widget.destroy()

        for widget in fact_frame.winfo_children():
            widget.destroy()

        earth_label = tk.Label(desc_frame, text=FULL_NEPTUNE_DESC, font=('Poppins', 9), bg='#121212', fg='white')
        earth_label.pack()

        earth_fact = tk.Label(fact_frame, text=NEPTUNE_FACT,font=('Poppins', 16), bg='#121212', fg='white')
        earth_fact.pack(side='left')

        item4.pack()

    if planet_type == option[8]:                                            
        image = Image.open("pluto.png")
        basewidth = 400

        canvas2 = tk.Canvas(root, height=400, width=400, bg='#171717',bd=0, highlightthickness=0, relief='ridge')
        wpercent = (basewidth / float(image.size[0]))
        hsize = int((float(image.size[1]) * float(wpercent)))
        image = image.resize((basewidth, hsize), PIL.Image.ANTIALIAS)
        photo = ImageTk.PhotoImage(image)
        item4 = canvas2.create_image(225, 210, image=photo)

        canvas2.place(relx=0.05, rely=0.1, relheight=0.6, relwidth=0.5)

        for widget in desc_frame.winfo_children():
            widget.destroy()

        for widget in fact_frame.winfo_children():
            widget.destroy()


        earth_label = tk.Label(desc_frame, text=FULL_PLUTO_DESC, font=('Poppins', 9), bg='#121212', fg='white')
        earth_label.pack()

        earth_fact = tk.Label(fact_frame, text=PLUTO_FACT,font=('Poppins', 12), bg='#121212', fg='white')
        earth_fact.pack(side='left')

        item4.pack()

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH, bg='#171717')
canvas.pack()

desc_frame = tk.Frame(root, bg='#121212')             
desc_frame.place(relx=0.6, rely=0.1, relheight=0.6, relwidth=0.35)

fact_frame = tk.Frame(root, bg='#121212')
fact_frame.place(relx=0.05, rely=0.72, relheight=0.2, relwidth=0.9)


option = ['Merkur', 'Venus', 'Erde', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptun', 'Pluto']
clicked = StringVar()
clicked.set(option[0])
drop = OptionMenu(root, clicked, *option)
drop.place(relx=0.3, rely=0.01, relheight=0.05, relwidth=0.1)

button = tk.Button(canvas, text='Informationen')
button.bind('<Button-1>', planet)
button.place(relx=0.4, rely=0.01, relheight=0.05, relwidth=0.1)

text = 'Willkommen in der Planeten App!\n \n \n Wähle einen Planeten aus, um zu starten.'
text2 = 'Fakten werden hier angezeigt.'

initial_label2 = tk.Label(fact_frame, text=text2, font=('Poppins', 18), bg='#121212', fg='white')
initial_label2.pack(side='left')

initial_label = tk.Label(desc_frame, text=text, font=('Poppins', 12), bg='#121212', fg='white')
initial_label.pack()

root.mainloop()
