## Project Overview

The YouTube Thumbnail Generator is a web application that allows content creators to automatically generate eye-catching thumbnails for their YouTube videos. Users input a video script and theme, and the application uses AI to generate a relevant image and title. The generated thumbnail can be customized with text overlay and downloaded for immediate use.

## Table of Contents

- [Features](#features)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Usage](#usage)
- [API Key Setup](#api-key-setup)
- [Compilation and Execution Instructions](#compilation-and-execution-instructions)

## Features

- Generate thumbnails using Stable Diffusion API
- Input video script and theme for personalized thumbnails
- Download generated thumbnails
- Responsive web design for desktop and mobile

## Technologies Used

- **Backend**: Python 3.8+, Flask
- **Frontend**: HTML, CSS (Tailwind CSS), JavaScript
- **Image Generation**: Stable Diffusion API
- **Image Processing**: Pillow (PIL)
- **HTTP Requests**: Requests library

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/gelantu/YoutubeThumbnailGenerator.git
   python3 -m venv venv
  Create a virtual environment (optional but recommended):
  bash
  python3 -m venv venv
  source venv/bin/activate  # On Windows, use: venv\Scripts\activate
  
  Install the required dependencies:
  bash
  pip install -r requirements.txt

  Create a folder called "templates" and pull index.html in that file. 

## Usage

  Set your Stable Diffusion API key as an environment variable:
  bash
  export STABILITY_KEY=your_api_key_here 
  On Windows use: set STABILITY_KEY=your_api_key_here
  
  Run the Flask application:
  bash
  python app.py
  
  Open a web browser and navigate to http://127.0.0.1:8080.
  Input your video script and theme, then click "Generate" to create your thumbnail.

## API Key Setup
  To use this application, you need an API key from the Stable Diffusion service:
  Sign up at the Stable Diffusion website.
  Obtain your API key.
  Set the API key as an environment variable as described above.

## Compilation and Execution Instructions

Prerequisites
Operating System: Ubuntu 20.04 LTS (or any modern Linux distribution)
Python Version: 3.8 or higher
pip (Python package installer)
Step 1: Clone the Repository
bash
git clone https://github.com/gelantu/youtubethumbnailgenerator.git
cd youtubethumbnailgenerator

Step 2: Set Up a Virtual Environment (Optional but Recommended)
bash
python3 -m venv venv
source venv/bin/activate  # On Windows, use: venv\Scripts\activate

Step 3: Install Dependencies
bash
pip install -r requirements.txt

Step 4: Set Up API Key
Set your Stable Diffusion API key as an environment variable:
bash
export STABILITY_KEY=your_api_key_here  # On Windows, use: set STABILITY_KEY=your_api_key_here

Step 5: Run the Application
bash
python app.py

The application will start running on http://127.0.0.1:8080. Open this URL in your web browser to use the YouTube Thumbnail Generator.
Troubleshooting
If you encounter any issues:
Ensure all dependencies are correctly installed.
Verify that your Stable Diffusion API key is valid and correctly set.
Check the console output for any error messages.
