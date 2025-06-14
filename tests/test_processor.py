import unittest
from unittest.mock import MagicMock
from src.processor import Processor
from src.config_manager import ConfigManager
from src.video_frame_manager import VideoFrameManager
from tests.support.mocked_video_frame_manager import MockedVideoFrameManager

from definitions import ROOT_DIR

class TestProcessor(unittest.TestCase):
    def setUp(self):
        print('TODO: Implement me!')
        #self.test_config_directory = ROOT_DIR + '\\tests\\support\\test_configs\\'
        #self.processor = Processor()
        #self.config_manager_booleans_true = ConfigManager(config_yaml_path=self.test_config_directory + 'test_processor_config_booleans_true.yml')
        #self.config_manager = MagicMock(name='mock_processor_config_manager')
        #self.processor.config_manager.return_value = self.config_manager_booleans_true
        #self.processor.project_cleaner.clean_current_workspace = MagicMock(name='mock_processor_project_cleaner_clean_current_workspace')
        #self.processor.video_frame_manager = MagicMock(name='mock_video_frame_manager')
        #self.processor.video_frame_manager.return_value = MockedVideoFrameManager(1, 2)

    #def tearDown(self):
        #src.video_frame_manager = self.original_video_frame_manager

    def test_workspace_cleaning_process_runs(self):
        print('TODO: Implement me!')
        #self.processor.process()
        #self.processor.project_cleaner.clean_current_workspace.assert_called()
