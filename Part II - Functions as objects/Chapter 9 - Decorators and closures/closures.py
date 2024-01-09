def foo():
    func_name = "foo"
    def foo_closure():
        print(func_name)
    return foo_closure()

def bar():
    func_name = "bar"
    foo()

bar() # "foo"

def create_state_incorrect():
    state = {"height": 1080, "width": 1920}
    
    def update_state(height, width):
        print(f"Old state {state}")
        state = {"height": height, "width": width}
        print(f"New state: {state}")
    
    return update_state

incorrect_state_updater = create_state_incorrect()
#incorrect_state_updater(480, 720) # raise UnboundLocalError


def create_state_correct():
    state = {"height": 1080, "width": 1920}
    
    def update_state(height, width):
        nonlocal state
        print(f"Old state {state}")
        state = {"height": height, "width": width}
        print(f"New state: {state}")
    
    return update_state

correct_state_updater = create_state_correct()
correct_state_updater(480, 720) # raise UnboundLocalError
