class Solution(object):
    def groupAnagrams(self, strs):
        strs_sorted = []
        checked = [False for _ in range(len(strs))]
        answers = []
        for sts in strs:
            strs_sorted.append("".join(sorted(sts)))

        for i in range(len(strs_sorted)):
            if checked[i]:
                continue

            checked[i] = True

            anagrams = []
            anagrams.append(strs[i])
            for j in range(i + 1, len(strs_sorted)):
                if strs_sorted[i] == strs_sorted[j]:
                    checked[j] = True
                    anagrams.append(strs[j])

            answers.append(anagrams)

        return answers