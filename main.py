import nodes
import engine
brain_data = engine.init_brain('brains/main.tqm')
routes = brain_data['routes']
print('Hey! Welcome to DQM!\n')
while True:
    prompt = nodes.uinput()
    if prompt in ['exit', 'quit']:
        print('Goodbye. Cya later!')
        break
    elif prompt in ['cls', 'clear']:
        nodes.cls()
        continue
    if not prompt:
        continue
    response = engine.traverse(routes, prompt)
    print(response)