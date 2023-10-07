from langchain.chat_models import ChatOpenAI
from langchain.agents import AgentType, create_csv_agent

csv_agent_executor = create_csv_agent(
    llm=ChatOpenAI(temperature=0, model="gpt-4"),
    path="the_office_series.csv",
    verbose=True,
    agent_type=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
)

# prompt = """
#     Provide 3 relevat insights about this TV serie and then decide on which
#     is the funniest episode of them all.
# """

# csv_agent_executor.run(prompt)
