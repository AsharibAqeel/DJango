from django.http import HttpResponse
from django.shortcuts import render

def homePage(request):
    data = {
        'title': 'Home Page',
        'clist': ['PHP', 'Java', 'Django'],
        'numbers': [10, 20, 30, 40, 50],
        'student_details': [
            {'name': 'Arshoo', 'phone': 3091981734},
            {'name': 'Asharib', 'phone': 3114480425}
        ]
    }
    return render(request, "index.html", data)

def aboutUS(request):
    return HttpResponse("<b>Welcome To MyProject</b>")

def course(request, courseid):
    return HttpResponse(courseid)

def index(request):
    return render(request, 'index.html')

def ex1(request):
    sites = [
        '''<h1>For Entertainment </h1><a href = "https://www.youtube.com" >YouTube Video</a>''',
        '''<h1>For Interaction </h1><a href = "https://www.facebook.com" >Facebook</a>''',
        '''<h1>For Insight   </h1><a href = "https://www.ted.com/talks" >Ted Talk</a>''',
        '''<h1>For Internship   </h1><a href="https://internshala.com" >Internship</a>''',
    ]
    return HttpResponse(sites)

def capfirst(request):
    return HttpResponse("capitalize first")

def removepunc(request):
    return HttpResponse("remove punc")

def newlineremove(request):
    return HttpResponse("new line remove")

def spaceremove(request):
    return HttpResponse("space remover")

def charcount(request):
    return HttpResponse("charcount")

def index(request):
    return render(request, 'index.html')

    # return HttpResponse("Home")


def ex1(request):
    sites = ['''<h1>For Entertainment  </h1> <a href="https://www.youtube.com/"> Youtube Videos</a> ''',
             '''<h1>For Interaction  </h1> <a href="https://www.facebook.com/"> Facebook</a> ''',
             '''<h1>For Insight  </h1> <a href="https://www.ted.com/talks"> Ted Talks</a> ''',
             '''<h1>For Internship  </h1> <a href="https://www.internshala.com">Internship</a> ''']
    return HttpResponse((sites))

def analyze(request):
    #Get the text
    djtext = request.GET.get('text', 'default')

    # Check checkbox values
    removepunc = request.GET.get('removepunc', 'off')
    fullcaps = request.GET.get('fullcaps', 'off')
    newlineremover = request.GET.get('newlineremover', 'off')
    extraspaceremover = request.GET.get('extraspaceremover', 'off')

    #Check which checkbox is on
    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose':'Removed Punctuations', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)

    elif(fullcaps=="on"):
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()

        params = {'purpose': 'Changed to Uppercase', 'analyzed_text': analyzed}
        # Analyze the text
        return render(request, 'analyze.html', params)
    elif(extraspaceremover=="on"):
        analyzed = ""
        for index, char in enumerate(djtext):
            if not(djtext[index] == " " and djtext[index+1]==" "):
                analyzed = analyzed + char

        params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}
        # Analyze the text
        return render(request, 'analyze.html', params)

    elif (newlineremover == "on"):
        analyzed = ""
        for char in djtext:
            if char != "\n":
                analyzed = analyzed + char

        params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}
        # Analyze the text
        return render(request, 'analyze.html', params)
    else:
        return HttpResponse("Error")
    
    

# def capfirst(request):
#     return HttpResponse("capitalize first")
#
# def newlineremove(request):
#     return HttpResponse("newline remove first")
#
#
# def spaceremove(request):
#     return HttpResponse("space remover back")
#
# def charcount(request):
#     return HttpResponse("charcount ")