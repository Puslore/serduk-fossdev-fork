'''
Script for style checking.
'''


def check_line_type(line: str) -> str:
    '''
    Check the type of a line in the code.
    Args:
        line (str): The line of code to check.
    Returns:
        str: The type of the line (e.g., 'import', 'function', 'class', 'other').
    '''
    try:
        if line is str:
            line = line.strip()
            
    except AttributeError as e:
        return f'Error with line type checking: {e}'
    
    if line == '':
        return 'empty'
    
    elif line.startswith('import') or line.startswith('from'):
        return 'import'
    
    elif line.startswith('def'):
        return 'function'
    
    elif line.startswith('class'):
        return 'class'
    
    elif line.startswith('if'):
        return 'conditional'
    
    elif line.startswith('for') or line.startswith('while'):
        return 'loop'
    
    elif line.startswith('#'):
        return 'comment'
    
    return 'average'
