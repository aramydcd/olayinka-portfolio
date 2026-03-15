from rest_framework import generics
from .models import MediaItem
from .serializers import MediaSerializer
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Experience, ContactMessage


# This view serves the actual HTML page
def index(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        
        # Save to Database
        ContactMessage.objects.create(full_name=name, email=email, message=message)
        
        messages.success(request, "Your message has been sent successfully!")
        return redirect('index')

    experiences = Experience.objects.all()
    return render(request, 'index.html', {'experiences': experiences})


# This view serves the filtered JSON data
class MediaList(generics.ListAPIView):
    serializer_class = MediaSerializer

    def get_queryset(self):
        category = self.request.query_params.get('category')
        if category and category != 'all':
            return MediaItem.objects.filter(category=category)
        return MediaItem.objects.all().order_by('-id')