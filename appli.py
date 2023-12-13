from kivymd.app import MDApp
from kivy.lang.builder import Builder
from kivy.uix.screenmanager import Screen, ScreenManager
from screen_helper import helper

class MenuScreen(Screen):
    pass

class EmployeeScreen(Screen):
    pass

class OwnerScreen(Screen):
    pass

class LoginScreen(Screen):
    def login(self, username, password):
        if username == 'admin' and password == 'password123':
            self.manager.current = 'owner'
        else:
            print("Invalid username or password")

class ReserveScreen(Screen):
    pass

class CheckScreen(Screen):
    pass

class RevenueScreen(Screen):
    pass

class AvailableScreen(Screen):
    pass

sm = ScreenManager()
sm.add_widget(MenuScreen(name='acceuil'))
sm.add_widget(EmployeeScreen(name='employee'))
sm.add_widget(OwnerScreen(name='owner'))
sm.add_widget(LoginScreen(name='login'))
sm.add_widget(AvailableScreen(name='available'))
sm.add_widget(ReserveScreen(name='reserve'))
sm.add_widget(CheckScreen(name='check'))
sm.add_widget(RevenueScreen(name='revenue'))

class ParkingApp(MDApp):

    def build(self):
        self.theme_cls.primary_palette = 'Orange'
        self.theme_cls.primary_hue = '900' 

        screen = Builder.load_string(helper) 

        return screen

ParkingApp().run()