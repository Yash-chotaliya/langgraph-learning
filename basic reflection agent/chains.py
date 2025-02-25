from langchain.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_google_genai import ChatGoogleGenerativeAI
import os

llm = ChatGoogleGenerativeAI(model="gemini-1.5-pro", api_key=os.getenv("GOOGLE_GENAI_API_KEY"))

generator_prompt = ChatPromptTemplate.from_messages([
    ("system", 
     "you are a twitter techie influencer assistant tasked with writing excellent twitter posts."
     "generate the best twitter post possible for the user's request."
     "if the user provides critique, respond with a revised version of your previous attempts." 
    ),
    MessagesPlaceholder(variable_name="messages"),
])

reflector_prompt = ChatPromptTemplate.from_messages([
    ("system",
     "you are a viral twitter influencer grading a tweet. generate critique and recommandations for the user's tweet"
     "always provide detailed recommandations, including requests for length, virality, style, etc."
    ),
    MessagesPlaceholder(variable_name="messages"),
])

generator_chain = generator_prompt | llm
reflector_chain = reflector_prompt | llm