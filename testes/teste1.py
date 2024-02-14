import customtkinter as ctk
import threading
import keyboard
from time import sleep
import win32api
import win32con
import mouse


class Click:
    def __init__(self, macro_value_bool):
        # data
        self.macro_is_on = macro_value_bool
        self.click_delay = 0
        self.click_repeat = 0
        self.mouse_pos = (0, 0)
        self.button_down = win32con.MOUSEEVENTF_LEFTDOWN
        self.button_up = win32con.MOUSEEVENTF_LEFTUP

        self.macro_is_active = False
        self.interna_macro_is_off = False

    def click(self):
        print('click')
        sleep(self.click_delay + 0.001)

    def normal_click(self):
        while self.macro_is_on.get() or self.interna_macro_is_off:
            self.click()

        self.macro_is_active = False

    def freeze_click(self):
        while self.macro_is_on.get() or self.interna_macro_is_off:
            win32api.SetCursorPos(self.mouse_pos)
            self.click()

        self.macro_is_active = False

    def repeat_click(self):
        while (self.macro_is_on.get() and self.click_repeat >= 0) or self.interna_macro_is_off:
            self.click()
            self.click_repeat -= 1

        self.macro_is_active = False

    def freeze_repeat_click(self):
        while (self.macro_is_on.get() and self.click_repeat >= 0) or self.interna_macro_is_off:
            win32api.SetCursorPos(self.mouse_pos)
            self.click()
            self.click_repeat -= 1

        self.macro_is_active = False


    def desligar_macro(self, *args):
        self.interna_macro_is_off = False

    def start_normal_macro(self, freeze, delay, infinite_repeat, quant_repeat, button):
        if self.macro_is_active == False:
            self.macro_is_active = True
            self.interna_macro_is_off = True
            self.macro_is_on.trace('w', self.desligar_macro)
            self.click_delay = delay
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
            if infinite_repeat:
                self.click_repeat = quant_repeat

            if freeze and infinite_repeat:
                self.mouse_pos = mouse.get_position()
                threading.Thread(
                    target=self.freeze_repeat_click, daemon=True).start()
            elif freeze:
                self.mouse_pos = mouse.get_position()
                threading.Thread(target=self.freeze_click, daemon=True).start()
            elif infinite_repeat:
                threading.Thread(target=self.repeat_click, daemon=True).start()
            else:
                threading.Thread(target=self.normal_click, daemon=True).start()


class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.switch = ctk.BooleanVar(value=False)


        self.macro = Click(self.switch)

        ctk.CTkSwitch(self, variable=self.switch,onvalue=True, offvalue=False).pack()


        keyboard.on_press_key('q', self.minha_funcao)

        self.mainloop()

    def minha_funcao(self, key):
        self.switch.set(not self.switch.get())
        if self.switch.get():
            #                           freeze, delay, infinite_repeat, quant_repeat, button):
            self.macro.start_normal_macro(False, 0.1, False, 10, 'Left')



App()
