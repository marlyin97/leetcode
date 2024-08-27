class Solution:
    def simplifyPath(self, path: str) -> str:
        stack =[]  #initialize the stack
        for portion in path.split("/"):  #split the input string on "/" as delimiter
            if portion == "..": # if the current component is ".." then we pop from stack
                if stack:
                    stack.pop()
            elif portion == "." or not portion: # "." or an empty string
                continue
            else:
                stack.append(portion) #add to the stack
        #stich together all the directory names         
        final_str = "/" + "/".join(stack) 
        return final_str