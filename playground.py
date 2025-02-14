from agno.agent import Agent
from agno.models.groq import Groq
from agno.tools.yfinance import YFinanceTools
from agno.tools.duckduckgo import DuckDuckGoTools
from dotenv import load_dotenv
from agno.playground import Playground, serve_playground_app
import os
import agno.api

agno.api=os.getenv("AGNO_API_KEY")

web_search_agent=Agent(
    name="Web Search Agent",
    role="Search the web for the information",
    model=Groq(id="llama-3.3-70b-versatile"),
    tools=[DuckDuckGoTools()],
    instructions=["Always include sources"],
    show_tool_calls=True,
    markdown=True
)

## Financial Agent
finance_agent=Agent(
    name="Finance AI Agent",
    model=Groq(id="llama-3.3-70b-versatile"),
    tools=[
        YFinanceTools(stock_price=True, 
                      analyst_recommendations=True, 
                      stock_fundamentals=True, 
                      company_news=True)
        ],
    instructions=["Use table to display the data"],
    show_tool_calls=True,
    markdown=True
)

app=Playground(agents=[finance_agent, web_search_agent]).get_app()

if __name__=="__main__":
    serve_playground_app("playground:app", reload=True)