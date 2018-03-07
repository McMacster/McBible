import pickle

def serialize(filename, entry):
    with open(filename, 'wb') as f:
        pickle.dump(entry, f)

def deserialize(filename):
    with open(filename, 'rb') as f:
        entry = pickle.load(f)
        return entry