from PIL import Image 
from rembg import remove
import numpy
from src.frame_manager import FrameManager

# TODO: Rename this class and rework its tests so that it doesn't duplicate the tests for what FrameManager is doing.
class VideoFrameManager:
    def __init__(self, original_video):
        self.original_video = original_video
        self.original_frames = self.__extract_original_frame_info()
        self.transparent_frames = self. __setup_transparent_frame_info()
    
    def get_original_video(self):
        return self.original_video
    
    def get_original_frames(self):
        return self.original_frames
    
    def get_transparent_frames(self):
        return self.transparent_frames
    
    def save_original_frames(self, frame_directory_path):
        self.__save_frames(frame_directory_path, self.original_frames)

    def save_transparent_frames(self, frame_directory_path):
        self.__save_frames(frame_directory_path, self.transparent_frames)

    def __save_frames(self, frame_directory_path, frames):
        for frame in frames:
            frame.save_frame(frame_directory_path)

    def __extract_original_frame_info(self):
        print('Extracting original frames from video.')
        frames = []
        for index, frame in enumerate(self.original_video.iter_frames()):
            frame_file_name = self.__get_frame_file_name(index + 1)
            frame_manager = FrameManager(frame_file_name, frame)
            frames.append(frame_manager)
        print(str(self.original_video.n_frames) + ' frames extracted.')
        return frames
    
    def __setup_transparent_frame_info(self):
        print('Setting up transparent versions of the frames')
        frames = []
        for original_frame_info in self.original_frames:
            frame_manager = FrameManager(original_frame_info.get_file_name(), original_frame_info.get_frame())
            frame_manager.remove_background_from_frame()
            frames.append(frame_manager)
            print('Extracted background from ' + frame_manager.get_file_name())
        return frames
    
    def __get_frame_file_name(self, current_frame_count):
        file_name = '_'
        duration_digits = self.__get_number_of_digits(self.original_video.n_frames)
        frame_digits = self.__get_number_of_digits(current_frame_count)
        if duration_digits == frame_digits:
            return file_name + str(current_frame_count) + '.png'
        prefix = '0' * (duration_digits - frame_digits)
        return file_name + prefix + str(current_frame_count) + '.png'

    def __get_number_of_digits(self, number):
        return len(str(abs(number)))
