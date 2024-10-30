from django.shortcuts import render, redirect

from .models import Message
def home_view(request):
    # Fetch all unique group names from the Message model
    existing_groups = Message.objects.values_list('group_name', flat=True).distinct()

    if request.method == 'POST':
        username = request.POST.get('username')
        group_name = request.POST.get('group_name')

        # Check if the group name exists in the database
        if username and group_name:
            # Redirect to the group chat, whether it's new or existing
            return redirect('group_chat', group_name=group_name, username=username)

    return render(request, 'home.html', {'existing_groups': existing_groups})

def group_chat_view(request, group_name, username):
    if request.method == 'POST':
        content = request.POST.get('content')
        if content:
            Message.objects.create(username=username, content=content, group_name=group_name)

    messages = Message.objects.filter(group_name=group_name).order_by('-timestamp')
    return render(request, 'group_chat.html', {'messages': messages, 'group_name': group_name, 'username': username})