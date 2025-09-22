from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager
from kivymd.app import MDApp

from screens.home import HomeScreen
from screens.project import ProjectScreen

class SparkVisApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "DeepPurple"

        sm = ScreenManager()
        sm.add_widget(HomeScreen(name="home"))
        sm.add_widget(ProjectScreen(name="project"))

        # Load kv files for each screen
        Builder.load_file("screens/home.kv")
        Builder.load_file("screens/project.kv")

        return sm

if __name__ == "__main__":
    SparkVisApp().run()
