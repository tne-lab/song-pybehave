from typing import List
from types import MethodType

import pygame

from Elements.CircleLightElement import CircleLightElement
from Elements.FoodLightElement import FoodLightElement
from Elements.Element import Element
from Elements.NosePokeElement import NosePokeElement
from Elements.ButtonElement import ButtonElement
from Elements.InfoBoxElement import InfoBoxElement
from GUIs import Colors
from GUIs.GUI import GUI


class SetShiftGUI(GUI):

    def __init__(self, ws, task):
        super().__init__(ws, task)
        self.np_lights = []
        self.np_inputs = []
        self.info_boxes = []

        def feed_mouse_up(self):
            self.clicked = False
            task.food.dispense()

        def pellets_text(self):
            return [str(task.food.pellets)]

        def trial_count_text(self):
            return [str(task.cur_trial+1)]

        for i in range(3):
            npl = CircleLightElement(self.task_gui, 50 + (i+1)*(25+60), 60, 30, Colors.lightgray, Colors.darkgray, task.nose_poke_lights[i])
            self.np_lights.append(npl)
            npi = NosePokeElement(self.task_gui, 50 + (i+1) * (25 + 60), 150, 30, task.nose_pokes[i])
            self.np_inputs.append(npi)
        self.food_poke = NosePokeElement(self.task_gui, 220, 360, 30, task.food_trough)
        self.feed_button = ButtonElement(self.task_gui, 225, 500, 50, 20, "FEED", task.food)
        self.feed_button.mouse_up = MethodType(feed_mouse_up, self.feed_button)
        pellets = InfoBoxElement(self.task_gui, 225, 455, 50, 15, "PELLETS", 'BOTTOM', ['0'])
        pellets.get_text = MethodType(pellets_text, pellets)
        self.info_boxes.append(pellets)
        trial_count = InfoBoxElement(self.task_gui, 400, 500, 50, 15, "TRIAL", 'BOTTOM', ['0'])
        trial_count.get_text = MethodType(trial_count_text, trial_count)
        self.info_boxes.append(trial_count)
        self.food_light = FoodLightElement(self.task_gui, 200, 250, 100, 90, Colors.lightgray, task.food_light, Colors.black)

    def draw(self):
        self.task_gui.fill(Colors.darkgray)
        for el in self.get_elements():
            el.draw()
        pygame.display.flip()

    def get_elements(self) -> List[Element]:
        return [*self.np_lights, *self.np_inputs, self.food_poke, self.food_light, self.feed_button, *self.info_boxes]