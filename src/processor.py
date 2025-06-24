import moviepy
from src.config_manager import ConfigManager
from src.project_cleaner import ProjectCleaner
from src.video_frame_manager import VideoFrameManager
from definitions import ROOT_DIR

class Processor:
    def __init__(self):
        self.config_manager = ConfigManager()
        self.project_cleaner = ProjectCleaner(
            original_frames_directory_name=self.config_manager.get_original_frames_directory(),
            transparent_frames_directory_name=self.config_manager.get_transparent_frames_directory(),
            background_color_frames_directory_name=self.config_manager.get_frames_with_background_color_directory(),
            result_output_file_name=self.config_manager.get_output_file()
        )
    
    def process(self):
        # TODO: 
        # 1) Ensure we capture all the dependencies.
        # 2) Add instructions to the readme.
        print('Root directory: ' + ROOT_DIR)
        print('Starting the process.')
        self.project_cleaner.clean_current_workspace()
        source_video = moviepy.VideoFileClip(self.config_manager.get_input_file())
        background_color_set = self.config_manager.get_background_color_rgb()
        self.video_frame_manager = VideoFrameManager(source_video, background_color_set)
        self.video_frame_manager.setup_frames()
        if self.config_manager.get_should_save_original_frames():
            self.video_frame_manager.save_original_frames(self.config_manager.get_original_frames_directory())
        if self.config_manager.get_should_save_transparent_frames():
            self.video_frame_manager.save_transparent_frames(self.config_manager.get_transparent_frames_directory())
        if self.config_manager.get_should_save_frames_with_background_color():
            self.video_frame_manager.save_background_color_frames(self.config_manager.get_frames_with_background_color_directory())
        self.video_frame_manager.save_result_video_from_background_color_frames(self.config_manager.get_output_file())
        print('Process finished!')
