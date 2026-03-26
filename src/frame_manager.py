import PIL
import rembg
import numpy
import subprocess
import platform
import tempfile
import os

class FrameManager:
    def __init__(self, file_name, frame):
        self.file_name = file_name
        self.frame = self._get_frame_as_image(frame)
        self.is_saved = False
    
    def save_frame(self, directory):
        file_path = directory + '\\' + self.file_name
        self.frame.save(file_path)
        self.is_saved = True
        print ('Saved frame ' + file_path)

    def remove_background_from_frame(self):
        self.frame = rembg.remove(self.frame)

    def put_frame_over_color_background(self, rgb_color_set):
        frame_with_alpha_channel = self.frame.convert('RGBA')
        frame_with_color_background = PIL.Image.new('RGB', self.frame.size, rgb_color_set)
        frame_with_color_background.paste(frame_with_alpha_channel, (0, 0), frame_with_alpha_channel)
        self.frame = frame_with_color_background

    def preview_frame(self):
        """Display the frame in the default image viewer."""
        try:
            # Create a temporary file for the preview
            with tempfile.NamedTemporaryFile(suffix='.png', delete=False) as tmp_file:
                self.frame.save(tmp_file.name)
            
            # Open with system viewer
            if platform.system() == 'Darwin':  # macOS
                subprocess.Popen(['open', tmp_file.name])
            elif platform.system() == 'Windows':
                subprocess.Popen(['start', tmp_file.name], shell=True)
            else:  # Linux
                subprocess.Popen(['xdg-open', tmp_file.name])
        except Exception as e:
            print(f'\t\tWarning: Could not display frame preview: {e}')

    def _get_frame_as_image(self, frame):
        if isinstance(frame, PIL.Image.Image):
            return frame
        return PIL.Image.fromarray(numpy.uint8(frame))        
