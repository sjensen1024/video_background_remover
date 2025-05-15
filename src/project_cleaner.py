import os
from src.config_manager import ConfigManager

class ProjectCleaner:
    def __init__(self, original_frames_directory_name = '', transparent_frames_directory_name = '', result_output_file_name = ''):
        self.original_frames_directory_name = original_frames_directory_name
        self.transparent_frames_directory_name = transparent_frames_directory_name
        self.result_output_file_name = result_output_file_name

    def clean(self):
        print('Start the process of cleaning the project.')
        print('Cleaning ' + self.original_frames_directory_name)
        print('Cleaning ' + self.transparent_frames_directory_name)
        print('Cleaning ' + self.result_output_file_name)
        print('Finished the process of cleaning the current project.')

