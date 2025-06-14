class MockedVideoFrameManager:
    def __init__(self, original_video, background_color_set):
        self.mock_print_statement = 'This call is being made from an instance of MockedVideoFrameManager:'
        self.original_video = original_video
        self.background_color_set = background_color_set
        self.was_save_original_frames_called_yet = False
        self.was_save_transparent_frames_called_yet = False
        self.was_save_background_color_frames_called_yet = False
        self.was_save_result_video_from_background_color_frames_called_yet = False

    def get_was_save_original_frames_called_yet(self):
        return self.was_save_original_frames_called_yet
    
    def get_was_save_transparent_frames_called_yet(self):
        return self.was_save_transparent_frames_called_yet
    
    def get_was_save_background_color_frames_called_yet(self):
        return self.was_save_background_color_frames_called_yet
    
    def get_was_save_result_video_from_background_color_frames_called_yet(self):
        return self.was_save_result_video_from_background_color_frames_called_yet

    def save_original_frames(self, output_path):
        self.was_save_original_frames_called_yet = True
        print(self.mock_print_statement + ' save_original_frames passing in ' + output_path )

    def save_transparent_frames(self, output_path):
        self.was_save_transparent_frames_called_yet = True
        print(self.mock_print_statement + ' save_transparent_frames passing in ' + output_path )

    def save_background_color_frames(self, output_path):
        self.was_save_background_color_frames_called_yet = True
        print(self.mock_print_statement + ' save_background_color_frames passing in ' + output_path )

    def save_result_video_from_background_color_frames(self, output_path):
        self.was_save_result_video_from_background_color_frames_called_yet = True
        print(self.mock_print_statement + ' save_result_video_from_background_color_frames passing in ' + output_path )
