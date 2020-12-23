from django.http import JsonResponse


def tick(request):
    data = {"tick": "tock!"}
    return JsonResponse(data)
