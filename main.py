from langchain.tools import Tool
from langchain.agents import initialize_agent, AgentType
from langchain.chat_models import ChatOpenAI

from qr_generator import python_agent_executor
from csv_analyzer import csv_agent_executor


def main():
    python_tool = Tool(
        name="PythonAgent",
        func=python_agent_executor.run,
        description="""
            Useful when you need to transform natural language and
            write from it python code and execute the code, returning
            the results of the code execution.
            DO NOT SEND PYTHON CODE TO THIS TOOL
        """,
    )

    csv_tool = Tool(
        name="CSVAgent",
        func=csv_agent_executor.run,
        description="""
            Userful when you need to answer questions over The Office TV serie,
            takes as input the entire question and returns the answer after running
            pandas calculations
        """,
    )

    grand_agent = initialize_agent(
        tools=[python_tool, csv_tool],
        llm=ChatOpenAI(temperature=0, model="gpt-4"),
        agent_type=AgentType.OPENAI_FUNCTIONS,
        verbose=True,
    )
    
    prompt = """
        Generate and save in current working directory 15 QRcodes that point to www.orla.dev
        All modules are already installed. Please save the qrcodes within 'qr_folder' folder
    """

    grand_agent.run(prompt)

if __name__ == "__main__":
    main()
