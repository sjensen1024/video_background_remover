import unittest
from src.config_manager import ConfigManager
from definitions import ROOT_DIR

class TestConfigManager(unittest.TestCase):
    def test_default_config(self):
        relative_directory = ROOT_DIR + '\\'
        config_manager = ConfigManager(config_yaml_path= relative_directory + 'tests\\support\\default_config.yml')
        self.assertEqual(
            config_manager.get_original_frames_directory(), 
            relative_directory + 'current_workspace\\original_frames'
        )
        self.assertEqual(
            config_manager.get_transparent_frames_directory(), 
            relative_directory + 'current_workspace\\transparent_frames'
        )
        self.assertEqual(
            config_manager.get_frames_with_background_color_directory(), 
            relative_directory + 'current_workspace\\frames_with_background_color'
        )
        self.assertEqual(config_manager.get_input_file(), relative_directory + 'current_workspace\\source.mp4')
        self.assertEqual(config_manager.get_output_file(), relative_directory + 'current_workspace\\result.mp4')
        self.assertTrue(config_manager.get_should_save_original_frames())
        self.assertTrue(config_manager.get_should_save_transparent_frames())
        self.assertTrue(config_manager.get_should_save_frames_with_background_color())
        self.assertEqual(config_manager.get_background_color_rgb(), (0,0,0))
    
    def test_config_with_green_background(self):
        relative_directory = ROOT_DIR + '\\'
        config_manager = ConfigManager(config_yaml_path= relative_directory + 'tests\\support\\config_with_green_background.yml')
        self.assertEqual(config_manager.get_background_color_rgb(), (0,255,0))
