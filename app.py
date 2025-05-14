from app.SQLAgent import SQLAgent

agent = SQLAgent()
agent.execute("select * from transactions limit 10")