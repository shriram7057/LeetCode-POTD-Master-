class Solution(object):
    def suggestedProducts(self, products, searchWord):
        """
        :type products: List[str]
        :type searchWord: str
        :rtype: List[List[str]]
        """
        products.sort()
        res = []

        prefix = ""
        start = 0
        n = len(products)

        for ch in searchWord:
            prefix += ch

            # Move start forward until products[start] >= prefix
            while start < n and products[start] < prefix:
                start += 1

            # Collect up to 3 suggestions
            suggestions = []
            i = start
            while i < n and len(suggestions) < 3 and products[i].startswith(prefix):
                suggestions.append(products[i])
                i += 1

            res.append(suggestions)

        return res
