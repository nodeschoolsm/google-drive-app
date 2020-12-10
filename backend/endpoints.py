from flask import Blueprint, request, jsonify, send_from_directory
from werkzeug.utils import secure_filename
import os
import typing
import shutil

endpoints_flask = Blueprint('endpoints_flask', __name__)

working_directory = os.getcwd() + "/files"

working_directory_crash = os.getcwd() + "/papelera"

@endpoints_flask.errorhandler(400)
def not_found(error=str):
    response = jsonify({
        "message": error,
        "upload": False
        })
    response.status_code = 400
    return response

#UPLOAD FILES
@endpoints_flask.route('/upload', methods=['POST'])
def upload():
    path = request.form['path']
    if request.method == 'POST':
        files = request.files.getlist("files")
        for file in files:
            try:
                filename = secure_filename(file.filename)
                file.save(working_directory + path + filename)
            except FileNotFoundError:
                return not_found(error="Error, folder does not exist")
        return jsonify({
            "message": "success",
            "upload": True
            })


#REMOVE FILES

@endpoints_flask.route('/delete', methods=["POST"])
def remove_files():
    filename = request.form['filename']
    path = request.form['path']
    if os.path.isfile(working_directory + path + filename) == False:
        return not_found(error="File not found")
    else:
        try:
            shutil.copy2(working_directory + path + filename, working_directory_crash + path + filename)
            os.remove(working_directory + path + filename)
        except OSError:
            return jsonify({
                "message": "Error, file does not exits",
                "removed": False
            })
        return jsonify({
            "message": "success",
            "removed": True
            })

# DOWNLOAD FILES
@endpoints_flask.route('/down/<string:path>/file/<string:file_name>')
def download_files(path, file_name):
    path_received = str(path)
    path_original_converted = path_received.replace('+', '/')
    return send_from_directory(working_directory + path_original_converted, filename=file_name, as_attachment=True)
