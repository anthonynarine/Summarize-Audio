import openai

def summarize_text(text):
    """
    Summarizes the given text using OpenAI's GPT-3.5-turbo model.

    Args:
        text (str): The text to summarize.

    Returns:
        str: A summary of the text.
    """
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": f"Summarize the following text:\n\n{text}"}
        ],
        max_tokens=150
    )
    summary = response.choices[0].message["content"].strip()
    return summary