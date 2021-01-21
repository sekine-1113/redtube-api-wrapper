from .core import *


class Videos:

    def search_videos(
            self, search="", category="", page=1,
            tags=None, stars=None, thumbsize=None,
            ordering="mostviewed", period="monthly"):
        """
        Search videos.

        :param search (optional): string, array
        :param category (optional): string
        :param page (optional): integer / default 1
        :param tags (optional): array
        :param stars (optional): array
        :param thumbsize (optional): medium, small, big, all, medium1, medium2
        :param ordering (optional): newest, mostviewed, rating
        :param period (optional): weekly, monthly, alltime
        """
        params = {
            "data" : "redtube.Videos.searchVideos",
            "search" : search if type(search) is str else ",".join(search),
            "category" : category,
            "page" : page,
            "tags[]" : ",".join(tags) if tags is not None else None,
            "stars[]" : ",".join(stars) if stars is not None else None,
            "thumbsize" : thumbsize,
            "ordering" : ordering,
            "period" : period,
        }
        return output(URL, params)


    def get_video_by_id(self, video_id, thumbsize=None):
        """
        get video by video_id.

        :param video_id (required): integer
        :param thumbsize (optional): medium, small, big, all, medium1, medium2
        """
        params = {
            "data" : "redtube.Videos.getVideoById",
            "video_id" : video_id,
            "thumbsize" : thumbsize,
        }
        return output(URL, params)


    def is_video_active(self, video_id):
        """
        is active by video_id.

        :param video_id (required): integer
        """
        params = {
            "data" : "redtube.Videos.isVideoActive",
            "video_id" : video_id
        }
        return output(URL, params)


    def get_video_embed_code(self, video_id):
        """
        get video embed code by video_id.

        :param video_id (required): integer
        """
        params = {
            "data" : "redtube.Videos.getVideoEmbedCode",
            "video_id" : video_id
        }
        return output(URL, params)


    def get_deleted_videos(self, page=1):
        """
        get deleted videos by page.

        :param page (required): integer / default 1
        """
        params = {
            "data" : "redtube.Videos.getDeletedVideos",
            "page" : page,
        }
        return output(URL, params)