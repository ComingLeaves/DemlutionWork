from django.http import JsonResponse
from django.shortcuts import render

from blog.models import User,BlogsPost,BlogComments,ToDos

def index(request):
    return render(request,'login.html')

def regist(request):
    if request.method == 'POST':
        email = request.POST.get('email', '')
        username = request.POST.get('username','')
        password = request.POST.get('password','')
        rpassword = request.POST.get('rpassword','')
        if password != rpassword:
            return render(request,'login.html',{'error':'两次密码输入不符！'})
        if User.objects.filter(email = email):
            return render(request,'login.html',{'error':'用户已存在'})
        user = User()
        user.username = username
        user.email = email
        user.password = password
        user.save()

        return render(request,'login.html',{'info':'注册成功，请继续登录操作！'})
    else:
        return render(request,'login.html',{'error':'数据库异常，请稍后再试！'})

def login(request):
    if request.method == 'POST':
        email = request.POST.get('email','')
        pass_word = request.POST.get('password','')
        exist = User.objects.filter(email=email)
        if exist:
            user = User.objects.get(email = email)
            if pass_word == user.password:
                request.session['IS_LOGIN'] = True
                request.session['username'] = user.username
                request.session['email'] = email
                blogs = BlogsPost.objects.filter()
                return render(request,'home.html',{'user':user,'blogs':blogs})
            else:
                return render(request,'login.html',{'error':'密码错误！'})
        else:
            return render(request,'login.html',{'error':'用户名不存在！'})
    else:
        return render(request,'login.html')

def display(request,blogFlag):
    b_content = BlogsPost.objects.get(flag=blogFlag)
    try:
        b_comments = BlogComments.objects.filter(flag=blogFlag)
    except:
        print("评论为空！！！")
        b_comments = None
    return render(request,'display.html',{'b_detail':b_content,'comments':b_comments})

def set_comment(request):
    if request.method == 'POST':
        comment = request.POST.get('comment', '')
        username = request.session['username']
        flag = request.POST.get('flag','')
        b_comment = BlogComments()
        b_comment.username = username
        b_comment.c_content = comment
        b_comment.flag = flag
        b_comment.save()
        return display(request,flag)
    else:
        return render(request,'login.html',{'error':'数据库异常，请稍后再试！'})

def blog_list(request):
    user = User.objects.get(email=request.session['email'])
    blogs = BlogsPost.objects.filter()
    return render(request, 'home.html', {'user': user, 'blogs': blogs})

def todo_post(request):
    value = request.session['email']
    title,id,completed = [],[],[]
    if ToDos.objects.filter(user=value):

        todos = ToDos.objects.all().filter(user=value).reverse()
        for todo in todos:
            #list.append({'completed':todo.completed,'title':todo.title})
            title.append(todo.title)
            id.append(todo.id)
            completed.append(todo.completed)
            # if todo.completed is 0:
            #     completed.append("false")
            # else:
            #     completed.append("true")
    return render(request,'todos.html',{'t_title':title,'t_id':id,'t_completed':completed})

# def update(request):
#     todos = request.GET.get('todos')
#     value = request.session['email']
#     ToDos.objects.filter(user=value).delete()
#     if not len(todos):
#         return JsonResponse("记事本为空", safe=False)
#     for todo in todos:
#         print(todo[0])
#         ToDos.objects.create(title=todo['title'],user=value,completed=todos['completed'])
#     return JsonResponse("修改成功", safe=False)

def insert(request):
    todo = request.GET.get('todo')
    value = request.session['email']
    ToDos.objects.create(title=todo,user=value,completed=0)
    return JsonResponse("添加成功", safe=False)

def del_todo(request):
    ids = request.GET.get('id')
    if isinstance(ids,list):
        for id in ids:
            ToDos.objects.filter(id=id).delete()
    else:
        ToDos.objects.filter(id=ids).delete()
    return JsonResponse("删除成功", safe=False)

def change_status(request):
    id = request.GET.get('id')
    status = request.GET.get('status')
    ToDos.objects.filter(id=id).update(completed=status)
    return JsonResponse("修改成功", safe=False)

def active(request):
    value = request.session['email']
    title, id, completed = [], [], []
    if ToDos.objects.filter(user=value):

        todos = ToDos.objects.all().filter(user=value,completed=0).reverse()
        for todo in todos:
            # list.append({'completed':todo.completed,'title':todo.title})
            title.append(todo.title)
            id.append(todo.id)
            completed.append(todo.completed)
            # if todo.completed is 0:
            #     completed.append("false")
            # else:
            #     completed.append("true")
    return render(request, 'todos.html', {'t_title': title, 't_id': id, 't_completed': completed})

def completed(request):
    value = request.session['email']
    title, id, completed = [], [], []
    if ToDos.objects.filter(user=value):

        todos = ToDos.objects.all().filter(user=value,completed=1).reverse()
        for todo in todos:
            # list.append({'completed':todo.completed,'title':todo.title})
            title.append(todo.title)
            id.append(todo.id)
            completed.append(todo.completed)
            # if todo.completed is 0:
            #     completed.append("false")
            # else:
            #     completed.append("true")
    return render(request, 'todos.html', {'t_title': title, 't_id': id, 't_completed': completed})
