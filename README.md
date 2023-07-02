# Zeta Gaming Blog Application

Zeta Gaming Blog is a web application built using Django, a high-level Python web framework, designed to create and manage a gaming blog where users can share their gaming experiences, reviews, and news.

## Features

- **User Registration and Authentication**: Users can sign up, log in, and manage their accounts.
- **Create and Manage Blog Posts**: Users can create, edit, and delete blog posts.
- **Browse and Search Blog Posts**: Users can browse through blog posts, filter by categories, and search for specific content.
- **Commenting System**: Users can leave comments on blog posts to engage in discussions.
- **User Profiles**: Users have personal profiles where they can view and manage their blog posts, comments, and profile information.
- **Admin Panel**: An admin panel is provided to manage blog posts, comments, categories, and user accounts.
- **Responsive Design**: The application is designed to provide a seamless experience across devices with responsive design.

## Prerequisites

Make sure you have the following dependencies installed before running the project:

- Python (v3.7 or above)
- Django (v3.2 or above)

## Getting Started

1. Clone the repository:

```shell
git clone https://github.com/Mohit-Mehra/GamingBlog-ZetaGaming.git
```

2. Navigate to the project directory:

```shell
cd zeta-gaming-blog
```

3. Create a virtual environment:

```shell
python -m venv venv
```

4. Activate the virtual environment:

- For Windows:

```shell
venv\Scripts\activate
```

- For macOS/Linux:

```shell
source venv/bin/activate
```

5. Install the project dependencies:

```shell
pip install -r requirements.txt
```

6. Run database migrations:

```shell
python manage.py migrate
```

7. Start the development server:

```shell
python manage.py runserver
```

8. Open your web browser and navigate to `http://localhost:8000` to see the application running.

## Acknowledgements

The Zeta Gaming Blog application is built with Django and incorporates various open-source libraries and frameworks. Special thanks to the contributors of these projects:

- [Django](https://www.djangoproject.com)
- [Bootstrap](https://getbootstrap.com)

## Contact

For any questions or inquiries regarding the Zeta Gaming Blog application, you can contact the project maintainer at [info.mohitverse@gmail.com](mailto:info.mohitverse@gmail.com).
