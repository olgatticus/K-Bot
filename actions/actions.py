from typing import Text, List, Any, Dict

from rasa_sdk import Tracker, FormValidationAction, Action
from rasa_sdk.events import EventType
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.types import DomainDict
from rasa_sdk.events import SlotSet
from actions import select_info as s_inf 
import random
from actions import select_solution as s_sol

ALLOWED_GROUPS = ["none", "nct", "bts", "stray kids", "txt", "seventeen", "exo", "blackpink"]
ALLOWED_GROUPS_info = ["nct", "bts", "stray kids", "txt", "seventeen", "exo", "blackpink"]


class ValidateSongSuggestionForm(FormValidationAction):
    def name(self) -> Text:
        return "validate_song_suggestion_form"

    def validate_group(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate 'group' value."""

        if slot_value.lower() not in ALLOWED_GROUPS:
            dispatcher.utter_message(text=f"I'm sorry I don't know about this group yet!")
            return {"group": None}
        else:
            dispatcher.utter_message(text=f"Sure.")
            return {"group": slot_value}

    def validate_random_song(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        """ Proceed according to the value assigned to random_song """

        if slot_value == True:
            dispatcher.utter_message(text="Ok, I'll decide for you.")
            val = "all"
            ener = "all"
            danc = "all" 
            if tracker.slots.get("song_valence"):
                val = tracker.slots.get("song_valence")
            if tracker.slots.get("song_energy"):
                ener = tracker.slots.get("song_energy")
            if tracker.slots.get("song_danceability"):
                danc = tracker.slots.get("song_danceability")
            return {"random_song": True, "song_valence": val, 
                    "song_energy": ener, "song_danceability": danc}
        
        else:
            val = tracker.slots.get("song_valence")
            ener = tracker.slots.get("song_energy")
            danc = tracker.slots.get("song_danceability") 
            for en in tracker.latest_message["entities"]:
                if en["entity"] == "song_valence":
                    if en["value"] == "high cheerfulness":
                        val = "high"
                    elif en["value"] == "low cheerfulness":
                        val = "low"
                    elif en["value"] == "medium cheerfulness":
                        val = "medium"
                if en["entity"] == "song_energy":
                    if en["value"] == "high energy":
                        ener = "high"
                    elif en["value"] == "low energy":
                        ener = "low"
                    elif en["value"] == "medium energy":
                        ener = "medium"
                if en["entity"] == "song_danceability":
                    if  en["value"] == "high danceability":
                        danc = "high"
                    elif en["value"] == "low danceability":
                        danc = "low"
                    elif  en["value"] == "medium danceability":
                        danc = "medium"
            if (not val or not ener or not danc):
                dispatcher.utter_message(text="Alright! You can answer positively, negatively, stay neutral or tell if random is ok.")
            return {"random_song": False, "song_valence": val, 
                    "song_energy": ener, "song_danceability": danc}

    def validate_song_valence(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        """ Proceed according to the value assigned to song_valence """

        if (slot_value != None
            and tracker.latest_message["intent"]["name"] != "request_song_suggestion_form"
            and tracker.latest_message["intent"]["name"] != "inform_song"):
            dispatcher.utter_message(text="Got it.")
        
        return {"song_valence": slot_value}

    def validate_song_energy(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        """ Proceed according to the value assigned to song_energy """

        if (slot_value != None
            and tracker.latest_message["intent"]["name"] != "request_song_suggestion_form"
            and tracker.latest_message["intent"]["name"] != "inform_song"):
            dispatcher.utter_message(text="Alright.")
        
        return {"song_energy": slot_value}

    def validate_song_danceability(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        """ Proceed according to the value assigned to song_danceability """

        if (slot_value != None
            and tracker.latest_message["intent"]["name"] != "request_song_suggestion_form"
            and tracker.latest_message["intent"]["name"] != "inform_song"):
            dispatcher.utter_message(text="Sure.")
        
        return {"song_danceability": slot_value}
        

class ValidateGroupInfoForm(FormValidationAction):
    def name(self) -> Text:
        return "validate_group_info_form"

    def validate_group(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate 'group' value."""

        if slot_value.lower() not in ALLOWED_GROUPS_info:
            dispatcher.utter_message(text=f"I'm sorry I don't know about this group yet! Please try with another one.")
            return {"group": None}
        else:
            return {"group": slot_value}

class ActionSetSongSlots(Action):

    def name(self) -> Text:
        return "action_set_song_slots"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        if tracker.latest_message["entities"] == []:
            if("random" in tracker.latest_message["text"]
                or "casual" in tracker.latest_message["text"]):
                if ("them" in tracker.latest_message["text"] 
                    or "their" in tracker.latest_message["text"]
                    or "theirs" in tracker.latest_message["text"]):
                    return [SlotSet("random_song", True), SlotSet("song_danceability", "all"),
                            SlotSet("song_energy", "all"), SlotSet("song_valence", "all")]
                else:
                    return [SlotSet("group", None), SlotSet("random_song", True), SlotSet("song_danceability", "all"),
                            SlotSet("song_energy", "all"), SlotSet("song_valence", "all")]

            else:
                if ("them" in tracker.latest_message["text"] 
                    or "their" in tracker.latest_message["text"]
                    or "theirs" in tracker.latest_message["text"]):
                    return [SlotSet("random_song", None), SlotSet("song_danceability", None),
                            SlotSet("song_energy", None), SlotSet("song_valence", None)]
                else:
                    return [SlotSet("group", None), SlotSet("random_song", None), SlotSet("song_danceability", None),
                            SlotSet("song_energy", None), SlotSet("song_valence", None)]
        else:
            val = None
            ener = None
            danc = None 
            rand = None
            cont = 0
            for en in tracker.latest_message["entities"]:
                if en["entity"] == "song_valence":
                    if en["value"] == "high cheerfulness":
                        val = "high"
                    elif en["value"] == "low cheerfulness":
                        val = "low"
                    elif en["value"] == "medium cheerfulness":
                        val = "medium"
                    cont +=1
                if en["entity"] == "song_energy":
                    if en["value"] == "high energy":
                        ener = "high"
                    elif en["value"] == "low energy":
                        ener = "low"
                    elif en["value"] == "medium energy":
                        ener = "medium"
                    cont +=1
                if en["entity"] == "song_danceability":
                    if  en["value"] == "high danceability":
                        danc = "high"
                    elif en["value"] == "low danceability":
                        danc = "low"
                    elif  en["value"] == "medium danceability":
                        danc = "medium"
                    cont +=1
            if cont == 3:
                rand = False
            return [SlotSet("random_song", rand), SlotSet("song_danceability", danc),
                        SlotSet("song_energy", ener), SlotSet("song_valence", val)]

        

class ActionFillInfoSlots(Action):

    def name(self) -> Text:
        return "action_fill_info_slots"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        group = tracker.slots["group"]

        if group == None:
            return [SlotSet("group_debut", None), SlotSet("group_members", None),
                    SlotSet("group_company", None), SlotSet("group_activity", None)]

        else:
            info = s_inf.extract_info(group)
            return [SlotSet("group_debut", info["debut"]), SlotSet("group_members", info["members"]),
                    SlotSet("group_company", info["company"]), SlotSet("group_activity", info["activity"])]

class ActionSubmit(Action):

    def name(self) -> Text:
        return "action_submit"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        group = tracker.slots["group"]
        valence = tracker.slots["song_valence"]
        energy = tracker.slots["song_energy"]
        danceability = tracker.slots["song_danceability"]

        if (group and valence and energy and danceability):
            if group == "none":
                group = "random"
            if valence == "all":
                valence = "random"
            if energy == "all":
                energy = "random"
            if danceability == "all":
                danceability = "random"

            if (valence == "random" and energy == "random" and danceability == "random"):
                dispatcher.utter_message(response = "utter_submit_random", group = group)
            else:
                dispatcher.utter_message(response = "utter_submit", group = group, valence=valence, energy=energy, danceability=danceability)
            
            return []

        else:
            return [SlotSet("group", group), SlotSet("song_valence", valence),
                    SlotSet("song_energy", energy), SlotSet("song_danceability", danceability)]

class ActionSuggestSong(Action):

    def name(self) -> Text:
        return "action_suggest_song"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        group = tracker.slots["group"]
        valence = tracker.slots["song_valence"]
        energy = tracker.slots["song_energy"]
        danceability = tracker.slots["song_danceability"]

        if (group and valence and energy and danceability):
            filtered_solutions = s_sol.find_solutions(s_sol.songs_solutions, group, valence, energy, danceability)
            solution = random.sample(filtered_solutions, 1)[0]

            dispatcher.utter_message(response = "utter_suggest_song", song = solution[0], group = solution[1])
            
            return [SlotSet("group", solution[1])]

        else:
            return [SlotSet("group", group), SlotSet("song_valence", valence),
                    SlotSet("song_energy", energy), SlotSet("song_danceability", danceability)]
