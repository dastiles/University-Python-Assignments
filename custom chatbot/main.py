# @stiles group 2 nlp
import json # to bot responses
from sklearn.feature_extraction.text import TfidfVectorizer # to find similarities between text
import random # to randomizes text responses for the bot


responses = json.loads(open('response.json').read()) # load responses
tfidf_vectorizer = TfidfVectorizer()

# function to find similarities between 2 users text and tags for the response
def cosine_sim(text1, text2):
    tfidf = tfidf_vectorizer.fit_transform([text1, text2])
    return ((tfidf * tfidf.T).A)[0,1]


# return the response with the highest similaritl
def Stiles_message_responder(msg: str) -> str:
   reply_message = {}
   for message in responses['messages']:
      tags = message['tags']
      msg_response = message['responses']
      
      for tag in tags:        
         msg_tag_similarity = cosine_sim(tag, msg)
         msg_bot_responder = random.choice(msg_response)
         if msg_tag_similarity > 0:             
            if reply_message.get(msg_bot_responder) == None:
               reply_message[msg_bot_responder] = msg_tag_similarity
            else:
               if reply_message[msg_bot_responder] < msg_tag_similarity:
                  reply_message[msg_bot_responder] = msg_tag_similarity
                  
   
   if len(reply_message) <= 0:
      return 'Stiles does not understand. please ask again'
   return max(reply_message)
         

while True:
   message = input('You: ')
   print(f'bot: {Stiles_message_responder(message)}')
   