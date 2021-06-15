# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List
#
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import xml.etree.ElementTree as ET
import urllib.request
import ssl
#

class ActionInfoProf(Action):
     def name(self) -> Text:
         return "action_Info_Prof"

     def run(self, dispatcher: CollectingDispatcher,
           tracker: Tracker,
             domain: Dict[Text, Any], ) -> List[Dict[Text, Any]]:
			 
         surname = "ciao"
         print(surname)
         name = "ciao"
         print(name)
         entities = tracker.latest_message['entities']
         print(entities)
         for e in entities:
             if e['entity'] == 'name':
                 name = e['value']
             if e['entity'] == 'surname':
                 surname = e['value']

			 
             if name == "salvatore":
                 if surname == "venticinque":
                     dispatcher.utter_message(text="His interests include multi-agent systems, cloud computing and bigdata, mobile computing, embedded systems and high performance computing. He has participated innational and international projects with different roles. He is coordinator of the H2020 Greencharge project.He was responsible of technical activities and technological development of the PRIST 2009 project")

					 
             if name == "rocco":
                 if surname == "aversa":
                     dispatcher.utter_message(text="His research interests in the area of parallel and distributed systems. Theresearch themes include: the use of the mobile agents paradigm in the distributed computing; the design ofsimulation tools for performance analysis of parallel applications running on heterogeneous computingarchitectures; the project and the development of innovative middleware software to enhance the Grid andCloud computing platform.")
					 
             if name == "massimo":
                 if surname == "ficco":
                     dispatcher.utter_message(text="His current research interests include security and reliability aspects of criticalinfrastructure, cloud computing, software engineering architecture, and mobile computing. M. Ficco hasbeen involved in national and EU funded research projects in the area of security and reliability of criticalinfrastructures.")					 
             
             if name == "Maurizio":
                 if surname == "d'arienzo":
                     dispatcher.utter_message(text="He collaborated in European projects with international partners includingUniversity of Cambridge and Imperial College of London. His research activity deals with the developmentand the experimentation of protocols and algorithms for the deployment of QoS on computer networks andnew models of admission control in self-aware networks, game theory applied to wireless networks, sensornetworks.")
			 
			 
             if name == "giuseppina":
                 if surname == "renda":
                     dispatcher.utter_message(text="She has maturated a long experience in the field of the AncientTopography and Preventive Archaeology for land-use planning, developing a special interest on thetransformation in the settlement patterns, Urbanism, Landscape. She has experience in archaeologicalmapping information management, data entry, G.I.S. and she is able to manage multimedia contents, usingOntologies, Semantic Techniques, Augmented and Virtual Reality.")
					 
             if name == "almerinda":
                 if surname == "di benedetto":
                     dispatcher.utter_message(text="She is the author of several monographs and essays focusing onthe artistic production of the nineteenth century and the first half of the twentieth century. Since 2016 she isa consultant for the historical and artistic heritage of the Foundation of the Opera di San Giuseppe dei Nudiin Naples. She is editorial director of ARTeS - Studies of Art and History, scientific series for NicolaLongobardi publisher.")
					 
             if name == "paola":
                 if surname == "cafora":
                     dispatcher.utter_message(text="She carried out topography researches. She reached great experience inArchaeological mapping information management and data entry. From several years involved in differentresearch programs with National institutiones to edit 'Carta Archeologica'. Her interests include Landscape,the hill forts systems, the ancient routes, the ancient architecture with a multidisciplinary approach and aparticular skills in the remote sensing.")
					 
             if name == "rosa":
                 if surname == "vitale":
                     dispatcher.utter_message(text="She is engaged on several research topics, such as currency in the ancientPompeii, examined through coin finds from the most ancient ones (III sec. a.C.) to the last ones, buriedduring the eruption in 79 d.C.; coinage phenomena in the ancient Campania with special regards toSamnites; Roman coinage and monetary issues of autonomous communities during the republican epoch.")
			 
         return []
class Actionpublprof(Action):
     def name(self) -> Text:
         return "action_Publ_Prof"

     def run(self, dispatcher: CollectingDispatcher,
           tracker: Tracker,
             domain: Dict[Text, Any], ) -> List[Dict[Text, Any]]:
			 
         surname = "ciao"
         print(surname)
         name = "ciao"
         print(name)
         entities = tracker.latest_message['entities']
         print(entities)
         for e in entities:
             if e['entity'] == 'name':
                 name = e['value']
             if e['entity'] == 'surname':
                 surname = e['value']
                 context = ssl._create_unverified_context()
                 url = 'https://dblp.org/search/publ/api?q='+name+'+'+surname
                 response = urllib.request.urlopen(url,context=context).read()
                 tree = ET.fromstring(response)
                 dispatcher.utter_message("last five pubblication:")
                 c=0
                 for i in tree:
                     for ii in i:
                         for iii in ii:
                             for iiii in iii:
                                 if(iiii.tag=='title'):
                                     c=c+1
                                     if(c<6):
                                         dispatcher.utter_message("-"+ iiii.text)
            
			 
         return []
		 
		 
		 
class ActionNull(Action):
    def name(self) -> Text:
        return "action_null"
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
            messaggio = tracker.latest_message['text']
            file = open("sent.txt",'a');
            file.write("Topic: Null\n");
            file.close()
            return []
class ActionInformation(Action):
    def name(self) -> Text:
        return "action_information"
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
            messaggio = tracker.latest_message['text']
            file = open("sent.txt",'a');
            file.write("Topic: Information\n");
            file.close()
            return []
class ActionStaff(Action):
    def name(self) -> Text:
        return "action_staff"
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
            messaggio = tracker.latest_message['text']
            file = open("sent.txt",'a');
            file.write("Topic: Staff\n");
            file.close()
            return []
class ActionAgents(Action):
    def name(self) -> Text:
        return "action_Agents"
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
            messaggio = tracker.latest_message['text']
            file = open("sent.txt",'a');
            file.write("Topic: Agents\n");
            file.close()
            return []
class Actioncyberarc(Action):
    def name(self) -> Text:
        return "action_cyberarc"
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
            messaggio = tracker.latest_message['text']
            file = open("sent.txt",'a');
            file.write("Topic: cyber archeology\n");
            file.close()
            return []
class Actionmusdiff(Action):
    def name(self) -> Text:
        return "action_musdiff"
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
            messaggio = tracker.latest_message['text']
            file = open("sent.txt",'a');
            file.write("Topic: museo diffuso\n");
            file.close()
            return []
class Actionsoa(Action):
    def name(self) -> Text:
        return "action_soa"
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
            messaggio = tracker.latest_message['text']
            file = open("sent.txt",'a');
            file.write("Topic: State of Arts\n");
            file.close()
            return []