import unittest
from unittest.mock import MagicMock
import moviepy
import PIL
import rembg
from src.frame_manager import FrameManager
from definitions import ROOT_DIR

class TestFrameManager(unittest.TestCase):
    def setUp(self):
        self.sample_file_name = '__01.png'
        self.sample_frame = moviepy.VideoFileClip(ROOT_DIR + '\\tests\\support\\media\\videos\\single_digit_frame_video.mp4').get_frame(1)
        self.frame_manager = FrameManager(self.sample_file_name, self.sample_frame)

    def test_new_frame_manager_has_correct_setup(self):
        self.assertEqual(self.frame_manager.get_file_name(), self.sample_file_name)
        self.assertTrue(isinstance(self.frame_manager.get_frame(), PIL.Image.Image))
        self.assertFalse(self.frame_manager.get_is_saved())

    def test_save_changes_is_saved_attribute(self):
        PIL.Image.Image.save = MagicMock(name='mock_image_save')
        self.frame_manager.save_frame(ROOT_DIR + '\\support\\test_workspaces\\has_files_and_directories\\original_frames')
        self.assertTrue(self.frame_manager.get_is_saved())
        PIL.Image.Image.save = PIL.Image.Image.save

    def test_rembg_remove_is_called_on_remove_background_from_frame(self):
        original_rembg_remove = rembg.remove
        rembg.remove = MagicMock(name='mock_rembg_remove')
        self.frame_manager.remove_background_from_frame()
        rembg.remove.assert_called()
        rembg.remove = original_rembg_remove
