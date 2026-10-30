# Week5_Day2-AutoGen_Weather _News_Agent


# AutoGen Weather News Agent

## 1. Project Overview

The AutoGen Weather News Agent is a tool-enabled AI assistant built using the AutoGen framework.

Unlike a basic conversational agent, this agent can use an external Python function (tool) to search the web for the latest weather-related news for a user-provided city.

It uses DuckDuckGo search through the `ddgs` Python package, which does not require a search API key.

The agent retrieves search results, interprets the information, and generates a concise response in exactly three short lines.

## 2. Objectives

- Build an AI agent using AutoGen.
- Understand how Python functions can be registered as agent tools.
- Use DuckDuckGo for web-based weather news searches.
- Understand tool calling and reflection in AutoGen.
- Generate concise responses from external search results.
- Securely manage API keys using environment variables.

## 3. Technology Stack

| Technology | Purpose |
|---|---|
| Python | Programming language |
| AutoGen AgentChat | Agent framework |
| OpenAI GPT-4o-mini | Language model |
| DuckDuckGo (ddgs) | Web news search |
| python-dotenv | Environment variable management |
| asyncio | Asynchronous execution |

## 4. Project Structure

```text
AutoGen_Weather_News/
│
├── venv/
│
├── weather_news.py
│
├── .env
│
├── requirements.txt
│
└── README.md
```

## 5. How It Works

The application follows this workflow:

1. User enters a city name.
2. The AutoGen agent receives the request.
3. The agent identifies the need for external weather news.
4. The agent calls the registered Python search function.
5. DuckDuckGo retrieves relevant weather news.
6. Search results are passed back to the agent.
7. The agent reflects on the tool output and summarizes the findings.
8. The final response is generated in exactly three short lines.

## 6. Installation and Setup

### Step 1: Create a Virtual Environment

```bash
python -m venv venv
```

### Step 2: Activate the Environment

Windows PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

Alternatively, install directly:

```bash
pip install -U autogen-agentchat "autogen-ext[openai]" ddgs python-dotenv
```

## 7. Environment Configuration

Create a `.env` file in the project root directory.

Add your OpenAI API key:

```env
OPENAI_API_KEY=your_openai_api_key
```

**Important:**
- Never hardcode API keys in Python files.
- Do not upload `.env` to GitHub.
- Add `.env` to `.gitignore`.

Example `.gitignore`:

```text
.env
venv/
__pycache__/
*.pyc
```

## 8. Application Execution

Run the application:

```bash
python weather_news.py
```

The application prompts the user:

```text
Which city?
```

Enter a city name:

```text
Chennai
```

The agent then searches for today's weather news and generates a three-line summary.

## 9. Important AutoGen Concepts

### A. Python Function as a Tool

```python
def search_weather_news(city: str) -> str:
    """
    Search today's weather news for the specified city.
    """
```

In AutoGen, a Python function can be exposed as a tool.

The agent uses the following information to understand the tool:

- Function name
- Parameter names
- Type hints
- Return type
- Docstring

A clear docstring helps the agent decide when to use the function.

### B. Registering Tools

```python
tools=[search_weather_news]
```

This registers the Python function with the AssistantAgent.

The agent can now invoke the function when required.

### C. DuckDuckGo Search

```python
results = DDGS().news(
    query=f"{city} weather today",
    max_results=5
)
```

This searches for up to five relevant news results.

The `ddgs` package does not require a separate search API key.

### D. Reflection on Tool Use

```python
reflect_on_tool_use=True
```

This enables the agent to generate a response based on the tool execution results.

Instead of simply returning raw search output, the agent interprets and summarizes the retrieved information.

### E. Asynchronous Execution

```python
async def main():
    await Console(agent.run_stream(task="..."))
```

AutoGen supports asynchronous agent execution.

The `await` keyword allows the application to wait for the agent's response.

### F. Closing the Model Client

```python
await model_client.close()
```

Closes the OpenAI model client after execution and releases associated resources.

## 10. Expected Output

Example:

```text
Which city? Chennai

---------- ToolCallRequestEvent ----------
search_weather_news(city='Chennai')

---------- TextMessage ----------
Weather conditions: [Latest reported conditions].
Weather alerts: [Relevant warnings, if any].
Forecast: [Upcoming weather outlook].
```

Note: The actual response depends on the search results available at execution time.

The three-line requirement applies to the final weather summary, not the AutoGen execution logs.

## 11. Key Learning Outcomes

After completing this assignment, we understand:

1. How to create an AutoGen AssistantAgent.
2. How to convert an ordinary Python function into an AI agent tool.
3. How function descriptions and type hints guide tool selection.
4. How to integrate DuckDuckGo search into an AI agent.
5. How `reflect_on_tool_use` improves the final response.
6. How to use asynchronous execution in AutoGen.
7. How to manage API keys securely using `.env`.

## 12. Future Enhancements

Possible improvements:

- Add current weather information using a weather API.
- Support multiple cities in one request.
- Add temperature, humidity and wind information.
- Display weather news sources and URLs.
- Build a Streamlit-based user interface.
- Add multiple tools for weather, news and alerts.

---

## Conclusion

This project demonstrates how an AutoGen agent can move beyond simple conversations and interact with external tools.

By integrating DuckDuckGo search with a Python function, the agent can retrieve external information, interpret the results, and generate a meaningful response.

**Core Concept: An AI agent becomes more useful when it can decide when and how to use external tools.**
