'''
Оценки
Создать список из словарей с оценками учеников разных классов школы вида [{'school_class': '4a', 'scores': [3,4,4,5,2]}, ...]
Посчитать и вывести средний балл по всей школе.
Посчитать и вывести средний балл по каждому классу.
'''
import statistics


marks = [
    {'school_class': '4a', 'scores': [3, 4, 4, 5, 2]},
    {'school_class': '4b', 'scores': [2, 2, 2, 2, 2]},
    {'school_class': '4c', 'scores': [2, 3, 4, 5]},
    {'school_class': '5a', 'scores': [3]},
    {'school_clas': '5a', 'scores': [3]},
    {'school_class': '5a', 'scores': []}
]

mean_mark_total = []


def calc_mean_mark(marks_dict):
    for class_number in marks_dict:
        try:
            mean_mark = statistics.mean(class_number['scores'])
            print(
                f"Mean mark at {class_number['school_class']} - {mean_mark}")
            mean_mark_total.append(mean_mark)
        except TypeError:
            print('Please check your entered marks list')
        except KeyError:
            print('There is no such class')
        except statistics.StatisticsError:
            print('Error while calculating the mean, please check the data')
    print(statistics.mean(mean_mark_total))


if __name__ == "__main__":
    calc_mean_mark(marks)
