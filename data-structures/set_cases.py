# Set is mutable object but it can store only immutable objects .

s={(2,4),6}
print(s) # {(2,4),6}

s={[2,4],6}
print(s) # TypeError: unhashable type: 'list'

