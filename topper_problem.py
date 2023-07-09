class Solution:
    @staticmethod
    def topper_problem(num):
        """"
        In the University Examinations conducted during the past 5 years, the toppers registration numbers were 7126, 82417914, 7687 and 6657. Your father is an expert in data mining and he could easily infer a pattern in the toppers registration numbers. In all the registration numbers listed here, the sum of the odd digits is equal to the sum of the even digits in the number. He termed the numbers that satisfy this property as Probable Topper Numbers. Write a program to find whether a given number is a probable topper number or not.
        """
        num=str(num)
        odd_sum,even_sum=0,0
        for i in range(len(num)):
            if i%2==0:
                even_sum+=int(num[i])
            else: odd_sum+=int(num[i])
        return "True" if even_sum==odd_sum else "False"

if __name__ == '__main__':
    s=Solution()
    print(s.topper_problem(143))
    print(s.topper_problem(344))
    print(s.topper_problem(275))

