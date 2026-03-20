import requests

# 完全用你提供的信息，不用改
API_KEY = "sk-gTRic3X8YVIEvR4L4e678d6665274c4dAeF6E499E5469679"
BASE_URL = "https://aihubmix.com/v1"
MODEL_NAME = "gemini-3.1-flash-image-preview-free"

# 构造标准OpenAI格式请求
headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}
data = {
    "model": MODEL_NAME,
    "messages": [{"role": "user", "content": "你好，测试API是否正常"}],
    "temperature": 0.3,
    "stream": False
}

# 执行测试
try:
    response = requests.post(
        f"{BASE_URL}/chat/completions",
        headers=headers,
        json=data,
        timeout=30
    )
    print(f"✅ 状态码：{response.status_code}")
    print(f"✅ 返回内容：{response.json()}")
except Exception as e:
    print(f"❌ 连接失败，完整错误：{str(e)}")
