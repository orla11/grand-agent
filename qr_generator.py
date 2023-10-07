from langchain.agents.agent_toolkits import create_python_agent
from langchain.chat_models import ChatOpenAI
from langchain.tools import PythonREPLTool
from langchain.agents import AgentType


python_agent_executor = create_python_agent(
    llm=ChatOpenAI(temperature=0, model="gpt-4"),
    tool=PythonREPLTool(),
    agent_type=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True,
    handle_parsing_errors=True
)

# prompt = """
#     Generate and save in current working directory 15 QRcodes that point to www.orla.dev
#     All modules are already installed. Please save the qrcodes within 'qr_folder' folder
# """
# python_agent_executor.run(prompt)
