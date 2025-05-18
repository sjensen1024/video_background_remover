import os

class ProjectCleaner:
    def __init__(self, original_frames_directory_name = '', transparent_frames_directory_name = '', result_output_file_name = ''):
        self.original_frames_directory_name = original_frames_directory_name
        self.transparent_frames_directory_name = transparent_frames_directory_name
        self.result_output_file_name = result_output_file_name

    def clean_current_workspace(self):
        print('Start the process of cleaning the project.')
        self.__clean_original_frames_directory()
        self.__clean_transparent_frames_directory()
        self.__clean_result_output()
        print('Finished the process of cleaning the current project.')

    def __clean_original_frames_directory(self):
        self.__clean_all_files_in_directory(self.original_frames_directory_name)

    def __clean_transparent_frames_directory(self):
        self.__clean_all_files_in_directory(self.transparent_frames_directory_name)

    def __clean_result_output(self):
        if not os.path.exists(self.result_output_file_name):
            print('Output file - ' + self.result_output_file_name + ' - does not exist. Nothing to clean up here.')
            return
        print('Removing output file: ' + self.result_output_file_name + ' ...')
        os.remove(self.result_output_file_name)
        print('Output file ' + self.result_output_file_name + ' successfully removed.')

    def __clean_all_files_in_directory(self, directory):
        if not os.path.exists(directory):
            print('Directory ' + directory + ' does not exist. Nothing to delete here.')
            return   

        existing_file_names = os.listdir(directory)
        if not existing_file_names:
            print('Directory ' + directory + ' does not contain any files. Nothing to clean up here.')
            return
        
        print('Cleaning directory ' + directory + ' ...')
        for file_name in existing_file_names:
            file_path = os.path.join(directory, file_name)
            if os.path.isfile(file_path):
                os.unlink(file_path)
                print(file_name + ' deleted.')
        print('Directory ' + directory + ' successfully cleaned.')
