import sys
import json
import xml.etree.ElementTree as ET

def addAnime(malid):
    anime = ET.SubElement(myanimelist, "anime")
    series_animedb_id = ET.SubElement(anime, "series_animedb_id").text = malid

    #obligatory xml elements where content is irrelevant for this purpose
    series_title = ET.SubElement(anime, "series_title").text="a"
    series_type = ET.SubElement(anime, "series_type").text="TV"
    series_episodes = ET.SubElement(anime, "series_episodes").text="1"
    my_id = ET.SubElement(anime, "my_id").text="0"
    my_watched_episodes = ET.SubElement(anime, "my_watched_episodes").text="0"
    my_start_date = ET.SubElement(anime, "my_start_date").text="0000-00-00"
    my_finish_date = ET.SubElement(anime ,"my_finish_date").text="0000-00-00"
    my_rated = ET.SubElement(anime, "my_rated")
    my_score = ET.SubElement(anime, "my_score").text="0"
    my_storage = ET.SubElement(anime, "my_storage")
    my_storage_value = ET.SubElement(anime, "my_storage_value").text="0.00"
    my_status = ET.SubElement(anime, "my_status").text = "Plan to Watch"
    my_comments = ET.SubElement(anime, "my_comments").text=""
    my_times_watched = ET.SubElement(anime, "my_times_watched").text="0"
    my_rewatch_value = ET.SubElement(anime, "my_rewatch_value")
    my_priority = ET.SubElement(anime, "my_priority").text="LOW"
    my_tags = ET.SubElement(anime, "my_tags").text=""
    my_rewatching = ET.SubElement(anime, "my_rewatching").text="0"
    my_rewatching_ep = ET.SubElement(anime, "my_rewatching_ep").text="0"
    my_discuss = ET.SubElement(anime, "my_discuss").text="1"
    my_sns = ET.SubElement(anime, "my_sns").text="default"

    #must be 1 for obvious reasons
    update_on_import = ET.SubElement(anime, "update_on_import").text = "1"

myanimelist = ET.Element("myanimelist")

#more required but irrelevant elements
myinfo = ET.SubElement(myanimelist, "myinfo")
user_id = ET.SubElement(myinfo, "user_id").text="11395603"
user_name = ET.SubElement(myinfo, "user_name").text="LwLAMQThing"
user_export_type = ET.SubElement(myinfo, "user_export_type").text="1"
user_total_anime = ET.SubElement(myinfo, "user_total_anime").text="0"
user_total_watching = ET.SubElement(myinfo, "user_total_watching").text="0"
user_total_completed = ET.SubElement(myinfo, "user_total_completed").text="0"
user_total_onhold = ET.SubElement(myinfo, "user_total_onhold").text="0"
user_total_dropped = ET.SubElement(myinfo, "user_total_dropped").text="0"
user_total_plantowatch = ET.SubElement(myinfo, "user_total_plantowatch").text="0"

with open(sys.argv[1], errors="replace") as amqjson:
    data =json.load(amqjson)
    for song in data:
        if song["correct"]==False:
            addAnime(str(song["siteIds"]["malId"]))

tree = ET.ElementTree(myanimelist)
tree.write("animelist.xml")