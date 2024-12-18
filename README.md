Spy Cat Agency API Welcome to the Spy Cat Agency API, a Django REST Framework-based application for managing spy cats, their missions, and targets. This API allows users to create, update, and delete spy cats and missions, as well as manage their targets.

🛠 Features CRUD operations for Spy Cats. Assign missions to cats and manage their completion status. Add and manage targets for specific missions. Input validation for data fields (e.g., valid breeds for spy cats). API endpoints for integration with front-end applications or external systems. 🚀 Quick Start Prerequisites Python 3.8+ Django 4.x Django REST Framework

Install dependencies:

bash pip install -r requirements.txt Apply migrations:

bash python manage.py migrate Run the development server:

bash python manage.py runserver

📚 API Endpoints Base URL http://127.0.0.1:8000/

🧪 Testing Run the test suite to ensure everything works as expected:

bash python manage.py test

Also use this URLs Spy Cat http://127.0.0.1:8000/api/cats/

Mission http://127.0.0.1:8000/api/missions/

