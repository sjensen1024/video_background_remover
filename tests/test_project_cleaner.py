import shutil
import unittest
from src.project_cleaner import ProjectCleaner
from definitions import ROOT_DIR

class TestProjectCleaner(unittest.TestCase):
    def setUp(self):
        self.workspace_path = ROOT_DIR + '\\tests\\support\\test_workspaces'
        self.original_frames_directory_name = 'original_frames'
        self.transparent_frames_directory_name = 'transparent_frames'
        self.result_file_name = 'result.mp4'

    def test_initialized_with_default_response_values(self):
        project_cleaner = ProjectCleaner()
        self.assert_new_project_cleaner_has_default_status(project_cleaner)

    def test_when_workspace_directory_does_not_exist(self):
        project_cleaner = self.__setup_test_project_cleaner('some_directory_that_does_not_exist')
        self.assert_new_project_cleaner_has_default_status(project_cleaner)
        project_cleaner.clean_current_workspace()
        self.assert_project_cleaner_status_shows_no_directories_or_files_exist(project_cleaner)

    def test_when_workspace_directory_exists_but_contains_no_files_or_directories(self):
        project_cleaner = self.__setup_test_project_cleaner('no_directories')
        self.assert_new_project_cleaner_has_default_status(project_cleaner)
        project_cleaner.clean_current_workspace()
        self.assert_project_cleaner_status_shows_no_directories_or_files_exist(project_cleaner)

    def test_when_workspace_directory_contains_directories_but_no_files(self):
        project_cleaner = self.__setup_test_project_cleaner('no_files')
        self.assert_new_project_cleaner_has_default_status(project_cleaner)
        project_cleaner.clean_current_workspace()
        self.assertEquals(
            project_cleaner.get_status(),
            {
                'clean_original_frames_result': 'This directory is empty, so it does not need cleaning.',
                'clean_transparent_frames_result': 'This directory is empty, so it does not need cleaning.',
                'clean_result_output_result': 'This file does not exist, so it cannot be removed.'
            }
        )

    def test_when_workspace_directory_contains_directories_and_files(self):
       project_cleaner = self.__setup_test_project_cleaner('has_files_and_directories')
       self.assert_new_project_cleaner_has_default_status(project_cleaner)
       project_cleaner.clean_current_workspace()
       self.assertEquals(
            project_cleaner.get_status(),
            {
                'clean_original_frames_result': 'Successfully cleaned.',
                'clean_transparent_frames_result': 'Successfully cleaned.',
                'clean_result_output_result': 'Successfully cleaned.'
            }
        )
       self.__repopulate_has_files_and_directories_workspace()

    def assert_new_project_cleaner_has_default_status(self, new_project_cleaner):
        self.assertEquals(
            new_project_cleaner.get_status(),
            {
                'clean_original_frames_result': 'Not yet run.',
                'clean_transparent_frames_result': 'Not yet run.',
                'clean_result_output_result': 'Not yet run.'
            }
        )

    def assert_project_cleaner_status_shows_no_directories_or_files_exist(self, project_cleaner):
        self.assertEquals(
            project_cleaner.get_status(),
            {
                'clean_original_frames_result': 'This directory does not exist, so it cannot be cleaned.',
                'clean_transparent_frames_result': 'This directory does not exist, so it cannot be cleaned.',
                'clean_result_output_result': 'This file does not exist, so it cannot be removed.'
            }
        )
    
    def __setup_test_project_cleaner(self, subdirectory_name):
        return ProjectCleaner(
            original_frames_directory_name = self.workspace_path + '\\' + subdirectory_name + '\\' + self.original_frames_directory_name,
            transparent_frames_directory_name = self.workspace_path + '\\' + subdirectory_name + '\\' + self.transparent_frames_directory_name,
            result_output_file_name = self.workspace_path + '\\' + subdirectory_name + '\\result.mp4'
        )

    def __repopulate_has_files_and_directories_workspace(self):
        media_directory = ROOT_DIR + '\\tests\\support\\media'
        video_path = media_directory + '\\videos\\result.mp4'
        image_1_path = media_directory + '\\images\\001.png'
        image_2_path = media_directory + '\\images\\002.png'
        has_files_and_directories_workspace_path = self.workspace_path + '\\has_files_and_directories'
        original_frames_path = has_files_and_directories_workspace_path + '\\' + self.original_frames_directory_name
        transparent_frames_path = has_files_and_directories_workspace_path + '\\' + self.transparent_frames_directory_name
        shutil.copy(video_path, has_files_and_directories_workspace_path)
        shutil.copy(image_1_path, original_frames_path)
        shutil.copy(image_2_path, original_frames_path)
        shutil.copy(image_1_path, transparent_frames_path)
        shutil.copy(image_2_path, transparent_frames_path)
