"""Re-Act -> Reasoning + Action.
   loop(Thought -> Action -> Observe) -> final answer"""
   
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.agents import initialize_agent
from langchain_community.tools import TavilySearchResults, tool
from dotenv import load_dotenv
from datetime import datetime
import os
load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-1.5-pro", temperature=0.0, api_key=os.getenv("GOOGLE_GENAI_API_KEY"))

search_tool = TavilySearchResults(search_depth="basic")

@tool
def get_current_date(format: str = "%Y-%m-%d"):
    """returns the current date"""
    return datetime.now().strftime(format)

agent = initialize_agent(
    tools=[search_tool, get_current_date],
    llm=model,
    agent="zero-shot-react-description",
    verbose=True,
)

agent.invoke("when was meri pyaari bundu bollywood movie realesed and how many days ago from today?")

"""disadvantages:
    flexible but not reliable( stucks in infinite tool loop)
"""