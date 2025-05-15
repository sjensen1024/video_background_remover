import yaml
import os
import unittest
from src.config_manager import ConfigManager

class TestConfigManager(unittest.TestCase):

    def test_initializer_reads_from_yaml_file(self):
        with open(os.path.dirname(__file__) + "/../config.yml", 'r') as stream:
            yaml_config = yaml.safe_load(stream)
        config_manager = ConfigManager()
        self.assertEqual(config_manager.get_original_frames_directory(), yaml_config.get('original_frames_directory'))
        self.assertEqual(config_manager.get_transparent_frames_directory(), yaml_config.get('transparent_frames_directory'))
        self.assertEqual(config_manager.get_input_file(), yaml_config.get('input_file'))
        self.assertEqual(config_manager.get_output_file(), yaml_config.get('output_file'))
        self.assertEqual(config_manager.get_should_save_original_frames(), yaml_config.get('should_save_original_frames'))
        self.assertEqual(config_manager.get_should_save_transparent_frames(), yaml_config.get('should_save_transparent_frames'))
