"""
Flask Documentation:     http://flask.pocoo.org/docs/
Jinja2 Documentation:    http://jinja.pocoo.org/2/documentation/
Werkzeug Documentation:  http://werkzeug.pocoo.org/documentation/
This file creates your application.
"""
import os
from app import app , db
from flask import render_template, request, redirect, url_for,flash
from app.forms import PropertyForm
from werkzeug.utils import secure_filename
from flask import send_from_directory
from app.models import PropertyList

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

@app.route('/property', methods=['POST','GET'])
def property():
    form= PropertyForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            title=form.title.data
            num_bedrooms=form.num_bedrooms.data
            num_bathrooms=form.num_bathrooms.data
            location=form.location.data
            price=form.price.data
            propertytype=form.propertytype.data
            description=form.description.data
            photo=form.photo.data
            filename=secure_filename(photo.filename)
            photo.save(os.path.join(app.config['UPLOAD_FOLDER'],filename))
            property_list=PropertyList(title,num_bedrooms,num_bathrooms,location,
                                        price,propertytype,description,filename)
            db.session.add(property_list)
            db.session.commit()

            flash("Property was successfully added", "success")
            return redirect(url_for('properties'))
        flash_errors(form)
    return render_template('property.html',form=form)
    
@app.route('/properties')
def properties():
    items = PropertyList.query.all()
    return render_template('properties.html', items=items)

@app.route('/property/<propertyid>')
def propertyid(propertyid):
    property= PropertyList.query.filter-by(id=propertyid).first()
    if request.method=='GET':
        return render_template('propertyid.html', foundproperty=property)

@app.route('/upload/<filename>')
def get_image(filename):
    root_dir = os.getcwd()
    return send_from_directory(os.path.join(root_dir, app.config['UPLOAD_FOLDER']), filename)
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
    app.run(debug=True,host="0.0.0.0",port="8090")
