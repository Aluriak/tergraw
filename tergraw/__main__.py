"""
Tergraw usage exemple

"""
import tergraw


GRAPH = {'a': {'b', 'c'}, 'd': {'b', 'e'}, 'f': {'g'}}


print('↧↧↧↧↧↧↧↧↧↧↧↧↧↧↧↧ ORIENTED ↧↧↧↧↧↧↧↧↧↧↧↧↧↧↧↧↧↧↧↧↧↧↧↧')
print('\n'.join(tergraw.pretty_view(GRAPH, oriented=True)))

print('↧↧↧↧↧↧↧↧↧↧↧↧↧↧ NON ORIENTED ↧↧↧↧↧↧↧↧↧↧↧↧↧↧↧↧↧↧↧↧↧↧')
print('\n'.join(tergraw.pretty_view(GRAPH, oriented=False)))
