import hashlib

class MerkleTree:
    def __init__(self, data_list):
        self.leaves = [hashlib.sha256(str(d).encode()).hexdigest() for d in data_list]
        self.root = self.build_tree(self.leaves)

    def build_tree(self, nodes):
        if len(nodes) == 1:
            return nodes[0]
        new_level = []
        for i in range(0, len(nodes), 2):
            # If odd number of nodes, duplicate the last one
            left = nodes[i]
            right = nodes[i+1] if i+1 < len(nodes) else nodes[i]
            combined = hashlib.sha256((left + right).encode()).hexdigest()
            new_level.append(combined)
        return self.build_tree(new_level)