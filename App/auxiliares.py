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
from kivy.uix.textinput import TextInput
from kivy.uix.checkbox import CheckBox



class HorarioItem(BoxLayout):
    def __init__(self, salida, llegada, empresa,dias, **kwargs):
        super().__init__(orientation='vertical', spacing=1, padding=5, size_hint_y=None, height=65)

        # Fondo de color
         
        if empresa == "Intercordoba":
            self.canvas.before.add(Color(0.4, 0 , 0, 0.3))
        elif empresa == "Fono Bus":
            self.canvas.before.add(Color(0, 0.17, 0, 0.3)) 
        elif empresa == "Eder directo":
            self.canvas.before.add(Color(0, 0, 0, 1)) 
        
        self.canvas.before.add(Rectangle(size=self.size, pos=self.pos))
        self.bind(size=self.update_rect, pos=self.update_rect)
        
        horario_label = Label(text=f"{salida[:5]}    -    {llegada[:5]} ", bold=True, size_hint_y=None,font_size=18, height=20)
        empresa_label = Label(text=empresa, size_hint_y=None, height=20)



        dias_layout = BoxLayout(orientation='horizontal', size_hint_y=None, height=10, spacing=0)
        lun=Label(text="Lu", height=7,font_size=10,  color=(0.5, 0.5, 0.5, 1))  
        mar=Label(text="Ma", height=7,font_size=10, color=(0.5, 0.5, 0.5, 1))
        mie=Label(text="Mi", height=7,font_size=10, color=(0.5, 0.5, 0.5, 1))
        jue=Label(text="Ju", height=7,font_size=10, color=(0.5, 0.5, 0.5, 1))
        vie=Label(text="Vi", height=7,font_size=10, color=(0.5, 0.5, 0.5, 1))
        sab=Label(text="Sa", height=7,font_size=10, color=(0.5, 0.5, 0.5, 1))
        dom=Label(text="Do", height=7,font_size=10, color=(0.5, 0.5, 0.5, 1))
        
        if dias >= 64:
            lun.color=(1, 1, 1, 1)
            dias = dias - 64
        if dias >= 32:
            mar.color=(1, 1, 1, 1)
            dias = dias - 32
        if dias >= 16:
            mie.color=(1, 1, 1, 1)
            dias = dias - 16
        if dias >= 8:
            jue.color=(1, 1, 1, 1)
            dias = dias - 8
        if dias >= 4:
            vie.color=(1, 1, 1, 1)
            dias = dias - 4
        if dias >= 2:
            sab.color=(1, 1, 1, 1)
            dias = dias - 2
        if dias >= 1:
            dom.color=(1, 1, 1, 1)
                                    
        dias_layout.add_widget(lun)
        dias_layout.add_widget(mar)
        dias_layout.add_widget(mie)
        dias_layout.add_widget(jue)
        dias_layout.add_widget(vie)
        dias_layout.add_widget(sab)
        dias_layout.add_widget(dom)                                          

        self.add_widget(horario_label)
        self.add_widget(empresa_label)
        self.add_widget(dias_layout)



    def update_rect(self, *args):
        self.canvas.before.children[-1].size = self.size
        self.canvas.before.children[-1].pos = self.pos




class CarreraPopup(Popup):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.title = "Agregar Carrera"
        self.size_hint = (0.9, 0.4)  # Tamaño de la ventana emergente
        self.auto_dismiss = False  # No se cierra al hacer clic fuera

        layout = BoxLayout(orientation="vertical", spacing=10, padding=10)


        self.text_input = TextInput(hint_text="nombre de la carrera", multiline=False, size_hint=(1, None), height=40)
        layout.add_widget(self.text_input)


        guardar_button = Button(text="Guardar", size_hint=(1, None), height=40)
        guardar_button.bind(on_release=lambda x: self.guardar_carrera())

        close_button = Button(text="Cerrar", size_hint=(1, None), height=40)
        close_button.bind(on_release=self.dismiss)  # Cierra la ventana

        layout.add_widget(guardar_button)
        layout.add_widget(close_button)

        self.content = layout

    def guardar_carrera(self):
        nombre=self.text_input.text
        funciones.guardar_carrera(nombre)
        self.dismiss()


class MateriaPopup(Popup):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.title = "Agregar nueva materia"
        self.size_hint = (0.9, 0.54)  # Tamaño de la ventana emergente
        self.auto_dismiss = False  # No se cierra al hacer clic fuera

        layout = BoxLayout(orientation="vertical", spacing=10, padding=10)

        carreras= funciones.buscar_carreras()
        
        self.diccionario = {item[1] : item[0] for item in carreras}
        


        self.spinner = Spinner(text="Selecciona una carrera", values=list(self.diccionario.keys()),size_hint=(1, None),height=40)
        

        self.text_input = TextInput(hint_text="nombre de la materia", multiline=False, size_hint=(1, None), height=40)
        
        self.comision_input = TextInput(hint_text="comision", multiline=False, size_hint=(1, None), height=40)

        guardar_button = Button(text="Guardar", size_hint=(1, None), height=40)
        guardar_button.bind(on_release=lambda x: self.guardar_materia())

        close_button = Button(text="Cerrar", size_hint=(1, None), height=40)
        close_button.bind(on_release=self.dismiss)  # Cierra la ventana

        layout.add_widget(self.spinner)
        layout.add_widget(self.text_input)
        layout.add_widget(self.comision_input)
        layout.add_widget(guardar_button)
        layout.add_widget(close_button)

        self.content = layout

    def guardar_materia(self):
        nombre=self.text_input.text
        comision = self.comision_input.text
        id = self.diccionario.get(self.spinner.text)
        funciones.guardar_materia(id,nombre,comision)
        self.dismiss()




class DetalleMatPopup(Popup):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.title = "Agregar nuevo horario"
        self.size_hint = (0.9, 0.9)  # Tamaño de la ventana emergente
        self.auto_dismiss = False  # No se cierra al hacer clic fuera

        layout = BoxLayout(orientation="vertical", spacing=5, padding=5)

        carreras= funciones.buscar_materias()
        
        self.diccionario = {item[1] : item[0] for item in carreras}
        


        self.spinner = Spinner(text="Selecciona una Materia", values=list(self.diccionario.keys()),size_hint=(1, None),height=40)
        

        self.tipo_input = TextInput(hint_text="Tipo", multiline=False, size_hint=(1, None), height=40)
        
        self.aula_input = TextInput(hint_text="aula", multiline=False, size_hint=(1, None), height=40)

        dias_layout = BoxLayout(orientation="horizontal", spacing=1)

        self.ch_lun = CheckBox( height=10)
        lun_lab =Label(text="Lun",size_hint_y=None, height=10)

        self.ch_mar = CheckBox( height=10)
        mar_lab =Label(text="Mar",size_hint_y=None, height=10)

        self.ch_mie = CheckBox( height=10)
        mie_lab =Label(text="Mie",size_hint_y=None, height=10)

        self.ch_jue = CheckBox(height=10)
        jue_lab =Label(text="Jue",size_hint_y=None, height=10)

        self.ch_vie = CheckBox( height=10)
        vie_lab =Label(text="Vie", size_hint_y=None, height=10)

        dias_layout.add_widget(lun_lab)
        dias_layout.add_widget(self.ch_lun)

        dias_layout.add_widget(mar_lab)
        dias_layout.add_widget(self.ch_mar)

        dias_layout.add_widget(mie_lab)
        dias_layout.add_widget(self.ch_mie)

        dias_layout.add_widget(jue_lab)
        dias_layout.add_widget(self.ch_jue)

        dias_layout.add_widget(vie_lab)
        dias_layout.add_widget(self.ch_vie)


        hs = ("08","09","10","11","12","13","14","15","16","17","18","19","20")
        min = ("00","10","20","30","40","50")

        inicio_lab =Label(text="Horario Inicio", size_hint_y=None, height=10)

        inicio_layout = BoxLayout(orientation="horizontal", spacing=1, height=10)
        self.inicio_hs = Spinner(text="hora", values=hs, size_hint=(1, 0.7))
        self.inicio_min = Spinner(text="minutos", values=min, size_hint=(1, 0.7))
        
        inicio_layout.add_widget(self.inicio_hs)
        inicio_layout.add_widget(self.inicio_min)

        fin_lab =Label(text="Horario Fin", size_hint_y=None, height=10)

        fin_layout = BoxLayout(orientation="horizontal", spacing=1, height=20)
        self.fin_hs = Spinner(text="hora", values=hs, size_hint=(1, 0.7))
        self.fin_min = Spinner(text="minutos", values=min, size_hint=(1, 0.7))
        
        fin_layout.add_widget(self.fin_hs)
        fin_layout.add_widget(self.fin_min)

        guardar_button = Button(text="Guardar", size_hint=(1, None), height=40)
        guardar_button.bind(on_release=lambda x: self.guardar_detalle())

        close_button = Button(text="Cerrar", size_hint=(1, None), height=40)
        close_button.bind(on_release=self.dismiss)  # Cierra la ventana

        layout.add_widget(self.spinner)
        layout.add_widget(self.tipo_input)
        layout.add_widget(self.aula_input)
        layout.add_widget(inicio_lab)
        layout.add_widget(inicio_layout)
        layout.add_widget(fin_lab)
        layout.add_widget(fin_layout)
        layout.add_widget(dias_layout)
        layout.add_widget(guardar_button)
        layout.add_widget(close_button)

        self.content = layout

    def guardar_detalle(self):

        id_materia = self.diccionario.get(self.spinner.text)
        tipo = self.tipo_input.text
        aula = self.aula_input.text 
        dias = 0
        if self.ch_lun.active:
            dias = dias + 64
        if self.ch_mar.active:
            dias = dias + 32
        if self.ch_mie.active:
            dias = dias + 16
        if self.ch_jue.active:
            dias = dias + 8
        if self.ch_vie.active:
            dias = dias + 4
        hora_inicio = f"{self.inicio_hs.text}:{self.inicio_min.text}"
        hora_fin = f"{self.fin_hs.text}:{self.fin_min.text}"
        
        funciones.guardar_detalle_mat(id_materia, tipo ,dias ,aula ,hora_inicio ,hora_fin)
        self.dismiss()

