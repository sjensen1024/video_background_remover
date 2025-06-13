import os

class ProjectCleaner:
    def __init__(self, original_frames_directory_name = '', transparent_frames_directory_name = '', background_color_frames_directory_name = '', result_output_file_name = ''):
        self.original_frames_directory_name = original_frames_directory_name
        self.transparent_frames_directory_name = transparent_frames_directory_name
        self.background_color_frames_directory_name = background_color_frames_directory_name
        self.result_output_file_name = result_output_file_name
        self.clean_original_frames_result = self.__status_messages().get('new')
        self.clean_transparent_frames_result = self.__status_messages().get('new')
        self.clean_background_color_frames_result = self.__status_messages().get('new')
        self.clean_result_output_result = self.__status_messages().get('new')

    def clean_current_workspace(self):
        print('Start the process of cleaning the current workspace.')
        self.__print_process_start_output_for_path(self.original_frames_directory_name)
        self.__clean_original_frames_directory()
        self.__print_process_result_output_for_path('clean_original_frames_result')
        self.__print_process_start_output_for_path(self.transparent_frames_directory_name)
        self.__clean_transparent_frames_directory()
        self.__print_process_result_output_for_path('clean_transparent_frames_result')
        self.__print_process_start_output_for_path(self.background_color_frames_directory_name)
        self.__clean_background_color_frames_directory()
        self.__print_process_result_output_for_path('clean_background_color_frames_result')
        self.__print_process_start_output_for_path(self.result_output_file_name)
        self.__clean_result_output()
        self.__print_process_result_output_for_path('clean_result_output_result')
        print('Finished the process of cleaning the current workspace.')

    def get_status(self):
        return {
            'clean_original_frames_result': self.clean_original_frames_result,
            'clean_transparent_frames_result': self.clean_transparent_frames_result,
            'clean_background_color_frames_result': self.clean_background_color_frames_result,
            'clean_result_output_result': self.clean_result_output_result
        }
    
    def __print_process_start_output_for_path(self, path):
        print('\tStarting cleaning process for ' + path)

    def __print_process_result_output_for_path(self, result_key):
        print('\t\tResult: ' + self.get_status().get(result_key))
    
    def __status_messages(self):
        return {
            'new': 'Not yet run.',
            'directory_does_not_exist': 'This directory does not exist, so it cannot be cleaned.',
            'directory_is_empty': 'This directory is empty, so it does not need cleaning.',
            'file_does_not_exist': 'This file does not exist, so it cannot be removed.',
            'success': 'Successfully cleaned.'
        }

    def __clean_original_frames_directory(self):
        self.__clean_all_pngs_in_directory(self.original_frames_directory_name)

    def __clean_transparent_frames_directory(self):
        self.__clean_all_pngs_in_directory(self.transparent_frames_directory_name)

    def __clean_background_color_frames_directory(self):
        self.__clean_all_pngs_in_directory(self.background_color_frames_directory_name)

    def __clean_result_output(self):
        if not os.path.exists(self.result_output_file_name):
            self.clean_result_output_result = self.__status_messages().get('file_does_not_exist')
            return
        os.remove(self.result_output_file_name)
        self.clean_result_output_result = self.__status_messages().get('success')

    def __clean_all_pngs_in_directory(self, directory):
        if not os.path.exists(directory):
            self.__set_status_result_for_directory(directory, self.__status_messages().get('directory_does_not_exist'))
            return   

        existing_file_names = os.listdir(directory)
        existing_png_file_names = list(filter(lambda file_name: file_name.endswith('png'), existing_file_names))
        if not existing_png_file_names:
            self.__set_status_result_for_directory(directory, self.__status_messages().get('directory_is_empty'))
            return
        
        [self.__delete_file_from_directory(file_name, directory) for file_name in existing_png_file_names]
        self.__set_status_result_for_directory(directory, self.__status_messages().get('success'))

    def __set_status_result_for_directory(self, directory, result_message):
        if directory == self.original_frames_directory_name:
            self.clean_original_frames_result = result_message
            return
        if directory == self.transparent_frames_directory_name:
            self.clean_transparent_frames_result = result_message
            return
        self.clean_background_color_frames_result = result_message

    def __delete_file_from_directory(self, file_name, directory):
        file_path = os.path.join(directory, file_name)
        os.unlink(file_path)
        print('\t\t' + file_name + ' deleted.')
            