# Carbon-intensive code patterns for testing EcoCode Analyzer
import requests
import time

def inefficient_fibonacci(n):
    """Recursive fibonacci without memoization - high carbon impact"""
    if n <= 1:
        return n
    return inefficient_fibonacci(n-1) + inefficient_fibonacci(n-2)

def nested_loop_example(data):
    """Triple nested loops - O(n³) complexity"""
    results = []
    for i in range(len(data)):
        for j in range(len(data)):
            for k in range(len(data)):
                if i != j and j != k:
                    results.append(data[i] + data[j] + data[k])
    return results

def synchronous_requests_example():
    """Synchronous HTTP requests - should be async"""
    urls = [
        'https://api.example1.com/data',
        'https://api.example2.com/data', 
        'https://api.example3.com/data'
    ]
    
    results = []
    for url in urls:
        response = requests.get(url)  # Synchronous - carbon intensive
        results.append(response.json())
    
    return results

def string_concatenation_example(items):
    """Inefficient string concatenation"""
    result = ""
    for item in items:
        result += str(item) + ", "  # Inefficient concatenation
    return result

# Test the carbon-heavy functions
if __name__ == "__main__":
    print("Testing carbon-heavy code patterns...")
    
    # This will be very slow and energy-intensive
    print(f"Fibonacci(30): {inefficient_fibonacci(30)}")
    
    # This will create O(n³) complexity
    test_data = list(range(10))
    nested_results = nested_loop_example(test_data)
    print(f"Nested loop results: {len(nested_results)} combinations")
    
    # Inefficient string building
    items = list(range(1000))
    result_string = string_concatenation_example(items)
    print(f"String length: {len(result_string)}")
