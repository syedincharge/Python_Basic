print("\n=== VS CODE TIPS ===")

print("""
VS Code Features for Learning PEMDAS:

1. Use the DEBUGGER: 
   - Set breakpoints on each line
   - Watch variables change step by step

2. Use the TERMINAL:
   - Run individual expressions
   - Test small parts of complex expressions

3. Use JUPYTER NOTEBOOKS in VS Code:
   - Execute cells individually
   - See intermediate results

4. Use the WATCH WINDOW:
   - Monitor specific variables
   - See how values change during execution

5. Use CODE RUNNER extension:
   - Run Python code with Ctrl+Alt+N
   - See immediate results
""")

# Example for debugging practice
def debug_pemdas():
    x = 5
    y = 3
    z = 2
    
    # Set breakpoints on the following lines and use debugger
    step1 = x + y * z      # Breakpoint here
    step2 = (x + y) * z    # Breakpoint here  
    step3 = x ** y * z     # Breakpoint here
    step4 = x ** (y * z)   # Breakpoint here
    
    return step1, step2, step3, step4

# Call the function to practice debugging
results = debug_pemdas()
print(f"Debug practice results: {results}")