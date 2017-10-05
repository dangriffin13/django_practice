from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template.loader import get_template
from django.shortcuts import render
from django.template import Template, Context
from django.core.mail import send_mail, get_connection
from mysite.forms import ContactForm
import datetime

def hello(request):
	return HttpResponse("Hello World")
	
def null(request):
	return HttpResponse("Placeholder for the homepage")

def current_datetime(request):
	now = datetime.datetime.now()
	return render(request, 'current_datetime.html', {'now': now})

	#t = get_template('current_datetime.html')
	#html = t.render({'now': now})
	# html = "<html><body>It's currently %s </body></html>" % now
	#return HttpResponse(html)

def hours_ahead(request, offset):
	try:
		offset = int(offset)
	except ValueError:
		raise Http404()
	dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
	return render(request, 'hours_ahead.html', {'offset': offset, 'future_time': dt})
	
	# html = "<html><body> In %s hours, it will be %s. </body></html>" % (offset, dt)
	# return HttpResponse(html)

def book_info(request, book):
	return render(request, 'book_info.html', {'book': book})

def ops_tool(request):
	return render(request, 'ops_tool.html') #, {'account': account}

def meta(request):
	meta = request.META
	return render(request, 'meta.html', {'meta': meta})

def display_meta(request):
	values = request.META
	html = []
	for k in sorted(values):
		html.append('<tr><td>%s</td><td>%s</td></tr>' % (k, values[k]))
	return HttpResponse('<table>%s</table>' % '\n'.join(html))


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            con = get_connection('django.core.mail.backends.console.EmailBackend')
            send_mail(
                cd['subject'],
                cd['message'],
                cd.get('email', 'noreply@example.com'),
                ['siteowner@example.com'],
                connection=con
            )
            return HttpResponseRedirect('/contact/thanks/')
    else:
        form = ContactForm()

    return render(request, 'contact_form.html', {'form': form})
