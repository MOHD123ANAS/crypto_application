Crypto Price Tracker

A Django-based application that fetches real-time cryptocurrency prices and displays them in a user-friendly UI with pagination.

Features:
- Fetches live **Bitcoin (BTC)** and **Ethereum (ETH)** prices.
- Secure API using **JWT authentication**.
- Uses **Celery + Redis** for background tasks.

Installation & Setup
Clone the Repository
```sh
# Clone the project
https://github.com/MOHD123ANAS/crypto_application.git
cd crypto_application
```

Install Redis (Required for Celery)
- Linux & Mac:Run `redis-server`.
- **Windows Users:** Install Redis from [here](https://redis.io/docs/latest/operate/oss_and_stack/install/install-redis/install-redis-on-windows/).


Running the Project (Step-by-Step)
Open the project folder in Terminal or Command Prompt**
```sh
cd E:\crypto_application
```

Activate Virtual Environment**
```sh
crypto\Scripts\Activate
```

Navigate to the **Django Project Folder**
```sh
cd crypto_project
```
**Install Dependencies**
```sh
pip install -r requirements.txt
```

Apply Migrations & Create Superuser (First Time Only)
```sh
python manage.py migrate
python manage.py createsuperuser  
```

Start the Django Server
```sh
python manage.py runserver
```
App will be available at: `http://127.0.0.1:8000/`

**Start Celery Worker** (For Background Tasks)
```sh
celery -A crypto_project worker --loglevel=info
```

Start Celery Beat (For Periodic Tasks Like Fetching Prices)
```sh
celery -A crypto_project beat --loglevel=info
```

API Endpoints
| Method | Endpoint | Description |
|--------|----------|-------------|
| `POST` | `/api/token/` | Obtain JWT token |
| `GET` | `/api/crypto-prices/` | Fetch crypto prices (Paginated) |

Use `Authorization: Bearer <your_token>` for API requests.



🎯 Usage
1. Login via the UI and click "Load Prices".
2. **Prices updates (handled by Celery)**.
3. Pagination allows easy navigation.
4. **Admin Panel** (`/admin`) lets you configure periodic tasks.


Made with ❤️ using Django, DRF, Celery, and Redis.

