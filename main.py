# 1. OpenCV (cv2): É uma biblioteca popular de visão computacional usada para processar imagens e vídeos. Com o OpenCV, você pode realizar tarefas como detecção de rostos, reconhecimento de objetos, calibração de câmera e muito mais. É amplamente utilizada em aplicações de visão por computador, como reconhecimento facial, monitoramento de segurança, realidade aumentada, entre outros.

# 2. cvzone: É uma extensão da OpenCV que fornece funcionalidades adicionais e simplificações para tarefas comuns de visão computacional. Oferece uma gama de recursos úteis para desenvolvimento rápido de aplicações, como detecção de mãos, rastreamento de pontos de interesse, entre outros.

# 3. A biblioteca cvzone.ColorModule importa uma classe chamada ColorFinder de um módulo específico da biblioteca cvzone. Esta classe é útil para identificar e encontrar cores em uma imagem.

# 4.NumPy (numpy): É uma biblioteca fundamental para computação numérica em Python. Ela fornece suporte para arrays multidimensionais, juntamente com uma grande coleção de funções matemáticas de alto nível para operar nesses arrays. NumPy é amplamente utilizado em processamento de imagem, análise de dados, aprendizado de máquina e muitas outras áreas onde a computação numérica é essencial.


# biblioteca do back
import cv2  # pip install opencv-python
import cvzone  # pip install cvzone
from cvzone.ColorModule import ColorFinder
import numpy as np  # pip install numpy

# Framework kivymd para cria font.
from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivy.lang import Builder
from kivy.core.window import Window
from kivymd.theming import ThemeManager
from kivy.config import Config
Config.set('graphics', 'resizable', False)

# Estrutura do front. 
KV = """
ScreenManager:
    id: screen_manager


    Telaentrda:
    Telalogin:
    

<Telaentrda>:
    name: 'Telaentrada'

    Image:
        source: 'f1.png'
        size: (2100, 2100)
        pos_hint: {'center_x': 0.5, 'center_y': 0.75 } 
    
    MDLabel:
        text: " Nosso aplicativo de previsão de jogadas de basquete apresenta uma abordagem inovadora para estratégia. Por meio de vídeos, nossa interface intuitiva revela os ângulos que faltaram para marcar pontos cruciais. Desenvolvido com Python e o framework KivyMD, ele utiliza as bibliotecas OpenCV, cvzone e NumPy para aprimorar os vídeos, criando linhas de mapeamento dos ângulos e oferecendo insights valiosos para os treinadores e jogadores. "
        icon: 'earth'
        font_style: 'H6'
        bold: True
        pos_hint: {'center_x': 0.53, 'center_y':0.35}


    MDRoundFlatIconButton:
        text: "ENTRAR"
        icon: "play"
        theme_text_color: "Custom"
        text_color: 1, 0.5, 0, 1  # Laranja padrão
        user_font_size: "50sp"  # Tamanho aumentado
        pos_hint: {"center_x": .5, "center_y": .12}      
        on_press: app.root.current = 'Telalogin' 
                    
<Telalogin>:
    name: 'Telalogin'

    
    Image:
        source: 'f1.png'
        size_hint: (50.0, 80.0)
        pos_hint: {'center_x': 0.5, 'center_y': 0.70 }  

    MDLabel:
        text: "1: Primeiro, por favor, mova o arquivo de vídeo para esta pasta."
        icon: 'earth'
        font_style: 'H5'
        bold: True
        pos_hint: {'center_x': 0.6, 'center_y':0.50}
    
    MDLabel:
        text: "2: Em seguida, insira o nome do vídeo na caixa abaixo. "
        icon: 'earth'
        font_style: 'H5'
        bold: True
        pos_hint: {'center_x': 0.6, 'center_y':0.45}

    MDLabel:
        text: "3: Por último, pressione o botão 'Gerar'. "
        icon: 'earth'
        font_style: 'H5'
        bold: True
        pos_hint: {'center_x': 0.6, 'center_y':0.40}

    MDTextField:
        
        id: usuario
        adaptive_size: True
        hint_text: "Nome_do_video"
        mode:"rectangle"
        pos_hint: {'center_x': 0.5, 'center_y': 0.25}
        size_hint_x: 0.8
        icon_right: "play"
        icon_right_color: app.theme_cls.primary_color

    MDRoundFlatIconButton:
        adaptive_size: True
        text: "Gerar"
        pos_hint: {'center_x': 0.5, 'center_y': 0.10}
        on_press: app.back_function()

     
"""
# Criação de class para gera novas telas.


class Telaentrda(MDScreen):
    pass

class Telalogin(MDScreen):
    pass
 
class MainApp(MDApp):
    theme_cls = ThemeManager()

    def build(self):
        self.Telalogin = Builder.load_string(KV)
        self.theme_cls.theme_style_switch_animation = True
        self.theme_cls.theme_style = "Dark" 
        self.theme_cls.primary_palette="Orange"
        Window.size = (900, 600)

        return self.Telalogin
    

    def back_function(self):
        # Obtendo dados dos campos de entrada da tela de cadastro !

         # Obtenha os valores dos campos de entrada de usuário e senha que ficam no Telalogin 
        name = self.Telalogin.get_screen('Telalogin').ids.usuario.text

        try:
            print(name)
            print(type(name))
    
            video = cv2.VideoCapture(name+'.mp4')  # Abrir o video 

            my_color_finder = ColorFinder(False)  # Instanciar o objeto ColorFinder
            # Valores HSV para a cor vermelha
            hsv_values = {'hmin': 8,
                        'smin': 96, 
                        'vmin': 115, 
                        'hmax': 14, 
                        'smax': 255, 
                        'vmax': 255}

            points_list = []  # Lista de pontos
            points_listX = []  # Lista de pontos X
            points_listY = []  # Lista de pontos Y
            x_list = [item for item in range(0,1300)]  # Lista de pontos X para desenhar a parabola

            while True:
                _, frame = video.read()  # Ler o frame
                img = frame[0:900, :] # Cortar o frame
                img_color, mask = my_color_finder.update(img, hsv_values)  # Atualizar o objeto ColorFinder
                img_contour, contours = cvzone.findContours(img, mask, minArea=500)  # Encontrar os contornos
                if contours:
                    # cx,cy = contours[0]['center']
                    points_list.append(contours[0]['center'])
                    points_listX.append(contours[0]['center'][0])
                    points_listY.append(contours[0]['center'][1])

                if points_listX:  # Se a lista de pontos X não estiver vazia
                    coeff = np.polyfit(points_listX, points_listY,2)  # Calcular os coeficientes da parabola
                    for point in points_list:  # Percorrer a lista de pontos
                        cv2.circle(img_contour, point,10,(0,255,0), cv2.FILLED)  # Desenhar um circulo em cada ponto

                    for x in x_list:  # Percorrer a lista de pontos X
                        poly = np.poly1d(coeff)  # Criar a parabola
                        y = int(poly(x))  # Calcular o ponto Y
                        # Desenhar um circulo em cada ponto da parabola
                        cv2.circle(img_contour, (x,y), 2, (255, 0, 255), cv2.FILLED)
                        if x >=330 and x <=410 and y >=580 and y<=610:  # Se o ponto estiver dentro do retangulo
                            cv2.rectangle(img_contour, (550,600),(850,660), (0,255,0),-1)
                            cv2.putText(img_contour, 'ACERTOU', (560,650), cv2.FONT_HERSHEY_SIMPLEX, 2, (255,255,255),5)

                cv2.imshow('Video', img_contour)
                cv2.waitKey(100)
        except:
                    print("erro")

if __name__ == '__main__':
    MainApp().run()