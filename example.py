import redtube


client = redtube.RedTube()  # default json
#        redtube.RedTube("xml")

# -- start video methods --
print(client.search_videos(search="japanese")["videos"][0], end="\n\n")  # first data

video_id = 35215931  # sample
if client.is_video_active(video_id)["active"]["is_active"]:
    print(client.get_video_by_id(video_id), end="\n\n")
    print(client.get_video_embed_code(video_id), end="\n\n")
# -- end video methods --


# -- start additional methods --
print(client.get_categories_list()["categories"][0], end="\n\n")  # first data
print(client.get_tag_list()["tags"][0], end="\n\n")  # first data
print(client.get_star_list()["stars"][0], end="\n\n")  # first data
# -- end additional methods --
