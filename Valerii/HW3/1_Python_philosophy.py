import codecs
import this

#this.s - returns zen of python in encoded format, with rot13 cypher. so we need to decode it.
zen_of_python = codecs.decode(this.s, 'rot13')

better_count = zen_of_python.count('better')
never_count = zen_of_python.count('never')
is_count = zen_of_python.count('is')

print(
    '\n"better" count is', better_count, 
    '\n"never" count is', never_count, 
    '\n"is" count is', is_count
      )

print("\n", zen_of_python.upper().replace("I", "&"))
