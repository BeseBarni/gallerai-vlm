import api_utils
import api_consts
from google import genai
from google.genai import types


def process_image(id, image_path, score, genres):
    """
    Analyzes a single image using the Gemini API

    Reutnrs:
        dict: A dictionary containing the analysis results, or None on error.

    """

    api_key = api_utils.get_gemini_key()

    client = genai.Client(api_key=api_key)

    system_prompt = (
        "You are an expert photography mentor. Your task is to analyze an image based on its "
        "aesthetic score and existing categories. Provide a professional feedback that explains"
        "the score and helps the user learn, expands the list of genres, and describes the colors and emotions conveyed."
    )
    user_prompt = (
        f"Aesthetic Score: {score}\n"
        f"Current Genres: {genres}\n\n"
        "Please provide a detailed analysis of this image in JSON format with the following keys:\n"
        "- 'feedback': A feedback based on the contents and techniques used in the photo and the overall aesthetic quality.\n"
        "- 'extended_genres': A comma-seperated list of additional relevant photography genres.\n"
        "- 'colors': A comma-seperated list of the dominant colors in the image.\n"
        "- 'emotions': A comma-seperated list of emotions the image evokes."
    )
    image_file = client.files.upload(file=image_path)

    config = types.GenerateContentConfig(system_instruction=system_prompt)

    response = client.models.generate_content(
        model=api_consts.GEMINI_MODEL, config=config, contents=[image_file, user_prompt]
    )
