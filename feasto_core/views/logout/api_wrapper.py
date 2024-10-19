from debugpy.adapter import access_token
from django.http import JsonResponse
from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from oauth2_provider.models import RefreshToken

from .validator_class import ValidatorClass



@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    phone_no = kwargs['request_data']['phone_no']
    refresh_token = kwargs['request_data']['refresh_token']

    RefreshToken.objects.filter(token=refresh_token).delete()

    return JsonResponse({"data": "Logout Success"}, status=200)
