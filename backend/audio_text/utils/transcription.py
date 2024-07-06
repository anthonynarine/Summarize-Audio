import openai

def transcribe_audio(file_path):
    """
    Transcribes audio from a given file path using OpenAI's Whisper model.

    This function opens the specified audio file in binary mode, sends it to 
    OpenAI's Whisper model for transcription, and returns the transcribed text.

    Args:
        file_path (str): The path to the audio file to be transcribed.

    Returns:
        str: The transcribed text from the audio file.

    Detailed Steps:
    1. Open the audio file in binary mode.
    2. Use OpenAI's Audio API to transcribe the audio file.
    3. Extract and return the transcribed text from the response.

    Example:
        >>> transcribe_audio("path/to/audio/file.mp3")
        "This is a transcribed text from the audio."

    Raises:
        Exception: If there is an error in the transcription process.
    """
    # Step 1: Open the audio file in binary mode for reading
    # The file is opened in binary mode ("rb") because it contains binary data.
    # The `with` statement ensures the file is properly closed after the block is executed.
    with open(file_path, "rb") as audio_file:
        # Step 2: Use OpenAI's Audio API to transcribe the audio file
        # The 'whisper-1' model is used for transcription.
        # The response contains the transcribed text and other metadata.
        response = openai.Audio.transcribe("whisper-1", audio_file)
        
        # Step 3: Extract the transcribed text from the response and return it
        # The transcribed text is accessed using the "text" key in the response dictionary.
        return response["text"]
