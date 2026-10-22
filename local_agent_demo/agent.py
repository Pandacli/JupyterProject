

from langchain_ollama import ChatOllama
from langgraph.prebuilt import create_react_agent

from utils.agent_tools import tools



#连接本地ollama 大模型服务
#创建一个ChatOllama 对象
#temperature降低随机性，保证工具调用稳定
llm = ChatOllama(model="qwen2.5:1.5b", base_url="http://127.0.0.1:11434", temperature=0.0)


agent = create_react_agent(llm, tools=tools)

#main测试
if __name__ == '__main__':
    while True:
        #获取用户输入的内容
        user_input = input("\n用户：")
        if user_input.lower() in ("quit", "exit"):
            break
        #agent 执行启动
        response = agent.invoke({"messages": [("human", user_input)]})
        for msg in response["messages"]:
            if msg.type == "ai":
                print(f"{msg.type}:{msg.content}")

