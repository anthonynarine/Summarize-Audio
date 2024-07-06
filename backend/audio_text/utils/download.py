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

def audio_upload_path(video_id, filename):
    """
    Determines the upload path for downloaded audio files.

    Args:
        video_id (str): The video ID of the YouTube video.
        filename (str): The original name of the file that was downloaded.

    Returns:
        str: The upload path for the file.
    """
    sanitized_filename = sanitize_filename(filename)
    return os.path.join("media", video_id, sanitized_filename)

def download_audio_from_youtube(url):
    """
    Downloads audio from a YouTube video and saves it to the specified media directory.

    Args:
        url (str): The URL of the YouTube video.

    Returns:
        str: The path to the saved audio file.

    Raises:
        Exception: If there is an error in the downloading process.
    """
    try:
        # Download audio from YouTube
        yt = YouTube(url)
        audio = yt.streams.filter(only_audio=True).first()

        # Sanitize the filename
        sanitized_filename = sanitize_filename(f"{yt.video_id}.mp4")

        # Use audio_upload_path to determine the final path
        output_file_path = audio_upload_path(yt.video_id, sanitized_filename)

        # Create subdirectory if it doesn't exist
        os.makedirs(os.path.dirname(output_file_path), exist_ok=True)

        # Download the audio file to the media directory with the sanitized filename
        audio.download(output_path=os.path.dirname(output_file_path), filename=sanitized_filename)

        return output_file_path
    except Exception as e:
        raise Exception(f"Error downloading audio: {e}")
