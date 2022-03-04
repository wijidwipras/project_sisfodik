from django.http import HttpResponse

def tentang(request):
    return HttpResponse('Halaman Tentang, aku adalah pras ganteng')
def index(request):
    return HttpResponse('Hello World')