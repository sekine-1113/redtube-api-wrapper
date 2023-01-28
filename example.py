from redtubeAPI import redtube

client = redtube.RedTube()

print(client.get_tag_list())