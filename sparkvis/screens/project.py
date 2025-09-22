from kivy.uix.screenmanager import Screen
from kivy.lang import Builder

Builder.load_string("""
<ProjectScreen>:
    MDBoxLayout:
        orientation: "vertical"

        MDTopAppBar:
            title: "Project"
            elevation: 4

        MDLabel:
            text: "This is the Project screen."
            halign: "center"
""")

class ProjectScreen(Screen):
    pass
