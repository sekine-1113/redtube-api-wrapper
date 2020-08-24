from .core import *


class Additionals:

    def __init__(self, output_type):
        self._output_type = output_type


    def get_categories_list(self):
        """
        get categories list.
        """
        url = f"{BASE_URL}data=redtube.Categories.getCategoriesList&output={self._output_type}"
        req = requests.get(url)
        return output(self._output_type, req.text)


    def get_tag_list(self):
        """
        get tags list.
        """
        url = f"{BASE_URL}data=redtube.Tags.getTagList&output={self._output_type}"
        req = requests.get(url)
        return output(self._output_type, req.text)


    def get_star_list(self):
        """
        get stars list.
        """
        url = f"{BASE_URL}data=redtube.Stars.getStarList&output={self._output_type}"
        req = requests.get(url)
        return output(self._output_type, req.text)


    def get_star_detailed_list(self):
        """
        get categories list.
        """
        url = f"{BASE_URL}data=redtube.Stars.getStarDetailedList&output={self._output_type}"
        req = requests.get(url)
        return output(self._output_type, req.text)