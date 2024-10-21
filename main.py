from kivy.lang import Builder
from kivy.core.window import Window
from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.dialog import MDDialog
from kivymd.uix.label import MDLabel
from kivy.uix.image import Image

# Устанавливаем размер окна (для разработки на ПК)
Window.size = (360, 640)

KV = '''
ScreenManager:
    LoginScreen:
    MainScreen:

<LoginScreen>:
    name: 'login'
    MDBoxLayout:
        orientation: 'vertical'
        padding: "20dp"
        spacing: "20dp"
        MDLabel:
            text: "Добро пожаловать!"
            halign: "center"
            font_style: "H5"
        MDTextField:
            id: username
            hint_text: "Username"
            size_hint_x: 0.8
            pos_hint: {"center_x": 0.5}
        MDTextField:
            id: password
            hint_text: "Password"
            password: True
            size_hint_x: 0.8
            pos_hint: {"center_x": 0.5}
        MDRaisedButton:
            text: "Login"
            size_hint_x: 0.8
            pos_hint: {"center_x": 0.5}
            on_release: app.check_login()

<MainScreen>:
    name: 'main'
    MDNavigationLayout:
        ScreenManager:
            Screen:
                MDTopAppBar:
                    title: "Navigation Drawer"
                    elevation: 4
                    pos_hint: {"top": 1}
                    md_bg_color: "#6200EE"
                    specific_text_color: "white"
                    left_action_items:
                        [['menu', lambda x: nav_drawer.set_state("open")]]
        MDNavigationDrawer:
            id: nav_drawer
            radius: (0, 16, 16, 0)
            ContentNavigationDrawer:
    MDBottomNavigation:
        id: bottom_navigation
        panel_color: "#6200EE"
        text_color_active: "white"
        text_color_normal: "gray"
        MDBottomNavigationItem:
            name: 'screen_home'
            text: 'Главная'
            icon: 'home'
            MDBoxLayout:
                orientation: 'vertical'
                MDLabel:
                    text: "IT технологии в 21 веке"
                    halign: 'center'
                    pos_hint: {"center_y": 0.6}
        MDBottomNavigationItem:
            name: 'screen_articles'
            text: 'Статьи'
            icon: 'newspaper'
            MDLabel:
                text: "Читать статьи"
                halign: 'center'
                pos_hint: {"center_y": 0.6}
        MDBottomNavigationItem:
            name: 'screen_navigation'
            text: 'NavigationDrawer'
            icon: 'menu'
            MDLabel:
                text: "Навигационный ящик"
                halign: 'center'
                pos_hint: {"center_y": 0.6}
            MDTextField:
                hint_text: "Введите текст"
                pos_hint: {"center_x": 0.5, "center_y": 0.4}
                size_hint_x: 0.8

<ContentNavigationDrawer@MDBoxLayout>:
    orientation: "vertical"
    padding: "8dp"
    spacing: "8dp"
    Image:
        source: "your_image.png"  # Путь к изображению
        size_hint: None, None
        size: "56dp", "56dp"
    MDLabel:
        text: "Ваше Имя"
        font_style: "Button"
        size_hint_y: None
        height: self.texture_size[1]
    MDLabel:
        text: "example@example.com"
        font_style: "Caption"
        size_hint_y: None
        height: self.texture_size[1]
'''


class LoginScreen(MDScreen):
    pass


class MainScreen(MDScreen):
    pass


class MyApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "DeepPurple"
        self.theme_cls.theme_style = "Light"
        return Builder.load_string(KV)

    def check_login(self):
        username = self.root.get_screen('login').ids.username.text
        password = self.root.get_screen('login').ids.password.text

        if username == "admin" and password == "admin":
            self.root.current = 'main'
        else:
            self.show_login_error()

    def show_login_error(self):
        dialog = MDDialog(
            title="Ошибка",
            text="Неверный логин или пароль.",
            size_hint=(0.8, 1),
        )
        dialog.open()

    def on_button_press(self):
        # Переход на вкладку "Статьи"
        self.root.get_screen('main').ids.bottom_navigation.current = 'screen_articles'


if __name__ == "__main__":
    MyApp().run()