from django.http import HttpResponse


def simple_route(request):
    if request.method == 'GET':
        return HttpResponse(status=200)
    else:
        return HttpResponse(status=405)


def slug_route(request, slug):
    return HttpResponse(slug, status=200)


def sum_route(request, first_num, second_num):
    return HttpResponse(str(int(first_num) + int(second_num)), status=200)


def sum_get_method(request):
    if not request.GET:
        return HttpResponse(status=400)
    first_num = int(request.GET.get('a'))
    second_num = int(request.GET.get('b'))
    if (first_num not in range(10)) or (second_num not in range(10)):
        return HttpResponse(status=400)
    return HttpResponse(str(first_num + second_num), status=200)


def sum_post_method(request):
    if not request.POST:
        return HttpResponse(status=400)
    first_num = int(request.POST.get('a'))
    second_num = int(request.POST.get('b'))
    if (first_num not in range(10)) or (second_num not in range(10)):
        return HttpResponse(status=400)
    return HttpResponse(str(first_num + second_num), status=200)
