from Myself_Project.student_project_class.student_info import *


def main():
    lst = []
    while True:
        choose = menu()
        if choose == 'q':
            break
        elif choose == '1':
            lst = input_student(lst)
        elif choose == '2':
            output_student(lst)
        elif choose == '3':
            lst = delete_student(lst)
        elif choose == '4':
            lst = change_student(lst)
        elif choose == '5':
            score_u2l(lst)
        elif choose == '6':
            score_l2u(lst)
        elif choose == '7':
            age_l2u(lst)
        elif choose == '8':
            age_u2l(lst)
        elif choose == '9':
            input_student_info(lst)
        elif choose == '10':
            lst = read_info_txt()

        elif choose == 'show':
            print(lst)


main()
