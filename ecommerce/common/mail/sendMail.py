from django.core.mail import BadHeaderError, EmailMessage, send_mail
# from django.http import HttpResponse, HttpResponseRedirect


# def send_email(request, *args, **kwargs):
#     subject = request.POST.get('subject', '')
#     message = request.POST.get('message', '')
#     from_email = request.POST.get('from_email', '')
#     if subject and message and from_email:
#         try:
#             send_mail(subject, message, from_email, ['admin@example.com'])
#         except BadHeaderError:
#             return HttpResponse('Invalid header found.')
#         return HttpResponseRedirect('/contact/thanks/')
#     else:
#         # In reality we'd use a form class
#         # to get proper validation errors.
#         return HttpResponse('Make sure all fields are entered and valid.')

def send_email(**kwargs):

    subject = kwargs.get('subject')
    message = kwargs.get('message')
    from_email = kwargs.get('from_email')
    to = kwargs.get('to')
    html_message = kwargs.get('html_message')

    if subject and message and from_email and to and html_message:
        print('----------------if---------------------')
        try:
            send_mail(subject, message, from_email, to, html_message)
        except BadHeaderError as e:
            return e
            # return HttpResponse('Invalid header found.')
    elif subject and message and from_email and to:
        try:
            print('----------------elif---------------------')
            msg = EmailMessage(subject, message, to=to, from_email=from_email)
            msg.content_subtype = 'html'
            msg.send()
        except IOError as e:
            return e
    else:
        print('----------------else---------------------')
        # In reality we'd use a form class
        # to get proper validation errors.
        return False
    return True