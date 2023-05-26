import openai


def get_completion(prompt: str, model="gpt-3.5-turbo", temperature=0) -> str:
    """Convenience function to get AI completion for a prompt.

    * Please use good Prompt Engineering practices to ensure the best results.
    * You can use ChatGPT to test your prompts before using them in this function.
    * `temperature` of 0 is deterministic which is great for automated pipelines.

    Args:
        prompt: The prompt to be completed.
        model: The model to use for completion.
        temperature: The degree of randomness of the model's output. 0 = deterministic.

    Returns:
        The AI's completion of the prompt.
    """
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=temperature,
    )
    return response.choices[0].message["content"]
