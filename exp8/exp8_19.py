class FlexObject:
    pass

obj = FlexObject()

# add attributes dynamically
obj.name  = "Dynamic"
obj.value = 42
setattr(obj, "color", "blue")

print(obj.name)
print(obj.value)
print(getattr(obj, "color"))
print(vars(obj))   # see all dynamic attrs