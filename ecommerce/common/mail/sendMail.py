from django.core.mail import BadHeaderError, send_mail
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

def send_email(request, **kwargs):
    subject = kwargs.subject
    message = kwargs.message
    from_email = kwargs.from_email
    to = kwargs.to

    if subject and message and from_email and to:
        try:
            send_mail(subject, message, from_email, to)
        except BadHeaderError as e:
            return e
            # return HttpResponse('Invalid header found.')
        # return HttpResponseRedirect('/contact/thanks/')
    else:
        # In reality we'd use a form class
        # to get proper validation errors.
        return False
        # return HttpResponse('Make sure all fields are entered and valid.')