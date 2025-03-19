from kivy.app import App

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.core.window import Window
from kivy.graphics import Color, Rectangle
from kivy.config import Config
from kivy.uix.gridlayout import GridLayout
import funciones
from datetime import datetime
import random
import sqlite3
from kivy.uix.popup import Popup
from kivy.uix.spinner import Spinner
from kivy.uix.widget import Widget

from auxiliares import *

Window.size = (270, 600)
#Window.size = (360, 800)

class HorariosScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical')
        

        self.scroll_horarios = ScrollView(size_hint=(1, 1))  
        self.horarios_layout = BoxLayout(orientation='vertical', size_hint_y=None, spacing=0, height=200)
        self.seccion_layout = BoxLayout(orientation='vertical', size_hint_y=None, spacing=20, height=300)
        self.horarios_layout.bind(minimum_height=self.horarios_layout.setter('height'))  

        

        dias_layout = BoxLayout(orientation='horizontal', size_hint_y=None, spacing=1)
        dias_layout.add_widget(Label(text="Hs",size_hint_y=None,height=10))
        dias_layout.add_widget(Label(text="Lun",size_hint_y=None,height=10))
        dias_layout.add_widget(Label(text="Mar",size_hint_y=None,height=10))
        dias_layout.add_widget(Label(text="Mie",size_hint_y=None,height=10))
        dias_layout.add_widget(Label(text="Jue",size_hint_y=None,height=10))
        dias_layout.add_widget(Label(text="Vie",size_hint_y=None,height=10))

        materias_layout = BoxLayout(orientation='horizontal', size_hint_y=None, spacing=1, height=200)
        #horas
        horas_layout = BoxLayout(orientation='vertical', size_hint_y=None, spacing=5)
        
        for hora in range(8, 21):  # De 8 AM a 8 PM
            if hora < 10:
                horas_layout.add_widget(Label(text=f"0{hora}:00", font_size=12, size_hint_y=None, height=10))
            else:
                horas_layout.add_widget(Label(text=f"{hora}:00" , font_size=12, size_hint_y=None, height=10))




        #Lunes
        self.lun_layout = BoxLayout(orientation='vertical', size_hint_y=None, spacing=1)



        #martes
        self.mar_layout = BoxLayout(orientation='vertical', size_hint_y=None, spacing=1)



        #miercoles
        self.mie_layout = BoxLayout(orientation='vertical', size_hint_y=None, spacing=1)
        


        #jueves
        self.jue_layout = BoxLayout(orientation='vertical', size_hint_y=None, spacing=1)
        


        #viernes
        self.vie_layout = BoxLayout(orientation='vertical', size_hint_y=None, spacing=1)
        
        
        
        
        
        
        acciones_layout = BoxLayout(orientation='horizontal', size_hint_y=None, height=30, spacing=5)
        carrera = Button(text="+ Carrera", size_hint_y=None, height=30)
        carrera.bind(on_release=self.open_popup_carrera)

        materia = Button(text="+ Materia", size_hint_y=None, height=30)
        materia.bind(on_release=self.open_popup_materia)

        horario = Button(text="+ Horario", size_hint_y=None, height=30)
        horario.bind(on_release=self.open_popup_detalle)

        #self.ida.bind(on_release=lambda x: self.cargar_colectivos(tipo="S"))
        #self.vuelta.bind(on_release=lambda x: self.cargar_colectivos(tipo="V"))
        acciones_layout.add_widget(carrera)
        acciones_layout.add_widget(materia)
        acciones_layout.add_widget(horario)
        
        
       
        

        materias_layout.add_widget(horas_layout)
        materias_layout.add_widget(self.lun_layout)
        materias_layout.add_widget(self.mar_layout)
        materias_layout.add_widget(self.mie_layout)
        materias_layout.add_widget(self.jue_layout)
        materias_layout.add_widget(self.vie_layout)


        self.horarios_layout.add_widget(dias_layout)
        self.horarios_layout.add_widget(materias_layout)


        
        self.seccion_layout.add_widget(self.horarios_layout)
        self.seccion_layout.add_widget(acciones_layout)

        self.scroll_horarios.add_widget(self.seccion_layout)
        


        acciones_layout = BoxLayout(orientation='horizontal', size_hint_y=None, height=30, spacing=5)












        layout.add_widget(self.scroll_horarios)
        self.add_widget(layout)
        self.cargar_materias()


        


    def open_popup_carrera(self, instance):
        popup = CarreraPopup()
        popup.open()
        



    def open_popup_materia(self, instance):
        popup = MateriaPopup()
        popup.open()
       

    def open_popup_detalle(self, instance):
        popup = DetalleMatPopup()
        popup.open()
        


    def cargar_materias(self):
        colores = [
    (0.1, 0.1, 0.1, 1),  # Negro casi puro
    (0.2, 0.0, 0.2, 1),  # Púrpura oscuro
    (0.2, 0.1, 0.1, 1),  # Rojo oscuro
    (0.1, 0.2, 0.2, 1),  # Verde azulado oscuro
    (0.15, 0.1, 0.3, 1),  # Azul profundo
    (0.2, 0.2, 0.0, 1),  # Verde oliva oscuro
    (0.3, 0.1, 0.1, 1),  # Rojo vino
    (0.1, 0.15, 0.25, 1),  # Azul acero
    (0.2, 0.05, 0.05, 1),  # Marrón oscuro
    (0.15, 0.15, 0.15, 1),  # Gris oscuro
    (0.1, 0.1, 0.2, 1),  # Azul noche
    (0.15, 0.05, 0.2, 1),  # Morado profundo
    (0.2, 0.15, 0.05, 1),  # Mostaza oscuro
    (0.1, 0.2, 0.1, 1),  # Verde bosque
    (0.2, 0.1, 0.15, 1),  # Granate oscuro
    (0.05, 0.05, 0.1, 1),  # Azul casi negro
    (0.1, 0.05, 0.05, 1),  # Marrón café
    (0.05, 0.1, 0.05, 1),  # Verde pino
    (0.1, 0.05, 0.15, 1),  # Púrpura negro
    (0.15, 0.1, 0.1, 1),  # Rojo ladrillo oscuro
]
        largo_box= 14.6 #190 / 13
        self.lun_layout.clear_widgets()
        self.mar_layout.clear_widgets()
        self.mie_layout.clear_widgets()
        self.jue_layout.clear_widgets()
        self.vie_layout.clear_widgets()
        lun = 0
        mar = 0
        mie = 0
        jue = 0
        vie = 0
        materias = funciones.Buscar_materias_completo()
        materias= sorted(materias, key=lambda x: x[7])
        for mat in materias:
            num = mat[5] 
            #Lunes
            if num >= 64:
                num = num - 64
                ini = int(mat[7][:2]) + (int(mat[7][3:5])/60)
                fin = int(mat[8][:2]) + (int(mat[8][3:5])/60)
                if (ini - 8) - lun > 0:#revisar los lun ini
                    self.lun_layout.add_widget(BoxLayout(orientation='horizontal', size_hint_y=None, spacing=1, height=largo_box*((ini - 8)-lun)))
                    lun = lun + ini - 8
                self.lun_layout.add_widget(Button(text=f"""{mat[2]}
{mat[4]}
{mat[3]} {mat[6]}""", size_hint_y=None, height=(fin + 1  - ini)*largo_box, font_size=8, background_color =colores[mat[1]]))
                lun = lun + (fin + 1  - ini)


            #Martes
            if num >= 32:
                num = num - 32
                ini = int(mat[7][:2]) + (int(mat[7][3:5])/60)
                fin = int(mat[8][:2]) + (int(mat[8][3:5])/60)
                if (ini - 8) - mar > 0:#revisar los lun ini
                    self.mar_layout.add_widget(BoxLayout(orientation='horizontal', size_hint_y=None, spacing=1, height=largo_box*((ini - 8)-mar)))
                    mar = mar + ini - 8
                self.mar_layout.add_widget(Button(text=f"""{mat[2]}
{mat[4]}
{mat[3]} {mat[6]}""", size_hint_y=None, height=(fin + 1  - ini)*largo_box, font_size=8, background_color =colores[mat[1]]))
                mar = mar + (fin + 1  - ini)


            #MIercoles
            if num >= 16:
                num = num - 16
                ini = int(mat[7][:2]) + (int(mat[7][3:5])/60)
                fin = int(mat[8][:2]) + (int(mat[8][3:5])/60)
                if (ini - 8) - mie > 0:
                    self.mie_layout.add_widget(BoxLayout(orientation='horizontal', size_hint_y=None, spacing=1, height=largo_box*((ini - 8)-mie)))
                    mie = mie + ini - 8
                self.mie_layout.add_widget(Button(text=f"""{mat[2]}
{mat[4]}
{mat[3]} {mat[6]}""", size_hint_y=None, height=(fin + 1  - ini)*largo_box, font_size=8, background_color =colores[mat[1]]))
                mie = mie + (fin + 1  - ini)

            #Jueves
            if num >= 8:
                num = num - 8
                ini = int(mat[7][:2]) + (int(mat[7][3:5])/60)
                fin = int(mat[8][:2]) + (int(mat[8][3:5])/60)
                if (ini - 8) - jue > 0:
                    self.jue_layout.add_widget(BoxLayout(orientation='horizontal', size_hint_y=None, spacing=1, height=largo_box*((ini - 8)-jue)))
                    jue = jue + ini - 8
                self.jue_layout.add_widget(Button(text=f"""{mat[2]}
{mat[4]}
{mat[3]} {mat[6]}""", size_hint_y=None, height=(fin + 1  - ini)*largo_box, font_size=8, background_color =colores[mat[1]]))
                jue = jue + (fin + 1  - ini)


            #Viernes
            if num >= 4:
                num = num - 4
                ini = int(mat[7][:2]) + (int(mat[7][3:5])/60)
                fin = int(mat[8][:2]) + (int(mat[8][3:5])/60)

                if (ini - 8) - vie > 0:#revisar los lun ini
                    self.vie_layout.add_widget(BoxLayout(orientation='horizontal', size_hint_y=None, spacing=1, height=largo_box*((ini - 8)-vie)))
                    vie = vie + ini - 8
                self.vie_layout.add_widget(Button(text=f"""{mat[2]}
{mat[4]}
{mat[3]} {mat[6]}""", size_hint_y=None, height=(fin + 1 - ini)*largo_box, font_size=8, background_color =colores[mat[1]]))
                vie = vie + (fin + 1  - ini)

        self.lun_layout.add_widget(BoxLayout(orientation='horizontal', size_hint_y=None, spacing=1, height=largo_box*(13-lun)))
        self.mar_layout.add_widget(BoxLayout(orientation='horizontal', size_hint_y=None, spacing=1, height=largo_box*(13-mar)))
        self.mie_layout.add_widget(BoxLayout(orientation='horizontal', size_hint_y=None, spacing=1, height=largo_box*(13-mie)))
        self.jue_layout.add_widget(BoxLayout(orientation='horizontal', size_hint_y=None, spacing=1, height=largo_box*(13-jue)))
        self.vie_layout.add_widget(BoxLayout(orientation='horizontal', size_hint_y=None, spacing=1, height=largo_box*(13-vie)))








class ColectivosScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.colectivos_inter = []

        # Layout principal
        layout = BoxLayout(orientation='vertical', spacing=10, padding=(10, 10, 10, 10))



        #Botones y texto
        #text_inter= Label(text="Interurbanos", height=20 , color=(1, 1, 1, 1)) 
        botones_layout = BoxLayout(orientation='horizontal', spacing=5, size_hint_y=None, height=40)
        self.ida = Button(text="""     IDA
Sal-->Cba""", size_hint_y=None, height=40)
        self.vuelta = Button(text="""   Vuelta
Cba-->Sal""", size_hint_y=None, height=40)

        self.ida.bind(on_release=lambda x: self.cargar_colectivos(tipo="S"))
        self.vuelta.bind(on_release=lambda x: self.cargar_colectivos(tipo="V"))

        botones_layout.add_widget(self.ida)
        botones_layout.add_widget(self.vuelta)
        #layout.add_widget(text_inter)
        layout.add_widget(botones_layout)



        # Contenedor de colectivos
        colectivos_layout = BoxLayout(orientation='vertical', spacing=5, size_hint_y=None, height=430)

        self.scroll_inter = ScrollView(size_hint=(1, 1))  
        self.inter_layout = BoxLayout(orientation='vertical', size_hint_y=None, spacing=5)
        self.inter_layout.bind(minimum_height=self.inter_layout.setter('height'))  

        
        self.scroll_inter.add_widget(self.inter_layout)

        
        colectivos_layout.add_widget(self.scroll_inter)
        layout.add_widget(colectivos_layout)



        acciones_layout = BoxLayout(orientation='horizontal', spacing=3, size_hint_y=None, height=30)

        editar = Button(text="Editar", size_hint_y=None, height=30)
        crear = Button(text="Nuevo", size_hint_y=None, height=30)
        borrar = Button(text="Borrar", size_hint_y=None, height=30)

        self.ida.bind(on_release=lambda x: self.cargar_colectivos(tipo="S"))
        self.vuelta.bind(on_release=lambda x: self.cargar_colectivos(tipo="V"))

        acciones_layout.add_widget(editar)
        acciones_layout.add_widget(crear)
        acciones_layout.add_widget(borrar)
        layout.add_widget(acciones_layout)
        self.add_widget(layout)

        # Cargar los colectivos al inicio
        self.cargar_colectivos(tipo="S")

    def cargar_colectivos(self, tipo):
        largo = 0
        ahora = 0

        if not self.colectivos_inter:
            self.colectivos_inter = funciones.Buscar_Colectivos("I")
        if tipo =="V":
            self.ida.background_color =(0.6, 0.6, 0.6, 1)
            self.vuelta.background_color =(0,0,0,1)
        elif tipo =="S":
            self.vuelta.background_color =(0.6, 0.6, 0.6, 1)
            self.ida.background_color =(0,0,0,1)
        # Limpiar los widgets anteriores en el layout
        self.inter_layout.clear_widgets()
        for colec in self.colectivos_inter:
            if colec[2] == tipo:
                largo = largo + 1
                if datetime.strptime(colec[4], "%H:%M:%S").time() >= datetime.now().time() and ahora == 0:
                    ahora = largo

                self.inter_layout.add_widget(HorarioItem(colec[4], colec[5], colec[0], colec[3]))
        self.scroll_inter.scroll_y =1 - (1/largo)*ahora
        




class Seccion3Screen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.add_widget(Label(text='Sección 3'))

class Seccion4Screen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.add_widget(Label(text='Sección 4'))

class Seccion5Screen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.add_widget(Label(text='Sección 5'))



class MainApp(App):
    def build(self):
        funciones.crear_db()
        

        self.sm = ScreenManager()
        self.sm.add_widget(ColectivosScreen(name='colectivos'))
        self.sm.add_widget(HorariosScreen(name='horarios'))
        
        self.sm.add_widget(Seccion3Screen(name='seccion3'))
        self.sm.add_widget(Seccion4Screen(name='seccion4'))
        self.sm.add_widget(Seccion5Screen(name='seccion5'))
        
        main_layout = BoxLayout(orientation='vertical')
        main_layout.add_widget(self.sm)
        
        nav_layout = BoxLayout(size_hint_y=0.1)
        buttons = [
            ('Horarios', 'horarios'),
            ('Colectivos', 'colectivos'),
            ('Sección 3', 'seccion3'),
            ('Sección 4', 'seccion4'),
            ('Sección 5', 'seccion5')
        ]
        
        for text, screen in buttons:
            btn = Button(text=text)
            btn.bind(on_release=lambda x, s=screen: setattr(self.sm, 'current', s))
            nav_layout.add_widget(btn)
        
        main_layout.add_widget(nav_layout)
        
        return main_layout




if __name__ == '__main__':
    MainApp().run()



        









