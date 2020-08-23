from .core import *


class Videos:

    def search_videos(self, **kwargs):
        """
        Search videos.

        :param search (optional): string, array
        :param output (optional): json, xml / default json
        :param category (optional): string
        :param page (optional): integer / default 1
        :param tags[] (optional): array
        :param stars[] (optional): array
        :param thumbsize (optional): medium, small, big, all, medium1, medium2
        :param ordering (optional): newest, mostviewed, rating
        :param period (optional): weekly, monthly, alltime
        """
        url = f"{BASE_URL}data=redtube.Videos.searchVideos"
        url += f"&output={kwargs.get('output', 'json')}"
        for k, v in kwargs.items():
            if k == "search":
                if type(v) in (list, set, tuple):
                    v = ','.join(v)
            elif k in ("tags", "stars"):
                k = f"{k}[]"
                v = urllib.parse.quote(",".join(v))
            url += f"&{GENERATE_URL.format(k, v)}"
        req = requests.get(url)
        return output(kwargs.get("output", "json"), req.text)


    def get_video_by_id(self, video_id, output_type="json", thumbsize=""):
        """
        get video by video_id.

        :param video_id (required): integer
        :param output_type (optional): json, xml / default json
        :param thumbsize (optional): medium, small, big, all, medium1, medium2
        """
        url = f"{BASE_URL}data=redtube.Videos.getVideoById&video_id={video_id}&output={output_type}"
        if thumbsize in ("medium", "small", "big", "all", "medium1", "medium2"):
            url += f"&thumbsize={thumbsize}"
        req = requests.get(url)
        return output(output_type, req.text)


    def is_video_active(self, video_id, output_type="json"):
        """
        is active by video_id.

        :param video_id (required): integer
        :param output_type (optional): json, xml / default json
        """
        url = f"{BASE_URL}data=redtube.Videos.isVideoActive&video_id={video_id}&output={output_type}"
        req = requests.get(url)
        return output(output_type, req.text)


    def get_video_embed_code(self, video_id, output_type="json"):
        """
        get video embed code by video_id.

        :param video_id (required): integer
        :param output_type (optional): json, xml / default json
        """
        url = f"{BASE_URL}data=redtube.Videos.getVideoEmbedCode&video_id={video_id}&output={output_type}"
        req = requests.get(url)
        return output(output_type, req.text)


    def get_deleted_videos(self, page=1, output_type="json"):
        """
        get deleted videos by page.

        :param page (required): integer / default 1
        :param output_type (optional): json, xml / default json
        """
        url = f"{BASE_URL}data=redtube.Videos.getDeletedVideos&page={page}&output={output_type}"
        req = requests.get(url)
        return output(output_type, req.text)