import moviepy
import numpy
from src.frame_manager import FrameManager

class VideoFrameManager:
    def __init__(self, original_video, background_color_set):
        self.original_video = original_video
        self.background_color_set = background_color_set
        self.original_frames = self._extract_original_frame_info()
        self.transparent_frames = self. _setup_transparent_frame_info()
        self.frames_with_background_color = self._setup_frame_with_background_color_info()
        self.result_video = None
    
    def save_original_frames(self, frame_directory_path):
        self._save_frames(frame_directory_path, self.original_frames)

    def save_transparent_frames(self, frame_directory_path):
        self._save_frames(frame_directory_path, self.transparent_frames)

    def save_background_color_frames(self, frame_directory_path):
        self._save_frames(frame_directory_path, self.frames_with_background_color)

    def save_result_video_from_background_color_frames(self, result_video_path):
        print('Processing image sequence.')
        frame_sequence = moviepy.video.io.ImageSequenceClip.ImageSequenceClip(
            list(map(lambda i: numpy.array(i.frame), self.frames_with_background_color)), 
            int(self.original_video.fps)
        )
        print('Creating video from image sequence.')
        frame_sequence.write_videofile(result_video_path)

    def _save_frames(self, frame_directory_path, frames):
        [frame.save_frame(frame_directory_path) for frame in frames]

    def _extract_original_frame_info(self):
        print('Extracting original frames from video.')
        frames = []
        for index, frame in enumerate(self.original_video.iter_frames()):
            frames = self._add_frame_manager_to_list(frames, frame, index + 1)
        print(str(self.original_video.n_frames) + ' frames extracted.')
        return frames
    
    def _add_frame_manager_to_list(self, frame_list, frame_to_convert_to_manager, frame_number):
         frame_file_name = self._get_frame_file_name(frame_number)
         frame_manager = FrameManager(frame_file_name, frame_to_convert_to_manager)
         frame_list.append(frame_manager)
         return frame_list
    
    def _setup_transparent_frame_info(self):
        print('Setting up transparent versions of the frames')
        frames = []
        for original_frame_info in self.original_frames:
            frames = self._add_transparent_copy_of_frame_manager_to_list(frames, original_frame_info)
        return frames
    
    def _setup_frame_with_background_color_info(self):
        print('Setting up versions of the frames that have the configured background color')
        frames = []
        for transparent_frame_info in self.transparent_frames:
            frames = self._add_background_color_copy_of_frame_manager_to_list(frames, transparent_frame_info)
        return frames
    
    def _add_transparent_copy_of_frame_manager_to_list(self, frame_list, original_frame_manager):
        transparent_frame_manager = FrameManager(original_frame_manager.file_name, original_frame_manager.frame)
        transparent_frame_manager.remove_background_from_frame()
        frame_list.append(transparent_frame_manager)
        print('\tExtracted background from ' + transparent_frame_manager.file_name)
        return frame_list
    
    def _add_background_color_copy_of_frame_manager_to_list(self, frame_list, transparent_frame_manager):
        background_color_frame_manager = FrameManager(transparent_frame_manager.file_name, transparent_frame_manager.frame)
        background_color_frame_manager.put_frame_over_color_background(self.background_color_set)
        frame_list.append(background_color_frame_manager)
        print('\tAdded color to background for ' + background_color_frame_manager.file_name)
        return frame_list
    
    def _get_frame_file_name(self, current_frame_count):
        file_name = '_'
        duration_digits = self._get_number_of_digits(self.original_video.n_frames)
        frame_digits = self._get_number_of_digits(current_frame_count)
        if duration_digits == frame_digits:
            return file_name + str(current_frame_count) + '.png'
        prefix = '0' * (duration_digits - frame_digits)
        return file_name + prefix + str(current_frame_count) + '.png'

    def _get_number_of_digits(self, number):
        return len(str(abs(number)))
