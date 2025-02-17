# Contact Us Project

This is a Django mini-project for a "Contact Us" form.

## Project Structure

- `contact_us_Proj/`: Main project directory.
- `contact_us_app/`: Django app for the contact form handling the form manually.
- `contact_us_modelforms/`: Django app for the contact form using ModelForms.
- `templates/`: HTML templates.
- `static/`: Static files (CSS, JavaScript).

## Differences Between Django Forms and Regular Method

- **Django Forms**: This method leverages Django's built-in form handling, providing automatic validation, error handling, and form rendering.
- **Regular Method**: This method involves manually handling form data, validation, and error handling, giving more control but requiring more code.

These two apps demonstrate the different approaches to handling forms in Django.

## Using ModelForms

- **ModelForms**: This method uses Django's ModelForms to automatically generate a form based on a model. It simplifies form creation and handling by tying the form directly to a database model, providing built-in validation and saving methods.

### Detailed Explanation of ModelForms in `contact_us_modelforms`

1. **Model Definition**:
    - The `Contact` model is defined in `models.py` with fields for `name`, `email`, and `message`.



2. **Form Definition**:
    - The `ContactForm` is defined in `forms.py` using Django's `ModelForm`. This form automatically includes fields from the `Contact` model.

3. **Views**:
    - The `contact_view` handles the form submission. If the form is valid, it saves the data and redirects to the success page.

   
4. **URLs**:
    - The URLs for the contact form and success page are defined in `urls.py`.


5. **Templates**:
    - The HTML templates for the contact form and success page are defined in the `templates/contact_us` directory.

l>
   

The `contact_us_modelforms` app demonstrates how to use Django ModelForms to create and handle a contact form efficiently.



