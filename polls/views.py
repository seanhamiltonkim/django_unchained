from django.http import HttpResponse

def index(request):
    return HttpResponse("""
    <html>
        <body>
            <h2>Hello!</h2>
            <p>Very cool</p>
        </body>
    </html>
    """)

def detail(request, question_id):
    return HttpResponse("Question #{}".format(question_id))

def results(request, question_id):
    response = "Result of question #%s"
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse(f"Voting on #{question_id}")
