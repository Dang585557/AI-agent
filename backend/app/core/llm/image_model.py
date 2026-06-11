import httpx

from ...config import get_settings


class ImageModel:
    async def generate(self, prompt: str, size: str) -> str:
        settings = get_settings()
        if not settings.openai_api_key:
            safe = prompt.lower().replace(" ", "-")[:48] or "image"
            return f"https://images.local/{safe}-{size}.png"
        async with httpx.AsyncClient(timeout=90) as client:
            response = await client.post(
                "https://api.openai.com/v1/images/generations",
                headers={"Authorization": f"Bearer {settings.openai_api_key}"},
                json={"model": settings.image_model, "prompt": prompt, "size": size},
            )
            response.raise_for_status()
            return response.json()["data"][0].get("url", "")
