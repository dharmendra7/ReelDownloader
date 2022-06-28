# Get instance
# import instaloader

# L = instaloader.Instaloader()

# # Login or load session
# username = "mrunal.shah.58"
# password = "Mrunal@123"
# L.login(username, password)  # (login)

# # Obtain profile metadata
# profile = instaloader.Profile.from_username(L.context, 'sonagara_bhargav')

# # Print list of followees
# follow_list = []
# count = 0
# for followee in profile.get_followers():
#     follow_list.append(followee.username)
#     file = open("prada_followers.txt", "a+")
#     file.write(follow_list[count])
#     file.write("\n")
#     file.close()
#     # print(follow_list[count])
#     count = count + 1
# print(count)
# (likewise with profile.get_followers())

# post = Post.from_shortcode(instance.context, "https://www.instagram.com/p/CewBPdwroE1/?utm_source=ig_web_copy_link")

# instance.download_post(post,target="Insta")

# import requests
# import re

# def get_response(url):
#     r = requests.get(url)
#     while r.status_code != 200:
#         r = requests.get(url)
#     return r.text

# def prepare_urls(matches):
#     return list({match.replace("\\u0026", "&") for match in matches})

# url = input('Enter Instagram URL: ')
# response = get_response(url)

# vid_matches = re.findall('"video_url":"([^"]+)"', response)
# pic_matches = re.findall('"display_url":"([^"]+)"', response)

# vid_urls = prepare_urls(vid_matches)
# pic_urls = prepare_urls(pic_matches)

# if vid_urls:
#     print('Detected Videos:\n{0}'.format('\n'.join(vid_urls)))

# if pic_urls:
#     print('Detected Pictures:\n{0}'.format('\n'.join(pic_urls)))

# if not (vid_urls or pic_urls):
#     print('Could not recognize the media in the provided URL.')

# import os
# import urllib.request
# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys

# current_path = os.path.dirname(os.path.realpath(__file__))
# exc_path = current_path + '/geckodriver'


# def video_downloader(url):
#     driver = webdriver.Firefox(executable_path=r'%s' % exc_path)
#     driver.get(url)
#     elementName = driver.find_elements_by_class_name("tWeCl")
#     src_url = elementName[0].get_attribute("src")
#     video_name = (url.split('/'))[4]
#     print(video_name)
#     url_link = src_url
#     urllib.request.urlretrieve(url_link, video_name + '.mp4')
#     driver.close()


# def main():
#     url = input("Please enter url_link> ")
#     video_downloader(url)


# if __name__ == '__main__':
#     main()
username = "mrunal.shah.58"
password = "dharmesh123"

from instagrapi import Client
cl = Client()
cl.login(username, password)
cl.story_download(cl.story_pk_from_url('https://www.instagram.com/stories/python.learning/2861211093694405244/'))
s = cl.story_info(2861211093694405244)

cl.story_download_by_url(s.video_url)
