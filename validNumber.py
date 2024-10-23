class Solution(object):
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = s.strip()
        n = len(s)
        
        # Define possible states
        state = 'q0'  # Start state
        i = 0  # Input index
        
        while i < n:
            char = s[i]
            
            if state == 'q0':
                if char in ['+', '-']:
                    state = 'q1'  # Sign state
                elif char.isdigit():
                    state = 'q2'  # Integer part
                elif char == '.':
                    state = 'q3'  # Decimal point (before integer part)
                else:
                    state = 'q_dead'  # Invalid input
                
            elif state == 'q1':
                if char.isdigit():
                    state = 'q2'  # Integer part
                elif char == '.':
                    state = 'q3'  # Decimal point (after sign)
                else:
                    state = 'q_dead'
            
            elif state == 'q2':
                if char.isdigit():
                    state = 'q2'  # Stay in integer part
                elif char == '.':
                    state = 'q4'  # Fraction part (digits can come after the dot)
                elif char in ['e', 'E']:
                    state = 'q5'  # Exponent part
                else:
                    state = 'q_dead'
            
            elif state == 'q3':
                if char.isdigit():
                    state = 'q4'  # Fractional part (after the dot)
                else:
                    state = 'q_dead'  # Isolated decimal point is invalid
            
            elif state == 'q4':
                if char.isdigit():
                    state = 'q4'  # Stay in fractional part
                elif char in ['e', 'E']:
                    state = 'q5'  # Exponent part
                else:
                    state = 'q_dead'
            
            elif state == 'q5':
                if char in ['+', '-']:
                    state = 'q6'  # Sign for exponent
                elif char.isdigit():
                    state = 'q7'  # Exponent number
                else:
                    state = 'q_dead'
            
            elif state == 'q6':
                if char.isdigit():
                    state = 'q7'  # Exponent number
                else:
                    state = 'q_dead'
            
            elif state == 'q7':
                if char.isdigit():
                    state = 'q7'  # Stay in exponent number
                else:
                    state = 'q_dead'
            
            elif state == 'q_dead':
                return False  # Already in dead state, no need to continue
            
            i += 1
        
        # Valid end states: q2 (integer), q4 (fraction), q7 (exponent)
        return state in ['q2', 'q4', 'q7']

# Printed some test cases so that you can see that it works ma'am
solution = Solution()
print("123: ", solution.isNumber("123"))        # True
print("0.1: ", solution.isNumber("0.1"))        # True
print("2e10: ",solution.isNumber("2e10"))       # True
print("-90E3: ",solution.isNumber("-90E3"))      # True
print("3.:",solution.isNumber("3."))         # True  
print(".5: ",solution.isNumber(".5"))         # True
print(".: ",solution.isNumber("."))          # False 
print("abc: ",solution.isNumber("abc"))        # False
print("1a: ",solution.isNumber("1a"))         # False
print("1e: ",solution.isNumber("1e"))         # False
print("e3: ",solution.isNumber("e3"))         # False
