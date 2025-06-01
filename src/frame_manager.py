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
    
    def save(self, directory):
        self.frame.save(directory + '\\' + self.file_name)
        self.is_saved = True

    def remove_background_from_frame(self):
        self.frame = rembg.remove(self.frame)

    def __get_frame_as_image(self, frame):
        if isinstance(frame, PIL.Image.Image):
            return frame
        return PIL.Image.fromarray(numpy.uint8(frame))    
