class Solution:
    
    # Helper function to check if books can be allocated to 'k' students
    # such that no student gets more than 'max_pages_allowed'
    def isPossible(self, pages_array, total_books, k, max_pages_allowed):
        required_students = 1
        current_pages_sum = 0
        
        for pages in pages_array:
            # If a single book has more pages than the allowed max, allocation is impossible
            if pages > max_pages_allowed:
                return False
            
            # If adding this book exceeds the allowed limit, assign to next student
            if current_pages_sum + pages > max_pages_allowed:
                required_students += 1
                current_pages_sum = pages

                # If more students are required than available, not possible
                if required_students > k:
                    return False
            else:
                current_pages_sum += pages
        
        return True
    
    # Main function to find the minimum value of the maximum pages assigned to any student
    def findPages(self, pages_array, k):
        total_books = len(pages_array)

        # Not enough books to allocate at least one to each student
        if total_books < k:
            return -1

        # Minimum possible max pages is the largest book
        # Maximum possible is the total sum (one student gets all books)
        low = max(pages_array)
        high = sum(pages_array)
        result = -1

        # Binary search on the range of possible max pages per student
        while low <= high:
            mid = (low + high) // 2

            # If allocation is possible with mid as max pages, try to minimize further
            if self.isPossible(pages_array, total_books, k, mid):
                result = mid
                high = mid - 1
            else:
                # If not possible, increase the lower bound
                low = mid + 1

        return result
