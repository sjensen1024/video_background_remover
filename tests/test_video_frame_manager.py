import unittest
from unittest.mock import MagicMock
import moviepy
from src.video_frame_manager import VideoFrameManager
from src.frame_manager import FrameManager
from tests.support.mocked_image_sequence_clip import MockedImageSequenceClip
from definitions import ROOT_DIR

class TestVideoFrameManager(unittest.TestCase):
    def setUp(self):
       self.original_save_frame_call = FrameManager.save_frame
       self.original_remove_background_from_frame_call = FrameManager.remove_background_from_frame
       self.original_image_sequence_clip_call = moviepy.video.io.ImageSequenceClip.ImageSequenceClip
       FrameManager.save_frame = MagicMock(name='mock_frame_manager_save_frame')
       FrameManager.remove_background_from_frame = MagicMock(name='mock_frame_manager_remove_background_from_frame')
       moviepy.video.io.ImageSequenceClip.ImageSequenceClip = MagicMock(name='mock_image_sequence_clip')
       self.mocked_image_sequence_clip = MockedImageSequenceClip()
       moviepy.video.io.ImageSequenceClip.ImageSequenceClip.return_value = self.mocked_image_sequence_clip

    def tearDown(self):
        FrameManager.save_frame = self.original_save_frame_call
        FrameManager.remove_background_from_frame = self.original_remove_background_from_frame_call
        moviepy.video.io.ImageSequenceClip.ImageSequenceClip = self.original_image_sequence_clip_call

    def test_suite_for_video_with_single_digit_number_of_frames(self):
        video = moviepy.VideoFileClip(ROOT_DIR + '\\tests\\support\\media\\videos\\single_digit_frame_video.mp4')
        self.__run_test_suite_for_video(video, self.__expected_file_names_for_9_frames())

    def test_suite_for_video_with_more_than_single_digit_number_of_frames(self):
        video = moviepy.VideoFileClip(ROOT_DIR + '\\tests\\support\\media\\videos\\result.mp4')
        self.__run_test_suite_for_video(video, self.__expected_file_names_for_25_frames())

    def __run_test_suite_for_video(self, video, expected_file_names_in_sets):
        video_frame_manager = VideoFrameManager(video)
        self.__assert_original_video_is_instance_of_correct_class(video_frame_manager)
        self.__assert_set_contains_frame_managers_with_expected_file_names(
            video_frame_manager.get_original_frames(),  
            expected_file_names_in_sets
        )
        self.__assert_set_contains_frame_managers_with_expected_file_names(
            video_frame_manager.get_transparent_frames(),  
            expected_file_names_in_sets
        )
        self.__assert_method_was_called_for_frames_in_set(FrameManager.remove_background_from_frame, video_frame_manager.get_transparent_frames())
        self.assertIsNone(video_frame_manager.get_result_video())
        video_frame_manager.save_original_frames(ROOT_DIR + '\\tests\\support\\test_workspaces\\original_frames')
        self.__assert_method_was_called_for_frames_in_set(FrameManager.save_frame, video_frame_manager.get_original_frames())
        FrameManager.save_frame.call_count = 0
        video_frame_manager.save_transparent_frames(ROOT_DIR + '\\tests\\support\\test_workspaces\\transparent_frames')
        self.__assert_method_was_called_for_frames_in_set(FrameManager.save_frame, video_frame_manager.get_transparent_frames())
        self.__assert_correct_calls_are_made_in_save_result_video_from_transparent_frames(video_frame_manager)

    def __assert_original_video_is_instance_of_correct_class(self, video_frame_manager):
        self.assertIsInstance(video_frame_manager.get_original_video(), moviepy.video.io.VideoFileClip.VideoFileClip)

    def __assert_set_contains_frame_managers_with_expected_file_names(self, set_to_check, expected_file_names):
        for index, file_name in enumerate(expected_file_names):
            element_in_set = set_to_check[index]
            self.assertIsInstance(element_in_set, FrameManager)
            self.assertEqual(element_in_set.get_file_name(), file_name)

    def __assert_method_was_called_for_frames_in_set(self, method_called, frame_set):
        self.assertEqual(method_called.call_count, len(frame_set))

    def __assert_correct_calls_are_made_in_save_result_video_from_transparent_frames(self, video_frame_manager):
        video_frame_manager.save_result_video_from_transparent_frames('\\tests\\support\\test_workspaces')
        self.assertTrue(self.mocked_image_sequence_clip.get_was_write_videofile_called_yet())

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
    