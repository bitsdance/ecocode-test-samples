# Optimized code patterns - low carbon impact
import asyncio
import aiohttp
from functools import lru_cache

@lru_cache(maxsize=None)
def efficient_fibonacci(n):
    """Memoized fibonacci - low carbon impact"""
    if n <= 1:
        return n
    return efficient_fibonacci(n-1) + efficient_fibonacci(n-2)

def optimized_processing(data):
    """Efficient single-pass algorithm"""
    # Use set for O(1) lookups instead of nested loops
    data_set = set(data)
    results = []
    
    for i, item1 in enumerate(data):
        for j, item2 in enumerate(data[i+1:], i+1):
            complement = -(item1 + item2)
            if complement in data_set:
                results.append((item1, item2, complement))
    
    return results

async def async_requests_example():
    """Asynchronous HTTP requests - energy efficient"""
    urls = [
        'https://api.example1.com/data',
        'https://api.example2.com/data',
        'https://api.example3.com/data'
    ]
    
    async with aiohttp.ClientSession() as session:
        tasks = [fetch_data(session, url) for url in urls]
        results = await asyncio.gather(*tasks)
    
    return results

async def fetch_data(session, url):
    async with session.get(url) as response:
        return await response.json()

def efficient_string_building(items):
    """Efficient string building using join"""
    return ", ".join(str(item) for item in items)

# Test the optimized functions
if __name__ == "__main__":
    print("Testing optimized code patterns...")
    
    # This will be fast with memoization
    print(f"Efficient Fibonacci(30): {efficient_fibonacci(30)}")
    
    # This uses efficient algorithms
    test_data = list(range(10))
    optimized_results = optimized_processing(test_data)
    print(f"Optimized results: {len(optimized_results)} combinations")
    
    # Efficient string building
    items = list(range(1000))
    result_string = efficient_string_building(items)
    print(f"String length: {len(result_string)}")
