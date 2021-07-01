"""A video playlist class."""


class Playlist:
    """A class used to represent a Playlist."""

    def __init__(self, playlist_name):
        self.name = playlist_name
        self._track_list = []
    
    def add_video(self, video):
        self._track_list.append(video)
    
    def get_video(self, video_id):
        for track in self._track_list:
            if video_id == track.video_id:
                return track
        return None