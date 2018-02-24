from rest_framework.views import APIView
from rest_framework.response import Response
from models import Notification
import datetime
import json
from django.http import HttpResponse
from serializer import NotificationSerializer

#
# def index(request):
#     print "HEREHERE"
#     if request.method == 'POST':
#         # save new post
#         data = request.POST
#         sender = data['sender']
#         content = data['content']
#         if 'request_moderation' in data:
#             request_moderation = data['request_moderation']
#         else:
#             request_moderation = False
#         post = Notification(sender=sender)
#         post.created_at = datetime.datetime.now()
#         post.content = content
#         post.active = True
#         post.request_moderation = request_moderation
#         post.save()
#
#         # Get all posts from DB
#         posts = Notification.objects.all()
#         return Response()


class PeerNotification(APIView):
    """
    Get tenant Information

    """
    # def get(self, request):
    #     tenant_obj = Tenant.objects.all()
    #     serializer = TenantSerializer(tenant_obj, many=True)
    #     return Response(serializer.data)

    def post(self, request):
        print "HEREHERE"
        # save new post
        data = request.POST
        if 'request_moderation' not in data:
            data['request_moderation'] = False
        serializer = NotificationSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)


    def get(self, request):
        data = Notification.objects.filter().values()
        print data
        data = [items for items in data]
        serialize = NotificationSerializer(data)
        return Response(serialize.data, content_type="application/json")
