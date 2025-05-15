import logging
from app.connection import Connection
from langchain_openai import ChatOpenAI
from langchain_community.utilities import SQLDatabase
from langchain_community.agent_toolkits import SQLDatabaseToolkit
from langchain.agents import create_sql_agent, AgentType
from app.configuration import config
conn = Connection()


def get_sql_database():
    """Wrap SQLAlchemy engine in LangChain's SQLDatabase."""
    try:
        db = SQLDatabase(conn.engine)
        logging.info("LangChain SQLDatabase initialized!")
        return db
    except Exception as e:
        logging.error(f"Failed to initialize SQLDatabase: {e}")
        return None


def initialize_llm():
    """Set up OpenAI LLM with API key."""
    try:
        llm = ChatOpenAI(
            model="gpt-4o-mini",  # Cost-effective model; adjust as needed
            api_key=config.API_KEY,
            temperature=0,  # Deterministic output for SQL generation
        )
        logging.info("OpenAI LLM initialized!")
        return llm
    except Exception as e:
        logging.error(f"Failed to initialize LLM: {e}")
        return None


class SQLAgent:
    """Build SQL agent with LangChain toolkit."""

    _agent = None

    def __init__(self):
        super().__init__()
        try:
            db = get_sql_database()
            llm = initialize_llm()
            toolkit = SQLDatabaseToolkit(db=db, llm=llm)
            self._agent = create_sql_agent(
                llm=llm,
                toolkit=toolkit,
                # React-based reasoning
                agent_type=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
                verbose=True,  # Show intermediate steps
            )
            logging.info("SQL Agent created successfully!")
        except Exception as e:
            logging.error(f"Failed to create agent: {e}")

    def execute(self, query):
        """Execute natural language query and return formatted response."""
        try:
            response = self._agent.run(query)
            # TODO: Format raw SQL output into natural language

            if "No results found" in response:
                return f"Sorry, I couldn’t find any data for: '{query}'."
            else:
                return f"Here’s what I found for '{query}':\n{response}"
        except Exception as e:
            return f"Error processing query '{query}': {e}"
