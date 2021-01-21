from .core import *


class Informations:

    def get_video_categories(self):
        """
        get categories list.
        """
        params = {"data":"redtube.Categories.getCategoriesList",}
        return output(URL, params)


    def get_tag_list(self):
        """
        get tags list.
        """
        params = {"data":"redtube.Tags.getTagList",}
        return output(URL, params)


    def get_star_list(self):
        """
        get stars list.
        """
        params = {"data":"redtube.Stars.getStarList",}
        return output(URL, params)


    def get_star_detailed_list(self):
        """
        get categories list.
        """
        params = {"data":"redtube.Stars.getStarDetailedList",}
        return output(URL, params)