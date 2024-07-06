from pytube import YouTube
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import os
import re


def transcribe_audio(file_path):
    
class SummarizeAudioView(APIView):
    def post(self, request):
        # Extract the URL from the request data
        url = request.data.get("url")
        
        if not url:
            return Response({"error": "URL is required"}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            #Download audio from youtube
            yt = YouTube(url)
            audio = yt.streams.filter(only_audio=True).first()
            output_file = audio.download()
            
            # Transcribe the audio 
        
        audio = yt.streams.filter(only_audio=True).first()
        output_file = audio.download()
        