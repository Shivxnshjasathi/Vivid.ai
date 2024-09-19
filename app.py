import streamlit as st
from youtube_transcript_api import YouTubeTranscriptApi
from urllib.parse import urlparse, parse_qs
import google.generativeai as genai

# Set up Google Gemini AI with your API key
api_key = 'AIzaSyBGwV0hwIhXw8OdeGBX8PyMbEepxLXeP9k'  # Replace with your actual API key
genai.configure(api_key=api_key)

def get_video_id(url):
    """Extract the video ID from a YouTube URL."""
    parsed_url = urlparse(url)
    if parsed_url.hostname in ('youtu.be', 'www.youtu.be'):
        return parsed_url.path[1:]  # Extract video ID from short URL
    if parsed_url.hostname in ('youtube.com', 'www.youtube.com'):
        if parsed_url.path == '/watch':
            return parse_qs(parsed_url.query).get('v', [None])[0]  # Extract video ID from full URL
    return None

def get_first_available_subtitle(url):
    """Retrieve the first available subtitle for a YouTube video."""
    video_id = get_video_id(url)
    if not video_id:
        return {"error": "Invalid YouTube URL"}
    
    try:
        # Fetch the list of transcripts and select the first one available
        transcript_list = YouTubeTranscriptApi.list_transcripts(video_id)
        first_transcript = next(iter(transcript_list), None)
        
        if not first_transcript:
            return {"error": "No subtitles available for this video."}
        
        language_name = first_transcript.language
        language_code = first_transcript.language_code
        
        # Combine the text from the subtitle entries
        subtitle_text = " ".join([entry['text'] for entry in first_transcript.fetch()])
        
        return {
            "language": f"{language_name} ({language_code})",
            "subtitle": subtitle_text
        }
    except Exception as e:
        return {"error": f"An error occurred while fetching subtitles: {str(e)}"}

def summarize_text(text, max_tokens=1000):
    """Summarize the given text using Google Gemini AI."""
    try:
        model = genai.GenerativeModel('gemini-pro')
        prompt = (
            "Please provide a detailed summary of the key points covered in the following video. "
            "Ensure to capture the main arguments, themes, and any critical information. The summary "
            "should be comprehensive enough for someone who doesn't have time to watch the video, offering "
            "a clear understanding of the content, including any important conclusions or insights.\n\n"
            f"{text}"
        )
        
        response = model.generate_content(prompt, generation_config=genai.types.GenerationConfig(
            max_output_tokens=max_tokens,
        ))
        
        return response.text
    except Exception as e:
        return f"An error occurred during summarization: {str(e)}"

# Streamlit app interface
st.title('YouTube Subtitle Summarizer')
st.markdown(
    """
    This app extracts subtitles from a YouTube video and provides a detailed summary. 
    Just enter the URL of the video, and get a concise overview without having to watch it.
    """
)

# Input for YouTube URL
youtube_url = st.text_input('Enter YouTube video URL:', '')

if st.button('Get Summary'):
    if youtube_url:
        result = get_first_available_subtitle(youtube_url)
        
        if "error" in result:
            st.error(result["error"])
        else:
            st.spinner('Generating summary...')
            summary = summarize_text(result['subtitle'])
            
            if "error" in summary:
                st.error(summary)
            else:
                st.subheader('Summary')
                st.write(summary)
                
                # Show full caption in an expandable section
                with st.expander("View Full Caption"):
                    st.write(result['subtitle'])
                
                # Display language info
                st.write(f"**Language:** {result['language']}")
    else:
        st.error("Please enter a valid YouTube URL.")
