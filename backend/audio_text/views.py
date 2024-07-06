from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from decouple import config
import os
import openai

# Utility functions created for this view
from utils.transcription import transcribe_audio
from utils.download import download_audio_from_youtube
from utils.summarization import summarize_text

# Set OpenAI API key
openai.api_key = config("OPENAI_API_KEY")

class SummarizeAudioView(APIView):
    def post(self, request):
        """
        Handles POST request to transcribe and summarize audio from a YouTube video.

        Args:
            request (Request): The request object containing the YouTube URL.
            
        Returns:
            Response: A response object containing the summary of the transcribed audio.
        """
        # Extract the URL from the request data
        url = request.data.get("url")
        
        if not url:
            return Response({"error": "URL is required"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            # Download audio from YouTube
            output_file_path = download_audio_from_youtube(url)
            
            # Transcribe the audio using OpenAI Whisper
            transcription = transcribe_audio(output_file_path)
            
            # Summarize the transcription
            summary = summarize_text(transcription)
            
            # Clean up the downloaded audio file
            os.remove(output_file_path)
            
            # Return the summary
            return Response({"summary": summary}, status=status.HTTP_200_OK)
        
        except openai.error.OpenAIError as oe:
            # Handle OpenAI API specific errors
            return Response({"error": str(oe)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        except Exception as e:
            # Handle any other errors
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
