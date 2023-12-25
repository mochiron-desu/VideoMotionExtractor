import cv2
import numpy as np
from tqdm import tqdm

def extract_motion(input_video_path, output_video_path, delay):
    # Read the input video
    cap = cv2.VideoCapture(input_video_path)

    # Get video properties
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = cap.get(cv2.CAP_PROP_FPS)
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

    # Create a VideoWriter object for the output video
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # You can change the codec based on your preference
    out = cv2.VideoWriter(output_video_path, fourcc, fps, (width, height))

    # Loop through the frames of the input video
    for _ in tqdm(range(total_frames), desc="Processing frames", unit="frame"):
        ret, frame = cap.read()
        if not ret:
            break

        # Duplicate the frame
        duplicate_frame = frame.copy()

        # Invert the colors of the duplicate frame
        inverted_frame = cv2.bitwise_not(duplicate_frame)

        # Calculate the delay in frames
        delay_frames = int(delay * fps)

        # Read the frame from the delayed position in the original video
        cap.set(cv2.CAP_PROP_POS_FRAMES, cap.get(cv2.CAP_PROP_POS_FRAMES) + delay_frames)
        ret, delayed_frame = cap.read()

        # Reset the video position for the next iteration
        cap.set(cv2.CAP_PROP_POS_FRAMES, cap.get(cv2.CAP_PROP_POS_FRAMES) - delay_frames)

        # Check if the delayed frame is not empty
        if not ret or delayed_frame is None:
            break

        # Resize frames to ensure they have the same dimensions
        duplicate_frame = cv2.resize(duplicate_frame, (width, height))
        delayed_frame = cv2.resize(delayed_frame, (width, height))

        # Enhance the result (you can perform additional processing here)
        result_frame = cv2.absdiff(duplicate_frame, delayed_frame)

        # Write the result frame to the output video
        out.write(result_frame)

    # Release video capture and writer objects
    cap.release()
    out.release()

if __name__ == "__main__":
    input_video_path = ""  # Change this to your input video path
    output_video_path = ""  # Change this to your desired output video path
    delay_seconds = 1  # Change this to your desired delay in seconds

    extract_motion(input_video_path, output_video_path, delay_seconds)