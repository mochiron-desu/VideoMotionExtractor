# Motion Extraction in Video

## Overview

This Python project is inspired by the video tutorial by Posy, available at [this link](https://www.youtube.com/watch?v=NSS6yAMZF78&pp=ygUKdGltZWxhcHNlIA%3D%3D), which demonstrates video feature extraction techniques. The project utilizes OpenCV for video processing and Numpy for array operations. It enables users to extract motion from a video, following concepts presented in Posy's tutorial. The script calculates frame differences and generates an output video, highlighting areas with motion.

## Features

- **Motion Extraction**: The script calculates the difference between each frame and its delayed version, emphasizing areas with motion.
- **Customizable Delay**: Users can adjust the delay parameter to control the sensitivity of motion detection.
- **Output Video**: The result is saved as a new video file, allowing for easy visualization of the detected motion.
- **Efficient Processing**: Utilizes frame buffering to reduce seeking and maintain consistent processing time.
- **Robust Error Handling**: Implements checks and error handling for various edge cases.
- **Progress Tracking**: Displays an accurate progress bar during processing.

## Dependencies

- OpenCV (`cv2`)
- Numpy (`numpy`)
- tqdm (`tqdm`)
- collections (`deque`)

## Example Comparison

Here is a side-by-side comparison of a frame from the input video and the corresponding frame from the output video:

| Input Frame                                     | Output Frame                                     |
| ----------------------------------------------- | ------------------------------------------------- |
| ![Input Frame](https://github.com/mochiron-desu/VideoMotionExtractor/blob/main/examples/input1.png?raw=true) | ![Output Frame](https://github.com/mochiron-desu/VideoMotionExtractor/blob/main/examples/output1.png?raw=true) |

## How to Use

1. **Installation**: Ensure you have the required dependencies installed. You can install them using:

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
    delay_seconds = 0.033  # Adjust this based on your preference
    ```

5. **Run the Script**: Execute the script, and the output video will be generated.

    ```bash
    python motion_extraction.py
    ```

## Recent Improvements

- Fixed progress bar calculation for accurate representation of processing status.
- Implemented frame buffering using `collections.deque` to reduce seeking and improve performance.
- Added comprehensive error handling for robust execution.
- Ensured minimum delay of 1 frame to prevent issues with very small delays.
- Added checks for video file opening and length to handle edge cases.
- Optimized frame reading for consistent processing time throughout the video.
- Improved code structure and readability.

## Notes

- Ensure the input video file exists and is accessible.
- The output video will be saved in MP4 format. You can change the codec in the `fourcc` variable if needed.
- Experiment with different delay values to achieve the desired level of motion extraction.
- The script now handles various edge cases, such as very short videos or extreme delay values, more gracefully.

Feel free to modify the script to suit your specific requirements or integrate it into your projects. Posy's video tutorial serves as inspiration for this project, offering insights into video feature extraction techniques. For more advanced features, consider exploring additional image processing techniques or using external libraries.

## Troubleshooting

If you encounter any issues while running the script, check the error message printed to the console. The script now includes error handling to provide more informative error messages for common issues.

For further assistance or to report bugs, please open an issue on the project's GitHub repository.