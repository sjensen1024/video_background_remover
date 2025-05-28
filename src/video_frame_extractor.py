from PIL import Image 
import numpy

class VideoFrameExtractor:
    def __init__(self, video):
        self.video = video

    def get_extracted_info(self):
        print('Extracting frames.')
        info = {
            'video': self.video,
            'total_frames': self.video.n_frames,
            'frames': []
        }
        count = 0
        for frame in self.video.iter_frames():
            count += 1
            frame_info = {
                'file_name': self.__get_frame_file_name(count),
                'image': self.__get_frame_as_image(frame)
            }
            info['frames'].append(frame_info)
        return info
    
    def __get_frame_file_name(self, current_frame_count):
        file_name = '_'
        duration_digits = self.__get_number_of_digits(self.video.n_frames)
        frame_digits = self.__get_number_of_digits(current_frame_count)
        if duration_digits == frame_digits:
            return file_name + str(current_frame_count) + '.png'
        prefix = '0' * (duration_digits - frame_digits)
        return file_name + prefix + str(current_frame_count) + '.png'

    def __get_number_of_digits(self, number):
        return len(str(abs(number)))
    
    def __get_frame_as_image(self, frame):
        return Image.fromarray(numpy.uint8(frame))
