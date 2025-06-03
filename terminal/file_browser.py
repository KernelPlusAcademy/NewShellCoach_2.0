
from flask import render_template, request, redirect, url_for
from .filesystem import root, VirtualFile
from flask import Blueprint

file_browser_bp = Blueprint('file_browser', __name__)

@file_browser_bp.route('/file-browser')
def file_browser():
    return render_template('file_browser.html', files=root.files)

@file_browser_bp.route('/create-file', methods=['POST'])
def create_file():
    filename = request.form['filename']
    content = request.form['content']
    if filename not in root.files:
        root.add_file(VirtualFile(filename, content))
    return redirect(url_for('file_browser.file_browser'))

@file_browser_bp.route('/edit-file', methods=['POST'])
def edit_file():
    filename = request.form['filename']
    content = request.form['content']
    if filename in root.files:
        root.files[filename].content = content
    return redirect(url_for('file_browser.file_browser'))
