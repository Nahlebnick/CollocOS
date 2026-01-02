from rest_framework.permissions import BasePermission, SAFE_METHODS
import logging

logger = logging.getLogger(__name__)

class IsOwnerOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True

        if obj.user != request.user:
            logging.warning(
                f"Unauthorized access attempt by user={request.user} on task={obj.id}"
            )
            return False

        return True

