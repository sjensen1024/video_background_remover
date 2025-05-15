import yaml
import os.path

class ConfigManager:
    def __init__(self):
        with open(os.path.dirname(__file__) + "/../config.yml", 'r') as stream:
            config = yaml.safe_load(stream)
        self.original_frames_directory = config.get('original_frames_directory')
        self.transparent_frames_directory = config.get('transparent_frames_directory')
        self.input_file = config.get('input_file')
        self.output_file = config.get('output_file')
        self.should_save_original_frames = config.get('should_save_original_frames')
        self.should_save_transparent_frames = config.get('should_save_transparent_frames')

    def get_original_frames_directory(self):
        return self.original_frames_directory
    
    def get_transparent_frames_directory(self):
        return self.transparent_frames_directory
    
    def get_input_file(self):
        return self.input_file
    
    def get_output_file(self):
        return self.output_file
    
    def get_should_save_original_frames(self):
        return self.should_save_original_frames
    
    def get_should_save_transparent_frames(self):
        return self.should_save_transparent_frames
    