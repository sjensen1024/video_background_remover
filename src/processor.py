from src.config_manager import ConfigManager

class Processor:
    def __init__(self):
        self.config_manager = ConfigManager()
        
    def get_config_manager(self):
        return self.config_manager
    
    @classmethod
    def process(cls):
        print('Starting the process.')
        processor = Processor()
        # TODO: Implement and test the following:
        #  1) Clear existing files from project directories.
        #  2) Extract the frames from the video file and save them as images if the config says we should.
        #  3) Remove the backgrounds from the frames and save the resulting images if the config says we should.
        #  4) Convert the frames into an image sequence and output it as a video result.
        #  5) Add an option to add a background color/image to each frame (ex: green screen instead of black screen).
        #  6) Ensure we capture all the dependencies.
        print('Process finished!')
