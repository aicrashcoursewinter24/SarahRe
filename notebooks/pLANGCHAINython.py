import os
from langchain.agents import AgentExecutor, AgentType, load_tools, initialize_agent
from langchain_community.chat_models import ChatAnyscale
from langchain.tools import AIPluginTool


# Set AnyScale API Key directly in the script
os.environ["ANYSCALE_API_KEY"] = "esecret_5ksmjdxmfj4kr9jj


def build_simple_agent():
    llm = ChatAnyscale(
        anyscale_api_base="https://api.endpoints.anyscale.com/v1",
        anyscale_api_key=os.getenv("ANYSCALE_API_KEY"),
        model_name="mistralai/Mixtral-8x7B-Instruct-v0.1",
        temperature=0.7,
        verbose=True
    )
    tool = AIPluginTool.from_plugin_url("https://www.klarna.com/.well-known/ai-plugin.json")
    tools = load_tools(tool_names={"llm-math": None, "ddg-search": None}, llm=llm)
    agent = initialize_agent(tools, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True)
    print(agent.agent.llm_chain.prompt.template)
    return agent

def chat_with_agent(agent: AgentExecutor, user_input: str):
    output = agent.invoke({"input": user_input})
    return output


llm = ChatOpenAI(temperature=0)
tools = load_tools(["requests_all"])
tools += [tool]

agent_chain = initialize_agent(
    tools, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True
)
agent_chain.run("what t shirts are available in klarna?")


# Import your script functions
#from your_script_name import build_simple_agent, chat_with_agent

# Build the agent
agent = build_simple_agent()

# Chat with the agent
user_input = "remember my name ok, its sara"
response = chat_with_agent(agent, user_input)

# Print the response
print(response)
