
def is_mobile(request):
    device_info=request.META['HTTP_USER_AGENT']
    index=0
    mobile=False
    while index+6 < len(device_info):
        if device_info[index:index+6].lower()=='mobile':
            mobile=True
            break
        else:
            index+=1
    return mobile
    
        




