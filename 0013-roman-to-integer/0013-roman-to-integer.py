class Solution(object):
    def romanToInt(self, s):
        letter_values = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100 , 'D': 500, 'M': 1000}
        sumo = letter_values[s[-1]]

        for i in range(len(s) - 1, 0, -1):
            if letter_values[s[i]] > letter_values[s[i-1]]:
                sumo = sumo - letter_values[s[i-1]]
            else:
                sumo = sumo + letter_values[s[i-1]]

        return sumo

        