"""
Flask Documentation:     https://flask.palletsprojects.com/
Jinja2 Documentation:    https://jinja.palletsprojects.com/
Werkzeug Documentation:  https://werkzeug.palletsprojects.com/
This file creates your application.
"""

from app import app,db
from flask import flash, render_template, request, redirect, url_for
from app.forms import Property
from app.model import Property
from werkzeug.utils import secure_filename
import os

###
# Routing for your application.
###

@app.route('/')
def home():
    """Render website's home page."""
    return render_template('home.html')


@app.route('/about/')
def about():
    """Render the website's about page."""
    return render_template('about.html', name="Mary Jane")

@app.route('/properties/create')
def addproperty():
    
    id=0
    if request.method == 'POST':
        if form.validate_on_submit(): 
            form = Property()
            photo=form.image.data
            filename=secure_filename(photo.filename)
            photo.save(os.path.join(app.confi['UPLOAD_FOLDER'], filename))
            id+=1

            title = form.title.data
            rooms= form.rooms.data
            bathroom = form.bathroom.data
            location = form.location.data
            price = form.price.data
            type= form.type.data
            description = form.description.data
            
            newProperty = Property(title=title,rooms=rooms,bathroom=bathroom,location=location,price=price,type=type,description=description,image=filename)
            db.session.add(newProperty)
            db.session.commit()

            properties =Property.query.all()
            flash('Success')    
            return redirect(url_for('/properties',properties=properties))
        else:
            flash('Error.Try again','Failed')
    return render_template('form.html',form=form)



@app.route('/properties')
def properties():
    properties = Property.query.all()
    return render_template('properties.html', properties = properties)


@app.route('/properties/<propertyid>')


###
# The functions below should be applicable to all Flask apps.
###

# Display Flask WTF errors as Flash messages
def flash_errors(form):
    for field, errors in form.errors.items():
        for error in errors:
            flash(u"Error in the %s field - %s" % (
                getattr(form, field).label.text,
                error
            ), 'danger')

@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also tell the browser not to cache the rendered page. If we wanted
    to we could change max-age to 600 seconds which would be 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0",port="8080")
