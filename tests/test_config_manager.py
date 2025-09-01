import unittest
from src.config_manager import ConfigManager
from definitions import ROOT_DIR

class TestConfigManager(unittest.TestCase):
    def setUp(self):
        self.test_config_directory = ROOT_DIR + '\\tests\\support\\test_configs\\'
    
    def test_directories_and_files_are_set_up_relative_to_root_dir(self):
        config_manager = ConfigManager(config_yaml_path = self.test_config_directory + 'default_config.yml')
        self.assertEqual(
            config_manager.get_original_frames_directory(), 
            ROOT_DIR + '\\current_workspace\\original_frames'
        )
        self.assertEqual(
            config_manager.get_transparent_frames_directory(), 
            ROOT_DIR + '\\current_workspace\\transparent_frames'
        )
        self.assertEqual(
            config_manager.get_frames_with_background_color_directory(), 
            ROOT_DIR + '\\current_workspace\\frames_with_background_color'
        )
        self.assertEqual(config_manager.get_input_file(), ROOT_DIR + '\\current_workspace\\source.mp4')
        self.assertEqual(config_manager.get_output_file(), ROOT_DIR + '\\current_workspace\\result.mp4')

    def test_when_configured_to_save_original_transparent_and_background_color_frames(self):
        config_manager_with_all_true = ConfigManager(config_yaml_path = self.test_config_directory + 'default_config.yml')
        self.assertTrue(config_manager_with_all_true.should_save_original_frames)
        self.assertTrue(config_manager_with_all_true.should_save_transparent_frames)
        self.assertTrue(config_manager_with_all_true.should_save_frames_with_background_color)

    def test_when_configured_not_to_save_any_frames(self):
        config_manager_with_all_false = ConfigManager(config_yaml_path = self.test_config_directory + 'config_with_all_booleans_false.yml')
        self.assertFalse(config_manager_with_all_false.should_save_original_frames)
        self.assertFalse(config_manager_with_all_false.should_save_transparent_frames)
        self.assertFalse(config_manager_with_all_false.should_save_frames_with_background_color)
    
    def test_when_configured_to_only_save_frames_with_background_color(self):
        config_manager_with_mixed_booleans = ConfigManager(config_yaml_path = self.test_config_directory + 'config_with_mixed_booleans.yml')
        self.assertFalse(config_manager_with_mixed_booleans.should_save_original_frames)
        self.assertFalse(config_manager_with_mixed_booleans.should_save_transparent_frames)
        self.assertTrue(config_manager_with_mixed_booleans.should_save_frames_with_background_color)
    
    def test_when_background_color_is_set_to_black(self):
        config_manager_black_background = ConfigManager(config_yaml_path = self.test_config_directory + 'default_config.yml')
        self.assertEqual(config_manager_black_background.get_background_color_rgb(), (0,0,0))

    def test_when_background_color_is_set_to_white(self):
        config_manager_black_background = ConfigManager(config_yaml_path = self.test_config_directory + 'config_with_white_background.yml')
        self.assertEqual(config_manager_black_background.get_background_color_rgb(), (255,255,255))
    
    def test_when_background_color_is_set_to_green(self):
        config_manager_green_background = ConfigManager(config_yaml_path= self.test_config_directory + 'config_with_green_background.yml')
        self.assertEqual(config_manager_green_background.get_background_color_rgb(), (0,255,0))
        
    def test_when_background_color_is_set_to_red(self):
        config_manager_red_background = ConfigManager(config_yaml_path= self.test_config_directory + 'config_with_red_background.yml')
        self.assertEqual(config_manager_red_background.get_background_color_rgb(), (255,0,0))
        
    def test_when_background_color_is_set_to_blue(self):
        config_manager_blue_background = ConfigManager(config_yaml_path= self.test_config_directory + 'config_with_blue_background.yml')
        self.assertEqual(config_manager_blue_background.get_background_color_rgb(), (0,0,255))
