from langchain.utilities import SQLDatabase
from langchain.llms import OpenAI,ChatGLM
from langchain_experimental.sql import SQLDatabaseChain

# os.environ['HTTPS_PROXY'] = 'http://127.0.0.1:7890'
from environs import Env
env = Env()
env.read_env()
import os
os.environ["OPENAI_API_KEY"] = env.str("OPENAI_API_KEY")


db = SQLDatabase.from_uri("sqlite:///Chinook.db")
llm = OpenAI(temperature=0,verbose=True,openai_proxy='http://127.0.0.1:7890')
# llm = ChatGLM(temperature=0,verbose=True)
db_chain = SQLDatabaseChain.from_llm(llm, db, verbose=True)

db_chain.run("How many employees are there?")