from pydantic import BaseModel
from cat.mad_hatter.decorators import plugin


class MySettings(BaseModel):
    summarization_prompt: str = """Write a concise summary of the following:"""
    group_size: int = 5


@plugin
def settings_schema():
    return MySettings.schema()
