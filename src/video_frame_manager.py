from PIL import Image 
from rembg import remove
import numpy

class VideoFrameManager:
    def __init__(self, original_video):
        self.original_video = original_video
        self.original_frame_info = self.__extract_original_frame_info()
        self.transparent_frame_info = self. __setup_transparent_frame_info()
    
    def get_original_video(self):
        return self.original_video
    
    def get_original_frame_info(self):
        return self.original_frame_info
    
    def get_transparent_frame_info(self):
        return self.transparent_frame_info
    
    def save_original_frames(self, frame_directory_path):
        self.__save_frames(frame_directory_path, self.original_frame_info)

    def save_transparent_frames(self, frame_directory_path):
        self.__save_frames(frame_directory_path, self.transparent_frame_info)

    # TODO: Instead of using a key value pair,
    #       make a class for info on an individual frame and do the save there.
    #       That way we don't bloat our tests with a bunch of saves and background removal calls.
    def __save_frames(self, frame_directory_path, frame_info_set):
        for index, frame_info in enumerate(frame_info_set):
            file_path = frame_directory_path + '\\' + frame_info.get('file_name')
            frame_info.get('image').save(file_path)
            frame_info_set[index]['image_saved'] = True
            print ('Saved ' + file_path)

    def __extract_original_frame_info(self):
        print('Extracting original frames from video.')
        frame_info_set = []
        for index, frame in enumerate(self.original_video.iter_frames()):
            frame_info = {
                'file_name': self.__get_frame_file_name(index + 1),
                'image': self.__get_frame_as_image(frame),
                'image_saved': False
            }
            frame_info_set.append(frame_info)
        print(str(self.original_video.n_frames) + ' frames extracted.')
        return frame_info_set
    
    def __setup_transparent_frame_info(self):
        print('Setting up transparent versions of the frames')
        transparent_frame_info_set = []
        for index, original_frame_info in enumerate(self.original_frame_info):
            transparent_frame_info = {
                'file_name': original_frame_info.get('file_name'),
                'image': remove(original_frame_info.get('image')),
                'image_saved': False
            }
            transparent_frame_info_set.append(transparent_frame_info)
            print('Extracted background from ' + original_frame_info.get('file_name'))
        return transparent_frame_info_set
    
    def __get_frame_file_name(self, current_frame_count):
        file_name = '_'
        duration_digits = self.__get_number_of_digits(self.original_video.n_frames)
        frame_digits = self.__get_number_of_digits(current_frame_count)
        if duration_digits == frame_digits:
            return file_name + str(current_frame_count) + '.png'
        prefix = '0' * (duration_digits - frame_digits)
        return file_name + prefix + str(current_frame_count) + '.png'

    def __get_number_of_digits(self, number):
        return len(str(abs(number)))
    
    def __get_frame_as_image(self, frame):
        return Image.fromarray(numpy.uint8(frame))
