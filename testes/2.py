import customtkinter as ctk
import keyboard
import asyncio

import win32api
import win32con
import mouse


class Click:
    def __init__(self, macro_value_bool):
        self.macro_is_on = macro_value_bool
        self.click_delay = 0
        self.click_repeat = 0
        self.mouse_pos = (0, 0)
        self.button_down = win32con.MOUSEEVENTF_LEFTDOWN
        self.button_up = win32con.MOUSEEVENTF_LEFTUP

    def click(self):
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)

    async def normal_click(self):
        print('aqui')
        print(self.macro_is_on.get())
        while self.macro_is_on.get():
            self.click()
            await asyncio.sleep(self.click_delay)
        print('parrou')

    async def freeze_click(self):
        while self.macro_is_on.get():
            print('click')
            win32api.SetCursorPos(self.mouse_pos)
            self.click()
            await asyncio.sleep(self.click_delay)

    async def repeat_click(self):
        while self.macro_is_on.get() and self.click_repeat >= 0:
            print(self.macro_is_on.get())
            print(self.click_repeat)
            self.click()
            await asyncio.sleep(self.click_delay)
            self.click_repeat -= 1

    async def freeze_repeat_click(self):
        while self.macro_is_on.get() and self.click_repeat >= 0:
            win32api.SetCursorPos(self.mouse_pos)
            self.click()
            await asyncio.sleep(self.click_delay)
            self.click_repeat -= 1

    async def start_normal_macro(self, freeze, delay, infinite_repeat, quant_repeat, button):
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
            self.freeze_repeat_click()
        elif freeze:
            self.mouse_pos = mouse.get_position()
            self.freeze_click()
        elif infinite_repeat:
            self.repeat_click()
        else:
            self.normal_click()


class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.switch = ctk.BooleanVar(value=False)
        self.macro = Click(self.switch)

        # 2 formas de ativar o macro
        ctk.CTkSwitch(self, variable=self.switch,onvalue=True, offvalue=False).pack()
        keyboard.on_press_key('q', self.minha_funcao)

        self.mainloop()

    def minha_funcao(self, key):
        self.switch.set(not self.switch.get())
        if self.switch.get():
            print('macro on')
            asyncio.run(self.macro.start_normal_macro(False, 1, True, 10, 'Left'))

        else:
            print('macro off')


App()
