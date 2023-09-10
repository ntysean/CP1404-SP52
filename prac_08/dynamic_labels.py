
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.properties import StringProperty
from kivy.uix.label import Label
from kivy.graphics import Color, Rectangle

class DynamicWidgetsApp(App):
    """Main program - Kivy app to demo dynamic widget creation."""
    status_text = StringProperty()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # basic data example - dictionary of names: phone numbers
        # TODO: After running it, add another entry to the dictionary and see how the layout changes
        self.name_to_phone = {"Sean": "12301230", "Asterix": "0441411211", "Obelix": "0432123456", "Herp": "12312312"}

    def build(self):
        self.title = "Dynamic Widgets"
        self.root = Builder.load_file('dynamic_widgets.kv')
        self.create_widgets()
        return self.root

    def create_widgets(self):
        for name in self.name_to_phone:
            temp_label = Label(text=name)
            temp_label.bind(on_release=self.press_entry)
            self.root.ids.entries_box.add_widget(temp_label)

    def press_entry(self, instance):
        # get name (dictionary key) from the text of Button we clicked on
        name = instance.text
        # update status text
        self.status_text = "{}'s number is {}".format(name, self.name_to_phone[name])



DynamicWidgetsApp().run()
