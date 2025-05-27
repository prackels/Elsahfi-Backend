# Elsahfi Backend

## Project Overview
A comprehensive business management system built with Django and Django REST Framework. This project was developed over a 2-month period as a first major backend project, designed to handle various business operations including user management, customer orders, invoices, expenses, and more. The system demonstrates rapid development capabilities while maintaining robust functionality and clean architecture.

## Development Timeline
- **Duration**: 2 months
- **Development Phase**: First major backend project
- **Key Achievements**:
  - Implemented complete business management functionality
  - Integrated real-time notifications system
  - Built robust authentication and authorization
  - Created comprehensive API documentation
  - Developed scalable database architecture

## Features
- 👥 User Management System
  - Role-based access control
  - Secure authentication using JWT
  - User profile management
  
- 🛍️ Customer Orders Management
  - Order tracking
  - Status updates
  - Order history
  
- 💰 Invoice Generation and Management
  - Automated invoice creation
  - PDF generation
  - Payment tracking
  
- 📊 Expense Tracking
  - Expense categories
  - Financial reporting
  - Budget management
  
- 💼 Employee Management
  - Employee profiles
  - Attendance tracking
  - Performance metrics
  
- 🏪 Cash Station Management
  - Real-time transaction processing
  - Cash flow monitoring
  - Daily reconciliation
  
- 📱 Real-time Notifications
  - WebSocket integration
  - Push notifications
  - Event tracking
  
- 🔍 Search Functionality
  - Advanced search filters
  - Quick search feature
  
- 📄 Report Generation
  - Customizable reports
  - Export functionality
  - Data visualization
  
- 🔐 Authentication and Authorization
  - JWT token-based auth
  - Permission management
  - Secure password handling

## Technology Stack
- **Framework**: Django 4.2.7
- **API Framework**: Django REST Framework 3.14.0
- **Database**: PostgreSQL
- **Real-time Communication**: Django Channels with Redis
- **Task Queue**: Celery 5.3.6
- **API Documentation**: drf-yasg (Swagger/OpenAPI)
- **Authentication**: JWT (djangorestframework-simplejwt)
- **Additional Tools**:
  - Redis for caching and real-time features
  - Celery for background tasks
  - Channels for WebSocket support

## Project Structure
```
elsahfi-backend/
├── cash_station/      # Cash management functionality
├── clients_/          # Client management and profiles
├── codes/            # Utility functions and helpers
├── core/             # Core project settings and configurations
├── customer_orders/  # Order processing and management
├── employee/         # Employee management system
├── expenses/         # Expense tracking and management
├── globals/         # Global utilities and constants
├── info/            # Information management
├── invoices/        # Invoice generation and processing
├── new_purchase/    # Purchase order management
├── notifications/   # Real-time notification system
├── reports/         # Report generation and templates
├── search/          # Search functionality
├── settings/        # Application settings
├── static/          # Static files (CSS, JS, images)
├── templates/       # HTML templates
├── users/           # User management and authentication
└── manage.py        # Django management script
```

## Prerequisites
- Python 3.x
- PostgreSQL
- Redis Server
- Virtual Environment (recommended)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/elsahfi-backend.git
cd elsahfi-backend
```

2. Create and activate virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Configure environment variables (create .env file in root directory):
```env
DEBUG=True
SECRET_KEY=your_secret_key
DATABASE_URL=postgresql://user:password@localhost:5432/dbname
REDIS_URL=redis://localhost:6379
```

5. Run migrations:
```bash
python manage.py migrate
```

6. Create superuser:
```bash
python manage.py createsuperuser
```

7. Start development server:
```bash
python manage.py runserver
```

## Running the Services
1. Start Redis Server
2. Start Celery Worker:
```bash
celery -A core worker -l info
```
3. Start Django Development Server:
```bash
python manage.py runserver
```

## API Documentation
After running the server, you can access the API documentation at:
- Swagger UI: `http://localhost:8000/swagger/`
- ReDoc: `http://localhost:8000/redoc/`

## Development Best Practices
- Modular architecture for scalability
- Comprehensive API documentation
- Robust error handling
- Unit tests for critical components
- Code comments and documentation
- Regular code reviews
- Version control with Git

## Contributing
1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License
This project is licensed under the terms of the license included in the repository.

## Support
For support, please contact the development team or create an issue in the repository.

## Acknowledgments
Special thanks to all contributors who helped in the development of this project during the intensive 2-month development period. 
