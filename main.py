from kivy.lang import Builder
from kivy.properties import ObjectProperty

from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
from kivymd.uix.scrollview import MDScrollView
from kivy.uix.button import Button

from kivymd.uix.menu import MDDropdownMenu
from kivymd.uix.banner import MDBanner
#PEKLAMA
from kivmob import KivMob, TestIds

from kivy.metrics import dp

from kivymd.uix.list import OneLineAvatarIconListItem
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton
from kivy.uix.label import Label

from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivymd.app import MDApp
from kivymd.uix.menu import MDDropdownMenu


from kivymd.uix.tab import MDTabsBase
from kivymd.uix.floatlayout import MDFloatLayout

from kivymd.uix.button import MDFloatingActionButton


KV = '''
<ContentNavigationDrawer>

    MDList:

        OneLineListItem:
            text: "Главная"
            on_press:
                root.nav_drawer.set_state("close")
                root.screen_manager.current = "scr 1"


        OneLineListItem:
            text: "Парки"
            on_press:
                root.nav_drawer.set_state("close")
                root.screen_manager.current = "scr 2"

        OneLineListItem:
            text: "Сады"
            on_press:
                root.nav_drawer.set_state("close")
                root.screen_manager.current = "scr 3"
                
        OneLineListItem:
            text: "Кинотеатры"
            on_press:
                root.nav_drawer.set_state("close")
                root.screen_manager.current = "scr 4"
                
        OneLineListItem:
            text: "Катки"
            on_press:
                root.nav_drawer.set_state("close")
                root.screen_manager.current = "scr 7"
                
        OneLineListItem:
            text: "Развлекательные центры"
            on_press:
                root.nav_drawer.set_state("close")
                root.screen_manager.current = "scr 8"

        OneLineListItem:
            text: "ТРЦ"
            on_press:
                root.nav_drawer.set_state("close")
                root.screen_manager.current = "scr 9"

        OneLineListItem:
            text: "Карта"
            on_press:
                root.nav_drawer.set_state("close")
                root.screen_manager.current = "FullScreenMap"
                


        OneLineListItem:
            text: "Выход"
            padding: 90, 56, 12, 16
            on_press:
                app.stop()
                
                


MDScreen:
    
        
    MDNavigationLayout:
        
        MDTopAppBar:
            id: toolbar
            pos_hint: {"top": 1}
            elevation: 7
            title: "ОренбургГид"
            left_action_items: [["menu", lambda x: nav_drawer.set_state("open")]]
            right_action_items: [["dots-vertical", lambda x: app.callback(x)]]
            md_bg_color: app.theme_cls.primary_color
    
        MDScreenManager:
            id: screen_manager
            pos: 0,-45
            MDScreen:
                name: "scr 1"

                BoxLayout:
                    orientation: 'vertical'
                    padding: "22dp"
                                
                MDLabel:
                    text: "Приветствуем Вас, в приложение ОренбургГид! Наше приложение создано,чтобы облегчить,и обеспечить прогулки и развлечения в городе!"
                    bold: True
                    color: 1, 1, 1, 1
                    halign: "center"
                    
                MDRaisedButton:
                    text: "Здесь может быть ваша реклама"
                    color: 5, 9, 0, 0
                    pos_hint: {'center_y': .11, 'center_x': .5}
                    on_press:
                        import webbrowser
                        webbrowser.open("https://vk.com/coderedit")                
                

            MDScreen:
                name: "scr 2"

                MDTabs:
                    id: tabs
                    
                    
                    Tab:
                        id: tab1
                        title: "Тополя"
                        
                        BoxLayout:
                            orientation: 'vertical'
                            padding: "22dp"
             

                            MDSmartTile:
                                
                                radius: 24
                                box_radius: [0, 0, 24, 24]
                                box_color: 0, 0, 0, .7
                                source: "orenburg-sad-topolya-1-1024x698.jpg"
                                
                                size_hint: None, None
                                size: "320dp", "320dp"
                                

                                MDIconButton:
                                    icon: "heart-outline"
                                    theme_icon_color: "Custom"
                                    icon_color: 1, 0, 0, 1
                                    pos_hint: {"center_y": .5}
                                    on_release: self.icon = "heart" if self.icon == "heart-outline" else "heart-outline"

                                MDLabel:
                                    text: "Парк «Тополя»"
                                    bold: True
                                    color: "white"
                                MDRectangleFlatButton:
                                    text: "На карте"
                                    theme_text_color: "Custom"
                                    text_color: "white"
                                    line_color: "red"
                                    on_press:
                                        import webbrowser
                                        webbrowser.open("https://yandex.ru/maps/org/topolya/221940216026/?ll=55.091853%2C51.769275&z=16.45")
                                    
                                    
                            MDScrollView:
                                do_scroll_x: False
                                do_scroll_y: True
                                
                                MDLabel:
                                    size_hint_y: None
                                    height: self.texture_size[1]    
                                    text: "Этот парк считается лучшим местом для семейного отдыха в городе. В теплое время года на территории парка работает множество аттракционов и тематических зон."
                                    color: 1, 1, 1, 1
                                    halign: "left"


                    Tab:
                        id: tab2
                        title: "Гуськова"
                        
                        BoxLayout:
                            orientation: 'vertical'
                            padding: "22dp"
                                

                            MDSmartTile:
                                
                                radius: 24
                                box_radius: [0, 0, 24, 24]
                                box_color: 0, 0, 0, .7
                                source: "orenburg-park-guskova-3-1024x715.jpg"
                                
                                size_hint: None, None
                                size: "320dp", "320dp"


                                MDIconButton:
                                    icon: "heart-outline"
                                    theme_icon_color: "Custom"
                                    icon_color: 1, 0, 0, 1
                                    pos_hint: {"center_y": .5}
                                    on_release: self.icon = "heart" if self.icon == "heart-outline" else "heart-outline"

                                MDLabel:
                                    text: "Парк им. Л.А. Гуськова"
                                    bold: True
                                    color: 1, 1, 1, 1
                                MDRectangleFlatButton:
                                    text: "На карте"
                                    theme_text_color: "Custom"
                                    text_color: "white"
                                    line_color: "red"
                                    on_press:
                                        import webbrowser
                                        webbrowser.open("https://yandex.ru/maps/org/park_imeni_l_a_guskova/191430380802/?ll=55.142669%2C51.805034&z=16.09")
                            MDScrollView:
                                do_scroll_x: False
                                do_scroll_y: True
                                
                                MDLabel:
                                    size_hint_y: None
                                    height: self.texture_size[1]            
                                    text: "В центре парка расположен Памятник доблестным советским воинам. На аллеях, прилегающих к главной площади, установлены памятники «Детям войны», «Звезда», «Серп и молот»."
                                    bold: True
                                    color: 1, 1, 1, 1
                                    halign: "left"

                    Tab:
                        id: tab3
                        title: "им. 50-летия СССР"
                        
                        BoxLayout:
                            orientation: 'vertical'
                            padding: "22dp"
                                

                            MDSmartTile:
                                
                                radius: 24
                                box_radius: [0, 0, 24, 24]
                                box_color: 0, 0, 0, .7
                                source: "orenburg-park-50-letiya-sssr-3-1024x683.jpg"
                                
                                size_hint: None, None
                                size: "320dp", "320dp"
                                 

                                MDIconButton:
                                    icon: "heart-outline"
                                    theme_icon_color: "Custom"
                                    icon_color: 1, 0, 0, 1
                                    pos_hint: {"center_y": .5}
                                    on_release: self.icon = "heart" if self.icon == "heart-outline" else "heart-outline"

                                MDLabel:
                                    text: "Парк им. 50-летия СССР"
                                    bold: True
                                    color: 1, 1, 1, 1
                                MDRectangleFlatButton:
                                    text: "На карте"
                                    theme_text_color: "Custom"
                                    text_color: "white"
                                    line_color: "red"
                                    on_press:
                                        import webbrowser
                                        webbrowser.open("https://yandex.ru/maps/org/park_kultury_i_otdykha_50_let_sssr/166782001728/?ll=55.135246%2C51.832152&z=16.27")
                                        
                            MDScrollView:
                                do_scroll_x: False
                                do_scroll_y: True
                                
                                MDLabel:
                                    size_hint_y: None
                                    height: self.texture_size[1]
                                    text: "В теплое время года в парке работают аттракционы, батуты и тир. На территории есть несколько кафе, в которых можно выпить кофе и подкрепится. Замечательное место для отдыха всей семьей."
                                    bold: True
                                    color: 1, 1, 1, 1
                                    halign: "left"
                    Tab:
                        id: tab4
                        title: "им. Перовского"
                        
                        BoxLayout:
                            orientation: 'vertical'
                            padding: "22dp"
                                

                            MDSmartTile:
                                
                                radius: 24
                                box_radius: [0, 0, 24, 24]
                                box_color: 0, 0, 0, .7
                                source: "orenburg-park-perovskogo-4-1024x768.jpg"
                                
                                size_hint: None, None
                                size: "320dp", "320dp"
                                          

                                MDIconButton:
                                    icon: "heart-outline"
                                    theme_icon_color: "Custom"
                                    icon_color: 1, 0, 0, 1
                                    pos_hint: {"center_y": .5}
                                    on_release: self.icon = "heart" if self.icon == "heart-outline" else "heart-outline"

                                MDLabel:
                                    text: "Парк им. Перовского"
                                    bold: True
                                    color: 1, 1, 1, 1
                                MDRectangleFlatButton:
                                    text: "На карте"
                                    theme_text_color: "Custom"
                                    text_color: "white"
                                    line_color: "red"
                                    on_press:
                                        import webbrowser
                                        webbrowser.open("https://yandex.ru/maps/org/park_imeni_v_a_perovskogo/164308038518/?ll=55.093642%2C51.771327&z=16.74")
                                        
                            MDScrollView:
                                do_scroll_x: False
                                do_scroll_y: True
                                
                                MDLabel:
                                    size_hint_y: None
                                    height: self.texture_size[1]
                                    text: "Парк имеет обширную инфраструктуру. В парке обустроена специальная площадка с тренажерами, футбольное мини-поле, зоны для игры в баскетбол и настольный теннис, а также трамплин для катания на велосипеде и скейтборде."
                                    bold: True
                                    color: 1, 1, 1, 1
                                    halign: "left"

                                
                                
                    Tab:
                        id: tab5
                        title: "Набережная Оренбурга"
                        
                        BoxLayout:
                            orientation: 'vertical'
                            padding: "22dp"
                                

                            MDSmartTile:
                                
                                radius: 24
                                box_radius: [0, 0, 24, 24]
                                box_color: 0, 0, 0, .7
                                source: "orenburg-pushkinskij-bulvar-na-naberezhnoj-3-1024x620.jpg"
                                
                                size_hint: None, None
                                size: "320dp", "320dp"
                                                                                

                                MDIconButton:
                                    icon: "heart-outline"
                                    theme_icon_color: "Custom"
                                    icon_color: 1, 0, 0, 1
                                    pos_hint: {"center_y": .5}
                                    on_release: self.icon = "heart" if self.icon == "heart-outline" else "heart-outline"

                                MDLabel:
                                    text: "Набережная Оренбурга"
                                    bold: True
                                    color: 1, 1, 1, 1
                                MDRectangleFlatButton:
                                    text: "На карте"
                                    theme_text_color: "Custom"
                                    text_color: "white"
                                    line_color: "red"
                                    on_press:
                                        import webbrowser
                                        webbrowser.open("https://yandex.ru/maps/org/orenburgskaya_naberezhnaya/7292358936/?ll=55.192684%2C51.777188&z=11.38")
                                        
                            MDScrollView:
                                do_scroll_x: False
                                do_scroll_y: True
                                
                                MDLabel:
                                    size_hint_y: None
                                    height: self.texture_size[1]
                                    text: "Инфраструктура парка очень насыщенная. В центре бульвара расположена лестница, ведущая к пешеходному посту через Урал. Вдоль неё есть лавочки и беседки для отдыха. Установлено освещение."
                                    bold: True
                                    color: 1, 1, 1, 1
                                    halign: "left"

                                
                    Tab:
                        id: tab6
                        title: "Зауральная роща"
                        
                        BoxLayout:
                            orientation: 'vertical'
                            padding: "22dp"
                                

                            MDSmartTile:
                                
                                radius: 24
                                box_radius: [0, 0, 24, 24]
                                box_color: 0, 0, 0, .7
                                source: "orenburg-zauralnaya-roshcha-2-1024x768.jpg"
                                
                                size_hint: None, None
                                size: "320dp", "320dp"
                                
                                
                                

                                MDIconButton:
                                    icon: "heart-outline"
                                    theme_icon_color: "Custom"
                                    icon_color: 1, 0, 0, 1
                                    pos_hint: {"center_y": .5}
                                    on_release: self.icon = "heart" if self.icon == "heart-outline" else "heart-outline"

                                MDLabel:
                                    text: "Зауральная роща"
                                    bold: True
                                    color: 1, 1, 1, 1
                                MDRectangleFlatButton:
                                    text: "На карте"
                                    theme_text_color: "Custom"
                                    text_color: "white"
                                    line_color: "red"
                                    on_press:
                                        import webbrowser
                                        webbrowser.open("https://yandex.ru/maps/org/zauralnaya_roshcha/25668124635/?ll=55.115173%2C51.747305&z=14.94")
                                        
                            MDScrollView:
                                do_scroll_x: False
                                do_scroll_y: True
                                
                                MDLabel:
                                    size_hint_y: None
                                    height: self.texture_size[1]
                                    text: "После реконструкции Зауральная роща обзавелась детским автодромом и новой спортивной площадкой. В летнее время в парке работает тир и детские аттракционы. Этот парк относят к числу самых посещаемых мест в городе."
                                    bold: True
                                    color: 1, 1, 1, 1
                                    halign: "left"
                        
                    Tab:
                        id: tab7
                        title: "50-летия ВЛКСМ"
                        
                        BoxLayout:
                            orientation: 'vertical'
                            padding: "22dp"
                                

                            MDSmartTile:
                                
                                radius: 24
                                box_radius: [0, 0, 24, 24]
                                box_color: 0, 0, 0, .7
                                source: "park-50-let-vlksm-2.jpg"
                                
                                size_hint: None, None
                                size: "320dp", "320dp"
                                
                                
                                

                                MDIconButton:
                                    icon: "heart-outline"
                                    theme_icon_color: "Custom"
                                    icon_color: 1, 0, 0, 1
                                    pos_hint: {"center_y": .5}
                                    on_release: self.icon = "heart" if self.icon == "heart-outline" else "heart-outline"

                                MDLabel:
                                    text: "Парк 50-летия ВЛКСМ"
                                    bold: True
                                    color: 1, 1, 1, 1
                                MDRectangleFlatButton:
                                    text: "На карте"
                                    theme_text_color: "Custom"
                                    text_color: "white"
                                    line_color: "red"
                                    on_press:
                                        import webbrowser
                                        webbrowser.open("https://yandex.ru/maps/org/park_kultury_i_otdykha_50_let_sssr/166782001728/?ll=55.135246%2C51.832152&z=16.27")
                                        
                            MDScrollView:
                                do_scroll_x: False
                                do_scroll_y: True
                                
                                MDLabel:
                                    size_hint_y: None
                                    height: self.texture_size[1]
                                    text: "На территории самого парка никаких строений нет. Рядом располагается Центр настольного тенниса России."
                                    bold: True
                                    color: 1, 1, 1, 1
                                    halign: "left"
                                
                                    


            MDScreen:
                name: "scr 3"

                MDTabs:
                    id: tabs
                                      
                    Tab:
                        id: tab8
                        title: "Октябрьской Революции"
                        
                        BoxLayout:
                            orientation: 'vertical'
                            padding: "22dp"
                                

                            MDSmartTile:
                                
                                radius: 24
                                box_radius: [0, 0, 24, 24]
                                box_color: 0, 0, 0, .7
                                source: "orenburg-sad-oktyabrskoj-revolyucii-1-1024x657.jpg"
                                
                                size_hint: None, None
                                size: "320dp", "320dp"
                                
                                
                                

                                MDIconButton:
                                    icon: "heart-outline"
                                    theme_icon_color: "Custom"
                                    icon_color: 1, 0, 0, 1
                                    pos_hint: {"center_y": .5}
                                    on_release: self.icon = "heart" if self.icon == "heart-outline" else "heart-outline"

                                MDLabel:
                                    text: "Сад Октябрьской Революции"
                                    bold: True
                                    color: 1, 1, 1, 1
                                MDRectangleFlatButton:
                                    text: "На карте"
                                    theme_text_color: "Custom"
                                    text_color: "white"
                                    line_color: "red"
                                    on_press:
                                        import webbrowser
                                        webbrowser.open("https://yandex.ru/maps/org/sad_imeni_oktyabrskoy_revolyutsii/23333542339/?ll=55.099190%2C51.790026&z=17.94")
                                        
                            MDScrollView:
                                do_scroll_x: False
                                do_scroll_y: True
                                
                                MDLabel:
                                    size_hint_y: None
                                    height: self.texture_size[1]
                                    text: "Треть всей площади сада была отдана под строительство спортивного комплекса. Также на исторической территории парка расположен кинотеатр, детский сад и недостроенный дом культуры."
                                    bold: True
                                    color: 1, 1, 1, 1
                                    halign: "left"

                    Tab:
                        id: tab9
                        title: "Фрунзе"
                        
                        BoxLayout:
                            orientation: 'vertical'
                            padding: "22dp"
                                

                            MDSmartTile:
                                
                                radius: 24
                                box_radius: [0, 0, 24, 24]
                                box_color: 0, 0, 0, .7
                                source: "orenburg-sad-frunze-3-1024x687.jpg"
                                
                                size_hint: None, None
                                size: "320dp", "320dp"
                                
                                
                                

                                MDIconButton:
                                    icon: "heart-outline"
                                    theme_icon_color: "Custom"
                                    icon_color: 1, 0, 0, 1
                                    pos_hint: {"center_y": .5}
                                    on_release: self.icon = "heart" if self.icon == "heart-outline" else "heart-outline"

                                MDLabel:
                                    text: "Сад Фрунзе"
                                    bold: True
                                    color: 1, 1, 1, 1
                                MDRectangleFlatButton:
                                    text: "На карте"
                                    theme_text_color: "Custom"
                                    text_color: "white"
                                    line_color: "red"
                                    on_press:
                                        import webbrowser
                                        webbrowser.open("https://yandex.ru/maps/48/orenburg/geo/sad_imeni_frunze/120718880/?ll=55.091054%2C51.760390&z=17.54")
                                        
                            MDScrollView:
                                do_scroll_x: False
                                do_scroll_y: True
                                
                                MDLabel:
                                    size_hint_y: None
                                    height: self.texture_size[1]
                                    text: "На территории парка открыт музей под открытым небом, посвященный советским солдатам. Установлена часовня."
                                    bold: True
                                    color: 1, 1, 1, 1
                                    halign: "left"

                    Tab:
                        id: tab10
                        title: "Цвиллинга"
                        
                        BoxLayout:
                            orientation: 'vertical'
                            padding: "22dp"
                                

                            MDSmartTile:
                                
                                radius: 24
                                box_radius: [0, 0, 24, 24]
                                box_color: 0, 0, 0, .7
                                source: "orenburg-sad-cvillinga-5-1024x768.jpg"
                                
                                size_hint: None, None
                                size: "320dp", "320dp"
                                
                                
                                

                                MDIconButton:
                                    icon: "heart-outline"
                                    theme_icon_color: "Custom"
                                    icon_color: 1, 0, 0, 1
                                    pos_hint: {"center_y": .5}
                                    on_release: self.icon = "heart" if self.icon == "heart-outline" else "heart-outline"

                                MDLabel:
                                    text: "Сад Цвиллинга"
                                    bold: True
                                    color: 1, 1, 1, 1
                                MDRectangleFlatButton:
                                    text: "На карте"
                                    theme_text_color: "Custom"
                                    text_color: "white"
                                    line_color: "red"
                                    on_press:
                                        import webbrowser
                                        webbrowser.open("https://yandex.ru/maps/org/park_im_tsvillinga/19923912117/?ll=55.068343%2C51.785229&z=17.54")
                                        
                            MDScrollView:
                                do_scroll_x: False
                                do_scroll_y: True
                                
                                MDLabel:
                                    size_hint_y: None
                                    height: self.texture_size[1]
                                    text: "Сад оснащен всей необходимой инфраструктурой. Есть лавочки для отдыха, зоны для игры в футбол и настольный теннис. В зимнее время в парке заливают каток."
                                    bold: True
                                    color: 1, 1, 1, 1
                                    halign: "left"                
                    

                    


            MDScreen:
                name: "scr 4"

                MDTabs:
                    id: tabs
                                      
                    Tab:
                        id: tab11
                        title: "Кинодом"
                        
                        BoxLayout:
                            orientation: 'vertical'
                            padding: "22dp"
                                

                            MDSmartTile:
                                
                                radius: 24
                                box_radius: [0, 0, 24, 24]
                                box_color: 0, 0, 0, .7
                                source: "kinodom.jpg"
                                
                                size_hint: None, None
                                size: "320dp", "320dp"
                                
                                
                                

                                MDIconButton:
                                    icon: "heart-outline"
                                    theme_icon_color: "Custom"
                                    icon_color: 1, 0, 0, 1
                                    pos_hint: {"center_y": .5}
                                    on_release: self.icon = "heart" if self.icon == "heart-outline" else "heart-outline"

                                MDLabel:
                                    text: "Кинодом"
                                    bold: True
                                    color: 1, 1, 1, 1
                                MDRectangleFlatButton:
                                    text: "На карте"
                                    theme_text_color: "Custom"
                                    text_color: "white"
                                    line_color: "red"
                                    on_press:
                                        import webbrowser
                                        webbrowser.open("https://yandex.ru/maps/org/kinodom/222967841250/?indoorLevel=1&ll=55.181478%2C51.812682&z=16.53")
                                        
                            MDScrollView:
                                do_scroll_x: False
                                do_scroll_y: True
                                
                                MDLabel:
                                    size_hint_y: None
                                    height: self.texture_size[1]
                                    text: "Уникальная особенность кинотеатра - специально разработанные премиальные мягкие кресла и 2-х местные диваны вместо стандартных кинотеатральных кресел."
                                    bold: True
                                    color: 1, 1, 1, 1
                                    halign: "left"

                    Tab:
                        id: tab12
                        title: "Космос"
                        
                        BoxLayout:
                            orientation: 'vertical'
                            padding: "22dp"
                                

                            MDSmartTile:
                                
                                radius: 24
                                box_radius: [0, 0, 24, 24]
                                box_color: 0, 0, 0, .7
                                source: "XXL.jpg"
                                
                                size_hint: None, None
                                size: "320dp", "320dp"
                                
                                
                                

                                MDIconButton:
                                    icon: "heart-outline"
                                    theme_icon_color: "Custom"
                                    icon_color: 1, 0, 0, 1
                                    pos_hint: {"center_y": .5}
                                    on_release: self.icon = "heart" if self.icon == "heart-outline" else "heart-outline"

                                MDLabel:
                                    text: "Космос"
                                    bold: True
                                    color: 1, 1, 1, 1
                                MDRectangleFlatButton:
                                    text: "На карте"
                                    theme_text_color: "Custom"
                                    text_color: "white"
                                    line_color: "red"
                                    on_press:
                                        import webbrowser
                                        webbrowser.open("https://yandex.ru/maps/org/kosmos/243619535364/?ll=55.092338%2C51.770478&z=16.53")
                                        
                            MDScrollView:
                                do_scroll_x: False
                                do_scroll_y: True
                                
                                MDLabel:
                                    size_hint_y: None
                                    height: self.texture_size[1]
                                    text: "Основная особенность заключается в том, что достроенный кинотеатр находится под землей. В старом здании также прошла реконструкция, в нем установили современное оборудование, создали новую архитектуру и интерьер."
                                    bold: True
                                    color: 1, 1, 1, 1
                                    halign: "left"

                    Tab:
                        id: tab13
                        title: "Мармелад Синема"
                        
                        BoxLayout:
                            orientation: 'vertical'
                            padding: "22dp"
                                

                            MDSmartTile:
                                
                                radius: 24
                                box_radius: [0, 0, 24, 24]
                                box_color: 0, 0, 0, .7
                                source: "marmelad.JPG"
                                
                                size_hint: None, None
                                size: "320dp", "320dp"
                                
                                
                                

                                MDIconButton:
                                    icon: "heart-outline"
                                    theme_icon_color: "Custom"
                                    icon_color: 1, 0, 0, 1
                                    pos_hint: {"center_y": .5}
                                    on_release: self.icon = "heart" if self.icon == "heart-outline" else "heart-outline"

                                MDLabel:
                                    text: "Мармелад Синема"
                                    bold: True
                                    color: 1, 1, 1, 1
                                MDRectangleFlatButton:
                                    text: "На карте"
                                    theme_text_color: "Custom"
                                    text_color: "white"
                                    line_color: "red"
                                    on_press:
                                        import webbrowser
                                        webbrowser.open("https://yandex.ru/maps/org/marmelad_sinema/189499497619/?indoorLevel=1&ll=55.117706%2C51.843896&z=16.53")
                                        
                            MDScrollView:
                                do_scroll_x: False
                                do_scroll_y: True
                                
                                MDLabel:
                                    size_hint_y: None
                                    height: self.texture_size[1]
                                    text: "Для вашего удобства предусмотрены 9 комфортных залов с удобными креслами и отличным звуком."
                                    bold: True
                                    color: 1, 1, 1, 1
                                    halign: "left"

                    Tab:
                        id: tab14
                        title: "Мистер Фёст"
                        
                        BoxLayout:
                            orientation: 'vertical'
                            padding: "22dp"
                                

                            MDSmartTile:
                                
                                radius: 24
                                box_radius: [0, 0, 24, 24]
                                box_color: 0, 0, 0, .7
                                source: "first.JPG"
                                
                                size_hint: None, None
                                size: "320dp", "320dp"
                                
                                
                                

                                MDIconButton:
                                    icon: "heart-outline"
                                    theme_icon_color: "Custom"
                                    icon_color: 1, 0, 0, 1
                                    pos_hint: {"center_y": .5}
                                    on_release: self.icon = "heart" if self.icon == "heart-outline" else "heart-outline"

                                MDLabel:
                                    text: "Мистер Фест"
                                    bold: True
                                    color: 1, 1, 1, 1
                                MDRectangleFlatButton:
                                    text: "На карте"
                                    theme_text_color: "Custom"
                                    text_color: "white"
                                    line_color: "red"
                                    on_press:
                                        import webbrowser
                                        webbrowser.open("https://yandex.ru/maps/org/mister_fyost/71450799782/?indoorLevel=1&ll=55.198411%2C51.775851&z=16.93")
                                        
                            MDScrollView:
                                do_scroll_x: False
                                do_scroll_y: True
                                
                                MDLabel:
                                    size_hint_y: None
                                    height: self.texture_size[1]
                                    text: "Киноцентр Мистер Фёст это: 5 залов на 600 мест, concession-бар с сотней видов попкорна, начос, соусов и напитков, продвинутая репертуарная политика - максимум премьер, а также три вида кресел, в том числе места для поцелуев ;)."
                                    bold: True
                                    color: 1, 1, 1, 1
                                    halign: "left"

                    Tab:
                        id: tab15
                        title: "Синема 5 Гуливер"
                        
                        BoxLayout:
                            orientation: 'vertical'
                            padding: "22dp"
                                

                            MDSmartTile:
                                
                                radius: 24
                                box_radius: [0, 0, 24, 24]
                                box_color: 0, 0, 0, .7
                                source: "guliver.JPG"
                                
                                size_hint: None, None
                                size: "320dp", "320dp"
                                
                                
                                

                                MDIconButton:
                                    icon: "heart-outline"
                                    theme_icon_color: "Custom"
                                    icon_color: 1, 0, 0, 1
                                    pos_hint: {"center_y": .5}
                                    on_release: self.icon = "heart" if self.icon == "heart-outline" else "heart-outline"

                                MDLabel:
                                    text: "Синема 5 Гуливер"
                                    bold: True
                                    color: 1, 1, 1, 1
                                MDRectangleFlatButton:
                                    text: "На карте"
                                    theme_text_color: "Custom"
                                    text_color: "white"
                                    line_color: "red"
                                    on_press:
                                        import webbrowser
                                        webbrowser.open("https://yandex.ru/maps/org/sinema_5/1159699073/?display-text=%D1%81%D0%B8%D0%BD%D0%B5%D0%BC%D0%B0%205%20%D0%B3%D1%83%D0%BB%D0%BB%D0%B8%D0%B2%D0%B5%D1%80&indoorLevel=1&ll=55.091026%2C51.811394&mode=search&sctx=ZAAAAAgBEAAaKAoSCVUVGohlmUtAEdLI5xVP40lAEhIJg4jUtItplj8R%2BKdUibK3hD8iBgABAgMEBSgKOABA258NSAFiIWFkZF9zbmlwcGV0PXRvcG9ueW1fZGlzY292ZXJ5LzEueGI2cmVhcnI9c2NoZW1lX0xvY2FsL0dlby9Db2xsZWN0aW9ucy9SYW5kb21Qb3NpdGlvbj10cnVlYkJyZWFycj1zY2hlbWVfTG9jYWwvR2VvL0xpc3REaXNjb3ZlcnkvRW5hYmxlRGlzY292ZXJ5VGV4dFJlcXVlc3RzPTFiOnJlYXJyPXNjaGVtZV9Mb2NhbC9HZW8vTGlzdERpc2NvdmVyeS9FbmFibGVFbXB0eVJlcXVlc3RzPTFiOnJlYXJyPXNjaGVtZV9Mb2NhbC9HZW8vTGlzdERpc2NvdmVyeS9FbmFibGVDb21tb25QaWNNZW51PTFiNXJlYXJyPXNjaGVtZV9Mb2NhbC9HZW8vTGlzdERpc2NvdmVyeS9FbmFibGVSZXF1ZXN0cz0xYjByZWFycj1zY2hlbWVfTG9jYWwvR2VvL0Fza0Rpc2NvdmVyeUZvclRvcG9ueW1zPTFiMnJlYXJyPXNjaGVtZV9Mb2NhbC9HZW8vQ29sbGVjdGlvbnMvRW5hYmxlZE1peD10cnVlYjVyZWFycj1zY2hlbWVfTG9jYWwvR2VvL0xpc3REaXNjb3ZlcnkvRW5hYmxlVmVydGljYWw9MWoCcnWdAc3MTD2gAQCoAQC9AWnxD3HCAQWBtf6oBOoBAPIBAPgBAIICH9GB0LjQvdC10LzQsCA1INCz0YPQu9C70LjQstC10YCKAgCSAgCaAgxkZXNrdG9wLW1hcHM%3D&sll=55.091026%2C51.811394&sspn=0.016743%2C0.005493&text=%D1%81%D0%B8%D0%BD%D0%B5%D0%BC%D0%B0%205%20%D0%B3%D1%83%D0%BB%D0%BB%D0%B8%D0%B2%D0%B5%D1%80&z=16.88")
                                        
                            MDScrollView:
                                do_scroll_x: False
                                do_scroll_y: True
                                
                                MDLabel:
                                    size_hint_y: None
                                    height: self.texture_size[1]
                                    text: "Залы оснащены эргономичными креслами в обычных залах и мягкими двухместными диванами со столиками  в зале «Комфорт». Дополнением к уютной атмосфере «Синема 5» служит кафе-бар, где можно приобрести различные закуски и напитки."
                                    bold: True
                                    color: 1, 1, 1, 1
                                    halign: "left"
                    Tab:
                        id: tab16
                        title: "Синема 5 Север"
                        
                        BoxLayout:
                            orientation: 'vertical'
                            padding: "22dp"
                                

                            MDSmartTile:
                                
                                radius: 24
                                box_radius: [0, 0, 24, 24]
                                box_color: 0, 0, 0, .7
                                source: "sever.JPG"
                                
                                size_hint: None, None
                                size: "320dp", "320dp"
                                
                                
                                

                                MDIconButton:
                                    icon: "heart-outline"
                                    theme_icon_color: "Custom"
                                    icon_color: 1, 0, 0, 1
                                    pos_hint: {"center_y": .5}
                                    on_release: self.icon = "heart" if self.icon == "heart-outline" else "heart-outline"

                                MDLabel:
                                    text: "Синема 5 Север"
                                    bold: True
                                    color: 1, 1, 1, 1
                                MDRectangleFlatButton:
                                    text: "На карте"
                                    theme_text_color: "Custom"
                                    text_color: "white"
                                    line_color: "red"
                                    on_press:
                                        import webbrowser
                                        webbrowser.open("https://yandex.ru/maps/org/sinema_5/1228265818/?indoorLevel=1&ll=55.127711%2C51.833072&mode=search&sctx=ZAAAAAgBEAAaKAoSCRNGs7J9kEtAEd1ELc2t6klAEhIJxqUqbXGNnz8RD167tOGwhD8iBgABAgMEBSgKOABA2p8NSAFiIWFkZF9zbmlwcGV0PXRvcG9ueW1fZGlzY292ZXJ5LzEueGI2cmVhcnI9c2NoZW1lX0xvY2FsL0dlby9Db2xsZWN0aW9ucy9SYW5kb21Qb3NpdGlvbj10cnVlYkJyZWFycj1zY2hlbWVfTG9jYWwvR2VvL0xpc3REaXNjb3ZlcnkvRW5hYmxlRGlzY292ZXJ5VGV4dFJlcXVlc3RzPTFiOnJlYXJyPXNjaGVtZV9Mb2NhbC9HZW8vTGlzdERpc2NvdmVyeS9FbmFibGVFbXB0eVJlcXVlc3RzPTFiOnJlYXJyPXNjaGVtZV9Mb2NhbC9HZW8vTGlzdERpc2NvdmVyeS9FbmFibGVDb21tb25QaWNNZW51PTFiNXJlYXJyPXNjaGVtZV9Mb2NhbC9HZW8vTGlzdERpc2NvdmVyeS9FbmFibGVSZXF1ZXN0cz0xYjByZWFycj1zY2hlbWVfTG9jYWwvR2VvL0Fza0Rpc2NvdmVyeUZvclRvcG9ueW1zPTFiMnJlYXJyPXNjaGVtZV9Mb2NhbC9HZW8vQ29sbGVjdGlvbnMvRW5hYmxlZE1peD10cnVlYjVyZWFycj1zY2hlbWVfTG9jYWwvR2VvL0xpc3REaXNjb3ZlcnkvRW5hYmxlVmVydGljYWw9MWoCcnWdAc3MTD2gAQCoAQC9AXUCbcvCAQXastfJBOoBAPIBAPgBAIICGdGB0LjQvdC10LzQsCA1INGB0LXQstC10YCKAgCSAgCaAgxkZXNrdG9wLW1hcHM%3D&sll=55.127711%2C51.833072&sspn=0.018322%2C0.006008&text=%D1%81%D0%B8%D0%BD%D0%B5%D0%BC%D0%B0%205%20%D1%81%D0%B5%D0%B2%D0%B5%D1%80&z=16.75")
                                        
                            MDScrollView:
                                do_scroll_x: False
                                do_scroll_y: True
                                
                                MDLabel:
                                    size_hint_y: None
                                    height: self.texture_size[1]
                                    text: "Во всех залах есть мягкие удобные сидения, лестничная подсветка и система кондиционирования зима-лето. Каждый посетитель имеет возможность просмотреть мировые премьеры фильмов и насладиться полным комфортом."
                                    bold: True
                                    color: 1, 1, 1, 1
                                    halign: "left"

                    Tab:
                        id: tab17
                        title: "Сокол"
                        
                        BoxLayout:
                            orientation: 'vertical'
                            padding: "22dp"
                                

                            MDSmartTile:
                                
                                radius: 24
                                box_radius: [0, 0, 24, 24]
                                box_color: 0, 0, 0, .7
                                source: "sokol.JPG"
                                
                                size_hint: None, None
                                size: "320dp", "320dp"
                                
                                
                                

                                MDIconButton:
                                    icon: "heart-outline"
                                    theme_icon_color: "Custom"
                                    icon_color: 1, 0, 0, 1
                                    pos_hint: {"center_y": .5}
                                    on_release: self.icon = "heart" if self.icon == "heart-outline" else "heart-outline"

                                MDLabel:
                                    text: "Сокол"
                                    bold: True
                                    color: 1, 1, 1, 1
                                MDRectangleFlatButton:
                                    text: "На карте"
                                    theme_text_color: "Custom"
                                    text_color: "white"
                                    line_color: "red"
                                    on_press:
                                        import webbrowser
                                        webbrowser.open("https://yandex.ru/maps/org/sokol/1104302040/?indoorLevel=1&ll=55.129931%2C51.794381&mode=search&sll=55.129931%2C51.795346&sspn=0.006086%2C0.001997&text=%D0%A1%D0%BE%D0%BA%D0%BE%D0%BB&z=16.77")
                                        
                            MDScrollView:
                                do_scroll_x: False
                                do_scroll_y: True
                                
                                MDLabel:
                                    size_hint_y: None
                                    height: self.texture_size[1]
                                    text: "Система звука Dolby и огромный широкоформатный экран, дает зрителю возможность полчувствовать себя участником происходящего на экране. Реалистичность показа, вот что привлекает современного зрителя. Большой зал вмещает в себя – 283 посадочных места."
                                    bold: True
                                    color: 1, 1, 1, 1
                                    halign: "left"
            MDScreen:
                name: "scr 5"
                    
                MDScreen:
                    name: "scr 6"

                MDLabel:
                    text: "Выход"
                    halign: "center"
                    
                    
            MDScreen:
                name: "scr 7"

                MDTabs:
                    id: tabs
                                      
                    Tab:
                        id: tab18
                        title: "Звёздный"
                        
                        BoxLayout:
                            orientation: 'vertical'
                            padding: "22dp"
                                

                            MDSmartTile:
                                
                                radius: 24
                                box_radius: [0, 0, 24, 24]
                                box_color: 0, 0, 0, .7
                                source: "zvezd.jpg"
                                
                                size_hint: None, None
                                size: "320dp", "320dp"
                                
                                
                                

                                MDIconButton:
                                    icon: "heart-outline"
                                    theme_icon_color: "Custom"
                                    icon_color: 1, 0, 0, 1
                                    pos_hint: {"center_y": .5}
                                    on_release: self.icon = "heart" if self.icon == "heart-outline" else "heart-outline"

                                MDLabel:
                                    text: "Звёздный"
                                    bold: True
                                    color: 1, 1, 1, 1
                                MDRectangleFlatButton:
                                    text: "На карте"
                                    theme_text_color: "Custom"
                                    text_color: "white"
                                    line_color: "red"
                                    on_press:
                                        import webbrowser
                                        webbrowser.open("https://yandex.ru/maps/org/ledovy_dvorets_zvezdny/64593801564/?indoorLevel=1&ll=55.099543%2C51.789201&z=16.93")
                                        
                            MDScrollView:
                                do_scroll_x: False
                                do_scroll_y: True
                                
                                MDLabel:
                                    size_hint_y: None
                                    height: self.texture_size[1]
                                    text: "Огромный комплекс спорта и развлечений, который открылся для своих посетителей в 2007 году. Большая ледовая арена оснащена самым современным видео и аудио оборудованием и льдом, который можно не растапливать до 50 лет. Ее трибуны могут вмещать до 3 тыс человек."
                                    bold: True
                                    color: 1, 1, 1, 1
                                    halign: "left"
                                
                    Tab:
                        id: tab18
                        title: "Центральный спортивный комплекс Оренбург"
                        
                        BoxLayout:
                            orientation: 'vertical'
                            padding: "22dp"
                                

                            MDSmartTile:
                                
                                radius: 24
                                box_radius: [0, 0, 24, 24]
                                box_color: 0, 0, 0, .7
                                source: "skoren.jpg"
                                
                                size_hint: None, None
                                size: "320dp", "320dp"
                                
                                
                                

                                MDIconButton:
                                    icon: "heart-outline"
                                    theme_icon_color: "Custom"
                                    icon_color: 1, 0, 0, 1
                                    pos_hint: {"center_y": .5}
                                    on_release: self.icon = "heart" if self.icon == "heart-outline" else "heart-outline"

                                MDLabel:
                                    text: "Центральный спортивный комплекс Оренбург"
                                    bold: True
                                    color: 1, 1, 1, 1
                                MDRectangleFlatButton:
                                    text: "На карте"
                                    theme_text_color: "Custom"
                                    text_color: "white"
                                    line_color: "red"
                                    on_press:
                                        import webbrowser
                                        webbrowser.open("https://yandex.ru/maps/org/tsentralny_sportivny_kompleks_orenburg/223389098381/?indoorLevel=1&ll=55.100849%2C51.810568&z=15.79")
                                        
                            MDScrollView:
                                do_scroll_x: False
                                do_scroll_y: True
                                
                                MDLabel:
                                    size_hint_y: None
                                    height: self.texture_size[1]
                                    text: "Проводятся различные мероприятия. Очень большой каток, есть теплые раздевалки."
                                    bold: True
                                    color: 1, 1, 1, 1
                                    halign: "left"
                    
                    Tab:
                        id: tab19
                        title: "Ледовый дворец на Цветном бульваре"
                        
                        BoxLayout:
                            orientation: 'vertical'
                            padding: "22dp"
                                

                            MDSmartTile:
                                
                                radius: 24
                                box_radius: [0, 0, 24, 24]
                                box_color: 0, 0, 0, .7
                                source: "cvetbul.jpg"
                                
                                size_hint: None, None
                                size: "320dp", "320dp"
                                
                                
                                

                                MDIconButton:
                                    icon: "heart-outline"
                                    theme_icon_color: "Custom"
                                    icon_color: 1, 0, 0, 1
                                    pos_hint: {"center_y": .5}
                                    on_release: self.icon = "heart" if self.icon == "heart-outline" else "heart-outline"

                                MDLabel:
                                    text: "Ледовый дворец на Цветном бульваре"
                                    bold: True
                                    color: 1, 1, 1, 1
                                MDRectangleFlatButton:
                                    text: "На карте"
                                    theme_text_color: "Custom"
                                    text_color: "white"
                                    line_color: "red"
                                    on_press:
                                        import webbrowser
                                        webbrowser.open("https://yandex.ru/maps/48/orenburg/?ll=55.216316%2C51.794633&mode=poi&poi%5Bpoint%5D=55.221561%2C51.783815&poi%5Buri%5D=ymapsbm1%3A%2F%2Forg%3Foid%3D1705256549&z=13.6")
                                        
                            MDScrollView:
                                do_scroll_x: False
                                do_scroll_y: True
                                
                                MDLabel:
                                    size_hint_y: None
                                    height: self.texture_size[1]
                                    text: "На протяжении всего года крытый каток с натуральным льдом в ледовом дворце «На цветном бульваре» ждет посетителей на массовые катания на коньках. Для удобства посетителей функционирует пункт проката и заточки коньков, гардероб, световое и музыкальное сопровождение. На катке проводятся различные турниры и тренировки, в свободное время площадка открыта для массовых катаний. В будни время катания с 12.00-14.00."
                                    bold: True
                                    color: 1, 1, 1, 1
                                    halign: "left"
                                
                    Tab:
                        id: tab20
                        title: "Ледовый дворец Олимпиец"
                        
                        BoxLayout:
                            orientation: 'vertical'
                            padding: "22dp"
                                

                            MDSmartTile:
                                
                                radius: 24
                                box_radius: [0, 0, 24, 24]
                                box_color: 0, 0, 0, .7
                                source: "olimp.jpg"
                                
                                size_hint: None, None
                                size: "320dp", "320dp"
                                
                                
                                

                                MDIconButton:
                                    icon: "heart-outline"
                                    theme_icon_color: "Custom"
                                    icon_color: 1, 0, 0, 1
                                    pos_hint: {"center_y": .5}
                                    on_release: self.icon = "heart" if self.icon == "heart-outline" else "heart-outline"

                                MDLabel:
                                    text: "Ледовый дворец Олимпиец"
                                    bold: True
                                    color: 1, 1, 1, 1
                                MDRectangleFlatButton:
                                    text: "На карте"
                                    theme_text_color: "Custom"
                                    text_color: "white"
                                    line_color: "red"
                                    on_press:
                                        import webbrowser
                                        webbrowser.open("https://yandex.ru/maps/48/orenburg/?ll=55.262679%2C51.773292&mode=poi&poi%5Bpoint%5D=55.270243%2C51.765156&poi%5Buri%5D=ymapsbm1%3A%2F%2Forg%3Foid%3D1010963162&z=14.2")
                                        
                            MDScrollView:
                                do_scroll_x: False
                                do_scroll_y: True
                                
                                MDLabel:
                                    size_hint_y: None
                                    height: self.texture_size[1]
                                    text: "Катание на катке — одно из лучших развлечений в зимний период. Это отличный способ повеселиться с семьей или друзьями, а также укрепить здоровье. Каток «Олимпиец» крытого типа работает как в зимний, так и в летний сезон. В пункте прокате можно взять коньки для катания, есть заточка, гардероб, парковка. Сеансы катания длятся по 45 минут."
                                    bold: True
                                    color: 1, 1, 1, 1
                                    halign: "left"            
                    
                    Tab:
                        id: tab21
                        title: "Ледовый дворец Кристалл"
                        
                        BoxLayout:
                            orientation: 'vertical'
                            padding: "22dp"
                                

                            MDSmartTile:
                                
                                radius: 24
                                box_radius: [0, 0, 24, 24]
                                box_color: 0, 0, 0, .7
                                source: "krist1.jpg"
                                
                                size_hint: None, None
                                size: "320dp", "320dp"

                                MDIconButton:
                                    icon: "heart-outline"
                                    theme_icon_color: "Custom"
                                    icon_color: 1, 0, 0, 1
                                    pos_hint: {"center_y": .5}
                                    on_release: self.icon = "heart" if self.icon == "heart-outline" else "heart-outline"

                                MDLabel:
                                    text: "Ледовый дворец Кристалл"
                                    bold: True
                                    color: 1, 1, 1, 1
                                MDRectangleFlatButton:
                                    text: "На карте"
                                    theme_text_color: "Custom"
                                    text_color: "white"
                                    line_color: "red"
                                    on_press:
                                        import webbrowser
                                        webbrowser.open("https://yandex.ru/maps/48/orenburg/?ll=55.120086%2C51.830215&mode=poi&poi%5Bpoint%5D=55.119057%2C51.829919&poi%5Buri%5D=ymapsbm1%3A%2F%2Forg%3Foid%3D1781300492&z=17.46")
                                        
                            MDScrollView:
                                do_scroll_x: False
                                do_scroll_y: True
                                
                                MDLabel:
                                    size_hint_y: None
                                    height: self.texture_size[1]
                                    text: "Для удобства посетителей функционирует пункт проката и заточки коньков, теплая раздевалка. Каток «Кристалл» расположен под надувным куполом, на катке поддерживается комфортная для катания температура. Массовые катания проходят по расписанию."
                                    bold: True
                                    color: 1, 1, 1, 1
                                    halign: "left"            
            MDScreen:
                name: "scr 9"

                MDTabs:
                    id: tabs

                    Tab:
                        id: tab29
                        title: "Новый мир"
                        
                        BoxLayout:
                            orientation: 'vertical'
                            padding: "22dp"

                                

                            MDSmartTile:
                                
                                radius: 24
                                box_radius: [0, 0, 24, 24]
                                box_color: 0, 0, 0, .7
                                source: "nov.jpg"
                                
                                size_hint: None, None
                                size: "320dp", "320dp"
                                
                                
                                

                                MDIconButton:
                                    icon: "heart-outline"
                                    theme_icon_color: "Custom"
                                    icon_color: 1, 0, 0, 1
                                    pos_hint: {"center_y": .5}
                                    on_release: self.icon = "heart" if self.icon == "heart-outline" else "heart-outline"

                                MDLabel:
                                    text: "Новый мир"
                                    bold: True
                                    color: "white"
                                MDRectangleFlatButton:
                                    text: "На карте"
                                    theme_text_color: "Custom"
                                    text_color: "white"
                                    line_color: "red"
                                    on_press:
                                        import webbrowser
                                        webbrowser.open("https://yandex.ru/maps/org/novy_mir/1143301634/?indoorLevel=1&ll=55.162907%2C51.827030&z=16.56")
                                        
                            MDScrollView:
                                do_scroll_x: False
                                do_scroll_y: True
                                
                                MDLabel:
                                    size_hint_y: None
                                    height: self.texture_size[1]
                                    text: "Oдин из крупнейших торгово-развлекательных центров Оренбурга. Это четыре этажа товаров и развлечений для Вас и Вашей семьи."
                                    bold: True
                                    color: 1, 1, 1, 1
                                    halign: "left"

                    Tab:
                        id: tab28
                        title: "Кит"
                        
                        BoxLayout:
                            orientation: 'vertical'
                            padding: "22dp"

                                

                            MDSmartTile:
                                
                                radius: 24
                                box_radius: [0, 0, 24, 24]
                                box_color: 0, 0, 0, .7
                                source: "kit.jpg"
                                
                                size_hint: None, None
                                size: "320dp", "320dp"
                                
                                
                                

                                MDIconButton:
                                    icon: "heart-outline"
                                    theme_icon_color: "Custom"
                                    icon_color: 1, 0, 0, 1
                                    pos_hint: {"center_y": .5}
                                    on_release: self.icon = "heart" if self.icon == "heart-outline" else "heart-outline"

                                MDLabel:
                                    text: "Кит"
                                    bold: True
                                    color: "white"
                                MDRectangleFlatButton:
                                    text: "На карте"
                                    theme_text_color: "Custom"
                                    text_color: "white"
                                    line_color: "red"
                                    on_press:
                                        import webbrowser
                                        webbrowser.open("https://yandex.ru/maps/org/kit/1001138352/?indoorLevel=1&ll=55.181335%2C51.812650&z=16.56")
                                        
                            MDScrollView:
                                do_scroll_x: False
                                do_scroll_y: True
                                
                                MDLabel:
                                    size_hint_y: None
                                    height: self.texture_size[1]
                                    text: "Огромная площадь торгового центра позволяет разместить на ней множество магазинов. Помимо этого в ТЦ немало развлечений: аквапарк, боулинг, детский центр развлечений, кинотеатр, батутный парк. Для удобства посетителей также расставлены зарядные устройства по всему Торгово-Развлекательному Центру."
                                    bold: True
                                    color: 1, 1, 1, 1
                                    halign: "left"

                    Tab:
                        id: tab27
                        title: "Европа-Азия"
                        
                        BoxLayout:
                            orientation: 'vertical'
                            padding: "22dp"

                                

                            MDSmartTile:
                                
                                radius: 24
                                box_radius: [0, 0, 24, 24]
                                box_color: 0, 0, 0, .7
                                source: "euroaz.jpg"
                                
                                size_hint: None, None
                                size: "320dp", "320dp"
                                
                                
                                

                                MDIconButton:
                                    icon: "heart-outline"
                                    theme_icon_color: "Custom"
                                    icon_color: 1, 0, 0, 1
                                    pos_hint: {"center_y": .5}
                                    on_release: self.icon = "heart" if self.icon == "heart-outline" else "heart-outline"

                                MDLabel:
                                    text: "Европа-Азия"
                                    bold: True
                                    color: "white"
                                MDRectangleFlatButton:
                                    text: "На карте"
                                    theme_text_color: "Custom"
                                    text_color: "white"
                                    line_color: "red"
                                    on_press:
                                        import webbrowser
                                        webbrowser.open("https://yandex.ru/maps/org/yevropa_aziya/1108455167/?ll=55.130387%2C51.768507&z=16.56")
                                        
                            MDScrollView:
                                do_scroll_x: False
                                do_scroll_y: True
                                
                                MDLabel:
                                    size_hint_y: None
                                    height: self.texture_size[1]
                                    text: "Торговый центр Европа-Азия находится в самом центре города Оренбурга, где одновременно окружен: - жилым массивом; - бизнес-центрами и офисами самых крупных компаний России."
                                    bold: True
                                    color: 1, 1, 1, 1
                                    halign: "left"
                    
                    Tab:
                        id: tab26
                        title: "Север"
                        
                        BoxLayout:
                            orientation: 'vertical'
                            padding: "22dp"

                                

                            MDSmartTile:
                                
                                radius: 24
                                box_radius: [0, 0, 24, 24]
                                box_color: 0, 0, 0, .7
                                source: "severtrc.jpg"
                                
                                size_hint: None, None
                                size: "320dp", "320dp"
                                
                                
                                

                                MDIconButton:
                                    icon: "heart-outline"
                                    theme_icon_color: "Custom"
                                    icon_color: 1, 0, 0, 1
                                    pos_hint: {"center_y": .5}
                                    on_release: self.icon = "heart" if self.icon == "heart-outline" else "heart-outline"

                                MDLabel:
                                    text: "Север"
                                    bold: True
                                    color: "white"
                                MDRectangleFlatButton:
                                    text: "На карте"
                                    theme_text_color: "Custom"
                                    text_color: "white"
                                    line_color: "red"
                                    on_press:
                                        import webbrowser
                                        webbrowser.open("https://yandex.ru/maps/org/torgovo_razvlekatelny_tsentr_sever/1105503477/?ll=55.128774%2C51.833354&z=14.96")
                                        
                            MDScrollView:
                                do_scroll_x: False
                                do_scroll_y: True
                                
                                MDLabel:
                                    size_hint_y: None
                                    height: self.texture_size[1]
                                    text: "В одном из лучших торговых центров Оренбурга - Территория Севера представлены 280 магазинов, кинотеатры, кафе и большой развлекательный комплекс для детей."
                                    bold: True
                                    color: 1, 1, 1, 1
                                    halign: "left"
                    Tab:
                        id: tab26
                        title: "Гулливер"
                        
                        BoxLayout:
                            orientation: 'vertical'
                            padding: "22dp"

                                

                            MDSmartTile:
                                
                                radius: 24
                                box_radius: [0, 0, 24, 24]
                                box_color: 0, 0, 0, .7
                                source: "gulivertrk.jpg"
                                
                                size_hint: None, None
                                size: "320dp", "320dp"
                                
                                
                                

                                MDIconButton:
                                    icon: "heart-outline"
                                    theme_icon_color: "Custom"
                                    icon_color: 1, 0, 0, 1
                                    pos_hint: {"center_y": .5}
                                    on_release: self.icon = "heart" if self.icon == "heart-outline" else "heart-outline"

                                MDLabel:
                                    text: "Гулливер"
                                    bold: True
                                    color: "white"
                                MDRectangleFlatButton:
                                    text: "На карте"
                                    theme_text_color: "Custom"
                                    text_color: "white"
                                    line_color: "red"
                                    on_press:
                                        import webbrowser
                                        webbrowser.open("https://yandex.ru/maps/org/armada/1881685729/?ll=55.117828%2C51.844487&z=16")
                                        
                            MDScrollView:
                                do_scroll_x: False
                                do_scroll_y: True
                                
                                MDLabel:
                                    size_hint_y: None
                                    height: self.texture_size[1]
                                    text: "Профессиональный торгово-развлекательный комплекс в Оренбурге. Концепция нашего ТРК разрабатывалась совместно с ведущими российскими и итальянскими компаниями. Мы хотели создать яркий оазис шопинга и развлечений в серой повседневности."
                                    bold: True
                                    color: 1, 1, 1, 1
                                    halign: "left"
                                    
                    Tab:
                        id: tab25
                        title: "Мегамолл Армада"
                        
                        BoxLayout:
                            orientation: 'vertical'
                            padding: "22dp"

                                

                            MDSmartTile:
                                
                                radius: 24
                                box_radius: [0, 0, 24, 24]
                                box_color: 0, 0, 0, .7
                                source: "caption.jpg"
                                
                                size_hint: None, None
                                size: "320dp", "320dp"
                                
                                
                                

                                MDIconButton:
                                    icon: "heart-outline"
                                    theme_icon_color: "Custom"
                                    icon_color: 1, 0, 0, 1
                                    pos_hint: {"center_y": .5}
                                    on_release: self.icon = "heart" if self.icon == "heart-outline" else "heart-outline"

                                MDLabel:
                                    text: "Мегамолл Армада"
                                    bold: True
                                    color: "white"
                                MDRectangleFlatButton:
                                    text: "На карте"
                                    theme_text_color: "Custom"
                                    text_color: "white"
                                    line_color: "red"
                                    on_press:
                                        import webbrowser
                                        webbrowser.open("https://yandex.ru/maps/org/armada/1881685729/?ll=55.117828%2C51.844487&z=16")
                                        
                            MDScrollView:
                                do_scroll_x: False
                                do_scroll_y: True
                                
                                MDLabel:
                                    size_hint_y: None
                                    height: self.texture_size[1]
                                    text: "Мегамолл «Армада» - это крупнейший торгово-развлекательный центр, на территории которого расположено 370 магазинов и развлекательных объектов, среди которых крупнейшие в регионе гипермаркеты, магазины наиболее популярных брендов, галерея товаров для дома и ремонта, галерея еды."
                                    bold: True
                                    color: 1, 1, 1, 1
                                    halign: "left"                    
            MDScreen:
                name: "scr 8"

                MDTabs:
                    id: tabs
                    
                    
                    Tab:
                        id: tab22
                        title: "Батутный парк Отрыв"
                        
                        BoxLayout:
                            orientation: 'vertical'
                            padding: "22dp"

                                

                            MDSmartTile:
                                
                                radius: 24
                                box_radius: [0, 0, 24, 24]
                                box_color: 0, 0, 0, .7
                                source: "otriv.jpg"
                                
                                size_hint: None, None
                                size: "320dp", "320dp"
                                
                                
                                

                                MDIconButton:
                                    icon: "heart-outline"
                                    theme_icon_color: "Custom"
                                    icon_color: 1, 0, 0, 1
                                    pos_hint: {"center_y": .5}
                                    on_release: self.icon = "heart" if self.icon == "heart-outline" else "heart-outline"

                                MDLabel:
                                    text: "Батутный парк Отрыв"
                                    bold: True
                                    color: "white"
                                MDRectangleFlatButton:
                                    text: "На карте"
                                    theme_text_color: "Custom"
                                    text_color: "white"
                                    line_color: "red"
                                    on_press:
                                        import webbrowser
                                        webbrowser.open("https://yandex.ru/maps/48/orenburg/?indoorLevel=2&ll=55.181438%2C51.812853&mode=poi&poi%5Bpoint%5D=55.181293%2C51.813164&poi%5Buri%5D=ymapsbm1%3A%2F%2Forg%3Foid%3D138672015422&z=17")
                                        
                            MDScrollView:
                                do_scroll_x: False
                                do_scroll_y: True
                                
                                MDLabel:
                                    size_hint_y: None
                                    height: self.texture_size[1]
                                    text: "Только у нас: 90 батутов. Cетка для фристайла, 2 поролоновых бассейна, надувная подушка, Боулдеринг, 2 баскетбольных кольца, Наклонные батуты, Батуты дорожки, Air Trick мат, зал для тренировок по спортивной гимнастике и прыжкам на батуте."
                                    bold: True
                                    color: 1, 1, 1, 1
                                    halign: "left"                

                    Tab:
                        id: tab23
                        title: "Троя"
                        
                        BoxLayout:
                            orientation: 'vertical'
                            padding: "22dp"

                                

                            MDSmartTile:
                                
                                radius: 24
                                box_radius: [0, 0, 24, 24]
                                box_color: 0, 0, 0, .7
                                source: "troya.jpg"
                                
                                size_hint: None, None
                                size: "320dp", "320dp"
                                
                                
                                

                                MDIconButton:
                                    icon: "heart-outline"
                                    theme_icon_color: "Custom"
                                    icon_color: 1, 0, 0, 1
                                    pos_hint: {"center_y": .5}
                                    on_release: self.icon = "heart" if self.icon == "heart-outline" else "heart-outline"

                                MDLabel:
                                    text: "Троя"
                                    bold: True
                                    color: "white"
                                MDRectangleFlatButton:
                                    text: "На карте"
                                    theme_text_color: "Custom"
                                    text_color: "white"
                                    line_color: "red"
                                    on_press:
                                        import webbrowser
                                        webbrowser.open("https://yandex.ru/maps/48/orenburg/?ll=55.073275%2C51.763967&mode=poi&poi%5Bpoint%5D=55.073534%2C51.763946&poi%5Buri%5D=ymapsbm1%3A%2F%2Forg%3Foid%3D1323721898&utm_source=main_stripe_big&z=18.13")
                                        
                            MDScrollView:
                                do_scroll_x: False
                                do_scroll_y: True
                                
                                MDLabel:
                                    size_hint_y: None
                                    height: self.texture_size[1]
                                    text: "Оренбургский клуб лазертаг <<ТРОЯ>>, дает вам возможность почувствовать себя бойцом отряда особого назначения. В котором Вы сможете спасти заложника, предотвратить теракт, освободить здание и много другое(Сценарии игры lasertag)."
                                    bold: True
                                    color: 1, 1, 1, 1
                                    halign: "left"      

            MDScreen:
                name: "FullScreenMap"
                
                        
                BoxLayout:
                    orientation: 'vertical'
                    padding: "22dp"
                                
                MDLabel:
                    text: "Находится на стадии разработки..."
                    bold: True
                    color: 1, 1, 1, 1
                    halign: "center"
                        

                                    
                                           
        MDNavigationDrawer:
            id: nav_drawer
            

            ContentNavigationDrawer:
                screen_manager: screen_manager
                nav_drawer: nav_drawer

#Визуализации списков с выбором                
<ItemConfirm>
    on_release: root.set_icon(check)

    CheckboxLeftWidget:
        id: check
        group: "check"

'''




    
class ContentNavigationDrawer(MDScrollView):
    screen_manager = ObjectProperty()
    nav_drawer = ObjectProperty()


class Tab(MDFloatLayout, MDTabsBase):
    pass

#Класс визуализации списков с выбором
class ItemConfirm(OneLineAvatarIconListItem):
    divider = None

    def set_icon(self, instance_check):
        instance_check.active = True
        check_list = instance_check.get_widgets(instance_check.group)
        for check in check_list:
            if check != instance_check:
                check.active = False

class GidOren(MDApp):
    title = "ОренбургГид"

    
    #Запуск в билде визуала и пунктов меню в троеточии
    def build(self):

        self.theme_cls.primary_palette = "Orange"
        self.theme_cls.theme_style = "Dark"

        self.ads = KivMob('ca-app-pub-3940256099942544~3347511713')
        self.ads.new_banner('ca-app-pub-3940256099942544/6300978111', top_pos=True)



        self.ads.request_banner()
        self.ads.show_banner()
        
        menu_items = [
            {"text": "Настройки",
             "viewclass": "OneLineListItem",
             "on_release": lambda x="Настройки": self.dotsmenu_settings(x),
            },
            {"text": "О программе",
             "viewclass": "OneLineListItem",
             "on_release": lambda x="О программе": self.dotsmenu_about(x),
            }
        ]
        self.menu = MDDropdownMenu(
            max_height=dp(100),
            background_color=self.theme_cls.primary_color,
            items=menu_items,
            width_mult=3,
        )
        return Builder.load_string(KV)

    # Вызов меню
    def callback(self, button):
        self.menu.caller = button
        self.menu.open()

    # Открытие диалогового окна "О программе" через троеточие
    def dotsmenu_about(self, text_item):
        self.menu.dismiss()
        self.dialog = MDDialog(
            title="О программе:",
            text="Version: 0.5" "\n" "By team: CodeRed",
            buttons=[
                MDFlatButton(
                    text="Закрыть",
                    theme_text_color="Custom",
                    text_color=self.theme_cls.primary_color,
                    on_press=self.close_dialog,
                ),
            ],
        )
        self.dialog.open()

    # Открытие диалогового окна "Настройки" через троеточие
    def dotsmenu_settings(self, text_item):
        self.menu.dismiss()
        self.dialog = MDDialog(
            title="Настройки:",
            type="confirmation",
            items=[
                
                ItemConfirm(text="Темная тема"),
            ],
            buttons=[
                MDFlatButton(
                    text="Применить",
                    theme_text_color="Custom",
                    text_color=self.theme_cls.primary_color,
                    on_press=self.close_dialog,
                ),
                MDFlatButton(
                    text="Закрыть",
                    theme_text_color="Custom",
                    text_color=self.theme_cls.primary_color,
                    on_press=self.close_dialog,
                ),
            ],
        )
        self.dialog.open()

    #Закрытие диалогового окна
    def close_dialog(self, *args):
        self.dialog.dismiss(force=True)

    



GidOren().run()
