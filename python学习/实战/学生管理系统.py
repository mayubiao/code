# 定义一个空列表，用于储存信息及后续操作。
stu_infos = []
#菜单提示
def menu():
    print("#" * 40)
    print('\t\t 学生管理系统')
    print("1 添加信息")
    print("2 删除信息")
    print("3 修改信息")
    print("4 查询信息")
    print("5 显示信息")
    print("0 退出系统")
    print("#" * 40)

# 获取信息
def get_info():
    global name_get
    global sex_get
    global id_get
    global score_get

    name_get = input("请输入学生姓名 ")
    sex_get = input("请输入学生性别 ")
    id_get = input("请输入学生学号 ")
    score_get = input("请输入学生成绩 ")
    #返回值
    return [name_get, sex_get, id_get, score_get]

# 添加信息
def add_info():
    get = get_info()  #调用后返回列表
    new_info = {} #建立字典储存信息

    new_info['name'] = get[0]
    new_info['sex'] = get[1]
    new_info['id'] = get[2]
    new_info['score'] = get[3]
    #在列表stu_infos中嵌套字典
    stu_infos.append(new_info)
    return None

# 删除信息
def remove_info():
    remove_number = int(input("请输入要删除信息的学生序号 "))
    stu_infos[remove_number-1] = {} #使用del会使序号发生变化

#修改信息
def change_info():
    change_number = int(input("请输入所需修改的学生序号 ")) # int将str类型转为int型
    #调用age_info函数输入
    get_info()
    stu_infos[change_number-1]['name'] = name_get
    stu_infos[change_number-1]['sex'] = sex_get
    stu_infos[change_number-1]['id'] = id_get
    stu_infos[change_number-1]['score'] = score_get

# 查询信息
def find_info():
    try:
        find_number = int(input("请输入要查询的序号 "))
        find_dict = {}
        find_dict = dict(stu_infos[find_number-1])
        print("姓名\t性别\t学号\t成绩.")
        print("%s\t%s\t%s\t%s"%(find_dict['name'], find_dict['sex'], find_dict['id'], find_dict['score']))
    except KeyError:
        print("序号{0}的学生信息已经被清空".format(find_number))


# 主函数
def run():
    while True:
        #显示菜单
        menu()
        choice = input("请输入操作序号 ")
        if choice == '0':
        	break
        if choice == '1':
            add_info()
        elif choice == '2':
            remove_info()
        elif choice == '3':
            change_info()
        elif choice == '4':
            find_info()
        elif choice == '5':
            print("\n学生信息预览.")
            print("序号\t姓名\t性别\t学号\t成绩.")
            number = 0
            for info in stu_infos:
                number += 1
                try:
                    print("%d\t%s\t%s\t%s\t%s"%(number, info['name'], info['sex'], info['id'], info['score']))
                except KeyError:
                    print("序号{0}的学生信息已经被清空".format(number))
               

run()
