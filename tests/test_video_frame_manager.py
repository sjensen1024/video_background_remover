import unittest
from unittest.mock import MagicMock
import moviepy
import PIL
from rembg import remove
from src.video_frame_manager import VideoFrameManager
from definitions import ROOT_DIR

class TestVideoFrameManager(unittest.TestCase):
    def test_new_video_frame_manager_when_video_has_single_digit_frames(self):
        video = moviepy.VideoFileClip(ROOT_DIR + '\\tests\\support\\media\\videos\\single_digit_frame_video.mp4')
        video_frame_manager = VideoFrameManager(video)
        self.__assert_original_video_is_instance_of_correct_class(video_frame_manager)
        self.__assert_frame_info_is_set_up_correctly(video_frame_manager.get_original_frame_info(),  self.__expected_file_names_for_9_frames())
        self.__assert_frame_info_is_set_up_correctly(video_frame_manager.get_transparent_frame_info(),  self.__expected_file_names_for_9_frames())

    def test_new_video_frame_manager_when_video_has_more_than_single_digit_frames(self):
        video = moviepy.VideoFileClip(ROOT_DIR + '\\tests\\support\\media\\videos\\result.mp4')
        video_frame_manager = VideoFrameManager(video)
        self.__assert_original_video_is_instance_of_correct_class(video_frame_manager)
        self.__assert_frame_info_is_set_up_correctly(video_frame_manager.get_original_frame_info(),  self.__expected_file_names_for_25_frames())
        self.__assert_frame_info_is_set_up_correctly(video_frame_manager.get_transparent_frame_info(),  self.__expected_file_names_for_25_frames())

    def test_save_original_frames(self):
        video = moviepy.VideoFileClip(ROOT_DIR + '\\tests\\support\\media\\videos\\single_digit_frame_video.mp4')
        video_frame_manager = VideoFrameManager(video)
        PIL.Image.Image.save = MagicMock(name='mock_image_save')
        video_frame_manager.save_original_frames(ROOT_DIR + '\\tests\\support\\test_workspaces\\original_frames')
        assert all(frame_info.get('image_saved') == True for frame_info in video_frame_manager.get_original_frame_info())

    def test_save_transparent_frames(self):
        video = moviepy.VideoFileClip(ROOT_DIR + '\\tests\\support\\media\\videos\\single_digit_frame_video.mp4')
        video_frame_manager = VideoFrameManager(video)
        PIL.Image.Image.save = MagicMock(name='mock_image_save')
        video_frame_manager.save_transparent_frames(ROOT_DIR + '\\tests\\support\\test_workspaces\\transparent_frames')
        assert all(frame_info.get('image_saved') == True for frame_info in video_frame_manager.get_transparent_frame_info())

    def __assert_original_video_is_instance_of_correct_class(self, video_frame_manager):
        self.assertTrue(isinstance(video_frame_manager.get_original_video(), moviepy.video.io.VideoFileClip.VideoFileClip))

    def __assert_frame_info_is_set_up_correctly(self, frame_info, expected_frame_file_names):
        for index, file_name in enumerate(expected_frame_file_names):
            frame_to_check = frame_info[index]
            self.assertEqual(frame_to_check.get('file_name'), file_name)
            self.assertTrue(isinstance(frame_to_check.get('image'), PIL.Image.Image))
            self.assertFalse(frame_to_check.get('image_saved'))

    def __expected_file_names_for_9_frames(self):
        return [
                    '_1.png',
                    '_2.png',
                    '_3.png',
                    '_4.png',
                    '_5.png',
                    '_6.png',
                    '_7.png',
                    '_8.png',
                    '_9.png'
                ]

    def __expected_file_names_for_25_frames(self):
        return [
                    '_01.png',
                    '_02.png',
                    '_03.png',
                    '_04.png',
                    '_05.png',
                    '_06.png',
                    '_07.png',
                    '_08.png',
                    '_09.png',
                    '_10.png',
                    '_11.png',
                    '_12.png',
                    '_13.png',
                    '_14.png',
                    '_15.png',
                    '_16.png',
                    '_17.png',
                    '_18.png',
                    '_19.png',
                    '_20.png',
                    '_21.png',
                    '_22.png',
                    '_23.png',
                    '_24.png',
                    '_25.png'
                ]