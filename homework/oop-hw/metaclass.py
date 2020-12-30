#!/bin/python

MetaClass = type("MetaClass", (), {"is_meta": True})

SubMetaClass = type("SubMetaClass", (MetaClass,), {})


class MyClass(SubMetaClass):
    pass


myVar = MyClass()

print(myVar)
print(myVar.is_meta)
