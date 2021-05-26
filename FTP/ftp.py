import functools

from flask import current_app

#from flask_app.db import get_db

from flask import request, abort, jsonify, redirect, render_template, url_for, send_from_directory, Blueprint, flash, g
import os
from werkzeug.utils import secure_filename


from flask import request
def shutdown_server():
    func = request.environ.get('werkzeug.server.shutdown')
    if func is None:
        raise RuntimeError('Asked to shutdown')
    func()


def testDirs():
	path = current_app.config['UPLOAD_DIRECTORY']
	print('checking path',path)
	check = os.path.exists(path)
	if check:
		return path
	else:
		
		return None


def allowed_file(filename):
	return '.' in filename and \
		   filename.rsplit('.', 1)[1].lower() in current_app.config['ALLOWED_EXTENSIONS']

bp = Blueprint('ftp', __name__, url_prefix='/ftp')


@bp.route('/')
def main():
	return('holla')

@bp.route('/upload', methods=['GET', 'POST'])
def upload_file():
	if request.method == 'POST':
		path = testDirs()
		# check if the post request has the file part
		if 'file' not in request.files:
			flash('No file part')
			return redirect(request.url)
		file = request.files['file']
		# if user does not select file, browser also
		# submit an empty part without filename
		if file.filename == '':
			flash('No selected file')
			return redirect(request.url)
		if file and allowed_file(file.filename):
			filename = secure_filename(file.filename)
			file.save(os.path.join(path, filename))
			return redirect(url_for('ftp.files_list'))
	return(render_template("upload.html"))

@bp.route('/files')
def files_list():
	path = testDirs()
	if path:
		list_of_files = os.listdir(path)
		return render_template("list_files.html", data=list_of_files)

	else:
		return redirect(url_for('ftp.main'))


@bp.route('/files/<string:filename>')
def uploaded_file(filename):
	path = testDirs()
	if path:
		return send_from_directory(path,filename,as_attachment=True)

	else:
		return redirect(url_for('ftp.main'))


