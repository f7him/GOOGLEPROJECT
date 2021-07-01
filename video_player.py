"""A video player class."""

from .video_library import VideoLibrary
from .video import Video
from typing import Sequence


class VideoPlayer:
    """A class used to represent a Video Player."""

    def __init__(self):
        self._video_library = VideoLibrary()
        self.video1 = Video(video_title="Amazing Cats", video_id="amazing_cats_video_id", video_tags=["#cat #animal"])
        self.video2 = Video(video_title="Another Cat Video", video_id="another_cat_video_id",
                            video_tags=["#cat #animal"])
        self.video3 = Video(video_title="Funny Dogs", video_id="funny_dogs_video_id", video_tags=["#dog #animal"])
        self.video4 = Video(video_title="Life at Google", video_id="life_at_google_video_id",
                            video_tags=["#google #career"])
        self.video5 = Video(video_title="Video about nothing", video_id="nothing_video_id", video_tags=[""])
        self.videoTitle = ""
        self.videoPlaying = 1
        self.videoPaused = 0
        self.newPlaylistname = ""
        self.playlist = [""]

    def number_of_videos(self):
        num_videos = len(self._video_library.get_all_videos())
        print(num_videos, "videos in the library")

    def show_all_videos(self):
        """Returns all videos."""
        print("Here's a list of all available videos:")
        print(self.video1.title, "(", self.video1.video_id, ")", self.video1.tags)
        print(self.video2.title, "(", self.video1.video_id, ")", self.video1.tags)
        print(self.video3.title, "(", self.video1.video_id, ")", self.video1.tags)
        print(self.video4.title, "(", self.video1.video_id, ")", self.video1.tags)
        print(self.video5.title, "(", self.video1.video_id, ")", self.video1.tags)

    def play_video(self, video_id):
        if self.videoPlaying == 0:
            print("Stopping video:", self.videoTitle)
            self.videoPlaying = 1
        if video_id == "amazing_cats_video_id" and self.videoPlaying:
            print("Playing video:", self.video1.title)
            self.videoTitle = "Amazing Cats"
            self.videoPlaying = 0
        elif video_id == "another_cat_video_id" and self.videoPlaying:
            print("Playing video:", self.video2.title)
            self.videoTitle = "Another Cat Video"
            self.videoPlaying = 0
        elif video_id == "funny_dogs_video_id" and self.videoPlaying:
            print("Playing video:", self.video3.title)
            self.videoTitle = "Funny Dogs"
            self.videoPlaying = 0
        elif video_id == "life_at_google_video_id" and self.videoPlaying:
            print("Playing video:", self.video4.title)
            self.videoTitle = "Life at Google"
            self.videoPlaying = 0
        elif video_id == "nothing_video_id" and self.videoPlaying:
            print("Playing video:", self.video5.title)
            self.videoTitle = "Video about nothing"
            self.videoPlaying = 0
        else:
            print("Cannot play video: Video does not exist")
            self.videoPlaying = 0

    def stop_video(self):
        """Stops the current video."""
        if self.videoTitle == "":
            print("Cannot stop video: No video is currently playing")
        else:
            print("Stopping video:", self.videoTitle)
            self.videoTitle = ""

    def play_random_video(self):
        """Plays a random video from the video library."""

        print("play_random_video needs implementation")

    def pause_video(self):
        """Pauses the current video."""
        if self.videoTitle == "":
            print("Cannot pause video: No video is currently playing")
        elif self.videoPaused == 0 and self.videoTitle != "":
            print("Pausing video:", self.videoTitle)
            self.videoPaused = 1
        elif self.videoPaused == 1 and self.videoTitle != "":
            print("Video already paused:", self.videoTitle)

    def continue_video(self):
        """Resumes playing the current video."""
        if self.videoPaused == 1:
            print("Continuing video:", self.videoTitle)
            self.videoPaused = 0
        elif self.videoPaused != 1:
            print("Cannot continue video: Video is not paused")

    def show_playing(self):
        """Displays video currently playing."""
        if self.videoTitle == "Amazing Cats":
            print("Currently playing:", self.video1.title, self.video1.video_id, self.video1.tags)
        elif self.videoTitle == "":
            print("No video is currently playing")

    def create_playlist(self, playlist_name):

        if playlist_name != self.newPlaylistname:
            print("Successfully created new playlist:", playlist_name)
            self.newPlaylistname = playlist_name
            self.playlist = [playlist_name]


    def add_to_playlist(self, playlist_name, video_id):

        self.playlist.append(video_id)
        print("Added video to my_cool_PLAYLIST:",  video_id)

    def show_all_playlists(self):
        """Display all playlists."""

        print("show_all_playlists needs implementation")

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
