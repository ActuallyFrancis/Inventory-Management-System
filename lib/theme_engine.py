import tkinter.ttk as ttk
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from lib import database as db


class ThemeEngine:
    """ Theme Engine consists of two themes: Light Mode and Dark Mode
        Two methods : (1) light_mode  (2) dark_mode
        Colour Pallete used =>
        Light blue for gradient button(TOP) : #05edfe
        Dark blue for gradient button(BOTTOM) : #ffffff
        Main Heading : #22d3fe <- Medium Blue
        Sub-Headings : #ffffff <- Dark blue
    """
    def __init__(self):
        self.style = ttk.Style()
        # self.style.theme_use("clam") #('winnative', 'clam', 'alt', 'default', 'classic', 'vista', 'xpnative')
        # Connecting to Database to fetch last saved theme settings
        db_obj = db.Database()
        theme_value = db_obj.get_theme_value()[1]
        # print(theme_value)
        if theme_value == "Light Mode":
            self.light_mode()
        elif theme_value == "Dark Mode":
            self.dark_mode()

    def light_mode(self):
        # Background Colour -> little grey
        self.style.configure('mainframe.TFrame', background='#c19a6b')
        # Content Frame Colour -> Pure White
        self.style.configure('TFrame', background='#c19a6b')
        # self.style.configure('headings.TLabel', foreground ='#222')
        self.style.configure('TLabel', background='#c19a6b', foreground="black")
        
        # Entry, Buttons Background and foreground
        self.entry_bg = self.button_bg = '#c19a6b'  # Same colour as Content Frame
        self.entry_fg = '#000'
        
    def dark_mode(self):
        # Background Colour -> more dark grey
        self.style.configure('mainframe.TFrame', background='#704214')
        # Background Colour -> less dark grey
        self.style.configure('TFrame', background='#704214')
        # self.style.configure('headings.TLabel', foreground ='red')
        self.style.configure('TLabel', background='#704214', foreground="white")
        
        # Entry, Buttons Background and foreground
        self.entry_bg = self.button_bg = '#704214' # Same colour as Content Frame
        self.entry_fg = '#fff'
        
        