from typing import List
from langgraph.graph import MessagesState

'''
Note. 
class MessagesState(TypedDict):
    messages: Annotated[list[AnyMessage], add_messages]

where add_messages is a custom function that helps append messages.

Read more details about MessagesState at
https://github.com/langchain-ai/langgraph/blob/main/libs/langgraph/langgraph/graph/message.py
'''

class AgentState(MessagesState):
    documents: List[str]