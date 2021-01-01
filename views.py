from sanja import render

@render("index.html.j2", "html")
async def index(request):
    return {}
