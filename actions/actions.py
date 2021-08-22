from typing import Any, Text, Dict, List, Union

from requests.models import Response

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormAction
from dotenv import load_dotenv

import requests
import json
import os


# load_dotenv()

# airtable_api_key=os.getenv("AIRTABLE_API_KEY")
# base_id=os.getenv("BASE_ID")
# table_name=os.getenv("TABLE_NAME")

# def create_health_log(confirm_exercise,exercise,sleep, diet, stress, goal):
#     request_url=f"https://api.airtable.com/v0/{base_id}/{table_name}"
#     headers = {
#         "Content-Type": "application/json",
#         "Accept": "application/json",
#         "Authorization": f"Bearer {airtable_api_key}"
#     }

#     data = {
#         "fileds": {
#             "Exercised?": confirm_exercise,
#             "Type of exercise": exercise,
#             "Amout of sleep": sleep,
#             "Stress": stress,
#             "Diet": diet,
#             "Goal": goal
#         }
#     }

#     try:
#         response = requests.post(
#             request_url, headers=headers, data=json.dumps(data)
#         )
#         response.raise_for_status()
#     except requests.exceptions.HTTPError as err:
#         raise SystemExit(err)
    
#     return response
 


class HealthForm(FormAction):

    def name(self):
        return "health_form"
    
    @staticmethod
    def required_slots(tracker):

        if tracker.get_slot("confirm_exercise") == True:
            return ["confirm_exercise", "exercise", "sleep", "diet","stress", "goal"]
        else:
            return ["confirm_exercise","sleep", "diet","stress", "goal"]
    
    def submit(
        self,
        diapatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict]:

        # response = create_health_log(
        #     tracker.get_slot("confirm_exercise"),
        #     tracker.get_slot("exercise"),
        #     tracker.get_slot("sleep"),
        #     tracker.get_slot("diet"),
        #     tracker.get_slot("stress"),
        #     tracker.get_slot("goal")
        # )
        # dispatcher.utter_message("Thanks, your answer have been recorded!")
        
        return []
    
    def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:
        return {
            "confirm_exercise": [
                self.from_intent(intent="affirm", value=True),
                self.from_intent(intent="deny", value=False),
                self.from_intent(intent="inform", value=True)
            ],
            "sleep": [
                self.from_entity(entity="sleep"),
                self.from_intent(intent="deny", value="None")
            ],
            "diet": [
                self.from_text(intent="inform"),
                self.from_text(intent="affirm"),
                self.from_text(intent="deny")
            ],
            "goal": [
                self.from_text(intent="inform")
            ]
        }