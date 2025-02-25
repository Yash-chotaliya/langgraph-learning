from typing import List, Sequence
from dotenv import load_dotenv
from chains import generator_chain, reflector_chain
from langchain_core.messages import BaseMessage, HumanMessage
from langgraph.graph import END, MessageGraph

load_dotenv()

graph = MessageGraph()

GENERATE = "generate"
REFLECT = "reflect"

def generate_node(state):
    print("Generator :")
    response = generator_chain.invoke({"messages": state})
    print("\n")
    print(state)
    print("\n")
    print(response)
    print("\n------------\n")
    return response

def reflect_node(state):
    print("Reflector :")
    response = reflector_chain.invoke({"messages": state})
    print("\n")
    print(state)
    print("\n")
    print(response)
    print("\n------------\n")
    return [HumanMessage(content=response.content)]

graph.add_node(GENERATE, generate_node)
graph.add_node(REFLECT, reflect_node)

graph.set_entry_point(GENERATE)

def should_reflect(state):
    if(len(state)>2):
        return END
    return REFLECT

graph.add_conditional_edges(GENERATE, should_reflect)

graph.add_edge(REFLECT, GENERATE)

app = graph.compile()

# to draw the graph
"""print(app.get_graph().draw_mermaid())
app.get_graph().print_ascii()"""

result = app.invoke(HumanMessage(content="AI agents taking over humans."))



