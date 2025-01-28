import openai
import os

# Use the OpenAI API key securely
openai.api_key = os.getenv("OPENAI_API_KEY")

def get_feedback(transcript):
    prompt = f"""
    Act as an IELTS examiner. Evaluate the following response based on these criteria:
    1. Fluency and Coherence
    2. Lexical Resource
    3. Grammatical Range and Accuracy
    4. Pronunciation

    Candidate's response:
    {transcript}

    Provide feedback for each criterion and a final band score.
    """
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content