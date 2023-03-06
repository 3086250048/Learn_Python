employees=[['001','czz','19','男','china']]
while True:
    print('''===================Employees Manager System==================
1.查询员工
2.添加员工
3.删除员工
4.退出系统''')
    emp=[None,None,None,None,None]
    emp_str=''
    opration=input('请输入操作编号')
    if opration not in '1234':print('error=>编号输入错误请重新输入')
    if opration == '1':
        for emp in employees:
            emp_str+=f'''{emp[0]}    {emp[1]}    {emp[2]}    {emp[3]}    {emp[4]}\n'''  

        print(f'''
==================Employees Information======================
id         name            age       gender      address
{emp_str}
''')
    if opration == '2':
        emp[0]=input('请输入员工的id')
        emp[1]=input('请输入员工的姓名') 
        emp[2]=input('请输入员工的年龄') 
        emp[3]=input('请输入员工的性别')
        emp[4]=input('请输入员工的住址') 
        employees += [emp]
    if opration == '3':
        del_id=input('请输入要删除员工的id')
        flag=False
        for emp in employees:
            if del_id in emp:
                employees.remove(emp)
                flag=True
                print(f'已经删除员工{emp}')
        if not flag:print('error=>没有此员工')
    if opration == '4':break