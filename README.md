# is_ai_odd

`is_ai_odd` is a Python package designed to identify "odd" patterns in data using Google’s generative AI models.

## Installation

You can install the package using `pip`:

```bash
pip install is_ai_odd
```

Alternatively, you can clone the repository and install it locally:

```bash
git clone https://github.com/trimpta/is_ai_odd.git
cd is_ai_odd
pip install .
```

## Usage

### Initialize the API

Before using the functions in this package, you need to initialize the API with your API key:

```python
import is_ai_odd

is_ai_odd.init(API_KEY="your_api_key_here")
```

### Example

To check if a number is "odd" using the `is_odd()` function:

```python
import is_ai_odd

# Initialize with your API key
is_ai_odd.init(API_KEY="your_api_key_here")

# Check if a number is odd
number = 5
result = is_ai_odd.is_odd(number)
print(f"Is {number} odd? {result}")
```

You can also import init and is_odd directly.

```python
from is_ai_odd import init, is_odd

# Initialize with your API key
init(API_KEY="your_api_key_here")

# Check if a number is odd
number = 5
result = is_odd(number)
print(f"Is {number} odd? {result}")
```
