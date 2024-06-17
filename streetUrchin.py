class Solution:
    def streetUrchin(self, a: int, b: int) -> int:
        buckets: list = [0 for i in range(len(a))]
        for i in range(len(a)):
            intergalactic_gargle_blaster: int = 0
            temp_int = 0
            for j in range(len(b)):
                if a[i] == b[j]:
                    intergalactic_gargle_blaster = temp_int + 1
                temp_int = buckets[j]
                buckets[j] = max(buckets[j], intergalactic_gargle_blaster)
        return buckets[len(a)-1]

    
    def takeBag(self, a, b):
        buckets = [[False for _ in range(len(a))] for _ in range(len(b) + 1)]
        for i in range(len(a)):
            matched = False
            for j in range(len(b)):
                if matched == True:
                    buckets[i][j] = False
                elif a[i] == b[j]:
                    buckets[i][j] = True
                    matched = True
            buckets[i + 1] = buckets[i].copy()
        return sum(buckets[len(b)])


    def giveBag(self, a, b):
        buckets = [[0 for _ in range(len(a) + 1)] for _ in range(len(b) + 1)]
        for i in range(len(a)):
            buckets[i + 1] = buckets[i].copy()
            for j in range(len(b)):
                if a[i] == b[j]:
                    buckets[i + 1][j + 1] =  buckets[i][j] + 1
                else:
                    buckets[i + 1][j + 1] = max(buckets[i + 1][j], buckets[i][j + 1])
        return buckets[len(a)][len(b)]
    

    def oldChiled(self, a, b):
        magic = [0 for i in range(len(a) + 1)]
        for i in range(len(a)):
            new_magic = [0]
            for j in range(len(b)):
                if a[i] == b[j]:
                    new_magic.append(magic[j] + 1)
                else:
                    new_magic.append(max(new_magic[-1], magic[j + 1]))
            magic = new_magic
        return(magic[len(a)])

    
def main():
    print('lets go')

    s1 = 'ABCD'
    s2 = 'ABDC'
    
    f = Solution()
    print(f.streetUrchin(s1, s2))
    print(f.oldChiled(s1, s2))
    print(f.takeBag(s1, s2)) # Still not fixed
    print(f.giveBag(s1, s2))

    
if __name__ == '__main__':
    main()
