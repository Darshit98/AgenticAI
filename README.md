# AgenticAI

AgenticAI is a Python-based project that integrates multiple AI agents to perform web searches and financial analysis. The project utilizes the Groq model and various tools to provide users with accurate and up-to-date information.

## Table of Contents
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Agents](#agents)
  - [Web Search Agent](#web-search-agent)
  - [Finance AI Agent](#finance-ai-agent)
  - [Multi AI Agent](#multi-ai-agent)
- [Dependencies](#dependencies)
- [Contributing](#contributing)
- [Contact](#contact)

## Features
- **Web Search**: Retrieve information from the web using DuckDuckGo.
- **Financial Analysis**: Access stock prices, analyst recommendations, and company news using Yahoo Finance tools.
- **Multi-Agent System**: Combine the capabilities of multiple agents for comprehensive responses.
- **Markdown Support**: Output results in markdown format for better readability.

## Installation
To set up the project, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/Darshit98/AgenticAI.git
   cd AgenticAI
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up environment variables:
   - Create a `.env` file in the root directory and add your API keys and other necessary configurations.

## Usage
To run the project, execute the following command in your terminal:
```bash
python financial_agent.py
```


You can modify the parameters in the script to customize the behavior of the agents.

## Agents

### Web Search Agent
The Web Search Agent is designed to search the web for information using DuckDuckGo. It is configured to always include sources in its responses and supports markdown formatting.

### Finance AI Agent
The Finance AI Agent provides financial data, including stock prices, analyst recommendations, and company news. It uses Yahoo Finance tools to gather and display this information in a structured format.

### Multi AI Agent
The Multi AI Agent combines the capabilities of both the Web Search Agent and the Finance AI Agent. It can handle requests that require both web search and financial analysis, providing comprehensive responses.

## Dependencies
The project requires the following Python packages:
- `agno`
- `dotenv`
- `yfinance`
- `duckduckgo`

You can install these dependencies using the `requirements.txt` file provided in the project.

## Contributing
Contributions are welcome! If you would like to contribute to the project, please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/YourFeature`).
3. Make your changes and commit them (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature/YourFeature`).
5. Open a pull request.
