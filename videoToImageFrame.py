import cv2
import os

# Path to the directory containing videos
videos_path = r"D:\TEST 2\Data\YT"
# Directory where frames will be saved
output_dir = r"D:\TEST 2\Data\YT\Frames"

# Create output directory if it does not exist
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Get list of video files in the directory
video_files = [f for f in os.listdir(videos_path) if f.lower().endswith(('.mp4', '.avi', '.mov', '.mkv'))]

# Process each video file
for video_file in video_files:
    video_path = os.path.join(videos_path, video_file)
    video_output_dir = os.path.join(output_dir, os.path.splitext(video_file)[0])
    
    # Create a directory for frames of the current video
    if not os.path.exists(video_output_dir):
        os.makedirs(video_output_dir)
    
    # Open the video file
    video = cv2.VideoCapture(video_path)

    # Check if video opened successfully
    if not video.isOpened():
        print(f"Error: Could not open video file {video_file}.")
        continue

    # Get the frames per second (fps) of the video
    fps = video.get(cv2.CAP_PROP_FPS)
    print(f"Processing {video_file} with {fps} fps")

    # Read and save frames
    frame_count = 0
    while True:
        ret, frame = video.read()
        if not ret:
            break

        # Save frame as image
        frame_filename = os.path.join(video_output_dir, f"frame_{frame_count:04d}.png")
        cv2.imwrite(frame_filename, frame)
        frame_count += 1

    # Release the video capture object
    video.release()
    print(f"Extracted {frame_count} frames from {video_file}.")

# Close all OpenCV windows
cv2.destroyAllWindows()
