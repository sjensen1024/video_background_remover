import moviepy
import numpy
from src.frame_manager import FrameManager

class VideoFrameManager:
    def __init__(self, original_video, background_color_set):
        self.original_video = original_video
        self.background_color_set = background_color_set
        self.original_frames = []
        self.transparent_frames = []
        self.frames_with_background_color = []
        self.result_video = None
    
    def get_original_video(self):
        return self.original_video
    
    def get_original_frames(self):
        return self.original_frames
    
    def get_transparent_frames(self):
        return self.transparent_frames
    
    def get_frames_with_background_color(self):
        return self.frames_with_background_color
    
    def get_result_video(self):
        return self.result_video
    
    def setup_frames(self):
        self.original_frames = self.__extract_original_frame_info()
        self.transparent_frames = self. __setup_transparent_frame_info()
        self.frames_with_background_color = self.__setup_frame_with_background_color_info()
    
    def save_original_frames(self, frame_directory_path):
        self.__save_frames(frame_directory_path, self.original_frames)

    def save_transparent_frames(self, frame_directory_path):
        self.__save_frames(frame_directory_path, self.transparent_frames)

    def save_background_color_frames(self, frame_directory_path):
        self.__save_frames(frame_directory_path, self.frames_with_background_color)

    def save_result_video_from_background_color_frames(self, result_video_path):
        print('Processing image sequence.')
        frame_sequence = moviepy.video.io.ImageSequenceClip.ImageSequenceClip(
            list(map(lambda i: numpy.array(i.get_frame()), self.frames_with_background_color)), 
            int(self.original_video.fps)
        )
        print('Creating video from image sequence.')
        frame_sequence.write_videofile(result_video_path)

    def __save_frames(self, frame_directory_path, frames):
        [frame.save_frame(frame_directory_path) for frame in frames]

    def __extract_original_frame_info(self):
        print('Extracting original frames from video.')
        frames = []
        for index, frame in enumerate(self.original_video.iter_frames()):
            frames = self.__add_frame_manager_to_list(frames, frame, index + 1)
        print(str(self.original_video.n_frames) + ' frames extracted.')
        return frames
    
    def __add_frame_manager_to_list(self, frame_list, frame_to_convert_to_manager, frame_number):
         frame_file_name = self.__get_frame_file_name(frame_number)
         frame_manager = FrameManager(frame_file_name, frame_to_convert_to_manager)
         frame_list.append(frame_manager)
         return frame_list
    
    def __setup_transparent_frame_info(self):
        print('Setting up transparent versions of the frames')
        frames = []
        for original_frame_info in self.original_frames:
            frames = self.__add_transparent_copy_of_frame_manager_to_list(frames, original_frame_info)
        return frames
    
    def __setup_frame_with_background_color_info(self):
        print('Setting up versions of the frames that have the configured background color')
        frames = []
        for transparent_frame_info in self.transparent_frames:
            frames = self.__add_background_color_copy_of_frame_manager_to_list(frames, transparent_frame_info)
        return frames
    
    def __add_transparent_copy_of_frame_manager_to_list(self, frame_list, original_frame_manager):
        transparent_frame_manager = FrameManager(original_frame_manager.get_file_name(), original_frame_manager.get_frame())
        transparent_frame_manager.remove_background_from_frame()
        frame_list.append(transparent_frame_manager)
        print('\tExtracted background from ' + transparent_frame_manager.get_file_name())
        return frame_list
    
    def __add_background_color_copy_of_frame_manager_to_list(self, frame_list, transparent_frame_manager):
        background_color_frame_manager = FrameManager(transparent_frame_manager.get_file_name(), transparent_frame_manager.get_frame())
        background_color_frame_manager.put_frame_over_color_background(self.background_color_set)
        frame_list.append(background_color_frame_manager)
        print('\tAdded color to background for ' + background_color_frame_manager.get_file_name())
        return frame_list
    
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
