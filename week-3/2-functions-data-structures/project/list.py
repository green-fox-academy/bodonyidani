class Elem(object):
    __slots__ = ["value", "next"]
    def __repr__(self):
        return "({}, {})".format(self.value, self.next)

# This part is OK:

def new_elem(value):
    elem = Elem()
    elem.value = value
    elem.next = None
    return elem

# This is where the ugly python grabbed me and I started to suffocate:

def append(head, value):
    end = head
    while end.next is not None:
        end = end.next
    end.next = new_elem(value)
    return head

# Was eaten by a python at this point..
