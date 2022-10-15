class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        students=collections.deque(students)
        for s in sandwiches:
            if s in students:
                while(s!=students[0]):
                    students.append(students.popleft())
                students.popleft()
            else:
                return len(students)
        return 0