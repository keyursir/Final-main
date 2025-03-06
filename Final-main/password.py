import os
os.environ['KIVY_GL_BACKEND'] = 'angle_sdl2'  # Use DirectX instead of OpenGL

from firebase import firebase
firebase = firebase.FirebaseApplication("https://radar-c44c6-default-rtdb.asia-southeast1.firebasedatabase.app/", None)

from kivymd.app import MDApp
from kivy.lang import Builder

KV = """
MDFloatLayout:
    MDNavigationLayout:
        ScreenManager:
            id: screen_manager

            MDScreen:
                name: "login_screen"
                MDLabel:
                    id: lab
                    text: "Login Screen"
"""

class WebView(MDApp):
    def build(self):
        screen = Builder.load_string(KV)
        
        return screen
    
    def on_start(self):
        #ak = firebase.delete("abhay-121-default-rtdb/Users/password","")
        res = firebase.get("radar-c44c6-default-rtdb/Users/password", "")
        print(res)
        try:
            for i in res.keys():
                pass
                ak = str(res[i]["password"])
                # print(ak)
        except:
            self.root.ids.lab.text = "There is no Password Currently"


        self.root.ids.lab.text = "Password: " + ak
        a = firebase.delete("radar-c44c6-default-rtdb/Users/password","")
        
            
if __name__ == "__main__":
    WebView().run()

