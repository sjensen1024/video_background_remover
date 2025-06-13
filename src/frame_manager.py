import PIL
import rembg
import numpy

class FrameManager:
    def __init__(self, file_name, frame):
        self.file_name = file_name
        self.frame = self.__get_frame_as_image(frame)
        self.is_saved = False

    def get_file_name(self):
        return self.file_name
    
    def get_frame(self):
        return self.frame
    
    def get_is_saved(self):
        return self.is_saved
    
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

    def __get_frame_as_image(self, frame):
        if isinstance(frame, PIL.Image.Image):
            return frame
        return PIL.Image.fromarray(numpy.uint8(frame))    
