from urllib.request import Request

from django.contrib.auth.models import User, Group
from rest_framework import permissions
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView

from api.serializers import UserSerializer, GroupSerializer


class FormGeneratorAPI(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request: Request) -> Response:
        return Response(
            data={
                "form": [
                    {
                        "component": "h3",
                        "children": "Order pizza"
                    },
                    {
                        "type": "select",
                        "label": "Pizza size",
                        "name": "size",
                        "placeholder": "Select a size",
                        "options": {
                            "small": "Small",
                            "large": "Large",
                            "extra_large": "Extra Large"
                        },
                        "validation": "required"
                    },
                    {
                        "component": "div",
                        "class": "flex-wrapper",
                        "children": [
                            {
                                "name": "cheese",
                                "label": "Cheese options",
                                "type": "checkbox",
                                "options": {
                                    "mozzarella": "Mozzarella",
                                    "feta": "Feta",
                                    "parmesan": "Parmesan",
                                    "extra": "Extra cheese"
                                }
                            },
                            {
                                "name": "toppings",
                                "label": "Toppings",
                                "type": "checkbox",
                                "options": {
                                    "salami": "Salami",
                                    "prosciutto": "Prosciutto",
                                    "avocado": "Avocado",
                                    "onion": "Onion"
                                }
                            }
                        ]
                    },
                    {
                        "component": "div",
                        "class": "flex-wrapper",
                        "children": [
                            {
                                "type": "select",
                                "name": "country_code",
                                "label": "Code",
                                "outer-class": ["flex-item-small"],
                                "value": "1",
                                "options": {
                                    "1": "+1",
                                    "49": "+49",
                                    "55": "+55"
                                }
                            },
                            {
                                "type": "text",
                                "label": "Phone number",
                                "name": "phone",
                                "inputmode": "numeric",
                                "pattern": "[0-9]*",
                                "validation": "matches:/^[0-9-]+$/",
                                "validation-messages": {
                                    "matches": "Phone number should only include numbers and dashes."
                                }
                            }
                        ]
                    },

                    {
                        "type": "submit",
                        "label": "Order pizza"
                    }
                ]
            }
        )


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]
