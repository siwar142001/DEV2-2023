helper = """
ScreenManager:
    MenuScreen:
    EmployeeScreen:
    OwnerScreen:
    LoginScreen:
    AvailableScreen:
    ReserveScreen:
    CheckScreen:
    RevenueScreen:

<MenuScreen>:
    name: 'acceuil'
    BoxLayout:
        canvas:
            Color:
                rgba: (251/255,132/255,0/255,1)
            Rectangle:
                size: self.size
                pos: self.pos
    MDLabel:
        text: 'Bienvenue Au Parking ParkMetre'
        halign: 'center'
        theme_text_color: 'Custom'
        text_color: (79/255,32/255,13/255,1)
        font_style: 'H3'
        pos_hint: {'center_x' :0.5, 'center_y' :0.9}
    MDLabel:
        text: 'Choisisez Votre Option'
        halign: 'center'
        theme_text_color: 'Custom'
        text_color: (79/255,32/255,13/255,1)
        font_style: 'H5'
        pos_hint: {'center_x' :0.5, 'center_y' :0.7}
    MDRectangleFlatButton:
        text: 'Employee'
        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
        on_press: root.manager.current = 'employee'
        md_bg_color: 255/255, 217/255, 61/255, 1
    MDRectangleFlatButton:
        text: 'Owner'
        pos_hint: {'center_x': 0.5, 'center_y': 0.6}
        on_press: root.manager.current = 'login'
        md_bg_color: 255/255, 217/255, 61/255, 1

<EmployeeScreen>
    name: 'employee'
    BoxLayout:
        canvas:
            Color:
                rgba: (251/255,132/255,0/255,1)
            Rectangle:
                size: self.size
                pos: self.pos
    MDLabel:
        text: 'Bienvenue'
        halign: 'center'
        theme_text_color: 'Custom'
        text_color: (79/255,32/255,13/255,1)
        font_style: 'H3'
        pos_hint: {'center_x' :0.5, 'center_y' :0.9}
    MDRectangleFlatButton:
        text: 'Retour'
        pos_hint: {'center_x': 0.5, 'center_y': 0.2}
        on_press: root.manager.current = 'acceuil'
        md_bg_color: 255/255, 217/255, 61/255, 1
    MDRectangleFlatButton:
        text: 'Available'
        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
        on_press: root.manager.current = 'available'
        md_bg_color: 255/255, 217/255, 61/255, 1

        
<OwnerScreen>
    name: 'owner'
    BoxLayout:
        canvas:
            Color:
                rgba: (251/255,132/255,0/255,1)
            Rectangle:
                size: self.size
                pos: self.pos    
    MDLabel: 
        text: 'Bienvenue M.parkmetre'
        halign: 'center'
        theme_text_color: 'Custom'
        text_color: (79/255,32/255,13/255,1)
        font_style: 'H3'
        pos_hint: {'center_x' :0.5, 'center_y' :0.9} 
    MDRectangleFlatButton:
        text: 'Retour'
        pos_hint: {'center_x': 0.5, 'center_y': 0.2}
        on_press: root.manager.current = 'acceuil'
        md_bg_color: 255/255, 217/255, 61/255, 1
    MDRectangleFlatButton:
        text: 'Check Status'
        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
        on_press: root.manager.current = 'check'
        md_bg_color: 255/255, 217/255, 61/255, 1
    MDRectangleFlatButton:
        text: 'Revenue'
        pos_hint: {'center_x': 0.3, 'center_y': 0.5}
        on_press: root.manager.current = 'revenue'
        md_bg_color: 255/255, 217/255, 61/255, 1
    MDRectangleFlatButton:
        text: 'Reserve'
        pos_hint: {'center_x': 0.7, 'center_y': 0.5}
        on_press: root.manager.current = 'reserve'
        md_bg_color: 255/255, 217/255, 61/255, 1

<LoginScreen>
    name: 'login'
    BoxLayout:
        canvas:
            Color:
                rgba: (251/255,132/255,0/255,1)
            Rectangle:
                size: self.size
                pos: self.pos
    MDTextField:
        id: username_input
        hint_text: 'Enter Username'
        helper_text: 'or click on forgot username'
        helper_text_mode: 'on_focus'
        icon_right: 'parking'
        icon_right_color: app.theme_cls.primary_color
        pos_hint: {'center_x' :0.5, 'center_y': 0.6}
        md_bg_color: 255/255, 217/255, 61/255, 1 
        size_hint_x: None
        width: 300
    MDTextField:
        id: password_input
        hint_text: 'Enter Password'
        password: True
        helper_text: 'Or click on forgot password'
        helper_text_mode: 'on_focus'
        icon_right: 'lock'
        icon_right_color: app.theme_cls.primary_color
        pos_hint: {'center_x' :0.5, 'center_y': 0.5}
        md_bg_color: 255/255, 217/255, 61/255, 1
        size_hint_x: None
        width: 300 
    MDRectangleFlatButton:
        text: 'Login'
        on_press: root.login(username_input.text, password_input.text)
        pos_hint: {'center_x' :0.5, 'center_y': 0.4}
        md_bg_color: 255/255, 217/255, 61/255, 1
        size_hint_x: None
        width: 300

<AvailableScreen>
    name: 'available'
    BoxLayout:
        canvas:
            Color:
                rgba: (251/255,132/255,0/255,1)
            Rectangle:
                size: self.size
                pos: self.pos
    MDLabel:
        text: 'Bienvenue Au Parking ParkMetre'
        halign: 'center'
        theme_text_color: 'Custom'
        text_color: (79/255,32/255,13/255,1)
        font_style: 'H3'
        pos_hint: {'center_x' :0.5, 'center_y' :0.9}
    MDLabel:
        text: 'You can check the availability of your parking'
        halign: 'center'
        theme_text_color: 'Custom'
        text_color: (79/255,32/255,13/255,1)
        font_style: 'H5'
        pos_hint: {'center_x' :0.5, 'center_y' :0.7}
    MDRectangleFlatButton:
        text: 'Retour'
        pos_hint: {'center_x': 0.5, 'center_y': 0.2}
        on_press: root.manager.current = 'employee'
        md_bg_color: 255/255, 217/255, 61/255, 1 

<ReserveScreen>
    name: 'reserve'
    BoxLayout:
        canvas:
            Color:
                rgba: (251/255,132/255,0/255,1)
            Rectangle:
                size: self.size
                pos: self.pos
    MDLabel:
        text: 'Bienvenue Au Parking ParkMetre'
        halign: 'center'
        theme_text_color: 'Custom'
        text_color: (79/255,32/255,13/255,1)
        font_style: 'H3'
        pos_hint: {'center_x' :0.5, 'center_y' :0.9}
    MDLabel:
        text: 'Choose level and spot to reserve'
        halign: 'center'
        theme_text_color: 'Custom'
        text_color: (79/255,32/255,13/255,1)
        font_style: 'H5'
        pos_hint: {'center_x' :0.5, 'center_y' :0.7}
    MDRectangleFlatButton:
        text: 'Retour'
        pos_hint: {'center_x': 0.5, 'center_y': 0.2}
        on_press: root.manager.current = 'owner'
        md_bg_color: 255/255, 217/255, 61/255, 1

<CheckScreen>
    name: 'check'
    BoxLayout:
        canvas:
            Color:
                rgba: (251/255,132/255,0/255,1)
            Rectangle:
                size: self.size
                pos: self.pos
    MDLabel:
        text: 'Bienvenue Au Parking ParkMetre'
        halign: 'center'
        theme_text_color: 'Custom'
        text_color: (79/255,32/255,13/255,1)
        font_style: 'H3'
        pos_hint: {'center_x' :0.5, 'center_y' :0.9}
    MDLabel:
        text: 'You can check the availability of your parking'
        halign: 'center'
        theme_text_color: 'Custom'
        text_color: (79/255,32/255,13/255,1)
        font_style: 'H5'
        pos_hint: {'center_x' :0.5, 'center_y' :0.7}
    MDRectangleFlatButton:
        text: 'Retour'
        pos_hint: {'center_x': 0.5, 'center_y': 0.2}
        on_press: root.manager.current = 'owner'
        md_bg_color: 255/255, 217/255, 61/255, 1 

<RevenueScreen>
    name: 'revenue'
    BoxLayout:
        canvas:
            Color:
                rgba: (251/255,132/255,0/255,1)
            Rectangle:
                size: self.size
                pos: self.pos
    MDLabel:
        text: 'Bienvenue Au Parking ParkMetre'
        halign: 'center'
        theme_text_color: 'Custom'
        text_color: (79/255,32/255,13/255,1)
        font_style: 'H3'
        pos_hint: {'center_x' :0.5, 'center_y' :0.9}
    MDLabel:
        text: 'You can see the profit made by the parking'
        halign: 'center'
        theme_text_color: 'Custom'
        text_color: (79/255,32/255,13/255,1)
        font_style: 'H5'
        pos_hint: {'center_x' :0.5, 'center_y' :0.7}      
    MDRectangleFlatButton:
        text: 'Retour'
        pos_hint: {'center_x': 0.5, 'center_y': 0.2}
        on_press: root.manager.current = 'owner'
        md_bg_color: 255/255, 217/255, 61/255, 1 

"""