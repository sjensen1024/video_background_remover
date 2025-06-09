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
            result_output_file_name=self.config_manager.get_output_file()
        )
    
    def process(self):
        # TODO: Implement and test the following:
        #  1) Fix the config manager so that it sets up the paths relative to the root path
        #  2) Add an option to add a background color/image to each frame (ex: green screen instead of black screen).
        #  3) Ensure we capture all the dependencies.
        print('Root directory: ' + ROOT_DIR)
        print('Starting the process.')
        self.project_cleaner.clean_current_workspace()
        source_video = moviepy.VideoFileClip(self.config_manager.get_input_file())
        video_frame_manager = VideoFrameManager(source_video)
        if self.config_manager.get_should_save_original_frames():
            video_frame_manager.save_original_frames(self.config_manager.get_original_frames_directory())
        if self.config_manager.get_should_save_transparent_frames():
            video_frame_manager.save_transparent_frames(self.config_manager.get_transparent_frames_directory())
        video_frame_manager.save_result_video_from_transparent_frames(self.config_manager.get_output_file())
        print('Process finished!')
