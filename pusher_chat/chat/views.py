from django.shortcuts import render_to_response
from django.conf import settings
from django.http import HttpResponse
from django.template import RequestContext
import pusher

pusher.app_id = settings.PUSHER_APP_ID
pusher.key = settings.PUSHER_KEY
pusher.secret = settings.PUSHER_SECRET

p = pusher.Pusher()

def home(request):
    if not request.session.get('user'):
        request.session['user'] = 'user-%s' % request.session.session_key
    return render_to_response('chat/home.html', {
        'PUSHER_KEY': settings.PUSHER_KEY,
    }, RequestContext(request)) 

def message(request):
    if request.session.get('user') and request.POST.get('message'):
        p['chat'].trigger('message', {
            'message': request.POST.get('message'),
            'user': request.session['user'],
        })
    return HttpResponse('')