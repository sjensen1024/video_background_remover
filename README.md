# Video Background Remover
This is a Python program that takes in a video file and produces a new video with the background removed and replaced by a solid color.
It does this mainly using moviepy and rembg.

# Installation
- If you don't have it already, you'll need FFmpeg installed. Otherwise moviePy won't work.
  https://ffmpeg.org/download.html
- Clone this repository.
- Go to the root directory of the project and run `pip install -r requirements.txt`.

# Configuration in the config.yml
### The following settings can be configured in your project's config.yml
- `original_frames_directory` tells your project where to save PNG's of each frame from your input file.
  Its default value is `current_workspace\original_frames`.
- `transparent_frames_directory` tells your project where to save PNG's of each frame from your input file where the background is removed.
  Its default value is `current_workspace\transparent_frames`.
- `frames_with_background_color_directory` tells your project where to save PNG's of each frame from your input file 
  with the background filled in with the config-specified color.
  Its default value is `current_workspace\frames_with_background_color`.
- `input_file` tells your project what MP4 video file to remove the background from.
  Its default value is `current_workspace\source.mp4`.
- `output_file` tells your project where to save the resulting MP4 video with the background removed.
  Its default value is `current_workspace\result.mp4`.
- `should_save_original_frames` tells your project whether it should save copies of the source video frames as PNG images.
  Its default value is `true`. 
- `should_save_transparent_frames` tells your project whether it should save copies of the source video frames 
  with the backgorund removed as PNG images. Its default value is `true`.
- `should_save_frames_with_background_color` tells your project whether it should save copies of the source video frames
  with the background filled in with the config-specified color. Its default value is `true`.
- `background_color_red_amount` Is the R (red) portion of the RGB value in your result video's background color. 
  Its default value is 0.
- `background_color_green_amount` Is the G (green) portion of the RGB value in your result video's background color.
  Its default value is 0.
- `background_color_blue_amount` Same thing as the two configs above, but for the B (blue) portion.
  Its default value is 0, which means if you use this default value with the other background color defaults, 
  your result video will have a black background.

### Other things to note about configuration
- In its current state, all video files must be MP4's and all images must be PNG's.
- All directory/file location-related configs are relative to your project's root directory.
- All background color amount configurations can go from 0 to 255.
  There are numerous RGB color picking tools available online that can help you determine what numbers to use, 
  but [here's an example](https://www.rapidtables.com/web/color/RGB_Color.html).

# Usage
### How to run the program
- Ensure there is an input file for your project to read from (see configuration above).
- Navigate to the root project directory in a terminal and run `python .`
- That's it. The video background remover should do its thing and save a result MP4 with the background replaced with a solid color.

### Important things to note about usage
- There's no "make it magically work" feature.
  The best results will come from a video with a very clearly defined foreground subject without much going on in the background.
- If you've already run the program and decide to run it again, it will delete all of the saved PNG frames
  that are still in the configured directory, as well as the result MP4 video.
  You can work around this by copy/pasting the resulting files to a different folder.
