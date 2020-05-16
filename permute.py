class Solution:
    def permute(self, nums):

        def permute(numbers, input=[]):
            output = []
            if len(numbers) == 0:
                return input
            if len(input) == 0:
                for i, num in enumerate(numbers):
                    temp = [num]
                    new_numbers = [n for n in numbers if n != num]
                    to_be_added = permute(new_numbers, temp)
                    for t in to_be_added:
                        output.append(t)
                return output
            else:
                for i, num in enumerate(numbers):
                    temp = [e for e in input]
                    temp.append(num)
                    new_numbers = [n for n in numbers if n != num]
                    to_be_added = permute(new_numbers,temp)
                    if len(numbers)==1:
                        output.append(to_be_added)
                    else:
                        for t in to_be_added:
                            output.append(t)
                return output
        if len(nums) == 1:
            return [permute(nums)]
        return permute(nums)



def main():
    nums =[1]
    s = Solution()
    print(s.permute(nums))

if __name__ == '__main__':
    main()