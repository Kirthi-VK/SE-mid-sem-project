# Multi Agent Research Assistant (Orchestral-AI)

# Overview

This project implements a multi gent AI system using the Orchestral AI framework. The system demonstrates how multiple agents can collaborate to perform a complex task searching and summarizing research papers.

Instead of using a single large language model the system is divided into specialized agents that work together under a coordinator.

# Features

- Multi agent architecture
- Local LLM execution (no API key required)
- Automated research paper suggestion
- Summarization of research topics
- Lightweight and fast execution using small models

# System Architecture

The system consists of three agents:

1. Coordinator Agent
- Controls the workflow
- Passes information between agents

2. Search Agent
- Takes a research topic as input
- Generates relevant research paper titles

3. Summary Agent
- Summarizes the generated papers
- Produces concise bullet points

# Installation

1. Install Orchestral AI
pip install orchestral-ai

2. Install Ollama
Download from: https://ollama.com

3. Pull a lightweight model
ollama pull phi3:mini or ollama pull tinyllama:latest

4. Running the Project
python main.py

Enter a research topic when prompted.
