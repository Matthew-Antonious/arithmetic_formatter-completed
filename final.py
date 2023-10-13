def arithmetic_arranger(problems, ans=False):
    valid_op = {"+", "-"}
    formatted_equations = []
    
    if len(problems) > 5:
        return "Error: Too many problems."
    
    for eq in problems:
        num1, op, num2 = eq.split()
        
        if not (num1.isdigit() and num2.isdigit()):
            return "Error: Numbers must only contain digits."   
        
        if op not in valid_op:
            return "Error: Operator must be '+' or '-'."  
        
        if len(num1) > 4 or len(num2) > 4:
            return "Error: Numbers cannot be more than four digits." 
        
        col_width = max(len(num1), len(num2)) + 2
        
        num1 = int(num1)
        num2 = int(num2)
        
        if op == "+":
            result = num1 + num2
        else:
            result = num1 - num2
            
        formatted_num1 = str(num1).rjust(col_width)
        formatted_op_and_num2 = f"{op} {str(num2).rjust(col_width-2)}"
        line = '-' * col_width
        formatted_result = str(result).rjust(col_width)
        
        if not ans:
            formatted_equation = f"{formatted_num1}\n{formatted_op_and_num2}\n{line}"
        else:
            formatted_equation = f"{formatted_num1}\n{formatted_op_and_num2}\n{line}\n{formatted_result}"
            
        formatted_equations.append(formatted_equation)
    
    rows = [eq.split("\n") for eq in formatted_equations]
    arranged_problems = "\n".join("    ".join(row) for row in zip(*rows))
    
    return arranged_problems

# Test cases
print(arithmetic_arranger(["325 - 6565", "32 + 698", "3801 - 2", "45 + 43", "123 + 49"], ans=True))
print(arithmetic_arranger(["32 / 698", "3801 - 2", "45 * 43", "123 + 49"]))
print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 - 43", "12343 + 49"]))
print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49", "32 + 2432", "3233 + 123"]))
print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49", "3233 - 9898"]))
print(arithmetic_arranger(["32.5 + 698", "3801 - 2", "45 + 43", "123 + 49"]))

