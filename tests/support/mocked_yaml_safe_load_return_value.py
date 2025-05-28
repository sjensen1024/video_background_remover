class MockedYamlSafeLoadReturnValue:
    def __init__(self, 
                 mocked_original_frames_directory = './tests/support/test_workspace/original_frames',
                 mocked_transparent_frames_directory = './tests/support/test_workspace/transparent_frames',
                 mocked_input_file = './tests/support/test_workspace/source_video.mp4',
                 mocked_output_file = './tests/support/test_workspace/result.mp4',
                 mocked_should_save_original_frames = True,
                 mocked_should_save_transparent_frames = True
                 ):
        self.mocked_original_frames_directory = mocked_original_frames_directory
        self.mocked_transparent_frames_directory = mocked_transparent_frames_directory
        self.mocked_input_file = mocked_input_file
        self.mocked_output_file = mocked_output_file
        self.mocked_should_save_original_frames = mocked_should_save_original_frames
        self.mocked_should_save_transparent_frames = mocked_should_save_transparent_frames

    def get_return_value(self):
        return {
            'original_frames_directory': self.mocked_original_frames_directory,
            'transparent_frames_directory': self.mocked_transparent_frames_directory,
            'input_file': self.mocked_input_file,
            'output_file': self.mocked_output_file,
            'should_save_original_frames': self.mocked_should_save_original_frames,
            'should_save_transparent_frames': self.mocked_transparent_frames_directory
        }
    