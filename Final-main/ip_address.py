import os
os.environ['KIVY_GL_BACKEND'] = 'angle_sdl2'  # Use DirectX instead of OpenGL

from firebase import firebase
firebase = firebase.FirebaseApplication("https://radar-c44c6-default-rtdb.asia-southeast1.firebasedatabase.app/", None)

res = firebase.get("radar-c44c6-default-rtdb/Users/Threat", "")
try:
    for i in res.keys():
        print(res[i]["ip_address"])

        ak = res[i]["ip_address"]

    bk = input("Do you want to remove :")
    if bk == "y":
        ak = firebase.delete("radar-c44c6-default-rtdb/Users/Threat","")
    else:
        pass


except:
    print("There is not an ip address")