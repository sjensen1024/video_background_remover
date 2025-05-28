import moviepy
from src.config_manager import ConfigManager
from src.project_cleaner import ProjectCleaner
from src.video_frame_extractor import VideoFrameExtractor
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
        #  1) Extract the frames from the video file and save them as images if the config says we should.
        #  2) Remove the backgrounds from the frames and save the resulting images if the config says we should.
        #  3) Convert the frames into an image sequence and output it as a video result.
        #  4) Add an option to add a background color/image to each frame (ex: green screen instead of black screen).
        #  5) Ensure we capture all the dependencies.
        print('Root directory: ' + ROOT_DIR)
        print('Starting the process.')
        self.project_cleaner.clean_current_workspace()
        source_video = moviepy.VideoFileClip(self.config_manager.get_input_file())
        extracted_frame_info = VideoFrameExtractor(source_video).get_extracted_info()
        print(str(extracted_frame_info.get('total_frames')) + ' frames extracted.')
        print('Process finished!')
