from redtube import RedTube

client = RedTube()

"""https://api.redtube.com/?data=redtube.Videos.searchVideos&output=json&search=hard&tags[]=Teen&thumbsize=medium"""
print(client.search_videos(
    search = "hard",
    tags = "Teen",
    thumbsize = "medium"
))  # -> {"videos": [...]}
