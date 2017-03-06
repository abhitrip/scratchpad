class Solution {
public:
    int evalRPN(vector<string>& tokens) {
        stack<int> operands;
        vector<string> s = {"+","-","*","/"};
        unordered_set<string> oper(s.begin(),s.end());
        
        for(int i=0;i<tokens.size();i++)
        {
            
           
            if(oper.count(tokens[i]))
            {
                int op1 = operands.top(); operands.pop();
                int op2 = operands.top(); operands.pop();
                if(tokens[i]=="+")
                    operands.push(op1+op2);
                else if(tokens[i]=="-")
                    operands.push(op2-op1);
                else if(tokens[i]=="/")
                    operands.push(op2/op1);
                else
                    operands.push(op2*op1);
                
            }
            else
                operands.push(stoi(tokens[i]));
        }
        
        return operands.top();
        
    }
};

