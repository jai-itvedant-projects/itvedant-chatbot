# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions

# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List, Union
from urllib import response

from rasa_sdk import Action, Tracker
from rasa_sdk.events import SlotSet, EventType
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormValidationAction
from rasa_sdk.types import DomainDict
from datetime import datetime as dt
#
#


class ActionCurrentTime(Action):

    def name(self) -> Text:
        return "action_current_time"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        time = str(dt.now().time())
        dispatcher.utter_message(text=time)

        return []

class ActionConsultancyForm(Action):
    def name(self) -> Text:
        return "user_details_form"

    def run(
        self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict
    ) -> List[EventType]:
        required_slots = ["name", "number"]

        for slot_name in required_slots:
            if tracker.slots.get(slot_name) is None:
                # The slot is not filled yet. Request the user to fill this slot next.
                return [SlotSet("requested_slot", slot_name)]

        # All slots are filled.
        return [SlotSet("requested_slot", None)]

class ActionSubmit(Action):
    def name(self) -> Text:
        return "action_submit"

    def run(
        self,
        dispatcher,
        tracker: Tracker,
        domain: "DomainDict",
    ) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(response="utter_details_thanks",
                                 Name=tracker.get_slot("name"),
                                 Mobile_number=tracker.get_slot("number"))


class ActionModules(Action):

    def name(self) -> Text:
        return "action_modules"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        entities = tracker.latest_message['entities']
        value = " "
        for entity in entities:
            value = entity['value'].lower()

        if (value == "ai") | (value == "ml") | (value == "dl") | (value == "nlp") | (value == "cv") | (value == "ds") | (value == "data science") | (value == "artificial intelligence") | (value == "machine learning") | (value == "deep learning") | (value == "natural language processing") | (value == "computer vision") | (value == "big data") | (value == "time series") | (value == "recommended system") | (value == "recommender system"):
            message = {
                "type": "template",
                        "payload": {
                            "template_type": "generic",
                            "elements": [
                                {
                                    "title": "Data Science with AI and AWS",
                                    "subtitle": " Masters Course ",
                                    "image_url": "https://imageio.forbes.com/specials-images/imageserve/615a844b0e678d9d11c5fc26/The-5-Biggest-Data-Science-Trends-In-2022/960x0.jpg?format=jpg&width=960",
                                    "buttons": [
                                        {
                                            "title": "Visit",
                                            "url": "https://www.itvedant.com/data-science-and-ai",
                                            "type": "web_url",
                                        }
                                    ]
                                },
                                {
                                    "title": "Data Science",
                                    "subtitle": " PG Course ",
                                    "image_url": "https://imageio.forbes.com/specials-images/imageserve/615a844b0e678d9d11c5fc26/The-5-Biggest-Data-Science-Trends-In-2022/960x0.jpg?format=jpg&width=960",
                                    "buttons": [
                                        {
                                            "title": "Visit",
                                            "url": "https://www.itvedant.com/data-science-course",
                                            "type": "web_url"
                                        }
                                    ]
                                },
                            ]
                        }
            }
            dispatcher.utter_message(attachment=message)

        elif (value == "bi") | (value == "business analytics") | (value == "analytics") | (value == "analysis") | (value == "tableau") | (value == "power bi") | (value == "data analysis") | (value == "visualization") | (value == "data visualization"):
            message = {
                "type": "template",
                        "payload": {
                            "template_type": "generic",
                            "elements": [
                                {
                                    "title": "Business Data Analytics",
                                    "subtitle": " Masters Course ",
                                    "image_url": "https://www.simplilearn.com/ice9/free_resources_article_thumb/Business_Analytics_Tools_Used_By_Companies_Today.jpg",
                                    "buttons": [
                                        {
                                            "title": "Visit",
                                            "url": "https://www.itvedant.com/master-business-data-analytics",
                                            "type": "web_url"
                                        }
                                    ]
                                },
                                {
                                    "title": "Data Analytics",
                                    "subtitle": " PG Course ",
                                    "image_url": "https://www.simplilearn.com/ice9/free_resources_article_thumb/Business_Analytics_Tools_Used_By_Companies_Today.jpg",
                                    "buttons": [
                                        {
                                            "title": "Visit",
                                            "url": "https://www.itvedant.com/business-data-analytics",
                                            "type": "web_url"
                                        }
                                    ]
                                },
                            ]
                        }
            }
            dispatcher.utter_message(attachment=message)

        elif (value == "web") | (value == "web development") | (value == "front end") | (value == "back end") | (value == "website") | (value == "website development") | (value == "stack") | (value == "full stack development") | (value == "full stack web development") | (value == "python") | (value == "java") | (value == "react") | (value == "node") | (value == "JS"):
            message = {
                "type": "template",
                        "payload": {
                            "template_type": "generic",
                            "elements": [
                                {
                                    "title": "Full Stack Developer",
                                    "subtitle": " Masters Course ",
                                    "image_url": "https://imageio.forbes.com/specials-images/imageserve/615a844b0e678d9d11c5fc26/The-5-Biggest-Data-Science-Trends-In-2022/960x0.jpg?format=jpg&width=960",
                                    "buttons": [
                                        {
                                            "title": "Visit",
                                            "url": "https://www.itvedant.com/full-stack-developer",
                                            "type": "web_url",
                                        }
                                    ]
                                },
                                {
                                    "title": "Python Developer",
                                    "subtitle": " PG Course ",
                                    "image_url": "https://tts.net.in/wp-content/uploads/2022/03/Python-01-2.png",
                                    "buttons": [
                                        {
                                            "title": "Visit",
                                            "url": "https://www.itvedant.com/python-training-course",
                                            "type": "web_url"
                                        }
                                    ]
                                },
                                {
                                    "title": "Java Developer",
                                    "subtitle": " PG Course ",
                                    "image_url": "https://softwareengineeringdaily.com/wp-content/uploads/2020/01/Java-Debugging-Tips-881x441.jpg",
                                    "buttons": [
                                        {
                                            "title": "Visit",
                                            "url": "https://www.itvedant.com/java-course",
                                            "type": "web_url"
                                        }
                                    ]
                                },
                                {
                                    "title": "MEAN Stack Developer",
                                    "subtitle": " PG Course ",
                                    "image_url": "https://miro.medium.com/max/1400/1*k0SazfSJ-tPSBbt2WDYIyw.png",
                                    "buttons": [
                                        {
                                            "title": "Visit",
                                            "url": "https://www.itvedant.com/training/mean-stack-development",
                                            "type": "web_url"
                                        }
                                    ]
                                },
                            ]
                        }
            }
            dispatcher.utter_message(attachment=message)

        elif (value == "cloud") | (value == "technology") | (value == "computing") | (value == "cloud technology") | (value == "cloud computing") | (value == "aws") | (value == "azure") | (value == "google cloud platform") | (value == "gcp") | (value == "amazon web services"):
            message = {
                "type": "template",
                        "payload": {
                            "template_type": "generic",
                            "elements": [
                                {
                                    "title": "Data Science with AI and AWS",
                                    "subtitle": " Masters Course ",
                                    "image_url": "https://imageio.forbes.com/specials-images/imageserve/615a844b0e678d9d11c5fc26/The-5-Biggest-Data-Science-Trends-In-2022/960x0.jpg?format=jpg&width=960",
                                    "buttons": [
                                        {
                                            "title": "Visit",
                                            "url": "https://www.itvedant.com/data-science-and-ai",
                                            "type": "web_url",
                                        }
                                    ]
                                },
                                {
                                    "title": "AWS and Azure",
                                    "subtitle": " Masters Course ",
                                    "image_url": "https://imageio.forbes.com/specials-images/imageserve/5f9fa9e815da35da1356a28b/The-5-Biggest-Cloud-Computing-Trends-In-2021/960x0.jpg?format=jpg&width=960",
                                    "buttons": [
                                        {
                                            "title": "Visit",
                                            "url": "https://www.itvedant.com/aws-azure-cloud-technology",
                                            "type": "web_url"
                                        }
                                    ]
                                },
                            ]
                        }
            }
            dispatcher.utter_message(attachment=message)

        else:
            dispatcher.utter_message(response="utter_no_data")

        return []


class ActionUserInput(Action):

    def name(self) -> Text:
        return "action_user_input"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: "DomainDict") -> List[Dict[Text, Any]]:
        entities = tracker.latest_message['entities']
        ct = " "
        cn = " "
        cd = " "

        for entity in entities:
            if entity['entity'] == 'course_type':
                ct = entity['value']

            if entity['entity'] == 'course_name':
                cn = entity['value']

            if entity['entity'] == 'course_duration':
                cd = entity['value']

        if (ct == 'masters') | (ct == 'master'):
            if cn == 'data science':
                if cd == '12 months':
                    message = {
                        "type": "template",
                        "payload": {
                            "template_type": "generic",
                            "elements": [
                                {
                                    "title": "Data Science with AI and AWS",
                                    "subtitle": " Masters Course ",
                                    "image_url": "https://imageio.forbes.com/specials-images/imageserve/615a844b0e678d9d11c5fc26/The-5-Biggest-Data-Science-Trends-In-2022/960x0.jpg?format=jpg&width=960",
                                    "buttons": [
                                        {
                                            "title": "Visit",
                                            "url": "https://www.itvedant.com/data-science-and-ai",
                                            "type": "web_url",
                                        }
                                    ]
                                }
                            ]
                        }
                    }
                    dispatcher.utter_message(attachment=message)
                elif cd == '6 months':
                    message = {
                        "type": "template",
                        "payload": {
                            "template_type": "generic",
                            "elements": [
                                {
                                    "title": "Data Science",
                                    "subtitle": " PG Course ",
                                    "image_url": "https://imageio.forbes.com/specials-images/imageserve/615a844b0e678d9d11c5fc26/The-5-Biggest-Data-Science-Trends-In-2022/960x0.jpg?format=jpg&width=960",
                                    "buttons": [
                                        {
                                            "title": "Visit",
                                            "url": "https://www.itvedant.com/data-science-course",
                                            "type": "web_url",
                                        }
                                    ]
                                }
                            ]
                        }
                    }
                    dispatcher.utter_message(attachment=message)
                else:
                    message = {
                        "type": "template",
                        "payload": {
                            "template_type": "generic",
                            "elements": [
                                {
                                    "title": "Data Science with AI and AWS",
                                    "subtitle": " Masters Course ",
                                    "image_url": "https://imageio.forbes.com/specials-images/imageserve/615a844b0e678d9d11c5fc26/The-5-Biggest-Data-Science-Trends-In-2022/960x0.jpg?format=jpg&width=960",
                                    "buttons": [
                                        {
                                            "title": "Visit",
                                            "url": "https://www.itvedant.com/data-science-and-ai",
                                            "type": "web_url",
                                        }
                                    ]
                                }
                            ]
                        }
                    }
                    dispatcher.utter_message(attachment=message)
            elif cn == 'web development':
                if cd == '12 months':
                    message = {
                        "type": "template",
                        "payload": {
                            "template_type": "generic",
                            "elements": [
                                {
                                    "title": "Full Stack Developer",
                                    "subtitle": " Masters Course ",
                                    "image_url": "https://imageio.forbes.com/specials-images/imageserve/615a844b0e678d9d11c5fc26/The-5-Biggest-Data-Science-Trends-In-2022/960x0.jpg?format=jpg&width=960",
                                    "buttons": [
                                        {
                                            "title": "Visit",
                                            "url": "https://www.itvedant.com/full-stack-developer",
                                            "type": "web_url",
                                        }
                                    ]
                                }
                            ]
                        }
                    }
                    dispatcher.utter_message(attachment=message)
                elif cd == '6 months':
                    message = {
                        "type": "template",
                        "payload": {
                            "template_type": "generic",
                            "elements": [
                                {
                                    "title": "Python Developer",
                                    "subtitle": " PG Course ",
                                    "image_url": "https://tts.net.in/wp-content/uploads/2022/03/Python-01-2.png",
                                    "buttons": [
                                        {
                                            "title": "Visit",
                                            "url": "https://www.itvedant.com/python-training-course",
                                            "type": "web_url"
                                        }
                                    ]
                                },
                                {
                                    "title": "Java Developer",
                                    "subtitle": " PG Course ",
                                    "image_url": "https://softwareengineeringdaily.com/wp-content/uploads/2020/01/Java-Debugging-Tips-881x441.jpg",
                                    "buttons": [
                                        {
                                            "title": "Visit",
                                            "url": "https://www.itvedant.com/java-course",
                                            "type": "web_url"
                                        }
                                    ]
                                },
                                {
                                    "title": "MEAN Stack Developer",
                                    "subtitle": " PG Course ",
                                    "image_url": "https://miro.medium.com/max/1400/1*k0SazfSJ-tPSBbt2WDYIyw.png",
                                    "buttons": [
                                        {
                                            "title": "Visit",
                                            "url": "https://www.itvedant.com/training/mean-stack-development",
                                            "type": "web_url"
                                        }
                                    ]
                                },
                            ]
                        }
                    }
                    dispatcher.utter_message(attachment=message)
                else:
                    message = {
                        "type": "template",
                        "payload": {
                            "template_type": "generic",
                            "elements": [
                                {
                                    "title": "Full Stack Developer",
                                    "subtitle": " Masters Course ",
                                    "image_url": "https://imageio.forbes.com/specials-images/imageserve/615a844b0e678d9d11c5fc26/The-5-Biggest-Data-Science-Trends-In-2022/960x0.jpg?format=jpg&width=960",
                                    "buttons": [
                                        {
                                            "title": "Visit",
                                            "url": "https://www.itvedant.com/full-stack-developer",
                                            "type": "web_url",
                                        }
                                    ]
                                }
                            ]
                        }
                    }
                    dispatcher.utter_message(attachment=message)
            elif cn == 'business analytics':
                if cd == '12 months':
                    message = {
                        "type": "template",
                        "payload": {
                            "template_type": "generic",
                            "elements": [
                                {
                                    "title": "Business Data Analytics",
                                    "subtitle": " Masters Course ",
                                    "image_url": "https://www.simplilearn.com/ice9/free_resources_article_thumb/Business_Analytics_Tools_Used_By_Companies_Today.jpg",
                                    "buttons": [
                                        {
                                            "title": "Visit",
                                            "url": "https://www.itvedant.com/master-business-data-analytics",
                                            "type": "web_url"
                                        }
                                    ]
                                },
                            ]
                        }
                    }
                    dispatcher.utter_message(attachment=message)
                elif cd == '6 months':
                    message = {
                        "type": "template",
                        "payload": {
                            "template_type": "generic",
                            "elements": [
                                {
                                    "title": "Data Analytics",
                                    "subtitle": " PG Course ",
                                    "image_url": "https://www.simplilearn.com/ice9/free_resources_article_thumb/Business_Analytics_Tools_Used_By_Companies_Today.jpg",
                                    "buttons": [
                                        {
                                            "title": "Visit",
                                            "url": "https://www.itvedant.com/business-data-analytics",
                                            "type": "web_url"
                                        }
                                    ]
                                },
                            ]
                        }
                    }
                    dispatcher.utter_message(attachment=message)
                else:
                    message = {
                        "type": "template",
                        "payload": {
                            "template_type": "generic",
                            "elements": [
                                {
                                    "title": "Business Data Analytics",
                                    "subtitle": " Masters Course ",
                                    "image_url": "https://www.simplilearn.com/ice9/free_resources_article_thumb/Business_Analytics_Tools_Used_By_Companies_Today.jpg",
                                    "buttons": [
                                        {
                                            "title": "Visit",
                                            "url": "https://www.itvedant.com/master-business-data-analytics",
                                            "type": "web_url"
                                        }
                                    ]
                                },
                            ]
                        }
                    }
                    dispatcher.utter_message(attachment=message)
            elif cn == 'cloud technology':
                if cd == '12 months':
                    message = {
                        "type": "template",
                        "payload": {
                            "template_type": "generic",
                            "elements": [
                                {
                                    "title": "AWS and Azure",
                                    "subtitle": " Masters Course ",
                                    "image_url": "https://imageio.forbes.com/specials-images/imageserve/5f9fa9e815da35da1356a28b/The-5-Biggest-Cloud-Computing-Trends-In-2021/960x0.jpg?format=jpg&width=960",
                                    "buttons": [
                                        {
                                            "title": "Visit",
                                            "url": "https://www.itvedant.com/aws-azure-cloud-technology",
                                            "type": "web_url"
                                        }
                                    ]
                                },
                            ]
                        }
                    }
                    dispatcher.utter_message(attachment=message)
                elif cd == '6 months':
                    message = {
                        "type": "template",
                        "payload": {
                            "template_type": "generic",
                            "elements": [
                                {
                                    "title": "AWS and Azure",
                                    "subtitle": " Masters Course ",
                                    "image_url": "https://imageio.forbes.com/specials-images/imageserve/5f9fa9e815da35da1356a28b/The-5-Biggest-Cloud-Computing-Trends-In-2021/960x0.jpg?format=jpg&width=960",
                                    "buttons": [
                                        {
                                            "title": "Visit",
                                            "url": "https://www.itvedant.com/aws-azure-cloud-technology",
                                            "type": "web_url"
                                        }
                                    ]
                                },
                            ]
                        }
                    }
                    dispatcher.utter_message(attachment=message)
                else:
                    message = {
                        "type": "template",
                        "payload": {
                            "template_type": "generic",
                            "elements": [
                                {
                                    "title": "AWS and Azure",
                                    "subtitle": " Masters Course ",
                                    "image_url": "https://imageio.forbes.com/specials-images/imageserve/5f9fa9e815da35da1356a28b/The-5-Biggest-Cloud-Computing-Trends-In-2021/960x0.jpg?format=jpg&width=960",
                                    "buttons": [
                                        {
                                            "title": "Visit",
                                            "url": "https://www.itvedant.com/aws-azure-cloud-technology",
                                            "type": "web_url"
                                        }
                                    ]
                                },
                            ]
                        }
                    }
                    dispatcher.utter_message(attachment=message)
            else:
                message = {
                    "type": "template",
                    "payload": {
                        "template_type": "generic",
                        "elements": [
                            {
                                "title": "Data Science with AI and AWS",
                                "subtitle": " Masters Course ",
                                "image_url": "https://imageio.forbes.com/specials-images/imageserve/615a844b0e678d9d11c5fc26/The-5-Biggest-Data-Science-Trends-In-2022/960x0.jpg?format=jpg&width=960",
                                "buttons": [
                                    {
                                        "title": "Visit",
                                        "url": "https://www.itvedant.com/data-science-and-ai",
                                        "type": "web_url",
                                    }
                                ]
                            },
                            {
                                "title": "Business Data Analytics",
                                "subtitle": " Masters Course ",
                                "image_url": "https://www.simplilearn.com/ice9/free_resources_article_thumb/Business_Analytics_Tools_Used_By_Companies_Today.jpg",
                                "buttons": [
                                    {
                                        "title": "Visit",
                                        "url": "https://www.itvedant.com/master-business-data-analytics",
                                        "type": "web_url"
                                    }
                                ]
                            },
                            {
                                "title": "Full Stack Developer",
                                "subtitle": " Masters Course ",
                                "image_url": "https://sdacademy.pl/sda-assets/uploads/2021/10/WEB-DEVELOPMENT-s-1.png",
                                "buttons": [
                                    {
                                        "title": "Visit",
                                        "url": "https://www.itvedant.com/full-stack-developer",
                                        "type": "web_url"
                                    }
                                ]
                            },
                            {
                                "title": "AWS and Azure",
                                "subtitle": " Masters Course ",
                                "image_url": "https://imageio.forbes.com/specials-images/imageserve/5f9fa9e815da35da1356a28b/The-5-Biggest-Cloud-Computing-Trends-In-2021/960x0.jpg?format=jpg&width=960",
                                "buttons": [
                                    {
                                        "title": "Visit",
                                        "url": "https://www.itvedant.com/aws-azure-cloud-technology",
                                        "type": "web_url"
                                    }
                                ]
                            },
                        ]
                    }
                }
                dispatcher.utter_message(attachment=message)

        elif ct == 'pg':
            if cn == 'data science':
                if cd == '6 months':
                    message = {
                        "type": "template",
                        "payload": {
                            "template_type": "generic",
                            "elements": [
                                {
                                    "title": "Data Science",
                                    "subtitle": " PG Course ",
                                    "image_url": "https://imageio.forbes.com/specials-images/imageserve/615a844b0e678d9d11c5fc26/The-5-Biggest-Data-Science-Trends-In-2022/960x0.jpg?format=jpg&width=960",
                                    "buttons": [
                                        {
                                            "title": "Visit",
                                            "url": "https://www.itvedant.com/data-science-course",
                                            "type": "web_url",
                                        }
                                    ]
                                }
                            ]
                        }
                    }
                    dispatcher.utter_message(attachment=message)
                elif cd == '12 months':
                    message = {
                        "type": "template",
                        "payload": {
                            "template_type": "generic",
                            "elements": [
                                {
                                    "title": "Data Science with AI and AWS",
                                    "subtitle": " Masters Course ",
                                    "image_url": "https://imageio.forbes.com/specials-images/imageserve/615a844b0e678d9d11c5fc26/The-5-Biggest-Data-Science-Trends-In-2022/960x0.jpg?format=jpg&width=960",
                                    "buttons": [
                                        {
                                            "title": "Visit",
                                            "url": "https://www.itvedant.com/data-science-and-ai",
                                            "type": "web_url",
                                        }
                                    ]
                                }
                            ]
                        }
                    }
                    dispatcher.utter_message(attachment=message)
                else:
                    message = {
                        "type": "template",
                        "payload": {
                            "template_type": "generic",
                            "elements": [
                                {
                                    "title": "Data Science",
                                    "subtitle": " PG Course ",
                                    "image_url": "https://imageio.forbes.com/specials-images/imageserve/615a844b0e678d9d11c5fc26/The-5-Biggest-Data-Science-Trends-In-2022/960x0.jpg?format=jpg&width=960",
                                    "buttons": [
                                        {
                                            "title": "Visit",
                                            "url": "https://www.itvedant.com/data-science-course",
                                            "type": "web_url",
                                        }
                                    ]
                                }
                            ]
                        }
                    }
                    dispatcher.utter_message(attachment=message)
            elif cn == 'web development':
                if cd == '6 months':
                    message = {
                        "type": "template",
                        "payload": {
                            "template_type": "generic",
                            "elements": [
                                {
                                    "title": "Python Developer",
                                    "subtitle": " PG Course ",
                                    "image_url": "https://tts.net.in/wp-content/uploads/2022/03/Python-01-2.png",
                                    "buttons": [
                                        {
                                            "title": "Visit",
                                            "url": "https://www.itvedant.com/python-training-course",
                                            "type": "web_url"
                                        }
                                    ]
                                },
                                {
                                    "title": "Java Developer",
                                    "subtitle": " PG Course ",
                                    "image_url": "https://softwareengineeringdaily.com/wp-content/uploads/2020/01/Java-Debugging-Tips-881x441.jpg",
                                    "buttons": [
                                        {
                                            "title": "Visit",
                                            "url": "https://www.itvedant.com/java-course",
                                            "type": "web_url"
                                        }
                                    ]
                                },
                                {
                                    "title": "MEAN Stack Developer",
                                    "subtitle": " PG Course ",
                                    "image_url": "https://miro.medium.com/max/1400/1*k0SazfSJ-tPSBbt2WDYIyw.png",
                                    "buttons": [
                                        {
                                            "title": "Visit",
                                            "url": "https://www.itvedant.com/training/mean-stack-development",
                                            "type": "web_url"
                                        }
                                    ]
                                },
                            ]
                        }
                    }
                    dispatcher.utter_message(attachment=message)
                elif cd == '12 months':
                    message = {
                        "type": "template",
                        "payload": {
                            "template_type": "generic",
                            "elements": [
                                {
                                    "title": "Full Stack Developer",
                                    "subtitle": " Masters Course ",
                                    "image_url": "https://imageio.forbes.com/specials-images/imageserve/615a844b0e678d9d11c5fc26/The-5-Biggest-Data-Science-Trends-In-2022/960x0.jpg?format=jpg&width=960",
                                    "buttons": [
                                        {
                                            "title": "Visit",
                                            "url": "https://www.itvedant.com/full-stack-developer",
                                            "type": "web_url",
                                        }
                                    ]
                                }
                            ]
                        }
                    }
                    dispatcher.utter_message(attachment=message)
                else:
                    message = {
                        "type": "template",
                        "payload": {
                            "template_type": "generic",
                            "elements": [
                                {
                                    "title": "Python Developer",
                                    "subtitle": " PG Course ",
                                    "image_url": "https://tts.net.in/wp-content/uploads/2022/03/Python-01-2.png",
                                    "buttons": [
                                        {
                                            "title": "Visit",
                                            "url": "https://www.itvedant.com/python-training-course",
                                            "type": "web_url"
                                        }
                                    ]
                                },
                                {
                                    "title": "Java Developer",
                                    "subtitle": " PG Course ",
                                    "image_url": "https://softwareengineeringdaily.com/wp-content/uploads/2020/01/Java-Debugging-Tips-881x441.jpg",
                                    "buttons": [
                                        {
                                            "title": "Visit",
                                            "url": "https://www.itvedant.com/java-course",
                                            "type": "web_url"
                                        }
                                    ]
                                },
                                {
                                    "title": "MEAN Stack Developer",
                                    "subtitle": " PG Course ",
                                    "image_url": "https://miro.medium.com/max/1400/1*k0SazfSJ-tPSBbt2WDYIyw.png",
                                    "buttons": [
                                        {
                                            "title": "Visit",
                                            "url": "https://www.itvedant.com/training/mean-stack-development",
                                            "type": "web_url"
                                        }
                                    ]
                                },
                            ]
                        }
                    }
                    dispatcher.utter_message(attachment=message)
            elif cn == 'business analytics':
                if cd == '6 months':
                    message = {
                        "type": "template",
                        "payload": {
                            "template_type": "generic",
                            "elements": [
                                {
                                    "title": "Data Analytics",
                                    "subtitle": " PG Course ",
                                    "image_url": "https://www.simplilearn.com/ice9/free_resources_article_thumb/Business_Analytics_Tools_Used_By_Companies_Today.jpg",
                                    "buttons": [
                                        {
                                             "title": "Visit",
                                             "url": "https://www.itvedant.com/business-data-analytics",
                                             "type": "web_url"
                                        }
                                    ]
                                },
                            ]
                        }
                    }
                    dispatcher.utter_message(attachment=message)
                elif cd == '12 months':
                    message = {
                        "type": "template",
                        "payload": {
                            "template_type": "generic",
                            "elements": [
                                {
                                    "title": "Business Data Analytics",
                                    "subtitle": " Masters Course ",
                                    "image_url": "https://www.simplilearn.com/ice9/free_resources_article_thumb/Business_Analytics_Tools_Used_By_Companies_Today.jpg",
                                    "buttons": [
                                        {
                                            "title": "Visit",
                                            "url": "https://www.itvedant.com/master-business-data-analytics",
                                            "type": "web_url"
                                        }
                                    ]
                                },
                            ]
                        }
                    }
                    dispatcher.utter_message(attachment=message)
                else:
                    message = {
                        "type": "template",
                        "payload": {
                            "template_type": "generic",
                            "elements": [
                                {
                                    "title": "Data Analytics",
                                    "subtitle": " PG Course ",
                                    "image_url": "https://www.simplilearn.com/ice9/free_resources_article_thumb/Business_Analytics_Tools_Used_By_Companies_Today.jpg",
                                    "buttons": [
                                        {
                                            "title": "Visit",
                                            "url": "https://www.itvedant.com/business-data-analytics",
                                            "type": "web_url"
                                        }
                                    ]
                                },
                            ]
                        }
                    }
                    dispatcher.utter_message(attachment=message)
            elif cn == 'cloud technology':
                if cd == '6 months':
                    message = {
                        "type": "template",
                        "payload": {
                            "template_type": "generic",
                            "elements": [
                                {
                                    "title": "AWS and Azure",
                                    "subtitle": " Masters Course ",
                                    "image_url": "https://imageio.forbes.com/specials-images/imageserve/5f9fa9e815da35da1356a28b/The-5-Biggest-Cloud-Computing-Trends-In-2021/960x0.jpg?format=jpg&width=960",
                                    "buttons": [
                                        {
                                            "title": "Visit",
                                            "url": "https://www.itvedant.com/aws-azure-cloud-technology",
                                            "type": "web_url"
                                        }
                                    ]
                                },
                            ]
                        }
                    }
                    dispatcher.utter_message(attachment=message)
                elif cd == '12 months':
                    message = {
                        "type": "template",
                        "payload": {
                            "template_type": "generic",
                            "elements": [
                                {
                                    "title": "AWS and Azure",
                                    "subtitle": " Masters Course ",
                                    "image_url": "https://imageio.forbes.com/specials-images/imageserve/5f9fa9e815da35da1356a28b/The-5-Biggest-Cloud-Computing-Trends-In-2021/960x0.jpg?format=jpg&width=960",
                                    "buttons": [
                                        {
                                            "title": "Visit",
                                            "url": "https://www.itvedant.com/aws-azure-cloud-technology",
                                            "type": "web_url"
                                        }
                                    ]
                                },
                            ]
                        }
                    }
                    dispatcher.utter_message(attachment=message)
                else:
                    message = {
                        "type": "template",
                        "payload": {
                            "template_type": "generic",
                            "elements": [
                                {
                                    "title": "AWS and Azure",
                                    "subtitle": " Masters Course ",
                                    "image_url": "https://imageio.forbes.com/specials-images/imageserve/5f9fa9e815da35da1356a28b/The-5-Biggest-Cloud-Computing-Trends-In-2021/960x0.jpg?format=jpg&width=960",
                                    "buttons": [
                                        {
                                            "title": "Visit",
                                            "url": "https://www.itvedant.com/aws-azure-cloud-technology",
                                            "type": "web_url"
                                        }
                                    ]
                                },
                            ]
                        }
                    }
                    dispatcher.utter_message(attachment=message)
            else:
                message = {
                    "type": "template",
                    "payload": {
                        "template_type": "generic",
                        "elements": [
                            {
                                "title": "Data Science",
                                "subtitle": " PG Course ",
                                "image_url": "https://imageio.forbes.com/specials-images/imageserve/615a844b0e678d9d11c5fc26/The-5-Biggest-Data-Science-Trends-In-2022/960x0.jpg?format=jpg&width=960",
                                "buttons": [
                                    {
                                        "title": "Visit",
                                        "url": "https://www.itvedant.com/data-science-course",
                                        "type": "web_url"
                                    }
                                ]
                            },
                            {
                                "title": "Data Analytics",
                                "subtitle": " PG Course ",
                                "image_url": "https://www.simplilearn.com/ice9/free_resources_article_thumb/Business_Analytics_Tools_Used_By_Companies_Today.jpg",
                                "buttons": [
                                    {
                                        "title": "Visit",
                                        "url": "https://www.itvedant.com/business-data-analytics",
                                        "type": "web_url"
                                    }
                                ]
                            },
                            {
                                "title": "Python Developer",
                                "subtitle": " PG Course ",
                                "image_url": "https://tts.net.in/wp-content/uploads/2022/03/Python-01-2.png",
                                "buttons": [
                                    {
                                        "title": "Visit",
                                        "url": "https://www.itvedant.com/python-training-course",
                                        "type": "web_url"
                                    }
                                ]
                            },
                            {
                                "title": "Java Developer",
                                "subtitle": " PG Course ",
                                "image_url": "https://softwareengineeringdaily.com/wp-content/uploads/2020/01/Java-Debugging-Tips-881x441.jpg",
                                "buttons": [
                                    {
                                        "title": "Visit",
                                        "url": "https://www.itvedant.com/java-course",
                                        "type": "web_url"
                                    }
                                ]
                            },
                            {
                                "title": "MEAN Stack Developer",
                                "subtitle": " PG Course ",
                                "image_url": "https://miro.medium.com/max/1400/1*k0SazfSJ-tPSBbt2WDYIyw.png",
                                "buttons": [
                                    {
                                        "title": "Visit",
                                        "url": "https://www.itvedant.com/training/mean-stack-development",
                                        "type": "web_url"
                                    }
                                ]
                            },
                            {
                                "title": "Digital Marketing",
                                "subtitle": " PG Course ",
                                "image_url": "https://indiandigitalmarketer.com/wp-content/uploads/2022/01/introduction-to-digital-marketing.png",
                                "buttons": [
                                    {
                                        "title": "Visit",
                                        "url": "https://www.itvedant.com/digital-marketing-with-analytics",
                                        "type": "web_url"
                                    }
                                ]
                            },
                        ]
                    }
                }
                dispatcher.utter_message(attachment=message)

        else:
            dispatcher.utter_message(response="utter_no_data")

        return []
