# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions
#
#
# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk.events import SlotSet
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher


dewy_products_inventory = {
'Glossier Skin Tint' : 5,
'Makeup By Mario Higlighter' : 10,
'Juvias Place Bronzed Lip Gloss' : 3
}
glam_products_inventory = {
'Natasha Denona Glam Eyeshadow Palette' : 5,
'Maybelline Fit Me Foundation' : 10,
'Fenty Beauty Killawat Highlighter' : 3
}
editorial_products_inventory = {
'Juvias Place The Masquerade Eyeshadow Palette' : 5,
'Fenty Beauty Stunna Lip Paint' : 10,
'Colourpop Super Shock Blush' : 3
}
natural_products_inventory = {
'Makeup By Mario Soft Pop Blush Stick' : 5,
'Estee Lauder Double Wear Foundation' : 10,
'Nars Air Matte Liquid Lipstick' : 3
}


store_locations = ["New York", "San Jose", "Los Angeles", "Mumbai", "Chicago", "Dallas", "San Francisco"]
class ActionRecommendDewy(Action):

    def name(self):
        return "action_recommend_dewy"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]): #-> List[Dict[Text, Any]]:

        global dewy_products_inventory

        product_options = dewy_products_inventory.keys()

        recommend_string = "These are the makeup products I would recommend for a dewy look -- "
        for i in product_options:
            recommend_string += i + ", "

        final_string = recommend_string[:len(recommend_string)-2]
        final_string += "\nWould you like to order one of these products?"
        dispatcher.utter_message(text=final_string)
        return []

class ActionRecommendGlam(Action):

    def name(self):
        return "action_recommend_glam"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]): #-> List[Dict[Text, Any]]:

        global glam_products_inventory

        product_options = glam_products_inventory.keys()

        recommend_string = "These are the makeup products I would recommend for a glam look -- "
        for i in product_options:
            recommend_string += i + ", "

        final_string = recommend_string[:len(recommend_string)-2]
        final_string += "\nWould you like to order one of these products?"
        dispatcher.utter_message(text=final_string)

        return []

class ActionRecommendNatural(Action):

    def name(self):
        return "action_recommend_natural"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]): #-> List[Dict[Text, Any]]:

        global natural_products_inventory

        product_options = natural_products_inventory.keys()

        recommend_string = "These are the makeup products I would recommend for a natural look -- \n "
        for i in product_options:
            recommend_string += i + ", "

        final_string = recommend_string[:len(recommend_string)-2]
        final_string += "\nWould you like to order one of these products?"
        dispatcher.utter_message(text=final_string)

        return []

class ActionRecommendEditorial(Action):

    def name(self):
        return "action_recommend_editorial"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]): #-> List[Dict[Text, Any]]:

        global glam_products_inventory

        product_options = editorial_products_inventory.keys()

        recommend_string = "These are the makeup products I would recommend for an editorial look -- "
        for i in product_options:
            recommend_string += i + ", "

        final_string = recommend_string[:len(recommend_string)-2]
        final_string += "\nWould you like to order one of these products?"
        dispatcher.utter_message(text=final_string)

        return []

class ActionRecommendSettingspray(Action):

    def name(self):
        return "action_recommend_settingspray"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]): #-> List[Dict[Text, Any]]:

        reversed_events = list(reversed(tracker.events))
        intents = []

        for e in reversed_events:
            if e['event'] == 'user':
                curr_intent = e['parse_data']['intent']['name']
                intents.append(curr_intent)

        choice = 0

        if 'wedding' in intents or 'glam' in intents:
            choice = 1
        elif 'natural' in intents or 'office' in intents:
            choice = 2
        elif 'editorial' in intents or 'photoshoot' in intents:
            choice = 3
        elif 'dewy' in intents or 'picnic' in intents:
            choice = 4

        final_string = ""

        if choice == 1:
            final_string += "Yes, you must use setting spray for a glam look, especially if you are wearing it a wedding. "
            final_string += "It will make your makeup last longer!"
        elif choice == 2:
            final_string += "While setting spray is always recommended, no it is not necessary to wear it for a natural look, especially for the office."

        elif choice == 3:
            final_string += "Yes, you must use setting spray for an editorial look, especially if you are wearing it a photoshoot. "
            final_string += "It will make your makeup last longer!"
        elif choice == 4:
            final_string += "While setting spray is always recommended, no it is not necessary to wear it for a dewy look, especially for a picnic."

        else:
            final_string += "Yes, setting spray is recommended in most casees."

        dispatcher.utter_message(text=final_string)

        return []

class ActionCheckLocation(Action):

    def name(self):
        return "action_check_location"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]): #-> List[Dict[Text, Any]]:

        city = tracker.get_slot("city")
        if city in store_locations:
            dispatcher.utter_message(text=f"Yes, we do have store location in {city}!")
        else:
            dispatcher.utter_message(text=f"Sorry, we do not have any store locations in {city}.")

        return []

class ActionCoolUndertones(Action):

    def name(self):
        return "action_cool_undertones"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]): #-> List[Dict[Text, Any]]:

        dispatcher.utter_message(text="Cool undertones are complemented by colors like blue, black, grey, mauve, purple etc.")
        return []

class ActionWarmUndertones(Action):

    def name(self):
        return "action_warm_undertones"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]): #-> List[Dict[Text, Any]]:

        dispatcher.utter_message(text="Warm undertones are complemented by colors like red, yellow, orange, pink etc etc.")
        return []

class ActionNeutralUndertones(Action):

    def name(self):
        return "action_neutral_undertones"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]): #-> List[Dict[Text, Any]]:

        dispatcher.utter_message(text="Neutral undertones are complemented by all colors.")
        return []

class ActionOliveUndertones(Action):

    def name(self):
        return "action_olive_undertones"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]): #-> List[Dict[Text, Any]]:

        dispatcher.utter_message(text="Olive undertones are complemented by colors like green, yellow, brown, golden etc.")
        return []

class ActionMakeupRemover(Action):

    def name(self):
        return "action_makeup_remover"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]): #-> List[Dict[Text, Any]]:

        dispatcher.utter_message(text="Makeup can be removed using wipes, balms or solutions. Our top rated product is the Neutrogena Makeup Remover Wipes!")
        return []


class ActionValidateOrder(Action):

    def name(self):
        return "action_validate_order"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]): #-> List[Dict[Text, Any]]:

        product_name = tracker.get_slot("product_name")
        address = tracker.get_slot("address")
        global glam_products_inventory
        global natural_products_inventory
        global dewy_products_inventory
        global editorial_products_inventory

        glam_keys = glam_products_inventory.keys()
        natural_keys = natural_products_inventory.keys()
        dewy_keys = dewy_products_inventory.keys()
        editorial_keys = editorial_products_inventory.keys()

        num_available = 0
        if product_name in glam_keys:
            num_available = glam_products_inventory[product_name]
            glam_products_inventory[product_name] -= 1
        elif product_name in natural_keys:
            num_available = natural_products_inventory[product_name]
            natural_products_inventory[product_name] -= 1
        elif product_name in dewy_keys:
            num_available = dewy_products_inventory[product_name]
            dewy_products_inventory[product_name] -= 1
        elif product_name in editorial_keys:
            num_available = editorial_products_inventory[product_name]
            editorial_products_inventory[product_name] -= 1

        final_string = ""
        if num_available > 0:
            final_string += f"Yes, the {product_name} is available!\n"
            final_string += f"We will ship 1 of these to {address}. Enjoy!"
        else:
            final_string += "Sorry, either we don't carry that product or it is out of stock at the moment."

        final_string += " Is there anything else I can help you with?"

        dispatcher.utter_message(text=final_string)

        return [SlotSet("product_name", product_name)]
