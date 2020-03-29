# About The Project
> This is a data-driven website which was created for my final year project.
# Local Hosting
## Prerequisites before hosting
1. Ensure Python 3.7 is installed on the machine.
2. Please use a Python virtual environment to proceed the following section.
   * Recommend to use `virtualenvwrapper` for creating a virtual environment (requires pip installation before use).
## How to run the development server
1. Download or clone the project into your computer.
2. Open your terminal or CMD.
3. Ensure your terminal or cmd has enabled the Python virtual environment.
   * If you have `virtualenvwrapper` installed, you can use the `workon` command to enable the virtual environment that you have created earlier.
4. Change directory to the project's home directory.
5. Run command `pip install -r requirements.txt` to install all dependencies required for this project.
6. Run command `python manage.py runserver`.
   * Note: If *WinError 10013* appeared, this indicates that the port 8000 has been occupied by another process. Please terminate that process and rerun the runserver command!
7. Open your browser and insert the URL `localhost:8000` or `127.0.0.1:8000`.

# Navigating the Site
## The Main site
You can navigate the site from the home page and find a subject or course in the corresponding pages.
> Note that not all subjects or courses will function properly because only some courses have added the relevant information. If you want to have a try at altering a course or subject feel free to do so with the superuser `admin` account in the **Admin Portal**.
> The **Introduction to Computer Science and Programming in Python** course under the **Computer Science** subject category will give you an insight of what the site is supposed to look like when it is fully functioning.
## The Admin Portal
The admin portal is located at `localhost:8000/admin` or `127.0.0.1:8000/admin`.
## Login to Admin portal
Account: `admin`
Password :`djangoadmin`
# Contact
For any issues in regards to the project please post an issue in this repo.
