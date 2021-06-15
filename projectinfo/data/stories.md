## goodbye path
  * goodbye
  - utter_goodbye
  - action_null
  
## thanks path
  * thanks
  - utter_respond
  - action_null

## happy path
  
  * greet
  - utter_greet
  - action_null
  * mood_great
  - utter_happy
  - action_null

## sad path 1
  
  * mood_unhappy
  - utter_cheer_up
  - action_null
  - utter_did_that_help
  * affirm
  - utter_happy
  - action_null

## sad path 2
  
  * mood_unhappy
  - utter_cheer_up
  - action_null
  - utter_did_that_help
  * deny
  - utter_sorry
  - action_null
  
## personal
  
  * personale
  - utter_personale
  - action_staff
  - utter_did_that_help
  * deny
  - utter_sorry
  - action_null
  
## personal 2
  
  * personale
  - utter_personale
  - action_staff
  - utter_did_that_help
  * affirm
  - utter_happy
  - action_null
  
  
## informazioni
  
  * info
  - utter_informazioni
  - action_information

## lista comandi
  
  * bot_actions
  - utter_buttons
  - action_information

## scopo
  
  * bot_purpose
  - utter_purpose
  - action_information
  - utter_did_that_help
  * deny
  - utter_sorry
  - action_null
  
## scopo 2
  
  * bot_purpose
  - utter_purpose
  - action_information
  - utter_did_that_help
  * affirm
  - utter_happy
  - action_null
  
## challenge
  
  * bot_challenge
  - utter_iamabot
  - action_information
  - utter_did_that_help
  * deny
  - utter_sorry
  - action_null
  
## challenge 2
  
  * bot_purpose
  - utter_purpose
  - action_information
  - utter_did_that_help
  * affirm
  - utter_happy
  - action_null
  
## sommario
  
  * sommario
  - utter_sommario
  - action_information
  - utter_did_that_help
  * deny
  - utter_sorry
  - action_null
  
## sommario 2
  
  * sommario
  - utter_sommario
  - action_information
  - utter_did_that_help
  * affirm
  - utter_happy
  - action_null
  
## soa
  
  * soa
  - utter_soa
  - action_soa
  
## ambizioniprogresso
  
  * ambizioni
  - utter_ambizioniprogresso
  - action_soa
  - utter_did_that_help
  * affirm
  - utter_happy
  - action_null
  
## ambizioniprogresso 2
  
  * ambizioni
  - utter_ambizioniprogresso
  - action_soa
  - utter_did_that_help
  * deny
  - utter_sorry
  - action_null
  
## obbiettivi
  
  * obbiettivi
  - utter_Objectives
  - action_information
  - utter_did_that_help
  * affirm
  - utter_happy
  - action_null
  
## obbiettivi 2
  
  * obbiettivi
  - utter_Objectives
  - action_information
  - utter_did_that_help
  * deny
  - utter_sorry
  - action_null
  
## professore
  
  * professore
  - action_Info_Prof
  - action_staff
  
## pubblicazioni
  
  * pubblicazioni
  - action_Publ_Prof
  - action_staff
  
## metodology 
  
  * metodologia
  - utter_metodologia
  - action_soa
  * deny
  - utter_sorry
  - action_null
  
## metodology 2
  
  * metodologia
  - utter_metodologia
  - action_soa
  * affirm
  - utter_happy
  - action_null
  
## cyarc 
  
  * cyberarc
  - utter_cyberarc
  - action_cyberarc
  * deny
  - utter_sorry
  - action_null
  
## cyarc 2
  
  * cyberarc
  - utter_cyberarc
  - action_cyberarc
  * affirm
  - utter_happy
  - action_null  
  
  
## ita  
  
  * ita
  - utter_ita
  - action_Agents
  * deny
  - utter_sorry
  - action_null
  
## ita 2
  
  * ita
  - utter_ita
  - action_Agents
  * affirm
  - utter_happy 
  - action_null
  
## emboagent  
  
  * emboage
  - utter_emboage
  - action_Agents
  * deny
  - utter_sorry
  - action_null
  
## emboagent 2
  
  * emboage
  - utter_emboage
  - action_Agents
  * affirm
  - utter_happy
  - action_null
  
## collabenv  
  
  * collabenv
  - utter_collabenv
  - action_soa
  * deny
  - utter_sorry
  - action_null
  
## collabenv 2
  
  * collabenv
  - utter_collabenv
  - action_soa
  * affirm
  - utter_happy 
  - action_null
  
## musdif  
  
  * musdif
  - utter_musdif
  - action_musdiff
  * deny
  - utter_sorry
  - action_null
  
## musdif 2
  
  * musdif
  - utter_musdif
  - action_musdiff
  * affirm
  - utter_happy 
  - action_null