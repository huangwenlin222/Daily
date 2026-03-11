# 测试调用千问模型qwen3.5-plus，进行问答
import os
from openai import OpenAI
from dotenv import load_dotenv

# 加载 .env 文件中的环境变量
load_dotenv()

client = OpenAI(
    # 若没有配置环境变量，请用百炼API Key将下行替换为：api_key="sk-xxx"
    api_key=os.getenv("DASHSCOPE_API_KEY"),
    base_url="https://dashscope.aliyuncs.com/api/v2/apps/protocols/compatible-mode/v1",
)

# 法一
# response = client.responses.create(
#     model="qwen3.5-plus",
#     input="你能做些什么？"
# )

# 法二
text="你能做些什么？"

response = client.responses.create(
    model="qwen3.5-plus",
    input=text
)

# 获取模型回复
print(response.output_text)
