
import asyncio
import os

from dotenv import load_dotenv
from ddgs import DDGS

from autogen_agentchat.agents import AssistantAgent
from autogen_agentchat.ui import Console
from autogen_ext.models.openai import OpenAIChatCompletionClient


# 1. Load environment variables
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise ValueError("OPENAI_API_KEY not found in .env file")

# 2. Create DuckDuckGo search tool
def search_weather_news(city: str) -> str:
    """
    Search the web for today's weather news and weather-related updates for the specified city.
    Returns the latest weather news headlines and summaries.
    """
    results = DDGS().news(query=f"{city} weather today",max_results=5)
    return str(results)
# 3. Configure OpenAI model client
model_client = OpenAIChatCompletionClient(model="gpt-4o-mini",api_key=api_key)
# 4. Create AutoGen agent
agent = AssistantAgent(
    name="weather_news",
    model_client=model_client,
    tools=[search_weather_news],
    system_message="""
    You are a Weather News Assistant.

    Find today's weather news for the requested city.Use the search_weather_news tool.
    Summarize the findings in exactly 3 short lines.Focus on weather conditions, alerts and upcoming weather.
    Never invent weather information.
    """,
    reflect_on_tool_use=True
)
# 5. Main execution
async def main():
    city = input("Which city? ")
    try:
        await Console(agent.run_stream(task=f"Find today's weather news for {city}."))
    finally:
        await model_client.close()
asyncio.run(main())
