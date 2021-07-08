from django.shortcuts import render
from django.http import HttpResponse
from pymongo import MongoClient
from mongoengine import connect,Document,ListField,StringField,URLField

connect(db='gamesite',host='localhost',port=27017)

class Entry(Document):
    userID = StringField(required=True, max_length=20)
    username = StringField(required=True,max_length=20)
    password = StringField(required=True, max_length=20)

def entry_form(request):

    entry_text = {
        'entrytext': 'こちらからエントリーしてください'
    }

    return render(request,'entry_form.html',entry_text)

def entry_list(request):
    newentry_ID = request.GET['userID_Text1']
    newentry_name =request.GET['username_Text1']
    newentry_pass = request.GET['password_Text1']

    if newentry_ID == '':
        entry_text ={
            'entrytext': 'userIDが入力されていません'
        }
        return render(request, 'entry_form.html',entry_text)
    elif newentry_name == '':
        entry_text ={
            'entrytext': 'usernameが入力されていません'
        }
        return render(request, 'entry_form.html',entry_text)
    elif newentry_pass == '':
        entry_text ={
            'entrytext': 'passwordが入力されていません'
        }
        return render(request, 'entry_form.html',entry_text)
    else:
        pass

    entry_up_IDlist = []
    entry_up_namelist = []
    for doc in Entry.objects:
        entry_up_IDlist.append(doc.userID)
        entry_up_namelist.append(doc.username)

    temp_list = []
    for i in range(len(entry_up_IDlist)):
        temp_list.append({
            'entryup_IDlist':entry_up_IDlist[i],
            'entryup_namelist': entry_up_namelist[i],
        })

    for doc in Entry.objects:
        if doc.username == newentry_name or doc.userID == newentry_ID:
            return render(request, 'entrylist.html',{'temp_list': temp_list, 'entryup': 'すでにエントリー済み'})
        else:
            pass

    newentry = Entry(userID=newentry_ID,username=newentry_name,password=newentry_pass)
    newentry.save()
    temp_list.append({
        'entryup_IDlist': newentry_ID,
        'entryup_namelist': newentry_name,
    })

    return render(request, 'entrylist.html', {'temp_list': temp_list, 'entryup': 'エントリー完了'})


def deentry_form(request):
    deentry_text = {
        'deentrytext': '情報を入力して取り消しボタンを押してください'
    }
    return render(request, 'deentry_form.html', deentry_text)


def redeentry_form(request):
    deentry_ID = request.GET['userID_Text2']
    deentry_name = request.GET['username_Text2']
    deentry_pass = request.GET['password_Text2']

    if deentry_ID == '' or deentry_name == '' or deentry_pass == '':
        deentry_text = {
            'deentrytext': '入力されていない情報があります'
        }
        return render(request, 'deentry_form.html', deentry_text)
    else:
        for doc in Entry.objects:
            if doc.userID == deentry_ID and doc.username == deentry_name and doc.password == deentry_pass:
                deentry = Entry.objects.get(userID = deentry_ID)
                deentry.delete()
                deentry_text = {
                    'deentrytext': 'エントリーの取り消しが完了しました'
                }
                return render(request, 'deentry_form.html', deentry_text)
            else:
                pass

        deentry_text = {
            'deentrytext': '入力情報が間違っています',
            'deentryID': deentry_ID,
            'deentryname': deentry_name,
        }
        return render(request, 'deentry_form.html', deentry_text)




# Create your views here.
