import unittest
import moviepy
import PIL
from src.video_frame_extractor import VideoFrameExtractor
from definitions import ROOT_DIR

class TestProjectCleaner(unittest.TestCase):

    def test_get_extracted_info_when_video_has_single_digit_frames(self):
        video = moviepy.VideoFileClip(ROOT_DIR + '\\tests\\support\\media\\videos\\single_digit_frame_video.mp4')
        extracted_info = VideoFrameExtractor(video).get_extracted_info()
        self.assertTrue(isinstance(extracted_info.get('video'), moviepy.video.io.VideoFileClip.VideoFileClip))
        self.assertEqual(extracted_info.get('total_frames'), 9)
        frames = extracted_info.get('frames')
        for index, file_name in enumerate(self.__expected_file_names_for_9_frames()):
            frame_to_check = frames[index]
            self.assertEqual(frame_to_check.get('file_name'), file_name)

    def test_get_extracted_info_when_video_has_more_than_single_digit_frames(self):
        video = moviepy.VideoFileClip(ROOT_DIR + '\\tests\\support\\media\\videos\\result.mp4')
        extracted_info = VideoFrameExtractor(video).get_extracted_info()
        self.assertTrue(isinstance(extracted_info.get('video'), moviepy.video.io.VideoFileClip.VideoFileClip))
        self.assertEqual(extracted_info.get('total_frames'), 25)
        frames = extracted_info.get('frames')
        for index, file_name in enumerate(self.__expected_file_names_for_25_frames()):
            frame_to_check = frames[index]
            self.assertEqual(frame_to_check.get('file_name'), file_name)
            self.assertTrue(isinstance(frame_to_check.get('image'), PIL.Image.Image))

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