import httpx

from ...config import get_settings


class TextModel:
    async def complete(self, system_prompt: str, user_message: str, plan: list[str]) -> str:
        settings = get_settings()
        if not settings.openai_api_key:
            return f"Local DANG response: {user_message}. Plan: {', '.join(plan)}."
        async with httpx.AsyncClient(timeout=45) as client:
            response = await client.post(
                "https://api.openai.com/v1/responses",
                headers={"Authorization": f"Bearer {settings.openai_api_key}"},
                json={"model": settings.text_model, "input": [{"role": "system", "content": system_prompt}, {"role": "user", "content": user_message}]},
            )
            response.raise_for_status()
            data = response.json()
            return data.get("output_text") or "I completed the request."
