from rest_framework import permissions


class UpdateOwnProfile(permissions.BasePermission):
    """Allow user to edit their own profile"""

    def has_object_permission(self, request, view, obj):
        """Check user is trying to edit their own profile"""
        if request.method in permissions.SAFE_METHODS:
            # An HTTP method is safe if it doesn't alter the state of the server
            # correspond to all read method
            return True
        return obj.id == request.user.id
        # return True if ==




