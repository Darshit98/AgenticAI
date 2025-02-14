import typer
from typing import Optional,List
from agno.assistant import Assistant
from phi.assistant import Assistant
from agno.storage.agent.postgres import PostgresAgentStorage
from agno.knowledge.pdf import PDFKnowledgeBase, PDFReader
from agno.vectordb.pgvector import PgVector

import os
from dotenv import load_dotenv
load_dotenv()

os.environ["GROQ_API_KEY"]=os.getenv("GROQ_API_KEY")