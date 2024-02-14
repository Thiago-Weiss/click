import threading
from time import sleep, time
import win32api
import win32con
import mouse


class Click:
    def __init__(self, macro_value_bool, att_text):
        # data
        self.macro_is_on = macro_value_bool
        self.att_text = att_text
        self.click_delay = 0
        self.click_repeat = 0
        self.mouse_pos = (0, 0)
        self.button_down = win32con.MOUSEEVENTF_LEFTDOWN
        self.button_up = win32con.MOUSEEVENTF_LEFTUP
        self.double_click = True
        self.macro_is_active = False
        self.interna_macro_is_off = False
        self.clicks_pos = ()
        self.freeze_click_bool = False

    # funcao que clica
    def click(self):
        win32api.mouse_event(self.button_down, 0, 0)
        win32api.mouse_event(self.button_up, 0, 0)

    # funçao que faz o double click ou nao e que faz o sleep entre os clicks
    def clicks(self):
        self.click()
        if self.double_click:
            self.click()
        # faz o sleep de uma forma que verifica se o macro foi desativado
        tempo_inicial = time()
        tempo_atual = tempo_inicial
        while tempo_atual - tempo_inicial < self.click_delay + 0.005:
            sleep(0.005)
            tempo_atual = time()
            if not self.macro_is_on.get() or not self.interna_macro_is_off:
                break


    '''
quatro funçoes para dois tipos de situaçoes
as duas primeiras funçoes sao para o macro normal uma dele infinito e outra com repetiçao

as ultimas duas sao funçoes para multi-clicks e uma para ele infinito e outra com repetiçao

e a varivael "self.macro_is_active = False" é uma variavel de controle para impedir de criar duas Thread
e bugar o programa ele impede o ativamento de um novo macro se um já estiver ligado

    '''

    # normal infinito
    def infinite_click(self):
        while self.macro_is_on.get() and self.interna_macro_is_off:
            if self.freeze_click_bool:
                win32api.SetCursorPos(self.mouse_pos)
            self.clicks()
        self.macro_is_active = False
    
    # normal finito
    def repeat_click(self):
        while self.click_repeat > 0 and self.macro_is_on.get() and self.interna_macro_is_off:
            if self.freeze_click_bool:
                win32api.SetCursorPos(self.mouse_pos)
            self.clicks()
            self.click_repeat -= 1
        self.macro_is_active = False
        self.desligar_main_macro()

    # multi-clicks infinito
    def infinite_multi_clicks(self):
        index = 0
        while self.macro_is_on.get() and self.interna_macro_is_off:
            win32api.SetCursorPos(self.clicks_pos[index])
            index += 1
            if index >= len(self.clicks_pos):
                index = 0
            self.clicks()
        self.macro_is_active = False

    # multi-clicks finito
    def repeat_multi_clicks(self):
        index = 0
        while self.click_repeat > 0 and self.macro_is_on.get() and self.interna_macro_is_off:
            win32api.SetCursorPos(self.clicks_pos[index])
            index += 1
            if index >= len(self.clicks_pos):
                index = 0
            self.clicks()
            self.click_repeat -= 1
        self.macro_is_active = False
        self.desligar_main_macro()



    # desabilita a bool do arquivo main quando o macro por repetiçao acaba e atualiza o texto
    def desligar_main_macro(self):
        self.macro_is_on.set(False)
        self.att_text()


    # é um tracer na variavel principal do macro que controla se ela for alterada
    # e quando for alterada ela vai desabilitar (false) qualquer Thread
    # e no final de qualquer Thread ele habilita o macro ser usado de novo
    # e quando o macro é ativado denovo ele habilita (true) posibilitando o macro funcionar
    def desligar_macro(self, *args):
        self.interna_macro_is_off = False



    # funçao que é chamada pela main pra ativar o macro com base nas variaveis passadas
    def start_normal_macro(self, freeze, delay, button, single_bool, repeat, clicks_pos, multi_clicks_bool):
        # logica pra impedir ativamento de dois macros (Thread) ao mesmo tempo
        if self.macro_is_active == False:
            self.macro_is_active = True
            self.interna_macro_is_off = True
            self.macro_is_on.trace('w', self.desligar_macro)

            # salva as variaveis passadas
            self.freeze_click_bool = freeze
            self.mouse_pos = mouse.get_position()
            self.double_click = single_bool
            self.click_delay = delay
            if repeat:
                self.click_repeat = repeat
            match button:
                case 'Left':
                    self.button_down = win32con.MOUSEEVENTF_LEFTDOWN
                    self.button_up = win32con.MOUSEEVENTF_LEFTUP
                case 'Right':
                    self.button_down = win32con.MOUSEEVENTF_RIGHTDOWN
                    self.button_up = win32con.MOUSEEVENTF_RIGHTUP
                case 'Mid':
                    self.button_down = win32con.MOUSEEVENTF_MIDDLEDOWN
                    self.button_up = win32con.MOUSEEVENTF_MIDDLEUP

            # ativa o macro de acordo com as variaveis e o tipo (normal ou multi-clicks) e se tem repeticao ou nao
            if multi_clicks_bool:
                self.clicks_pos = clicks_pos
                if repeat:
                    threading.Thread(target=self.repeat_multi_clicks, daemon=True).start()
                else:
                    threading.Thread(target=self.infinite_multi_clicks, daemon=True).start()
            elif repeat:
                threading.Thread(target=self.repeat_click, daemon=True).start()
            else:
                threading.Thread(target=self.infinite_click, daemon=True).start()
