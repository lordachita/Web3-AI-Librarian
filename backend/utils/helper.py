import os
import yaml

def load_env():
    with open("./config/configs.yaml", "r") as f:
        configs = yaml.safe_load(f)

    os.environ["OPENAI_API_KEY"] = configs["OPENAI_API_KEY"]

    os.environ["LANGSMITH_TRACING"] = configs["LANGSMITH_TRACING"]
    os.environ["LANGSMITH_ENDPOINT"]= configs["LANGSMITH_ENDPOINT"]
    os.environ["LANGSMITH_API_KEY"] = configs["LANGSMITH_API_KEY"]
    os.environ["LANGSMITH_PROJECT"] = configs["LANGSMITH_PROJECT"]