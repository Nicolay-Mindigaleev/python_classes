class Friends:
    connections: set[frozenset [str]]
    def __init__(self, connection: (list[frozenset[str] | set[str]] | tuple[frozenset[str] | set[str]])) -> None:
        self.connections = set()
        for i in connection:
            self.connections.add(frozenset(i))
    def add(self, connection: set[str] | frozenset[str]) -> bool:
        if connection not in self.connections:
            self.connections.add(frozenset(connection))
            return True
        return False
    def remove(self, connection: set[str] | frozenset[str]) -> bool:
        if connection in self.connections:
            self.connections.remove(frozenset(connection))
            return True
        return False
    def names(self) -> set[str]:
        names_set = set()
        for i in self.connections:
            for j in i:
                names_set.add(j)
        return names_set
    def connected(self, name: str) -> set[str]:
        conections_set = set()
        for i in self.connections:
            if name in i:
                for j in i:
                    if j != name:
                        conections_set.add(j)
        return conections_set

f = Friends([{"1", "2"}, {"3", "1"}])
print(f"adding ('1', '3'): {f.add({"1", "3"})}")
print(f"adding ('4', '5'): {f.add({"4", "5"})}")
f = Friends([{"1", "2"}, {"3", "1"}])
print(f"deleting ('1', '3'): {f.remove({"1", "3"})}")
print(f"deleting ('4', '5'): {f.remove({"4", "5"})}")

a = Friends([{"a", "b"}, {"b", "c"}, {"c", "a"}, {"a", "c"}, {"d", "c"}])
print(f"a.names: {a.names()}")
print(f"deleting ('d', 'c'): {a.remove({"d", "c"})}")
print(f"a.names: {a.names()}")

c = Friends([{"a", "b"}, {"b", "c"}, {"c", "a"}])
print(f"c.connected(a): {c.connected("a")}")
print(f"c.connected(a): {c.connected("d")}")
print(f"deleting('c', 'a'): {c.remove({"c", "a"})}")
print(f"c.connected(a): {c.connected("c")}")