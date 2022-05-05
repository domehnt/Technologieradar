from tkinter import *
import webbrowser
from tkinter import messagebox
from matplotlib import pyplot as plt


class Page(Frame):
    def __init__(self, *args, **kwargs):
        Frame.__init__(self, *args, **kwargs)

    def show(self):
        self.lift()


class Page1(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)

        label = Label(self, text="Radar", bg="#f6f7fb")
        label.place(x=2, y=2)

        # Keywords
        keywords = Entry(self)

        def printKeywords():
            kwords = keywords.get()
            keywords_label = Label(self, text=f'Keywords: {kwords}', pady=1, anchor=W)
            keywords_label.place(relx=0.2, rely=0.2, relwidth=0.5, anchor=NW)

        # Start Button toggle and Warning-Message
        def toggle():
            if start_button.config('text')[-1] == 'START':
                start_button.config(text='STOP')
            else:
                ab = messagebox.askquestion("Wirklich Abbrechen?", "Wollen Sie den Vorgang abbrechen?")
                if ab == "yes":
                    start_button.config(text='START')
                    #### Christian start Button

        # Icons
        self.facebook_icon = PhotoImage(file="icons/facebook.png")
        self.linkedin_icon = PhotoImage(file="icons/linkedin.png")
        self.twitter_icon = PhotoImage(file="icons/twitter.png")

        # Buttons
        facebook_btn = Button(self, image=self.facebook_icon, bg="#f6f7fb", activebackground="#f6f7fb", borderwidth=0)
        linkedin_btn = Button(self, image=self.linkedin_icon, bg="#f6f7fb", activebackground="#f6f7fb", borderwidth=0)
        twitter_btn = Button(self, image=self.twitter_icon, bg="#f6f7fb", activebackground="#f6f7fb", borderwidth=0)

        # Enter Keywords Button ###Christian
        enter_button = Button(self, text="Enter", padx=10, pady=5, command=printKeywords, borderwidth=1)

        # Start Button
        start_button = Button(self, text="START", font=8, bg="#f9faff", command=toggle, activebackground='white',
                              borderwidth=0.5)

        # Slider
        sltext = Label(self, text="Tage:", font=6, bg="#f6f7fb")
        sl = Scale(self, from_=1, to=7, font=6, bg="#f6f7fb", orient=HORIZONTAL)

        # Placements
        keywords.place(relx=0.2, rely=0.1, relwidth=0.5, height=30, anchor=NW)
        enter_button.place(relx=0.75, rely=0.1, anchor=N)
        facebook_btn.place(relx=0.2, rely=0.3, height=100, anchor=NW)
        linkedin_btn.place(relx=0.4, rely=0.3, height=100, anchor=NW)
        twitter_btn.place(relx=0.6, rely=0.3, height=100, anchor=NW)
        sltext.place(relx=0.25, rely=0.6, anchor=NW)
        sl.place(relx=0.35, rely=0.6, relwidth=0.3, anchor=NW)
        start_button.place(relx=0.3, rely=0.8, relheight=0.1, relwidth=0.3, anchor=NW)


class Page2(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)
        label = Label(self, text="Databank", bg="#f6f7fb")

        dataset = 0
        dataset_count = Label(self, text=f'Datensätze . . . . . . . . . . . . . . . . . . . .  {dataset}', bg="#f6f7fb",
                              anchor=W)

        dataset_count.place(relx=0.2, rely=0.1, relwidth=0.5, height=30, anchor=NW)
        label.place(x=2, y=2)


class Page3(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)
        label = Label(self, text="Diagram", bg="#f6f7fb")

        # x-axis values in a list
        x = [7, 2, 5]

        # y-axis values in a list
        stimmen = ['Positiv', 'Negativ', 'Neutral']

        self.pie_icon = PhotoImage(file="icons/diagram.png")
        pie_icon = Button(self, image=self.pie_icon, bg="#f6f7fb", command=lambda: plt.show(),
                          activebackground="#f6f7fb")

        def export():
            plt.pie(x, labels=stimmen)
            plt.savefig('Technologie-Radar.pdf')

        self.download_icon = PhotoImage(file="icons/download.png")
        download_icon = Button(self, image=self.download_icon, bg="#f6f7fb", command=export,
                               activebackground="#f6f7fb", borderwidth=0.5)

        label.place(x=2, y=2)
        download_icon.place(relx=0.95, rely=0.95, anchor=SE)
        pie_icon.place(relx=0.2, rely=0.3, anchor=NW)


class Page4(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)

        # Language Settings
        def display_selected(choice):
            choice = variable.get()
            if choice == "Deutsch":
                print("Hallo!")
            else:
                print("hello")

        # Define a callback function for Link
        def callback(url):
            webbrowser.open_new_tab(url)

        # Dropdown Menu for Languages
        languages = ['Deutsch', 'English']
        variable = StringVar()
        variable.set(languages[0])
        dropdown = OptionMenu(self, variable, *languages, command=display_selected)

        self.logo_png = PhotoImage(file="icons/Logo.png")

        # Labels
        link = Label(self, text="Github", bg="#f6f7fb", font=('Helveticabold', 12), fg="blue", cursor="hand2")
        readmelink = Label(self, text="readme", bg="#f6f7fb", font=('Helveticabold', 12), fg="blue", cursor="hand2")
        logo = Label(self, image=self.logo_png, bg="#f6f7fb")
        ll = Label(self, text="Sprache:", bg="#f6f7fb")
        vt = Label(self, text="Technologie-Radar\nCopyright ⓒ 2022 \nVersion 1.0", bg="#f6f7fb")

        link.bind('<Button-1>', lambda e: callback("https://github.com/mrfabixx/Technologie_Radar"))
        readmelink.bind('<Button-1>', lambda e: callback("README.md"))

        # Placements
        vt.place(relx=0.1, rely=0.2)
        dropdown.place(relx=0.2, rely=0.4)
        ll.place(relx=0.1, rely=0.4)
        link.place(relx=0.1, rely=.55)
        readmelink.place(relx=0.1, rely=.6)
        logo.place(relx=1, rely=1, anchor=SE)


# Menu System
class MainView(Frame):
    def __init__(self, *args, **kwargs):
        Frame.__init__(self, *args, **kwargs)
        p1 = Page1(self, bg="#f6f7fb")
        p2 = Page2(self, bg="#f6f7fb")
        p3 = Page3(self, bg="#f6f7fb")
        p4 = Page4(self, bg="#f6f7fb")

        buttonframe = Frame(self, bg="#0f65af")
        container = Frame(self, bg="#f6f7fb")
        buttonframe.pack(side="left", fill="y", expand=False)
        container.pack(side="top", fill="both", expand=True)

        p1.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p2.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p3.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p4.place(in_=container, x=0, y=0, relwidth=1, relheight=1)

        # Icons
        self.radar_btn = PhotoImage(file="icons/wradar.png")
        self.databank_btn = PhotoImage(file="icons/wdatabank.png")
        self.diagram_btn = PhotoImage(file="icons/wdiagram.png")
        self.settings_btn = PhotoImage(file="icons/wsettings.png")

        # Buttons for Pages
        b1 = Button(buttonframe, image=self.radar_btn, bg="#0f65af", activebackground="#003055", command=p1.show,
                    borderwidth=0)
        b2 = Button(buttonframe, image=self.databank_btn, bg="#0f65af", activebackground="#003055", command=p2.show,
                    borderwidth=0)
        b3 = Button(buttonframe, image=self.diagram_btn, bg="#0f65af", activebackground="#003055", command=p3.show,
                    borderwidth=0)
        b4 = Button(buttonframe, image=self.settings_btn, bg="#0f65af", activebackground="#003055", command=p4.show,
                    borderwidth=0)

        b1.pack(side="top")
        b2.pack(side="top")
        b3.pack(side="top")
        b4.pack(side="bottom")

        p2.show()
        p1.show()


if __name__ == "__main__":
    root = Tk()
    main = MainView(root)
    main.pack(side="top", fill="both", expand=True)
    root.title('Technologie Radar')
    root.iconbitmap('icons/radar.ico')
    root.wm_geometry('800x600')
    root.minsize(800, 600)
    # root.resizable(width=False, height=False)
    root.mainloop()