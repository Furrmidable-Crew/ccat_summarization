from pydantic import BaseModel
from cat.mad_hatter.decorators import hook


class MySettings(BaseModel):
    summarization_prompt: str = """Write a concise summary of the following:"""
    group_size: int = 5


@hook
def plugin_settings_schema():
    return MySettings.schema()
