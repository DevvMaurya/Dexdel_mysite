from django.shortcuts import render
from django.http import HttpResponse
# from dbconn import connection
import mysql.connector as db
conn = db.connect(user='root',passwd = 'MySql@123',host='127.0.0.1',database='dexdel_data')
cursor = conn.cursor()

def tesing(request):
    # return HttpResponse("<h1> Dexllo </h1>")
    return render(request,'index.html')

def search(request):
    res = []
    que = request.GET.get('ask')
    q = 'INSERT INTO dexdel_app_searchhistory (ask) VALUES ( "{}");'.format(que)
    cursor.execute(q)

    qury = {
        'projlink' : 'SELECT * FROM dexdel_app_projects;',
        'dexlink' : 'SELECT * FROM dexdel_app_links;',

    }

    if 'project'.casefold() in que.casefold():
        cursor.execute(qury['projlink'])
        res += cursor.fetchall()
    if 'Dev'.casefold() in que.casefold():
        cursor.execute(qury['dexlink'])
        res += cursor.fetchall()
    if not res:
        cursor.execute(qury['dexlink'])
        extralinks = cursor.fetchall()
        res += extralinks

    conn.commit()

    data = {
        'ask' : que,
        'boold' : False,
        'boolc' : False,
        'bools' : False,
        'link' :res,
        
    }

    


    # print(que)

    if "dev maurya".casefold() in que.casefold() or 'dev'.casefold() in que.casefold() :
        data['boold'] = True
        data['bools'] = True

    Edu_list=['College','Education','study']
    if any(s.casefold() in que.casefold() for s in Edu_list):
    # if que.casefold() in Edu_list:
        data['boolc'] = True
        data['bools'] = True


    return render(request,'search.html',data)




