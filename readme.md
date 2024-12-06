# Conversational AI Hackathon @ UCL 🎙️🤖
## 6th December 2024
Welcome to the **Conversational AI Hackathon**, hosted at UCL! 🚀 This event is your opportunity to dive into the exciting world of Conversational AI and build real-time, voice-driven applications that tackle innovative challenges.

Email {sohaib, jiameng, adnan, lohith, emma}@neuphonic.com if you need any help!

---

## Challenge

**Build a real-time conversational AI solution** that delivers seamless, voice-driven interactions for innovative use cases. Your goal is to combine state-of-the-art components to create a functional, impactful system.

---

## Judging Criteria

Your project will be judged based on the following criteria:

1. **Functionality (15%)**
   - How well does the solution perform its intended task?  
   - Does the conversational AI respond appropriately and handle various inputs effectively?

2. **Innovation & Creativity (40%)**
   - Is the idea unique, or does it improve upon existing solutions?  
   - Does it demonstrate creative use of conversational AI technology?

3. **User Experience (15%)**
   - Is the AI interaction intuitive and engaging for users?  
   - Are the responses natural and contextually relevant?

4. **Impact & Applicability (30%)**
   - How well does the solution address a real-world problem?  
   - Can the project be scaled or adapted for broader use cases?

---

## Table of Contents

1. [Introduction](#introduction)  
2. [Setup](#setup)  
3. [Project Structure](#project-structure)  
4. [Code Overview](#code-overview)  
   - [Text-to-Speech (TTS)](#text-to-speech)  
   - [Speech-to-Speech (STS)](#speech-to-speech)  
5. [How to Run](#how-to-run)  
6. [Challenges & Ideas](#challenges--ideas)  
7. [Contribution Guidelines](#contribution-guidelines)  
8. [License](#license)  


---

## Introduction

The hackathon is designed to give you hands-on experience with:  
- **Text-to-Speech (TTS):** Utilising Neuphonic's API for Voice Synthesis.  
- **Speech-to-Speech (TTS):** Utilising Neuphonic's API for Conversational AI

In what follows, we'll show you how to get started and use our software!

---

## Setup

### Prerequisites

You will need to be running a minimum of Python 3.10+ 

You'll also need to get an API Key, which you can get from [beta.neuphonic.com](https://beta.neuphonic.com).


### MacOS

If you're on MacOS, install `brew` at [https://brew.sh/](https://brew.sh/) if you don't have it already.

In most cases, you will be playing the audio returned from our servers directly on your device.

> :warning: Mac users encountering a `'portaudio.h' file not found` error can resolve it by running
> `brew install portaudio`.

### Installation

Clone the repository:  
```bash
git clone https://github.com/neuphonic/ucl_hackathon.git
cd UCL-Hackathon
```

Create a virtual environment and install the dependencies:

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

---

### Project Structure
```bash
├── hackathon_demo_ucl.ipynb        # JupyterNotebook going over various helpful examples
├── neuphonic_texttospeech.py       # TTS module
├── neuphonic_speech_to_speech.py   # Main integration program
├── README.md                       # Documentation
├── LICENSE                         # MIT License
└── requirements.txt                # Dependencies
```

---

## Getting started

Try out the ipython notebook `hackathon_demo_ucl.ipynb` in your IDE!

For more detailed documentation and examples, please refer to the `pyneuphonic` SDK README available 
at [pyneuphonic GitHub repository](https://github.com/neuphonic/pyneuphonic).

## Code Overview

### Text-to-Speech (TTS)

The **Text-to-Speech** module leverages Neuphonic’s API for generating high-quality audio.

**Key Functionality:**  
- `neuphonic_tts(input_text)`: Converts input text into speech and plays it.

Test this out with

```python
python neuphonic_texttospeech.py
```



### Speech-To-Speech (STS)
   *** NOTE: The speech recognition is quite sensitive, so you might need to be in a quiet area (and using headphones) to make this work fluidly, otherwise it can pick up background noise.

We've also created a file called neuphonic_speech_to_speech.py which allows you to talk to a module in a speech to speech fashion. It's connected to a Deepgram ASR, OpenAI LLM, and then the Neuphonic TTS. By installing pyneuphonic, you install all the depencies required to get it up and running.

1. Speak into the microphone, and the system will transcribe your speech in real time.
2. The transcribed text is sent to the LLM to generate a response.
3. The response is converted to speech using the TTS module and played back to you.
4. Repeat the process to continue the conversation.


Test this out with

```bash
python neuphonic_speech_to_speech.py
```


---

## Challenges & Ideas

### Challenges
- **Real-time performance**: Ensure smooth, low-latency interactions.  
- **Robustness**: Handle varied accents, speech rates, and noisy environments.  

### Project Ideas
- **Virtual Assistant**: Build a personalized voice assistant.  
- **Interactive Learning**: Develop a language learning app.  
- **Accessibility Tool**: Create tools for users with disabilities.
- **News Summarisation**: Fetch the latest news, generates concise summaries, and delivers them as personalized audio clips.
- **Dynamic Storytelling**: Create interactive audiobooks, with the story adapting based on mood or context.
- **TTS Fitness Coach**: Cirtual fitness coach that provides real-time, motivational voice instructions during workouts.
- **AI Audioguides**:Design a tool for generating personalized audioguides for museums or attractions.

---

## Contribution Guidelines

All contributions during the hackathon should be:  
- Clearly documented.  
- Tested to ensure compatibility with the main system.  

---

## License

This project is licensed under the MIT License. See `LICENSE` for more details.

---

Happy Hacking! 🎉
