"""A video player class."""

from operator import attrgetter
from .video_library import VideoLibrary
from .video_playlist import Playlist
import random


class VideoPlayer:
    """A class used to represent a Video Player."""

    def __init__(self):
        self._video_library = VideoLibrary() 
        self._video_playlists = {}
        self._current_video = None
        self._is_paused = False

    def number_of_videos(self):
        num_videos = len(self._video_library.get_all_videos())
        print(f"{num_videos} videos in the library")

    def show_all_videos(self):
        """Returns all videos."""
        video_list = self._video_library.get_all_videos()
        video_list.sort(key=attrgetter('title'))
    

        print("Here's a list of all available videos:")
        for video in video_list:
            video_tags = " ".join(video.tags)
            print(f"{video.title} ({video.video_id}) [{video_tags}]")

    def play_video(self, video_id):
        """Plays the respective video.
        
        Args:
            video_id: The video_id to be played.
        """

        video_list = self._video_library.get_all_videos()
        video_to_play = None

        for video in video_list:
            if video_id == video.video_id:
                video_to_play = video

        if video_to_play is not None:
            if self._current_video is not None:
                print(f"Stopping video: {self._current_video.title}")
                self._is_paused = False
            self._current_video = video_to_play
            print(f"Playing video: {video_to_play.title}")
            self._is_paused = False
        else :
            print("Cannot play video: Video does not exist")

    def stop_video(self):
        """Stops the current video."""
        video_list = self._video_library.get_all_videos()
        if self._current_video is not None:
            print(f"Stopping video: {self._current_video.title}")
            self._current_video = None
            self._is_paused = False
        else:
            print("Cannot stop video: No video is currently playing")
            

    def play_random_video(self):
        """Plays a random video from the video library."""
        video_list = self._video_library.get_all_videos()
        video_to_play = None

        if self._current_video is not None:
            print(f"Stopping video: {self._current_video.title}")
        video_to_play = random.choice(video_list)
        print(f"Playing video: {video_to_play.title}")

    def pause_video(self):
        """Pauses the current video."""
        if self._current_video is not None:
            if self._is_paused == False:
                print(f"Pausing video: {self._current_video.title}")
                self._is_paused = True
            else: 
                print(f"Video already paused: {self._current_video.title}")
        else:
            print("Cannot pause video: No video is currently playing")

    def continue_video(self):
        """Resumes playing the current video."""
        if self._current_video is not None:
            if self._is_paused == True:
                print(f"Continuing video: {self._current_video.title}")
                self._is_paused = False
            else:
                print("Cannot continue video: Video is not paused")
        else:
            print("Cannot continue video: No video is currently playing")

    def show_playing(self):
        """Displays video currently playing."""
        current_video_tags = None
        if self._current_video is not None:
            current_video_tags = " ".join(self._current_video.tags)
            video_details = f"Currently playing: {self._current_video.title} ({self._current_video.video_id}) [{current_video_tags}]"
            if self._is_paused == False:
                print(video_details)
            else:
                print(f"{video_details} - PAUSED")
        else:
            print("No video is currently playing")

    def create_playlist(self, playlist_name):
        """Creates a playlist with a given name.
        Args:
            playlist_name: The playlist name.
        """
        if playlist_name.lower() not in self._video_playlists:
            self._video_playlists[playlist_name.lower()] = Playlist(playlist_name)
            print(f"Successfully created new playlist: {playlist_name}")
        else:
            print("Cannot create playlist: A playlist with the same name already exists")

    def add_to_playlist(self, playlist_name, video_id):
        """Adds a video to a playlist with a given name.
        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be added.
        """
        video = self._video_library.get_video(video_id)

        if playlist_name.lower() not in self._video_playlists:
            print(f"Cannot add video to {playlist_name}: Playlist does not exist")
        elif video is None:
            print(f"Cannot add video to {playlist_name}: Video does not exist")
        elif self._video_playlists[playlist_name.lower()].get_video(video_id) is not None:
            print(f"Cannot add video to {playlist_name}: Video already added")
        else:
            print(f"Added video to {playlist_name}: {video.title}")
            self._video_playlists[playlist_name.lower()].add_video(video)


    def show_all_playlists(self):
        """Display all playlists."""
        names =[]
        if self._video_playlists:
            print("Showing all playlists:")
            for playlist in self._video_playlists.values():
                names.append(playlist.name)
            names_alphabetical = sorted(names)
            for name in names_alphabetical:
                print(name)
        else:
            print("No playlists exist yet")

    def show_playlist(self, playlist_name):
        """Display all videos in a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("show_playlist needs implementation")

    def remove_from_playlist(self, playlist_name, video_id):
        """Removes a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be removed.
        """
        print("remove_from_playlist needs implementation")

    def clear_playlist(self, playlist_name):
        """Removes all videos from a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("clears_playlist needs implementation")

    def delete_playlist(self, playlist_name):
        """Deletes a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("deletes_playlist needs implementation")

    def search_videos(self, search_term):
        """Display all the videos whose titles contain the search_term.

        Args:
            search_term: The query to be used in search.
        """
        print("search_videos needs implementation")

    def search_videos_tag(self, video_tag):
        """Display all videos whose tags contains the provided tag.

        Args:
            video_tag: The video tag to be used in search.
        """
        print("search_videos_tag needs implementation")

    def flag_video(self, video_id, flag_reason=""):
        """Mark a video as flagged.

        Args:
            video_id: The video_id to be flagged.
            flag_reason: Reason for flagging the video.
        """
        print("flag_video needs implementation")

    def allow_video(self, video_id):
        """Removes a flag from a video.

        Args:
            video_id: The video_id to be allowed again.
        """
        print("allow_video needs implementation")
