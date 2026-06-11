class Reasoner:
    def system_prompt(self, session_id: str) -> str:
        return (
            "You are DANG-AI-AGENT, a premium Thai/English mobile AI assistant. "
            f"Session: {session_id}. Be concise, useful, and privacy aware."
        )
