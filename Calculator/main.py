from kivy.app import App
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.uix.widget import Widget

Window.size=(400,500)
Builder.load_file("calc.kv")
class Root(Widget):
    string=''
    def clear(self):
        self.ids.input.text="0"
    def back(self):
        string = self.ids.input.text
        if len(string)==1 or string=="**2":
            string='0'
            self.ids.input.text = string
            return
        if string.endswith("**2"):
            string=string[:-2]
            self.ids.input.text = string
        string=string[:-1]
        self.ids.input.text=string
    def evaluate(self):
        try:
            string = self.ids.input.text
            self.ids.input.text=str(eval(string))
        except:
            self.ids.input.text="ERROR"
    def click(self, s):
        string = self.ids.input.text
        if string=='0':
            self.ids.input.text=""
            self.ids.input.text=f'{s}'
        else:
            self.ids.input.text=f'{string}{s}'

class MainApp(App):
    title = "Calculator"
    def build(self):
        return Root()
if __name__=="__main__":
    MainApp().run()