import tkinter as tk
from tkinter import filedialog, messagebox
import cv2
import img_stego  # Import your custom steganography module
import text_stego  # Import your custom text steganography module
import audio_stego # Import the audio steganography functions
import video_stego  # Import the video steganography module
import numpy as np

# Initialize the main window
root = tk.Tk()
root.title("Steganography Tool")
root.geometry("400x400")

# Function to handle the image button click
def handle_image_button():
    # Hide the root window
    root.withdraw()

    # Create a new top-level window called "Image"
    image_window = tk.Toplevel()
    image_window.title("Image Steganography")
    image_window.geometry("500x700")

    # Header Section
    header_label = tk.Label(image_window, text="Image Steganography", font=("Arial", 20, "bold"), fg="#4CAF50")
    header_label.pack(pady=20)

    # Encode Section
    encode_label = tk.Label(image_window, text="Encode a Message", font=("Arial", 16, "bold"), fg="#4CAF50")
    encode_label.pack(pady=10)

    # Upload Cover Image
    cover_image_label = tk.Label(image_window, text="Upload Cover Image:")
    cover_image_label.pack()
    cover_image_button = tk.Button(image_window, text="Choose Cover Image", command=lambda: upload_image("encode"))
    cover_image_button.pack(pady=5)

    # Secret Message Entry
    secret_message_label = tk.Label(image_window, text="Enter Secret Message:")
    secret_message_label.pack(pady=10)
    secret_message_entry = tk.Entry(image_window, width=40)
    secret_message_entry.pack(pady=5)

    # Result Filename Entry
    result_filename_label = tk.Label(image_window, text="Enter Result Filename (with extension):")
    result_filename_label.pack(pady=10)
    result_filename_entry = tk.Entry(image_window, width=40)
    result_filename_entry.pack(pady=5)

    # Encode Button
    encode_button = tk.Button(
        image_window,
        text="Encode Message",
        command=lambda: encode_message(secret_message_entry, result_filename_entry)
    )
    encode_button.pack(pady=20)

    # Decode Section
    decode_label = tk.Label(image_window, text="Decode a Message", font=("Arial", 16, "bold"), fg="#4CAF50")
    decode_label.pack(pady=10)

    # Upload Stego Image
    stego_image_label = tk.Label(image_window, text="Upload Stego Image:")
    stego_image_label.pack()
    stego_image_button = tk.Button(image_window, text="Choose Encoded Image", command=lambda: upload_image("decode"))
    stego_image_button.pack(pady=5)

    # Decode Button
    decode_button = tk.Button(image_window, text="Decode Message", command=lambda: decode_message())
    decode_button.pack(pady=20)

    # Footer Section
    footer_label = tk.Label(image_window, text="© 2024 Steganography Tool. All rights reserved.", font=("Arial", 8), fg="#4CAF50")
    footer_label.pack(side="bottom", pady=10)

    # Close the Image Window and Show Root Again
    def close_image_window():
        image_window.destroy()
        root.deiconify()  # Show the main root window again

    # Close Button
    close_button = tk.Button(image_window, text="Close", command=close_image_window)
    close_button.pack(pady=10)

# Variables to hold the selected image file paths
cover_image_path = None
stego_image_path = None

# Function to upload an image
def upload_image(mode):
    global cover_image_path, stego_image_path
    file_path = filedialog.askopenfilename(title="Select an Image", filetypes=[("Image Files", "*.*")])
    
    if file_path:
        if mode == "encode":
            cover_image_path = file_path
            print(f"Selected Cover Image for encoding: {cover_image_path}")
        elif mode == "decode":
            stego_image_path = file_path
            print(f"Selected Stego Image for decoding: {stego_image_path}")

def encode_message(secret_message_entry, result_filename_entry):
    # global cover_image_path
    if not cover_image_path:
        messagebox.showerror("Error", "Please select a cover image first.")
        return

    message = secret_message_entry.get()
    filename = result_filename_entry.get()
    # Clear the entry fields
    secret_message_entry.delete(0, tk.END)
    result_filename_entry.delete(0, tk.END)

    if not message or not filename:
        messagebox.showerror("Error", "Please enter a secret message and a result filename.")
        return

    image = cv2.imread(cover_image_path)
    try:
        img_stego.encode_img_data(image, message, filename)  # Call the encoding function
        messagebox.showinfo("Success", f"Message encoded and saved as {filename}.")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to encode message: {str(e)}")

# Function to decode a message
def decode_message():
    global stego_image_path
    if not stego_image_path:
        messagebox.showerror("Error", "Please select a stego image to decode.")
        return

    image = cv2.imread(stego_image_path)
    
    if image is None:
        print("Failed to read the image. Check the file path or format.")
        return
    
    try:
        decoded_message = img_stego.decode_img_data(image)  # Call the decoding function
        if decoded_message:
            messagebox.showinfo("Decoded Message", f"The hidden message is: {decoded_message}")
        else:
            messagebox.showerror("Error", "No hidden message found in the image.")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to decode message: {str(e)}")

#######################---------------------------------------------------------------------------#######################
#######################---------------------------------------------------------------------------#######################
#######################---------------------------------------------------------------------------#######################
#######################---------------------------------------------------------------------------#######################
#######################---------------------------------------------------------------------------#######################
#######################---------------------------------------------------------------------------#######################
#######################---------------------------------------------------------------------------#######################

# Function to handle the text button click
def handle_text_button():
    # Hide the root window
    root.withdraw()

    # Create a new top-level window called "Text"
    text_window = tk.Toplevel()
    text_window.title("Text Steganography")
    text_window.geometry("500x600")

    # Header Section
    header_label = tk.Label(text_window, text="Text Steganography", font=("Arial", 20, "bold"), fg="#4CAF50")
    header_label.pack(pady=20)

    # Encode Message Section
    encode_label = tk.Label(text_window, text="Encode a Message", font=("Arial", 16, "bold"), fg="#4CAF50")
    encode_label.pack(pady=10)

    # Secret Message Entry
    secret_message_label = tk.Label(text_window, text="Enter Secret Message:")
    secret_message_label.pack()
    secret_message_entry = tk.Entry(text_window, width=40)
    secret_message_entry.pack(pady=5)

    # Result Filename Entry
    result_filename_label = tk.Label(text_window, text="Enter Result Filename (with extension):")
    result_filename_label.pack(pady=10)
    result_filename_entry = tk.Entry(text_window, width=40)
    result_filename_entry.pack(pady=5)

    # Encode Button
    def handle_encode():
        secret_message = secret_message_entry.get()
        result_filename = result_filename_entry.get()

        if not secret_message or not result_filename:
            tk.messagebox.showerror("Error", "Please provide both the secret message and result filename.")
            return

        # Call the encode function from text_stego
        text_stego.encode_txt_data(secret_message, result_filename)

        # Clear the fields after encoding
        secret_message_entry.delete(0, tk.END)
        result_filename_entry.delete(0, tk.END)
        tk.messagebox.showinfo("Success", f"Message encoded successfully into {result_filename}.")

    encode_button = tk.Button(
        text_window,
        text="Encode Message",
        command=handle_encode
    )
    encode_button.pack(pady=10)

    # Decode Section
    decode_label = tk.Label(text_window, text="Decode a Message", font=("Arial", 16, "bold"), fg="#4CAF50")
    decode_label.pack(pady=10)

    # Decode Button
    def handle_decode():
        # Open file dialog to select the stego file
        stego_file = filedialog.askopenfilename(title="Select Stego File", filetypes=[("Text Files", "*.txt")])
        if not stego_file:
            return


        # Call the decode function from text_stego
        decoded_message = text_stego.decode_txt_data(stego_file)
        tk.messagebox.showinfo("Decoded Message", f"Decoded Message: {decoded_message}")

    decode_button = tk.Button(
        text_window,
        text="Decode Message",
        command=handle_decode
    )
    decode_button.pack(pady=10)

    # Close the Text Window and Show Root Again
    def close_text_window():
        text_window.destroy()
        root.deiconify()

    # Close Button
    close_button = tk.Button(text_window, text="Close", command=close_text_window)
    close_button.pack(pady=20)

    # ASCII Art Text (Fixed at the bottom)
    ascii_art = """
                    ███████╗██╗    ██╗ ██████╗ ███████╗                 
                    ╚════██╝██║    ██║██╔════╝ ██╔════╝             
                    ███████╗██║ █╗ ██║██║      ███████╗             
                    ██═════╝██║███╗██║██║      ╚════██║             
                    ███████║╚███╔███╔╝╚██████╗ ███████║         
                    ╚══════╝ ╚══╝╚══╝  ╚═════╝ ╚══════╝             
        """

    # Container Frame for ASCII art
    ascii_frame = tk.Frame(text_window, bg="black", height=100)
    ascii_frame.pack(fill="x", side="bottom")

    # Fixed ASCII art label
    ascii_label = tk.Label(
        ascii_frame,
        text=ascii_art,
        font=("Courier", 10),
        fg="#4CAF50",  # Green color
        bg="black",
        justify="left"
    )
    ascii_label.pack()

#######################---------------------------------------------------------------------------#######################
#######################---------------------------------------------------------------------------#######################
#######################---------------------------------------------------------------------------#######################
#######################---------------------------------------------------------------------------#######################
#######################---------------------------------------------------------------------------#######################
#######################---------------------------------------------------------------------------#######################
#######################---------------------------------------------------------------------------#######################

# Function to handle the audio button click
def handle_audio_button():
    # Hide the root window
    root.withdraw()

    # Create a new top-level window called "Audio"
    audio_window = tk.Toplevel()
    audio_window.title("Audio Steganography")
    audio_window.geometry("500x700")

    # Header Section
    header_label = tk.Label(audio_window, text="Audio Steganography", font=("Arial", 20, "bold"), fg="#4CAF50")
    header_label.pack(pady=20)

    # Encode Message Section
    encode_label = tk.Label(audio_window, text="Encode a Message", font=("Arial", 16, "bold"), fg="#4CAF50")
    encode_label.pack(pady=10)

    # Audio File Upload Section
    audio_stego_file = None

    def upload_audio():
        nonlocal audio_stego_file  # Use the variable defined outside of the function
        audio_stego_file = filedialog.askopenfilename(title="Select Audio File", filetypes=[("Audio Files", "*.wav;*.mp3")])
        if not audio_stego_file:
            return
        messagebox.showinfo("Audio File", f"Selected Audio File: {audio_stego_file}")

    upload_button = tk.Button(audio_window, text="Upload Audio File", command=upload_audio)
    upload_button.pack(pady=10)

    # Secret Message Entry
    secret_message_label = tk.Label(audio_window, text="Enter Secret Message:")
    secret_message_label.pack()
    secret_message_entry = tk.Entry(audio_window, width=40)
    secret_message_entry.pack(pady=5)

    # Result Filename Entry
    result_filename_label = tk.Label(audio_window, text="Enter Result Filename (with extension):")
    result_filename_label.pack(pady=10)
    result_filename_entry = tk.Entry(audio_window, width=40)
    result_filename_entry.pack(pady=5)

    # Encode Button
    def handle_encode_audio():
        audio_path = audio_stego_file
        secret_message = secret_message_entry.get()
        result_filename = result_filename_entry.get()

        if not audio_path or not secret_message or not result_filename:
            messagebox.showerror("Error", "Please provide an audio file, secret message, and result filename.")
            return

        try:
            audio_stego.encode_aud_data(audio_path, secret_message, result_filename)  # Adjusted to use the imported function
            messagebox.showinfo("Success", f"Message encoded successfully into {result_filename}.")
            # Clear inputs
            secret_message_entry.delete(0, tk.END)
            result_filename_entry.delete(0, tk.END)
        except Exception as e:
            messagebox.showerror("Error", str(e))

    encode_button = tk.Button(audio_window, text="Encode Message", command=handle_encode_audio)
    encode_button.pack(pady=10)

    # Decode Section
    decode_label = tk.Label(audio_window, text="Decode a Message", font=("Arial", 16, "bold"), fg="#4CAF50")
    decode_label.pack(pady=10)

    # Decode Button
    def handle_decode_audio():
        stego_file = filedialog.askopenfilename(title="Select Stego Audio File", filetypes=[("Audio Files", "*.wav")])
        if not stego_file:
            return

        try:
            decoded_message = audio_stego.decode_aud_data(stego_file)  # Adjusted to use the imported function
            messagebox.showinfo("Decoded Message", f"Decoded Message: {decoded_message}")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    decode_button = tk.Button(audio_window, text="Decode Message", command=handle_decode_audio)
    decode_button.pack(pady=10)

    # Close the Audio Window and Show Root Again
    def close_audio_window():
        audio_window.destroy()
        root.deiconify()

    # Close Button
    close_button = tk.Button(audio_window, text="Close", command=close_audio_window)
    close_button.pack(pady=20)

#######################---------------------------------------------------------------------------#######################
#######################---------------------------------------------------------------------------#######################
#######################---------------------------------------------------------------------------#######################
#######################---------------------------------------------------------------------------#######################
#######################---------------------------------------------------------------------------#######################
#######################---------------------------------------------------------------------------#######################
#######################---------------------------------------------------------------------------#######################

# Function to handle the video button click
def handle_video_button():
    # Hide the root window
    root.withdraw()

    # Create a new top-level window called "Video"
    video_window = tk.Toplevel()
    video_window.title("Video Steganography")
    video_window.geometry("600x800")
    

    # Header Section
    header_label = tk.Label(video_window, text="Video Steganography", font=("Arial", 20, "bold"), fg="#4CAF50")
    header_label.pack(pady=20)

    # Encode Message Section
    encode_label = tk.Label(video_window, text="Encode a Message", font=("Arial", 16, "bold"), fg="#4CAF50")
    encode_label.pack(pady=10)

    # Video File Upload Section
    video_stego_file = None

    def upload_video():
        nonlocal video_stego_file  # Use the variable defined outside of the function
        video_stego_file = filedialog.askopenfilename(title="Select Video File", filetypes=[("Video Files", "*.mp4;*.avi;*.mov")])
        if not video_stego_file:
            return
        messagebox.showinfo("Video File", f"Selected Video File: {video_stego_file}")

    upload_button = tk.Button(video_window, text="Upload Video File", command=upload_video)
    upload_button.pack(pady=10)

    # Secret Message Entry
    secret_message_label = tk.Label(video_window, text="Enter Secret Message:")
    secret_message_label.pack()
    secret_message_entry = tk.Entry(video_window, width=40)
    secret_message_entry.pack(pady=5)

    # Frame Number Entry
    frame_number_label = tk.Label(video_window, text="Enter Frame number:")
    frame_number_label.pack(pady=10)
    frame_number_entry = tk.Entry(video_window, width=40)
    frame_number_entry.pack(pady=5)

    # Encryption Key Entry
    encrypt_key_label = tk.Label(video_window, text="Enter Encryption Key:")
    encrypt_key_label.pack(pady=10)
    encrypt_key_entry = tk.Entry(video_window, width=40)
    encrypt_key_entry.pack(pady=5)

    # Encode Button
    def handle_encode_video():
        video_path = video_stego_file
        secret_message = secret_message_entry.get()
        frame_number = frame_number_entry.get()
        encrypt_key = encrypt_key_entry.get()

        if not video_path or not secret_message or not frame_number or not encrypt_key:
            messagebox.showerror("Error", "Please provide a video file, secret message, frame number, and encryption key.")
            return

        try:
            # Here we call the encode_vid_data function from video_stego module
            frame_ = video_stego.encode_vid_data(video_path, int(frame_number), secret_message, encrypt_key)
            np.save("encoded_frame.npy", frame_)
            
            messagebox.showinfo("Success", f"Message encoded successfully into frame {frame_number}.\nResult saved in 'encoded_frame.npy'")
            
            # Clear inputs
            secret_message_entry.delete(0, tk.END)
            frame_number_entry.delete(0, tk.END)
            encrypt_key_entry.delete(0, tk.END)
        except Exception as e:
            messagebox.showerror("Error", str(e))


    encode_button = tk.Button(video_window, text="Encode Message", command=handle_encode_video)
    encode_button.pack(pady=10)

    # Decode Section
    decode_label = tk.Label(video_window, text="Decode a Message", font=("Arial", 16, "bold"), fg="#4CAF50")
    decode_label.pack(pady=10)

    # Video File Upload Section for Decoding
    def upload_video_decode():
        global video_decode_file  # Use a global variable for the decode video file
        video_decode_file = filedialog.askopenfilename(title="Select Video File", filetypes=[("Video Files", "*.mp4;*.avi;*.mov")])
        if not video_decode_file:
            return
        messagebox.showinfo("Video File", f"Selected Video File for Decoding: {video_decode_file}")

    decode_video_button = tk.Button(video_window, text="Upload Video File for Decoding", command=upload_video_decode)
    decode_video_button.pack(pady=10)

    # Text File Upload Section for Decoding
    def upload_text_file():
        global saved_frame_file  # Use a global variable to hold the path to the saved frame file
        text_file_path = filedialog.askopenfilename(title="Select Frame File", filetypes=[("Numpy Files", "*.npy")])
        if text_file_path:
            try:
                # Store the selected file path in a global variable
                saved_frame_file = text_file_path
                messagebox.showinfo("Frame File Loaded", f"Frame file loaded successfully.\nPath: {saved_frame_file}")
            except Exception as e:
                messagebox.showerror("Error", f"Failed to load frame file: {e}")
        else:
            messagebox.showerror("Error", "No frame file selected.")

    text_file_button = tk.Button(video_window, text="Load Text File", command=upload_text_file)
    text_file_button.pack(pady=10)

    # Frame Number Entry for Decoding
    decode_frame_number_label = tk.Label(video_window, text="Enter Frame Number:")
    decode_frame_number_label.pack(pady=10)
    decode_frame_number_entry = tk.Entry(video_window, width=40)
    decode_frame_number_entry.pack(pady=5)

    # Encryption Key Entry for Decoding
    decode_encrypt_key_label = tk.Label(video_window, text="Enter Encryption Key:")
    decode_encrypt_key_label.pack(pady=10)
    decode_encrypt_key_entry = tk.Entry(video_window, width=40)
    decode_encrypt_key_entry.pack(pady=5)

    # Decode Button
    def handle_decode_video():
        video_path = video_decode_file
        frame_number = decode_frame_number_entry.get()
        dencrypt_key = decode_encrypt_key_entry.get()

        if not video_path or not frame_number or not dencrypt_key:
            messagebox.showerror("Error", "Please provide a video file, frame number, and encryption key.")
            return

        try:
            # Use the file path obtained from the text file button
            if not video_path:
                raise FileNotFoundError("No text file loaded. Please load the encoded frame file first.")

            # Here we call the decode_vid_data function from the video_stego module
            decoded_message = video_stego.decode_vid_data(saved_frame_file, video_path, int(frame_number), dencrypt_key)
            messagebox.showinfo("Decoded Message", f"The hidden message is: {decoded_message}")
            
            # Clear inputs
            decode_frame_number_entry.delete(0, tk.END)
            decode_encrypt_key_entry.delete(0, tk.END)
        except FileNotFoundError as fnf_error:
            messagebox.showerror("Error", str(fnf_error))
        except Exception as e:
            messagebox.showerror("Error", str(e))


    decode_button = tk.Button(video_window, text="Decode Message", command=handle_decode_video)
    decode_button.pack(pady=10)

    # Close the Video Window and Show Root Again
    def close_video_window():
        video_window.destroy()
        root.deiconify()

    # Close Button
    close_button = tk.Button(video_window, text="Close", command=close_video_window)
    close_button.pack(pady=20)

#######################---------------------------------------------------------------------------#######################
#######################---------------------------------------------------------------------------#######################
#######################---------------------------------------------------------------------------#######################
#######################---------------------------------------------------------------------------#######################
#######################---------------------------------------------------------------------------#######################
#######################---------------------------------------------------------------------------#######################
#######################---------------------------------------------------------------------------#######################




# Buttons for different modes
button_image = tk.Button(root, text="Image Steganography", command=handle_image_button)
button_image.pack(pady=20)

but_txt = tk.Button(root, text="Text Steganography", command=handle_text_button)
but_txt.pack(padx=10, pady=10)

but_audio = tk.Button(root, text="Audio Steganography", command=handle_audio_button)
but_audio.pack(padx=10, pady=10)

but_video = tk.Button(root, text="Video Steganography", command=handle_video_button)
but_video.pack(padx=10, pady=10)

button_close = tk.Button(root, text="Close the Program", command=exit)
button_close.pack(pady=20)

# ASCII Art Text (Fixed at the bottom)
ascii_art = """
             █████╗ ██████╗  ██████╗ ██╗
            ██╔═══╝██╔═══██╗██╔═══██╗██║
            ██║    ██║   ██║██║   ██║██║   
            ██║    ██║   ██║██║   ██║██║   
            ╚█████ ╚██████╔╝╚██████╔╝╚█████╗
             ╚════  ╚═════╝  ╚═════╝  ╚════╝          
    """

# Container Frame for ASCII art
ascii_frame = tk.Frame(root, bg="black", height=100)
ascii_frame.pack(fill="x", side="bottom")

# Fixed ASCII art label
ascii_label = tk.Label(
    ascii_frame,
    text=ascii_art,
    font=("Courier", 10),
    fg="#4CAF50",  # Green color
    bg="black",
    justify="left"
)
ascii_label.pack()

# Run the Tkinter main loop
root.mainloop()
