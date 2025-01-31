# Steganography-Tools-master
This project is a Steganography Tool that allows users to hide and retrieve secret messages within different types of media files, including images, audio, text, and videos, to better understand the read-me file.

# Steganography Tool

This project is a **Steganography Tool** that allows users to hide and retrieve secret messages within different types of media files, including images, audio, text, and videos.

### Features:
- **Image Steganography**: Hide messages in image files (PNG) using the LSB (Least Significant Bit) technique.
- **Audio Steganography**: Hide messages in WAV audio files using LSB.
- **Text Steganography**: Hide messages in text files using Unicode zero-width characters.
- **Video Steganography**: Hide messages in video files with frame manipulation and optional encryption for security.

---

## How it Works

### File Breakdown:
1. **audio_stego.py**  
   Embeds and retrieves secret messages from WAV audio files using the Least Significant Bit (LSB) method.

2. **demo.py**  
   The main graphical user interface (GUI) that lets users interact with the tool. It provides a simple way to select the media type (image, audio, text, video) and perform encoding/decoding operations.

3. **img_stego.py**  
   Encodes secret messages into images and retrieves them from PNG files using the LSB method.

4. **text_stego.py**  
   Hides secret messages in text files using Unicode zero-width characters.

5. **video_stego.py**  
   Allows encoding and decoding of messages in video files by manipulating frames. Encryption can also be applied for additional security.

---

## Demo GIF
Here is a simple animation of the steganography process in action:

![Steganography Demo](https://media2.giphy.com/media/v1.Y2lkPTc5MGI3NjExdzM0Zms0Ymp4M2lhOW01emx3bXI5am91ZnJjOXY1aWVmaGV4MWFtZiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/WySK0nQiJKLy25HLhp/giphy.gif)

---

## Installation

To run this tool, you'll need Python 3.x installed on your system. Then, install the required dependencies:

```bash
pip install -r requirements.txt
