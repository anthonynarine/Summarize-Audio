import os
import re
from pytube import YouTube

def sanitize_filename(filename):
    """
    Sanitizes the filename by replacing spaces with underscores and removing special characters.

    Args:
        filename (str): The original filename.

    Returns:
        str: The sanitized filename.
    """
    # Replace spaces with underscores
    filename = filename.replace(" ", "_")
    # Remove any characters that are not alphanumeric, underscores, hyphens, or dots
    filename = re.sub(r'[^a-zA-Z0-9._-]', '', filename)
    return filename

def download_audio_from_youtube(url, media_dir):
    """
    Downloads audio from a YouTube video and saves it to the specified media directory.

    Args:
        url (str): The URL of the YouTube video.
        media_dir (str): The directory where the audio file will be saved.

    Returns:
        str: The path to the saved audio file.

    Raises:
        Exception: If there is an error in the downloading process.
    """
    try:
        # Ensure the media directory exists
        if not os.path.exists(media_dir):
            os.makedirs(media_dir)
        
        # Download audio from YouTube
        yt = YouTube(url)
        audio = yt.streams.filter(only_audio=True).first()
        
        # Sanitize the filename
        sanitized_filename = sanitize_filename(f"{yt.video_id}.mp4")
        
        # Define the output file path using the sanitized filename
        output_file_path = os.path.join(media_dir, sanitized_filename)
        
        # Download the audio file to the media directory with the sanitized filename
        audio.download(output_path=media_dir, filename=sanitized_filename)
        
        return output_file_path
    except Exception as e:
        raise Exception(f"Error downloading audio: {e}")
