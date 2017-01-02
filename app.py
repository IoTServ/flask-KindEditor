from werkzeug.utils import secure_filename
from flask import render_template, request
app.route('/upload', methods=['POST'])
def upload():
    dict_tmp = {}
    f = request.files['imgFile']
    dir = request.args.get('dir')
    if dir == 'image':
        if os.path.splitext(f.filename)[1] not in ['.png','.gif', '.jpg','.JPG', '.jpeg', '.bmp']:
            dict_tmp['error'] = 1
            dict_tmp['message'] = "保存出错！文件扩展名只能是：png,gif, jpg, jpeg, bmp"
            return json.dumps(dict_tmp)
    if dir == 'flash':
        if os.path.splitext(f.filename)[1] not in ['.swf', '.flv']:
            dict_tmp['error'] = 1
            dict_tmp['message'] = "保存出错！文件扩展名只能是：swf, flv"
            return json.dumps(dict_tmp)
    if dir == 'media':
        if os.path.splitext(f.filename)[1] not in ['.swf', '.flv', '.mp3', '.wav', '.wma', '.wmv', '.mid', '.avi', '.mpg', '.asf', '.rm', '.rmvb']:
            dict_tmp['error'] = 1
            dict_tmp['message'] = "保存出错！文件扩展名只能是：swf, flv, mp3, wav, wma, wmv, mid, avi, mpg, asf, rm, rmvb"
            return json.dumps(dict_tmp)
    if dir == 'file':
        if os.path.splitext(f.filename)[1] not in ['.doc', '.docx', '.xls', '.xlsx', '.ppt', '.htm', '.html', '.txt', '.zip', '.rar', '.gz', '.bz2']:
            dict_tmp['error'] = 1
            dict_tmp['message'] = "保存出错！文件扩展名只能是：doc, docx, xls, xlsx, ppt, htm, html, txt, zip, rar, gz, bz2"
            return json.dumps(dict_tmp)
    fname = secure_filename(f.filename) #获取一个安全的文件名，且仅仅支持ascii字符；
    try:
        f.save('app/static/up/'+ fname)
    except:
        dict_tmp['error'] = 1  # 成功{ "error":0, "url": "/static/image/filename"}
        dict_tmp['message'] = "保存出错！"
        return json.dumps(dict_tmp)
    dict_tmp['error'] = 0  # 成功{ "error":0, "url": "/static/image/filename"}
    dict_tmp['url'] = "/static/up/" + fname
    return json.dumps(dict_tmp)
