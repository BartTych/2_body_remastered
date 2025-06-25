import pickle

def save_lists_to_pickle(list1, list2, filename='data.pkl'):
    data = {
        'list1': list1,
        'list2': list2
    }
    with open(filename, 'wb') as f:
        pickle.dump(data, f)

def save_lists_to_pickle_with_steps(list1, list2, steps, filename='data.pkl'):
    data = {
        'list1': list1,
        'list2': list2,
        'steps': steps
    }
    with open(filename, 'wb') as f:
        pickle.dump(data, f)
        
def load_lists_from_pickle_with_steps(filename='data.pkl'):
    with open(filename, 'rb') as f:
        data = pickle.load(f)
    return data['list1'], data['list2'], data['steps']

def load_lists_from_pickle(filename='data.pkl'):
    with open(filename, 'rb') as f:
        data = pickle.load(f)
    return data['list1'], data['list2']

def describe_pickle_contents(filename='data.pkl'):
    with open(filename, 'rb') as f:
        data = pickle.load(f)

    if isinstance(data, dict):
        print("Pickle contains a dictionary with the following keys:")
        for key in data:
            print(f"  - {key}: {type(data[key]).__name__}, length: {len(data[key]) if hasattr(data[key], '__len__') else 'N/A'}")
    else:
        print(f"Pickle contains an object of type: {type(data).__name__}")