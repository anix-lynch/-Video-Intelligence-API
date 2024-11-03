# -Video-Intelligence-API
# README: Google Cloud Video Intelligence API Tutorial

## Table of Contents
- [Project Overview](#project-overview)
- [Initial Setup](#initial-setup)
  - [Step 1: Google Cloud Project Setup](#step-1-google-cloud-project-setup)
  - [Step 2: Enable the API](#step-2-enable-the-api)
  - [Step 3: Create a Service Account](#step-3-create-a-service-account)
  - [Step 4: Install Python Packages](#step-4-install-python-packages)
- [Python Examples](#python-examples)
  - [Face Detection](#face-detection)
  - [People Detection](#people-detection)
  - [Logo Detection](#logo-detection)
  - [Text Detection](#text-detection)
  - [Speech Transcription](#speech-transcription)
- [Conclusion](#conclusion)

## Project Overview
Google Cloud Video Intelligence API is a powerful tool for analyzing video content and extracting rich metadata. This tutorial covers how to use Python to interact with the API for various video analysis tasks such as detecting faces, people, logos, text, and performing speech transcription.

## Initial Setup
### Step 1: Google Cloud Project Setup
- Go to [Google Cloud Console](https://console.cloud.google.com/).
- Create a new project by clicking the project dropdown and selecting **New Project**.
- Name your project and click **Create**.

### Step 2: Enable the API
- In the **Navigation Menu**, go to **APIs & Services** > **Library**.
- Search for **Cloud Video Intelligence API** and enable it.

### Step 3: Create a Service Account
- Go to **APIs & Services** > **Credentials**.
- Click **Create Credentials** and select **Service Account**.
- Provide a name and assign a role under **Vision AI** with the least permissions needed.
- Once created, click on the service account, navigate to **Keys**, and select **Add Key** > **Create New Key** (choose JSON format).
- Save the key file in your project folder.

### Step 4: Install Python Packages
Run the following commands in your terminal:
```bash
pip install google-cloud-video-intelligence python-dotenv
```

## Python Examples

### Face Detection
**Purpose**: Detect faces in a video and analyze attributes like bounding boxes and likelihood of facial expressions.

**Steps**:
1. Import necessary libraries and load the video content.
2. Create a function to configure face detection.
3. Use the `annotate_video` method to process the video.
4. Print the results with a function that iterates over the detected face annotations.

### People Detection
**Purpose**: Identify individuals in the video, even when faces are not visible.

**Steps**:
1. Import the libraries and create a function to configure people detection.
2. Set up the process similar to face detection but with the `PERSON_DETECTION` feature.
3. Print detected individuals with relevant attributes and time segments.

### Logo Detection
**Purpose**: Detect logos within the video content.

**Steps**:
1. Use the `LOGO_RECOGNITION` feature in the `annotate_video` method.
2. Print the results, including the entity ID, description (logo name), and time segments.

### Text Detection
**Purpose**: Extract text from videos, useful for analyzing video frames with embedded text.

**Steps**:
1. Import the necessary libraries.
2. Configure the `TEXT_DETECTION` feature.
3. Print the detected text, time segments, and confidence scores.

### Speech Transcription
**Purpose**: Convert spoken language in video content into text.

**Steps**:
1. Import libraries and create a function to configure speech transcription.
2. Use the `annotate_video` method with the `SPEECH_TRANSCRIPTION` feature.
3. Print the transcription, confidence level, and speaker tags.

## Conclusion
This crash course covered the fundamentals of using the Google Cloud Video Intelligence API with Python. By following the provided steps and examples, you can leverage video analysis to detect faces, people, logos, text, and transcribe speech, enhancing your ability to manage and understand video data.

