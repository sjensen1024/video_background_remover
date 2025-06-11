import yaml
import os.path
from definitions import ROOT_DIR

class ConfigManager:
    def __init__(self, config_yaml_path = ROOT_DIR + '//' + 'config.yml'):
        with open(config_yaml_path, 'r') as stream:
            config = yaml.safe_load(stream)
        self.original_frames_directory = config.get('original_frames_directory')
        self.transparent_frames_directory = config.get('transparent_frames_directory')
        self.frames_with_background_color_directory = config.get('frames_with_background_color_directory')
        self.input_file = config.get('input_file')
        self.output_file = config.get('output_file')
        self.should_save_original_frames = config.get('should_save_original_frames')
        self.should_save_transparent_frames = config.get('should_save_transparent_frames')
        self.should_save_frames_with_background_color = config.get('should_save_frames_with_background_color')
        self.background_color_red_amount = config.get('background_color_red_amount')
        self.background_color_green_amount = config.get('background_color_green_amount')
        self.background_color_blue_amount = config.get('background_color_blue_amount')


    def get_original_frames_directory(self):
        return self.__make_relative_to_root_path(self.original_frames_directory)
    
    def get_transparent_frames_directory(self):
        return self.__make_relative_to_root_path(self.transparent_frames_directory)
    
    def get_frames_with_background_color_directory(self):
        return self.__make_relative_to_root_path(self.frames_with_background_color_directory)
    
    def get_input_file(self):
        return self.__make_relative_to_root_path(self.input_file)
    
    def get_output_file(self):
        return self.__make_relative_to_root_path(self.output_file)
    
    def get_should_save_original_frames(self):
        return self.should_save_original_frames
    
    def get_should_save_transparent_frames(self):
        return self.should_save_transparent_frames
    
    def get_should_save_frames_with_background_color(self):
        return self.should_save_frames_with_background_color
    
    def get_background_color_rgb(self):
        return (self.background_color_red_amount, self.background_color_green_amount, self.background_color_blue_amount)
    
    def __make_relative_to_root_path(self, path):
        return ROOT_DIR + '\\' + path
    