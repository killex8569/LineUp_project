import customtkinter
from frames.Youtube import Youtube


class controller:
    def __init__(self, app):
        self.current_frame = Youtube(master=app)