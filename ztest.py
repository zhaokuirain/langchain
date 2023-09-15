from langchain.utilities import SQLDatabase
from langchain.llms import OpenAI,ChatGLM
from langchain_experimental.sql import SQLDatabaseChain
import os
os.environ["OPENAI_API_KEY"] = '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'
# os.environ['HTTPS_PROXY'] = 'http://127.0.0.1:7890'

db = SQLDatabase.from_uri("sqlite:///Chinook.db")
llm = OpenAI(temperature=0,verbose=True,openai_proxy='http://127.0.0.1:7890')
# llm = ChatGLM(temperature=0,verbose=True)
db_chain = SQLDatabaseChain.from_llm(llm, db, verbose=True)

db_chain.run("How many employees are there?")