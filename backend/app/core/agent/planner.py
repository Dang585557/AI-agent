class Planner:
    def plan(self, user_message: str) -> list[str]:
        text = user_message.lower()
        if "image" in text or "ภาพ" in text:
            return ["understand_visual_request", "generate_image", "store_result"]
        if "remember" in text or "จำ" in text:
            return ["extract_memory", "save_memory", "respond"]
        return ["understand_request", "reason", "respond"]
