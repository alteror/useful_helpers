# main.py
import random

from functions import function_one, function_two
from functools import partial

# Example usage
kwargs_one = {'one_arg1': 'value1', 'arg2': 'value2', 'arg3': 'value3', 'function': function_one}
kwargs_two = {'two_arg1': 'value1', 'arg2': 'value2', 'arg3': 'value3', 'arg4': 'value4', 'function': function_two}

# Using functools.partial to bind the function and arguments
kwargs = random.choice([kwargs_one, kwargs_two])
random_func_with_args = partial(kwargs.pop('function'), **kwargs)

# Calling the partially applied function directly
result_var = random_func_with_args()

print(result_var)  # Output: function_two called with two_arg1=value1, kwargs={'arg2': 'value2', 'arg3': 'value3'}
