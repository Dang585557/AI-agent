from .executor import Executor
from .planner import Planner
from .reasoner import Reasoner


class AgentOrchestrator:
    def __init__(self) -> None:
        self.planner = Planner()
        self.reasoner = Reasoner()
        self.executor = Executor()

    async def respond(self, message: str, session_id: str) -> str:
        plan = self.planner.plan(message)
        prompt = self.reasoner.system_prompt(session_id)
        return await self.executor.execute(prompt, message, plan)
