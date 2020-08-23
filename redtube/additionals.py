from .core import *


class Additionals:


    def get_categories_list(self, output_type="json"):
        """
        get categories list.

        :param output_type (optional): json, xml / default json
        """
        url = f"{BASE_URL}data=redtube.Categories.getCategoriesList&output={output_type}"
        req = requests.get(url)
        return output(output_type, req.text)


    def get_tag_list(self, output_type="json"):
        """
        get tags list.

        :param output_type (optional): json, xml / default json
        """
        url = f"{BASE_URL}data=redtube.Tags.getTagList&output={output_type}"
        req = requests.get(url)
        return output(output_type, req.text)


    def get_star_list(self, output_type="json"):
        """
        get stars list.

        :param output_type (optional): json, xml / default json
        """
        url = f"{BASE_URL}data=redtube.Stars.getStarList&output={output_type}"
        req = requests.get(url)
        return output(output_type, req.text)


    def get_star_detailed_list(self, output_type="json"):
        """
        get categories list.

        :param output_type (optional): json, xml / default json
        """
        url = f"{BASE_URL}data=redtube.Stars.getStarDetailedList&output={output_type}"
        req = requests.get(url)
        return output(output_type, req.text)