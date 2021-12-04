# rasa_makeup_virtual_assistant
Final project for CMPE 252 Fall 2021 by Megha Jain.

## About The Bot
This bot is virstual assistant for a makeup store (Sephora). It does a combination of recommendations + query answerting + checking inventory and taking orders from customer. 

## Notable Parts
One of the more difficult and notable things to implement was using the tracker's events to search for/establish a previous context for the conversion. I got this idea from my research paper presentation where the paper my team presented on emphasized the importance and usefulness of context-driven chatbots.

This part is implements in the action_recommend_settingspray functon in actions.py. This function indexes and searches all the previous intents that are tracked in the tracker object in order to get the latest type of look that was referenced. Since setting spray is recommended for some looks but not others, the bot can use the information about the previously mentioned look, aka context extracted from previous intents in order to decide whether to recommend a setting spray or not.
