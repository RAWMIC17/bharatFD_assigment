# Bharat FD

A multilingual FAQ management API built using Django.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/RAWMIC17/bharatFD_assignment.git

2. Install dependencies:

    pip install -r requirements.txt

3. Set up Redis for caching:

    # Start Redis server
    redis-server

4. Apply migrations:

    python manage.py migrate

## API Usage

    GET /faq/: Returns list of FAQs.
        Query Parameter lang: Language code (e.g., en, es).

## Contribution

  1.  Fork the repository.
  2.  Create a new branch (git checkout -b feature-branch).
  3.  Commit your changes (git commit -m 'feat: added new feature').
  4.  Push to your branch (git push origin feature-branch).
  5.  Open a pull request.