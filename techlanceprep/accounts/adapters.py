from allauth.socialaccount.adapter import DefaultSocialAccountAdapter
from allauth.exceptions import ImmediateHttpResponse
from django.contrib.auth import get_user_model
from django.contrib import messages
from django.shortcuts import redirect

User = get_user_model()

class RestrictSignupSocialAccountAdapter(DefaultSocialAccountAdapter):
    def pre_social_login(self, request, sociallogin):
        # 1. If the social account is already registered and linked, allow the login
        if sociallogin.is_existing:
            return
            
        # 2. Check if a standard user account already exists with the Google account's email
        email = sociallogin.user.email
        if email:
            email = email.lower().strip()
            if User.objects.filter(email__iexact=email).exists():
                # Allow the login so allauth can automatically link the Google login to the existing account
                return
        
        # 3. If the user explicitly requested a signup flow (clicked Google button on Register page), allow it
        process = sociallogin.state.get('process')
        if process == 'signup':
            return
            
        # 4. If no user exists and they tried to login, reject the request
        messages.error(request, "Account Not Created. Please register first!")
        raise ImmediateHttpResponse(redirect('login'))
