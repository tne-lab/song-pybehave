from typing import List
from types import MethodType

from Elements.CircleLightElement import CircleLightElement
from Elements.FoodLightElement import FoodLightElement
from Elements.Element import Element
from Elements.NosePokeElement import NosePokeElement
from Elements.ButtonElement import ButtonElement
from Elements.InfoBoxElement import InfoBoxElement
from GUIs.GUI import GUI


class FiveChoiceGUI(GUI):

    def __init__(self, task_gui, task):
        super().__init__(task_gui, task)
        self.np_lights = []
        self.np_inputs = []
        self.info_boxes = []

        def feed_mouse_up(self, _):
            self.clicked = False
            task.food.toggle(task.dispense_time)

        def pellets_text(self):
            return [str(task.food.count)]

        def trial_count_text(self):
            return [str(task.cur_trial+1)]

        for i in range(5):
            npl = CircleLightElement(self, 50 + i*(25+60), 60, 30, comp=task.nose_poke_lights[i])
            self.np_lights.append(npl)
            npi = NosePokeElement(self, 50 + i * (25 + 60), 150, 30, comp=task.nose_pokes[i])
            self.np_inputs.append(npi)
        self.food_poke = NosePokeElement(self, 220, 360, 30, comp=task.food_trough)
        self.feed_button = ButtonElement(self, 225, 500, 50, 20, "FEED")
        self.feed_button.mouse_up = MethodType(feed_mouse_up, self.feed_button)
        pellets = InfoBoxElement(self, 225, 455, 50, 15, "PELLETS", 'BOTTOM', ['0'])
        pellets.get_text = MethodType(pellets_text, pellets)
        self.info_boxes.append(pellets)
        trial_count = InfoBoxElement(self, 400, 500, 50, 15, "TRIAL", 'BOTTOM', ['0'])
        trial_count.get_text = MethodType(trial_count_text, trial_count)
        self.info_boxes.append(trial_count)
        self.food_light = FoodLightElement(self, 200, 250, 100, 90, comp=task.food_light)

    def get_elements(self) -> List[Element]:
        return [*self.np_lights, *self.np_inputs, self.food_poke, self.food_light, self.feed_button, *self.info_boxes]
