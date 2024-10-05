class Solution(object):
    def calPoints(self, ops):
        """
        :type ops: List[str]
        :rtype: int
        """
        stack=[]
        prev=0
        top=-1
        # for i in range(len(ops)):
            
        #     if ops[i]=='+':
        #         temp=int(stack[top])+int(stack[top-1])
        #         stack.append(temp)
        #         top+=1


        #     elif ops[i]=='D':
        #         temp=int(stack[top])*int(prev)
        #         stack.append(temp)
        #         top+=1

        #     elif ops[i]=='C':
        #         prev=2
        #         stack.pop()
        #         print(stack)
        #         top-=1
        #     else:
        #         stack.append(int(ops[i]))
        #         top+=1
        # print(stack)

        # return sum(stack)

        
        
        for op in ops:
            if op=='+':
                stack.append(stack[-1]+stack[-2])

            elif op=='D':
                stack.append(stack[-1]*2)

            elif op=='C':
                stack.pop()

            else:
                stack.append(int(op))
        # print(stack)
        return sum(stack)