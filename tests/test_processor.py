import unittest
from unittest.mock import MagicMock
from src.processor import Processor
from src.config_manager import ConfigManager
from src.project_cleaner import ProjectCleaner
from src.video_frame_manager import VideoFrameManager
from definitions import ROOT_DIR

class TestProcessor(unittest.TestCase):
    def setUp(self):
        self.test_config_directory = ROOT_DIR + '\\tests\\support\\test_configs\\'
        self.processor = Processor()
        self.original_processor_config_manager = self.processor.config_manager
        self.original_project_cleaner_clean_current_workspace = ProjectCleaner.clean_current_workspace
        ProjectCleaner.clean_current_workspace = MagicMock(name='test_processor_clean_current_workspace_mock')
        self.original_video_frame_manager_setup_frames = VideoFrameManager.setup_frames
        VideoFrameManager.setup_frames = MagicMock(name='test_processor_video_frame_manager_setup_frames_mock')
        self.original_video_frame_manager_save_original_frames = VideoFrameManager.save_original_frames
        VideoFrameManager.save_original_frames = MagicMock(name='test_processor_video_frame_manager_save_original_frames_mock')
        self.original_video_frame_manager_save_transparent_frames = VideoFrameManager.save_transparent_frames
        VideoFrameManager.save_transparent_frames = MagicMock(name='test_processor_video_frame_manager_save_transparent_frames_mock')
        self.original_video_frame_manager_save_background_color_frames = VideoFrameManager.save_background_color_frames
        VideoFrameManager.save_background_color_frames = MagicMock(name='test_processor_video_frame_manager_save_background_color_frames_mock')
        self.original_video_frame_manager_save_result_video_from_background_color_frames = VideoFrameManager.save_result_video_from_background_color_frames
        VideoFrameManager.save_result_video_from_background_color_frames = MagicMock(name='test_processor_video_frame_manager_save_result_video_from_background_color_frames_mock')

    def tearDown(self):
        self.processor.config_manager = self.original_processor_config_manager
        ProjectCleaner.clean_current_workspace = self.original_project_cleaner_clean_current_workspace 
        VideoFrameManager.setup_frames = self.original_video_frame_manager_setup_frames
        VideoFrameManager.save_original_frames = self.original_video_frame_manager_save_original_frames
        VideoFrameManager.save_transparent_frames = self.original_video_frame_manager_save_transparent_frames
        VideoFrameManager.save_background_color_frames = self.original_video_frame_manager_save_background_color_frames
        VideoFrameManager.save_result_video_from_background_color_frames = self.original_video_frame_manager_save_result_video_from_background_color_frames

    def test_processor_with_all_config_booleans_true(self):
        self.processor.config_manager = ConfigManager(config_yaml_path=self.test_config_directory + 'test_processor_config_booleans_true.yml')
        self.processor.process()
        ProjectCleaner.clean_current_workspace.assert_called()
        VideoFrameManager.setup_frames.assert_called()
        VideoFrameManager.save_original_frames.assert_called()
        VideoFrameManager.save_transparent_frames.assert_called()
        VideoFrameManager.save_background_color_frames.assert_called()
        VideoFrameManager.save_result_video_from_background_color_frames.assert_called()

    def test_processor_with_all_config_booleans_false(self):
        self.processor.config_manager = ConfigManager(config_yaml_path=self.test_config_directory + 'test_processor_config_booleans_false.yml')
        self.processor.process()
        ProjectCleaner.clean_current_workspace.assert_called()
        VideoFrameManager.setup_frames.assert_called()
        VideoFrameManager.save_original_frames.assert_not_called()
        VideoFrameManager.save_transparent_frames.assert_not_called()
        VideoFrameManager.save_background_color_frames.assert_not_called()
        VideoFrameManager.save_result_video_from_background_color_frames.assert_called()
