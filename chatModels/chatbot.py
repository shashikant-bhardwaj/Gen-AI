# import os
# from dotenv import load_dotenv

# from langchain_huggingface import ChatHuggingFace
# from langchain_huggingface import HuggingFaceEndpoint

# load_dotenv()
# llm = HuggingFaceEndpoint(
#     repo_id="deepseek-ai/DeepSeek-V4-Flash-0731",
#     huggingfacehub_api_token=os.getenv("HUGGINGFACEHUB_API_TOKEN")
# )

# model = ChatHuggingFace( llm=llm)
# print("----------------Welcome type 0 to exit the application-----------------------")
# while True:
   
#    prompt = input("You : ")
#    if prompt == "0":
#       break
   
#    response = model.invoke(prompt)

#    print("Bot : ",response.content)


# ab mistralai se chatbot bnate h

import langchain
import os
from dotenv import load_dotenv
from langchain_mistralai import ChatMistralAI
from langchain_core.messages import AIMessage, SystemMessage, HumanMessage

load_dotenv()

model = ChatMistralAI(
    model="mistral-small-2603",
    api_key=os.getenv("MISTRAL_API_KEY"),
    temperature=0.9,
    
)
print("Choose your AI mode")
print("press 1 for Angry mode")
print("press 2 for Funny mode")
print("press 3 for Sad mode")
choice = int(input("tell your response:- "))

if choice == 1:
   mode = "You are an Angry AI agent. You respond aggressively and impatiently."
elif choice == 2:
   mode = "You are a very Funny AI agent. You responnd with humor and jokes."
elif choice == 3:
   mode = "You are a very Sad AI agent. You responnd with sadness"      
messages = [
   SystemMessage(content=mode)
]
print("---------------hello if you want to exit the application press 0---------------")
while True:
   prompt = input("You :")
   messages.append(HumanMessage(content=prompt))
   if prompt == "0":
      break
   response = model.invoke(messages)
   messages.append(AIMessage(content=response.content))

   print("Bot :",response.content)

print(messages)   


