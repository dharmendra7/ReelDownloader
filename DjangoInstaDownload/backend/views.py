from django.http import HttpResponse
from django.shortcuts import redirect, render
from rest_framework.generics import GenericAPIView,RetrieveAPIView
from rest_framework.permissions import AllowAny
from .serializers import *
from .models import *
from rest_framework.response import Response
from common.utils.views import send_response, send_response_validation, validate_token, required_header, required_header_validate, isUserAuth
from drf_spectacular.utils import extend_schema, OpenApiParameter
from drf_spectacular.types import OpenApiTypes
from instagrapi import Client
from django.utils.translation import gettext_lazy as _

from urllib.parse import urlparse

import instaloader
from instaloader import Profile, Post

# Create your views here.
ACCOUNT_USERNAME =     "mrunal.shah.58"      # "solvederror081"
ACCOUNT_PASSWORD =      'solved123'                        #"solved@123"


headerParam = [OpenApiParameter(
    name='Link', 
    location=OpenApiParameter.HEADER,
    type=OpenApiTypes.STR,
    description='Paste your link here',
    required=True,
),]

def index(request):
    return render(request,"index.html")

def pureLink(request): 
    # print(request.POST['link'])
    url = urlparse(request.POST['link'])
    #ParseResult(scheme='https', netloc='www.instagram.com', path='/tv/CeAvvgFgpMc/', params='', query='utm_source=ig_web_copy_link', fragment='')
    sort_url = url.path.split('/')[2]
    # print(sort_url)

    instance = instaloader.Instaloader(download_video_thumbnails=False,save_metadata=False)
    instance.login(ACCOUNT_USERNAME, ACCOUNT_PASSWORD)  
    post = Post.from_shortcode(instance.context, str(sort_url))
    # print(post.caption)
    print(post.video_url)
    # print(post.url)
    # instance.download_post(post,target="media")
    video_url = post.video_url
    # thumbnails_url = post.url
    import webbrowser
    # webbrowser.open(video_url,new=0)
    return redirect(video_url)

    # return render(request,"video.html",{"video_url":video_url,"thumbnails_url":thumbnails_url})


class ReelDownloadLink(GenericAPIView):
    serializer_class = LinkSerializer
    
    
    @extend_schema(
    parameters=headerParam,
    responses={200:ReelResponse,400: errorResponse()},
    summary='Paste Reel link to download the Reel'
    )
    def get(self, request):
        try:
            url = urlparse(self.request.headers['link'])
            #ParseResult(scheme='https', netloc='www.instagram.com', path='/tv/CeAvvgFgpMc/', params='', query='utm_source=ig_web_copy_link', fragment='')
            
            sort_url = url.path.split('/')[2]
            # instance = instaloader.Instaloader(download_video_thumbnails=False,save_metadata=False)
            # instance.login(ACCOUNT_USERNAME, ACCOUNT_PASSWORD)  
            
            # post = Post.from_shortcode(instance.context, str(sort_url))
            # video_url = post.video_url
            
            cl = Client()
            cl.login(ACCOUNT_USERNAME, ACCOUNT_PASSWORD)
            print("login success")
            data1 = cl.media_pk_from_url(self.request.headers['link'])
            data = cl.media_info(data1).dict()
            lst = []
            # print(data['video_url'])




            return send_response(request, code=200, message= _("Success"), data=data['video_url'])
        
        except Exception as e:
            return send_response_validation(request, code=205, message= str(e))


class DownloadPost(RetrieveAPIView):
    serializer_class = LinkSerializer
    
    @extend_schema(
    parameters=headerParam,
    responses={200:ReelResponse(),400: errorResponse()},
    summary='Paste Post link to download the Post'
    )

    def get(self, request):
        try:
            url = urlparse(self.request.headers['link'])
            #ParseResult(scheme='https', netloc='www.instagram.com', path='/tv/CeAvvgFgpMc/', params='', query='utm_source=ig_web_copy_link', fragment='')
            
            sort_url = url.path.split('/')[2]
            # instance = instaloader.Instaloader()
            # instance.login(ACCOUNT_USERNAME, ACCOUNT_PASSWORD)  
            
            # post = Post.from_shortcode(instance.context, str(sort_url))
            # img_url = post.__dict__['_node']['display_url']
            cl = Client()
            cl.login(ACCOUNT_USERNAME, ACCOUNT_PASSWORD)
            print("login success")
            data1 = cl.media_pk_from_url(self.request.headers['link'])
            data = cl.media_info(data1).dict()
            lst = []
            if data['resources'] != []:
                # print(data['resources'][0])
                for i in data['resources']:
                    lst.append({
                            "image" : i['thumbnail_url']
                        })
                    
            else:
                lst.append({
                    "image" : data['thumbnail_url']
                    })
            
            return send_response(request, code=200, message= _("Success"), data=lst)
        
        except Exception as e:
            return send_response_validation(request, code=205, message= str(e))

 
class Profile(RetrieveAPIView):
    serializer_class = LinkSerializer
    
    @extend_schema(
    parameters=headerParam,
    responses={200:ReelResponse,400: errorResponse()},
    summary='Paste user profile link to Get profile of user'
    )


    def get(self, request):
        try:
            url = urlparse(self.request.headers['link'])
            sort_url = url.path.split('/')[1]
            cl = Client()
            cl.login(ACCOUNT_USERNAME, ACCOUNT_PASSWORD)
            print("login success")     
            t= cl.user_info_by_username(str(sort_url)).dict()

            return send_response(request, code=200, message= _("Success"),data=t)
        
        except Exception as e:
            return send_response_validation(request, code=205, message= str(e))


class StoryDownload(RetrieveAPIView):
    serializer_class = LinkSerializer
    
    @extend_schema(
    parameters=headerParam,
    responses={200:ReelResponse,400: errorResponse()},
    summary='Paste Story link to download Story'
    )


    def get(self, request):
        try:
            url = urlparse(self.request.headers['link'])
            #ParseResult(scheme='https', netloc='www.instagram.com', path='/tv/CeAvvgFgpMc/', params='', query='utm_source=ig_web_copy_link', fragment='')
            sort_url = url.path.split('/')[3]

            cl = Client()
            cl.login(ACCOUNT_USERNAME, ACCOUNT_PASSWORD)
            print("login success")
            s = cl.story_info(sort_url)
        
            if s.video_url is None:
                data = s.thumbnail_url
            else:
                data = s.video_url
            
            return send_response(request, code=200, message= _("Success"),data=data)
        
        except Exception as e:
            return send_response_validation(request, code=205, message= str(e))