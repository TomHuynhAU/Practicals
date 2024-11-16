from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label

class SimpleLabelsApp(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # Basic data (model) example - list of names
        self.names = ["Alice", "Bob", "Charlie"]

    def build(self):
        self.title = "Simple Labels"
        self.root = Builder.load_file('dynamic_labels.kv')
        self.create_labels()
        return self.root

    def create_labels(self):
        for name in self.names:
            label = Label(text=name)
            self.root.ids.main.add_widget(label)

if __name__ == "__main__":
    SimpleLabelsApp().run()
