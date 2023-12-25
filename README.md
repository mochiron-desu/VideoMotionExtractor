# Motion Extraction in Video

## Overview

This Python project provides a simple yet effective way to extract motion from a video. It uses the OpenCV library for video processing and Numpy for array operations. The script takes an input video, processes each frame, and generates an output video highlighting the motion between consecutive frames.

## Features

- **Motion Extraction**: The script calculates the difference between each frame and its delayed version, emphasizing areas with motion.
- **Customizable Delay**: Users can adjust the delay parameter to control the sensitivity of motion detection.
- **Output Video**: The result is saved as a new video file, allowing for easy visualization of the detected motion.

## Dependencies

- OpenCV (`cv2`)
- Numpy (`numpy`)
- tqdm (`tqdm`)

## How to Use

1. **Installation**: Make sure you have the required dependencies installed. You can install them using:

    ```bash
    pip install opencv-python numpy tqdm
    ```

2. **Input Video**: Set the `input_video_path` variable to the path of your input video file.

    ```python
    input_video_path = "path/to/your/input/video.mp4"
    ```

3. **Output Video**: Set the `output_video_path` variable to your desired output video file path.

    ```python
    output_video_path = "path/to/your/output/video.mp4"
    ```

4. **Adjust Delay**: Set the `delay_seconds` variable to control the delay between frames for motion extraction.

    ```python
    delay_seconds = 1  # Adjust this based on your preference
    ```

5. **Run the Script**: Execute the script, and the output video will be generated.

    ```bash
    python motion_extraction.py
    ```

## Notes

- Ensure the input video file exists and is accessible.
- The output video will be saved in MP4 format. You can change the codec in the `fourcc` variable if needed.
- Experiment with different delay values to achieve the desired level of motion extraction.

Feel free to modify the script to suit your specific requirements or integrate it into your projects. For more advanced features, consider exploring additional image processing techniques or using external libraries.