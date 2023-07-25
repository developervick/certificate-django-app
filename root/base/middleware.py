class A:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        print('start', self.middleware_name)
        response = self.get_response(request)
        print('End', self.middleware_name)

class B1(A):
    middleware_name = 'first middleware'

class B2(A):
    middleware_name = 'second middleware'

class B3(A):
    middleware_name = 'third middleware'
