from app.SQLAgent import SQLAgent

agent = SQLAgent()
response = agent.execute("select * from transactions")
print(str(response))