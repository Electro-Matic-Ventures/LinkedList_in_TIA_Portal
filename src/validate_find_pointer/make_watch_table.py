output = ''
for i in range(5):
    pointer = f'"LinkedList.IDB".list.list[{i}].pointer\r\n'
    id = f'"LinkedList.IDB".list.list[{i}].payload.id\r\n'
    status = f'"LinkedList.IDB".list.list[{i}].payload.status\r\n'
    output += pointer + id + status
output = output[:-1]
with open('./output.txt', 'w') as _file:
    _file.write(output)
