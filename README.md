# Web3 AI Librarian

## Introduction

Imagine being a Key Opinion Leader (KOL) in Web3, struggling to keep up with the latest research while your followers expect you to stay ahead of the curve. Falling behind isn’t an option. 
The same challenge applies to end users and builders who need to stay informed in this rapidly evolving space.
This project introduces a Web3 AI librarian, an intelligent assistant designed to track, analyze, and deliver insights on the latest developments in Web3 projects. Using an Agentic workflow, it autonomously searches for relevant information, ensuring you stay informed without the hassle of sifting through endless papers.

## Overview
### Tech Stack:
- OpenAI
- LangGraph
- LangSmith


### How it works:
Our AI uses the user's question to select relevant files from the database, retrieves the necessary information, and utilizes an LLM to summarize it. This ensures the context is concise and directly relevant to the user's query.


### Using our project:
1. Upload your PDF files to the `data` folder (now limited to whitepapers only).
2. Set up configs in `configs`.
3. Use `main.ipynb` to easily interact with our AI.
4. Also, you can use command `langgraph dev` to [run UI interface locally](https://langchain-ai.github.io/langgraph/how-tos/local-studio/#install-langgraph-cli)

## Future Work:
For instance,
1. Add a Chat Interface UI, so that non-builders can easily use our AI.
2. Find the way to update the database efficiently e.g. automatic update the information.
3. Optimize Agentic Workflow, which is already scalable thanks to LangGraph.
4. Use Open Source LLM, after we have addressed most of the issues i.e. input length limitations
5. Use Nillion SDK for building private AI

## Acknowledgements:
- [LangGraph](https://www.langchain.com/langgraph) for the AI Agent framework
- [Tavily](https://tavily.com/) inspired us the AI Agent coding structure
