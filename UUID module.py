import uuid
items=[['laptop',1200],['Mouse',20],['Keyboard',30],['tablet',200]]
item_data={}
for item in items:
    id=uuid.uuid5(uuid.NAMESPACE_OID, item[0])
    key=id.hex[:6]
    item_data[key]=item
print(" Item Data:")
for key, value in item_data.items():
    print(f"{key}:{value}")