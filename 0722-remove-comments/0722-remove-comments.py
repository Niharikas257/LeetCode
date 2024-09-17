class Solution(object):
    def removeComments(self, source):
        """
        :type source: List[str]
        :rtype: List[str]
        """
        result = []
        in_block_comment = False
        new_line = []
        
        
        for line in source:
            i = 0 # pointer to traverse the line
            if not in_block_comment:
                new_line = []
                
            while i < len(line):
                if not in_block_comment and i+1 < len(line) and line[i:i+2] == "/*":
                    # This marks the start of the block comment
                    in_block_comment = True
                    i += 2 # Move the pointer by 2 because we need to move past the / and *
                    
                elif in_block_comment and i+1<len(line) and line[i:i+2] == "*/":
                    # This marks the end of the block comment
                    in_block_comment = False
                    i += 2
                
                elif not in_block_comment and i+1 <len(line) and line[i:i+2] == "//":
                    # This marks the start of line comment
                    break
                
                elif not in_block_comment:
                    new_line.append(line[i])
                    i+=1
                    
                else:
                    i+=1
            
            if new_line and not in_block_comment:
                 result.append("".join(new_line))
            
        return result

# class Solution(object):
#     def removeComments(self, source):
#         """
#         :type source: List[str]
#         :rtype: List[str]
#         """
#         result = []  # To store the final uncommented code
#         in_block_comment = False  # Track if we are inside a block comment
#         new_line = []  # Temporary list to store parts of the current line

#         for line in source:
#             i = 0  # Index to traverse the current line

#             if not in_block_comment:
#                 new_line = []  # Start a new line if not in block comment

#             while i < len(line):
#                 # Handle block comment start
#                 if not in_block_comment and i + 1 < len(line) and line[i:i + 2] == "/*":
#                     in_block_comment = True
#                     i += 2  # Skip the start of the block comment "/*"
#                 # Handle block comment end
#                 elif in_block_comment and i + 1 < len(line) and line[i:i + 2] == "*/":
#                     in_block_comment = False
#                     i += 2  # Skip the end of the block comment "*/"
#                 # Handle line comments
#                 elif not in_block_comment and i + 1 < len(line) and line[i:i + 2] == "//":
#                     break  # Ignore the rest of the line
#                 # Add valid characters
#                 elif not in_block_comment:
#                     new_line.append(line[i])
#                     i += 1
#                 else:
#                     i += 1  # If in a block comment, just skip the characters

#             # If the current line has content and we're not in a block comment, append it
#             if new_line and not in_block_comment:
#                 result.append("".join(new_line))

#         return result




        