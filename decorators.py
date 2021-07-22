
#decorate1#######################################################
def decorator(func):
    def decorated():
        print('함수 시작!')
        func()
        print('함수 끝!')
    return decorated

@decorator
def hello_world():
    print('Hello World')

hello_world()


#decorate2######################################################
def check_integer(func):
    def decorated(width, height):
        if width>=0 and height>=0 :
            return func(width, height)
        else:
            raise ValueError('Input must be positive value')
    return decorated

@check_integer
def tri_area(width, height):
    return width * height / 2
@check_integer
def rect_area(width, height):
    return width * height

#r_area = rect_area(-10,10)
#r_area
r_area = tri_area(-10,10)
print(r_area)


#decorator3####################################################
class User:
    def __init__(self, auth):
        self.is_authenticated = auth

def check_int(func):
    def decorated(user, width, height):
        if width >= 0 and height >= 0:
            return func(user, width, height)
        else:
            raise ValueError('Input must be positive value')
    return decorated

def login_required(func):
    def decorated(user, width, height):
        if user.is_authenticated:
            return func(user, width, height)
        else:
            raise PermissionError('Login required')
    return decorated

@check_int
@login_required
def tri_area(user, width, height):
    return width * height / 2
@check_int
@login_required
def rect_area(user, width, height):
    return width * height

user = User(auth=False)
r_area = rect_area(user, 10, 10)
print(r_area)

