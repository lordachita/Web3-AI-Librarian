# External Libraries
import os
from langchain_openai import ChatOpenAI
from langgraph.graph import StateGraph, MessagesState, START, END
from langchain_community.document_loaders import PyPDFLoader

# Internal Libraries
from ..classes import AgentState

class Graph:
    def __init__(self, is_memory = False):

        self.document_searcher_node = self.DocumentSearcherNode
        #self.pdf_to_text_node = self.PDFToTextNode
        #self.summary_node = self.SummaryNode
        self.answer_node = self.AnswerNode

        self.llm = ChatOpenAI(model="gpt-4o")
        self.workflow = StateGraph(AgentState, input=MessagesState, output=AgentState)

        # Add nodes to the graph
        self.workflow.add_node("document_searcher", self.document_searcher_node)
        #self.workflow.add_node("pdf_to_text", self.pdf_to_text_node)
        #self.workflow.add_node("summary", self.summary_node.run)
        self.workflow.add_node("answer", self.answer_node)

        # Add edges to the graph
        self.workflow.add_edge(START, "document_searcher")
        self.workflow.add_edge("document_searcher", "answer")
        #self.workflow.add_edge("document_searcher", "pdf_to_text")
        #self.workflow.add_edge("pdf_to_text", "summary")
        #self.workflow.add_edge("summary", "answer")
        self.workflow.add_edge("answer", END)

        self.memory = None
        if is_memory:
            from langgraph.checkpoint.memory import MemorySaver
            self.memory = MemorySaver()
            self.graph = self.workflow.compile(checkpointer=self.memory)
        else:
            self.graph = self.workflow.compile()
    
    def DocumentSearcherNode(self, state: AgentState) -> AgentState:
        
        response = {}
        data_files = os.listdir('./data')
        pdf_files = [f for f in data_files if f.endswith('.pdf')]
    
        system_prompt = (
            f"Files in our databases are whitepapers of Web3 projects: {pdf_files}, "
            "user's questions are expected to be mostly about the projects. "
            "list all relevant documents to the projects mentioned in the user's question. "
            "Even if only one relevant document is found, return that document name. "
            "Return only the file name e.g. file_name.pdf"
            "Return 'None' if no documents are relevant."
        )
        messages = [
            {"role": "system", 
             "content": system_prompt},
        ] 
        messages += state["messages"]
        document_list = self.llm.invoke(messages)
        document_list = document_list.content

        if document_list == 'None':
            document_list = []
        else:
            document_list = [x.strip().replace("''", "") for x in document_list.split(',')]

        #PDFToTextNode
        pdf_list = []
        for pdf_path in document_list:
            try:
                loader = PyPDFLoader(f'./data/{pdf_path}')
                pages = loader.load()
                full_content = "\n".join(page.page_content for page in pages)
            except:
                full_content = ""
            pdf_list.append(full_content)

        #SummaryNode
        summarize_messages = []
        for content in pdf_list:
            prompt = (
                f"Summarize the following content: {content}\n"
                "Key Points:\n"
                "- What the project is doing up to 3 sentences\n"
                "- What the project is trying to build to achieve up to 3 sentences"
            )
            summarize_messages.append(prompt)
        document_list = self.llm.batch(summarize_messages)

        return {'documents': document_list}
    
    def AnswerNode(self, state: AgentState) -> AgentState:
        print('Answer', state)
        question = state['messages'][0]
        documents = state['documents']

        prompt = f'Answer the following question: {question}\n Using the following documents: {documents}'
        response = self.llm.invoke(prompt)
        return {'messages': [response]}

    def plot(self):
        '''
        A function to plot the graph.
        '''
        from IPython.display import Image, display
        graph = self.graph
        display(Image(graph.get_graph().draw_mermaid_png()))
    
    def compile(self):
        '''
        A function to return the compiled graph.
        '''
        graph = self.graph
        return graph

    def run(self, prompt = None):
        '''
        A function to invoke the graph. Required for every graph.
        '''
        response = self.graph.invoke({"messages": [("user", prompt)]})
        return response
    
    def stream(self, prompt = 'Hello World'):
        '''
        A function to stream the graph. Mainly required for the main graph.
        '''
        graph = self.graph
        config = {}
        if self.memory:
            config["configurable"] = {"thread_id": "1"}
        
        response = []
        for s in graph.stream({"messages": [("user", prompt)]}, config):
            print(s)
            print("---")
            response.append(s)
            
        return response
