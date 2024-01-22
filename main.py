import os
from dotenv import load_dotenv

load_dotenv()
name = os.getenv("DEVELOPER_NAME")
print(f"Hi, I am {name}")
