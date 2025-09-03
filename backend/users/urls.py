from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import (
    RegisterView, LoginView, LogoutView, ChangePasswordView,
    PasswordResetView, PasswordResetConfirmView,
    MeProfileView, MeProfileUpdateView, view_profile,
    create_notification, notify_post_action,
    UserNotificationsView, NotificationListView, toggle_follow,
    UserSearchView, like_post, get_notifications
)

urlpatterns = [
    # Authentication
    path("register/", RegisterView.as_view(), name="register"),
    path("login/", LoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("change-password/", ChangePasswordView.as_view(), name="change-password"),

    # Password reset
    path("password-reset/", PasswordResetView.as_view(), name="password-reset"),
    path("password-reset-confirm/", PasswordResetConfirmView.as_view(), name="password-reset-confirm"),

    # JWT
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),

    # Profile
    path("me/", MeProfileView.as_view(), name="me-profile"),
    path("me/update/", MeProfileUpdateView.as_view(), name="me-profile-update"),
    path("profile/<int:user_id>/", view_profile, name="view-profile"),
    path("profile/<int:user_id>/follow/", toggle_follow, name="toggle-follow"),

    # Posts / Notifications
    path("like/<int:post_id>/", like_post, name="like_post"),
    path("posts/<int:post_id>/notify/", notify_post_action, name="notify_post_action"),
    path("notifications/user/", UserNotificationsView.as_view(), name="user-notifications"),
    path("notifications/all/", NotificationListView.as_view(), name="all-notifications"),
    path("notifications/fetch/", get_notifications, name="get_notifications"),

    # User search
    path("search/", UserSearchView.as_view(), name="user-search"),
]
