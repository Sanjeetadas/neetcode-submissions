class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        unique = []
        freq = []

        # Count frequencies manually
        for num in nums:

            found = False

            # Check if number already exists
            for i in range(len(unique)):

                if unique[i] == num:
                    freq[i] += 1
                    found = True
                    break

            # If number not found
            if found == False:
                unique.append(num)
                freq.append(1)

        result = []

        # Find top k frequent elements
        for i in range(k):

            max_freq = 0
            max_index = 0

            # Find largest frequency
            for j in range(len(freq)):

                if freq[j] > max_freq:
                    max_freq = freq[j]
                    max_index = j

            # Add answer
            result.append(unique[max_index])

            # Mark frequency as used
            freq[max_index] = -1

        return result