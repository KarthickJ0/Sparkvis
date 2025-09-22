from kivy.uix.screenmanager import Screen
from kivy.lang import Builder

Builder.load_string("""
<HomeScreen>:
    MDBoxLayout:
        orientation: "vertical"

        MDTopAppBar:
            title: "Home"
            elevation: 4

        MDLabel:
            text: "Welcome to SparkVis!"
            halign: "center"
""")

class HomeScreen(Screen):
    pass
