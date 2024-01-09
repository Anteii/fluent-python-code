from functools import wraps
import random
from typing import Callable
import re

path_handlers = {}

class HttpResponse:
    
    def __init__(self, body: str, status: int) -> None:
        pass

class HttpRequest:
    ...

# MOCK
def extract_path_params(path: str, request: HttpRequest):
    param_pattern = re.compile(r"\{(.+)\}")
    print("extracting params (at handler call): ", path, param_pattern.findall(path))
    # Here we extracting params specified in path from request
    return {
        p: random.randrange(0, 10) for p in param_pattern.findall(path)
    }

# MOCK
def strip_path(path: str):
    return path

# MOCK
def dispatch_response(response: HttpResponse):
    ...

# If we wan't to modify behavior in a complex way
# We have the following nesting:
# Factory -> Decorator -> Modified Function
def get(path: str):
    print("Run decorator_factory")
    def decorator(handler: Callable):
        print("Run decorator")
        
        @wraps(handler) # to preserve __doc__, __name__
        def get_handler(request: HttpRequest, *args, **kwargs):
            params = extract_path_params(path, request)
            response = handler(request, **params) 
            dispatch_response(response)
            return response

        # should be registered this get_handler func
        # if we register handler, than we get unmodified behavior
        path_handlers[strip_path(path)] = get_handler
        
        return get_handler
    
    return decorator

@get("/")
def handle_root(request: HttpRequest, **params):
    """
    Handles root requests
    """
    
    print("Params (handler body): ", params)
    return HttpResponse("Hello World!", 200)

@get("/auth/{app_name}")
def handle_auth(request: HttpRequest, **params):
    """
    Handles auth requests
    """
    
    print("Params (handler body): ", params)
    return HttpResponse("Authenticated!", 200)

print(path_handlers)
handle_root(HttpRequest()) # same as path_handlers["/"](HttpRequest())
handle_auth(HttpRequest())

# Will be those of get_handler if functools.wraps wasn't used
print(handle_auth.__name__)
print(handle_auth.__doc__)