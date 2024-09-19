# YouTube Video Summarizer 🎥📄

## Overview

**YouTube Subtitle Summarizer** is a user-friendly web application designed to extract subtitles from YouTube videos and generate concise summaries of their content. By leveraging the Google Gemini AI model, this tool provides a comprehensive overview of video content, enabling users to quickly grasp key points without having to watch the entire video.

## Features

- **Subtitle Extraction**: Automatically fetch subtitles from YouTube videos based on the provided URL.
- **AI-Powered Summarization**: Utilize the Google Gemini AI model to generate detailed summaries of video content, highlighting main arguments, themes, and critical information.
- **Language Detection**: Identify and display the language of the extracted subtitles.
- **User-Friendly Interface**: A clean and intuitive interface built with Streamlit, allowing easy input of video URLs and display of summaries.
- **Expandable Full Caption**: View the full transcript of the video in an expandable section for more detailed review.

## How It Works

1. **Input YouTube URL**: Enter the URL of the YouTube video from which you want to extract subtitles.
2. **Fetch Subtitles**: The application retrieves the first available subtitle track for the video.
3. **Generate Summary**: The extracted subtitle text is processed by the Google Gemini AI model to produce a detailed summary.
4. **View Results**: The summary and full transcript are displayed, along with information about the subtitle's language.

## Technologies Used

- **Streamlit**: For building the interactive web application.
- **YouTube Transcript API**: For fetching subtitles from YouTube videos.
- **Google Generative AI (Gemini)**: For generating detailed summaries of subtitle text.

## Getting Started

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/your-username/youtube-subtitle-summarizer.git
    ```

2. **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

3. **Run the Application**:
    ```bash
    streamlit run app.py
    ```

4. **Configure API Key**: Replace `'YOUR_API_KEY_HERE'` in `app.py` with your actual Google Gemini API key.

## Usage

- **Enter a YouTube Video URL**: Paste the URL of the video in the provided input field.
- **Click "Get Summary"**: Fetch subtitles and generate a summary.
- **View Summary**: Read the AI-generated summary and expand to view the full subtitle text.

## Contributing

Contributions are welcome! If you have ideas for improving the application or find any issues, please feel free to fork the repository and submit a pull request. Ensure that your code adheres to the project's coding standards and includes appropriate tests.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Contact

For any questions or support, please reach out to https://www,shivanshjasathi.co or open an issue on the GitHub repository.
