import tkinter as tk
from tkinter import messagebox
import requests
import os

# Function to download the game file
def download_game():
    url = "https://example.com/guess_game.py"  # Replace this with the actual game file URL
    download_path = os.path.join(os.getcwd(), "guess_game.py")
    
    try:
        response = requests.get(url)
        response.raise_for_status()  # Check if the request was successful
        with open(download_path, 'wb') as file:
            file.write(response.content)
        messagebox.showinfo("Download Complete", "The game file has been downloaded successfully.")
        play_game_button.pack()  # Show the play button after download
    except requests.exceptions.RequestException as e:
        messagebox.showerror("Download Failed", f"An error occurred: {e}")

# Function to simulate running the game (in reality, you could use subprocess to launch the game)
def play_game():
    # Simulate running the game (for actual use, you'd launch a Python script or executable)
    messagebox.showinfo("Game Starting", "The game is now starting!")
    # You could use subprocess to run the downloaded game like so:
    # subprocess.run(["python", "guess_game.py"])

# Create the main window
root = tk.Tk()
root.title("Game Downloader")
root.geometry("400x300")

# Instructions label
instructions_label = tk.Label(root, text="Click below to download the game!", font=("Arial", 14))
instructions_label.pack(pady=20)

# Download button
download_button = tk.Button(root, text="Download Game", font=("Arial", 14), command=download_game)
download_button.pack(pady=20)

# Play button (hidden initially)
play_game_button = tk.Button(root, text="Play Game", font=("Arial", 14), command=play_game)

# Start the app
root.mainloop()
