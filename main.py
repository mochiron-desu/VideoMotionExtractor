import cv2
import numpy as np
from tqdm import tqdm
from collections import deque

def extract_motion(input_video_path, output_video_path, delay):
    cap = cv2.VideoCapture(input_video_path)

    if not cap.isOpened():
        raise ValueError("Error opening video file")

    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = cap.get(cv2.CAP_PROP_FPS)
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(output_video_path, fourcc, fps, (width, height))

    delay_frames = max(1, int(delay * fps))  # Ensure at least 1 frame delay
    frames_to_process = max(0, total_frames - delay_frames)

    delayed_frames = deque(maxlen=delay_frames)

    # Pre-fill the deque with initial frames
    for _ in range(delay_frames):
        ret, frame = cap.read()
        if not ret:
            raise ValueError("Video is too short for the specified delay")
        delayed_frames.append(frame)

    with tqdm(total=frames_to_process, desc="Processing frames", unit="frame") as pbar:
        for _ in range(frames_to_process):
            ret, current_frame = cap.read()
            if not ret:
                break

            delayed_frame = delayed_frames.popleft()
            delayed_frames.append(current_frame)

            # Ensure frames have the same dimensions
            current_frame = cv2.resize(current_frame, (width, height))
            delayed_frame = cv2.resize(delayed_frame, (width, height))

            # Calculate the absolute difference
            result_frame = cv2.absdiff(current_frame, delayed_frame)

            # Write the result frame to the output video
            out.write(result_frame)

            pbar.update(1)

    cap.release()
    out.release()

    print(f"Processed {frames_to_process} frames. Output saved to {output_video_path}")

if __name__ == "__main__":
    input_video_path = "path/to/your/input/video.mp4"  # Change this to your input video path
    output_video_path = "path/to/your/output/video.mp4"  # Change this to your desired output video path
    delay_seconds = 1  # Change this to your desired delay in seconds

    try:
        extract_motion(input_video_path, output_video_path, delay_seconds)
    except Exception as e:
        print(f"An error occurred: {str(e)}")