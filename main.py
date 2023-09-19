# Решить задания, которые не успели решить на семинаре.
# Добавьте ко всем задачам с семинара строки документации и методы вывода информации на печать.
# Создайте класс Матрица. Добавьте методы для: - вывода на печать,
# сравнения,
# сложения,
# *умножения матриц

class Matrix:

    def __init__(self, matrix_):
        len_1_line = len(matrix_[0])
        res_of_check_size = [len_1_line == len(m) for m in matrix_]
        res_of_check_type = []

        if not all(res_of_check_size):
            raise TypeError
        else:
            for i in range(len(matrix_)):
                for j in range(len(matrix_[0])):
                    if isinstance(matrix_[i][j], int):
                        res_of_check_type.append(1)
                    else:
                        res_of_check_type.append(0)
        if not all(res_of_check_type):
            raise ValueError
        else:
            self.matrix_ = matrix_
            self.type_matrix = "int_matrix"
            self.matrix_size = (len(self.matrix_), len(self.matrix_[0]))
            self.l = len(self.matrix_)

    def __str__(self):
        result = [[str(num) for num in line] for line in self.matrix_]
        result = list(map(lambda x: '  '.join(x), result))
        return 'Matrix->\n' + '\n'.join(result) + '\n*'

    def __repr__(self):
        result = [[str(num) for num in line] for line in self.matrix_]
        result = list(map(lambda x: '  '.join(x), result))
        return 'Matrix:\n' + '\n'.join(result) + f'\n{self.matrix_size}\n*'

    def __lt__(self, other):
        if isinstance(other, Matrix):
            option1 = self.matrix_size[0] < other.matrix_size[0]
            option2 = self.matrix_size[1] < other.matrix_size[1]
            option3 = self.matrix_size[0] == other.matrix_size[0]
            option4 = self.matrix_size[1] == other.matrix_size[1]
            return (option1 and option4) or (option2 and option3) or (option1 and option2)
        else:
            raise TypeError

    def __eq__(self, other):
        if isinstance(other, Matrix):
            option1 = self.matrix_size[0] == other.matrix_size[0]
            option2 = self.matrix_size[1] == other.matrix_size[1]
            return option1 and option2
        else:
            raise TypeError

    def __add__(self, other):
        if isinstance(other, Matrix):
            if self == other:
                add_res = [[self.matrix_[j][i] + other.matrix_[j][i] for i in range(len(self.matrix_[j]))] for j in
                           range(len(self.matrix_))]
            return Matrix(add_res)
        else:
            raise TypeError

    def __mul__(self, other):
        if isinstance(other, Matrix):
            if self.matrix_size[1] == other.matrix_size[0]:
                res = Matrix([[0 for j in range(other.matrix_size[1])] for i in range(self.matrix_size[0])])
                print('res', res)
                for i in range(self.matrix_size[0]):
                    for j in range(other.matrix_size[1]):
                        for k in range(self.matrix_size[1]):
                            res.matrix_[i][j] += self.matrix_[i][k] * other.matrix_[k][j]
            return res
        elif isinstance(other, int):
            res = Matrix(
                [[self.matrix_[i][j] * other for j in range(self.matrix_size[1])] for i in range(self.matrix_size[0])])
            return res
        else:
            raise TypeError


# my_m = Matrix([[2,224,9], [2,3,4],[2,3,4]])
# my_m2 = Matrix([[0, 9, 7], [3, 6,9], [3,5,7]])
# # print(my_m.type_matrix)
# print(my_m)
# print(my_m2)
# print(my_m + my_m2)
a = Matrix([[2, 3], [5, 0], [3, 0], [1, 1]])
print(a)

b = Matrix([[3, 3, 0], [10, 10, 10]])
print(b)
print(a * b)
print(a * 10)
print(f'{a = }')
