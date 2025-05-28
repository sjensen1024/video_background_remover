import yaml
import os
import unittest
from unittest.mock import MagicMock
from tests.support.mocked_yaml_safe_load_return_value import MockedYamlSafeLoadReturnValue
from src.config_manager import ConfigManager
from definitions import ROOT_DIR

class TestConfigManager(unittest.TestCase):
    def test_initializer_reads_from_config_yaml(self):
        with open(ROOT_DIR + "/config.yml", 'r') as stream:
            yaml_config = yaml.safe_load(stream)
        config_manager = ConfigManager()
        self.assertEqual(config_manager.get_original_frames_directory(), yaml_config.get('original_frames_directory'))
        self.assertEqual(config_manager.get_transparent_frames_directory(), yaml_config.get('transparent_frames_directory'))
        self.assertEqual(config_manager.get_input_file(), yaml_config.get('input_file'))
        self.assertEqual(config_manager.get_output_file(), yaml_config.get('output_file'))
        self.assertEqual(config_manager.get_should_save_original_frames(), yaml_config.get('should_save_original_frames'))
        self.assertEqual(config_manager.get_should_save_transparent_frames(), yaml_config.get('should_save_transparent_frames'))

    def test_initializer_with_mocked_yaml(self):
        yaml.safe_load = MagicMock(name='default_yaml_mock')
        yaml.safe_load.return_value = MockedYamlSafeLoadReturnValue().get_return_value()
        config_manager = ConfigManager()
        self.assertEqual(config_manager.get_original_frames_directory(), './tests/support/test_workspace/original_frames')
        self.assertEqual(config_manager.get_transparent_frames_directory(), './tests/support/test_workspace/transparent_frames')
        self.assertEqual(config_manager.get_input_file(), './tests/support/test_workspace/source_video.mp4')
        self.assertEqual(config_manager.get_output_file(), './tests/support/test_workspace/result.mp4')
        self.assertTrue(config_manager.get_should_save_original_frames())
        self.assertTrue(config_manager.get_should_save_transparent_frames())
