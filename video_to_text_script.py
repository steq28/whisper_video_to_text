import sys
import whisper
import os

def video_to_text(input_folder, output_folder):
    model = whisper.load_model("large")
    for files in os.walk(input_folder):
        for name in files:
            # Transcribe the video using the model
            text = model.transcribe(input_folder+name, fp16=False)
            # Remove .mp4 at the end of the string
            name = name[:-4]
            try:
                # Open the file and write the transcription
                with open(output_folder+name+".txt", 'w') as file:
                    file.write(text["text"])
            except FileNotFoundError:
                # If the file doesn't exist, create it and write the transcription
                with open(output_folder+name+".txt", 'x') as file:
                    file.write(text["text"])
            file.close()
if __name__== "__main__":
    if len(sys.argv) == 3:
        video_to_text(sys.argv[1], sys.argv[2])
    else:
        print("Usage: python video_to_text_script.py <input_folder> <output_folder>")
        sys.exit(1)