class FlexibleDict(dict):
    def __getitem__(self, key):
        # Convert key to string if it's an integer
        if isinstance(key, int) and str(key) in self:
            key = str(key)
        elif isinstance(key, str) and int(key) in self:
            key = int(key)
        return super().__getitem__(key)

# Example usage:
flexible_dict = FlexibleDict({1: 'value1', '2': 'value2'})

# Access values using string key
print(flexible_dict['1'])  # Output: value1

# Access values using integer key
print(flexible_dict[2])    # Output: value2

# Access values using integer key provided as string
