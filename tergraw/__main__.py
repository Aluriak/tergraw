"""
Tergraw usage exemple

"""
import time
import tergraw


GRAPH = {'a': {'b', 'c'}, 'd': {'b', 'e'}, 'f': {'g'}}


for frame in tergraw.pretty_view(GRAPH, oriented=True, construction=True):
    print(chr(27) + "[2J")
    print('\n'.join(frame))
    print('↥↥↥↥↥↥↥↥↥↥↥↥↥↥↥ CONSTRUCTION ↥↥↥↥↥↥↥↥↥↥↥↥↥↥↥↥')
    time.sleep(0.1)

print('↧↧↧↧↧↧↧↧↧↧↧↧↧↧↧↧ ORIENTED ↧↧↧↧↧↧↧↧↧↧↧↧↧↧↧↧↧↧↧↧↧↧↧↧')
print('\n'.join(tergraw.pretty_view(GRAPH, oriented=True)))

print('↧↧↧↧↧↧↧↧↧↧↧↧↧↧ NON ORIENTED ↧↧↧↧↧↧↧↧↧↧↧↧↧↧↧↧↧↧↧↧↧↧')
print('\n'.join(tergraw.pretty_view(GRAPH, oriented=False)))


GRAPH_LONG_LABEL = {'aaaa': {'bbbb', 'cccc'},
                    'dddd': {'bbbb', 'eeee'},
                    'ffff': {'gggg'},
                    'hh'  : {'i'}}

print('↧↧↧↧↧↧↧↧↧↧↧↧↧↧↧ LONG LABEL ↧↧↧↧↧↧↧↧↧↧↧↧↧↧↧↧↧↧↧↧↧↧↧')
print('\n'.join(tergraw.pretty_view(GRAPH_LONG_LABEL, oriented=True)))
