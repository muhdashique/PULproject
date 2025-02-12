# pulapp/middleware.py
from django.shortcuts import redirect
from django.urls import reverse

class PreventBackMiddleware:
    """
    Middleware to prevent logged-out users from accessing protected pages after logout.
    """
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # List of allowed pages that don't require authentication
        allowed_urls = [
            reverse('login'),  # Login page
            reverse('logout'),  # Logout page
            reverse('index'),  # Home page (if you have a public home page)
            reverse('about'),  # About page (if applicable)
            reverse('contact'),
            reverse('gallery'),  # Contact page (if applicable)
            # Add any other public pages that shouldn't require login
        ]

        # If the user is not authenticated and tries to access a protected page
        if not request.user.is_authenticated:
            # If the user tries to access any page other than the allowed ones
            if request.path not in allowed_urls:
                return redirect('login')  # Redirect to login page if not authenticated
        
        response = self.get_response(request)
        return response
