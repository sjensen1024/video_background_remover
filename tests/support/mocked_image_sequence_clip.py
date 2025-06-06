class MockedImageSequenceClip:
    def __init__(self):
        self.mock_print_statement = 'This call is being made from an instance of MockedImageSequenceClip:'
        self.was_write_videofile_called_yet = False

    def get_was_write_videofile_called_yet(self):
        return self.was_write_videofile_called_yet

    def write_videofile(self, output_path):
        self.was_write_videofile_called_yet = True
        print(self.mock_print_statement + ' write_videofile passing in path of ' + output_path )
