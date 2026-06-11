from ..llm.text_model import TextModel


class Executor:
    def __init__(self) -> None:
        self.text_model = TextModel()

    async def execute(self, system_prompt: str, user_message: str, plan: list[str]) -> str:
        return await self.text_model.complete(system_prompt, user_message, plan)
