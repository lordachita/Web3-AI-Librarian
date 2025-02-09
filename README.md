# Web3 AI Librarian

## Introduction

Imagine being a Key Opinion Leader (KOL) in Web3, struggling to keep up with the latest research while your followers expect you to stay ahead of the curve. Falling behind isn’t an option.

This project introduces a Web3 AI librarian, an intelligent assistant designed to track, analyze, and deliver insights on the latest developments in Web3 projects. Using an Agentic workflow, it autonomously searches for relevant information, ensuring you stay informed without the hassle of sifting through endless papers.

## Overview
### Tech Stack:
- OpenAI
- LangGraph
- LangSmith


### How it works:
Our AI uses the user's question to select relevant files from the database, retrieves the necessary information, and utilizes an LLM to summarize it. This ensures the context is concise and directly relevant to the user's query.


### Using our project:
- Upload your PDF files to the `data` folder, now limited to whitepapers only.
- Use command langgraph dev to run UI locally (https://langchain-ai.github.io/langgraph/how-tos/local-studio/#install-langgraph-cli)

## Future Work:
- Use Open Source LLM
- Use Nillion for secure database
- Find the way to update the database efficiently
- Add a Chat Interface UI
- Optimize pdf extraction, incl. summarization

## Acknowledgements:
- [LangSmith](https://smith.langchain.com/) for the AI Agent framework
- [Tavily](https://tavily.com/) inspired us the AI Agent coding structure
